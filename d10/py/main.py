from collections import OrderedDict
from copy import deepcopy
from typing import Self, TypeAlias

import numpy as np
import scipy.linalg as la

from sympy import ZZ
from sympy.polys.matrices import DM
from sympy.polys.matrices.normalforms import smith_normal_decomp


Idx: TypeAlias = int


class Machine:
    def __init__(
        self,
        lights: int,
        nlights: int,
        buttons: tuple[int, ...],
        joltage: tuple[int, ...],
    ):
        self.lights = lights
        self.nlights = nlights
        self.buttons = buttons
        self.joltage = joltage

    @classmethod
    def from_input(cls, line: str) -> Self:
        lights: int = 0
        nlights: int = 0
        buttons: list[int] = []
        joltage: tuple[int, ...] = tuple()

        for section in line.strip().split(" "):
            if "[" in section:
                for i, c in enumerate(section.strip("[]")):
                    if c == "#":
                        lights |= 1 << i
                    nlights += 1
            elif "(" in section:
                button = 0
                for i, v in enumerate(section.strip("()").split(",")):
                    button |= 1 << int(v)
                buttons.append(button)
            elif "{" in section:
                joltage = tuple([int(v) for v in section[1:-1].split(",")])
        return cls(lights, nlights, tuple(buttons), joltage)

    def btn_mtx(self) -> list[list[int]]:
        mtx: list[list[int]] = []
        for btn in self.buttons:
            row = self.nlights * [0]
            for i in range(self.nlights):
                if btn & (1 << i):
                    row[i] = 1
            mtx.append(row)
        mtx.append(list(self.joltage))
        return mtx

    def __repr__(self) -> str:
        buttons = ",".join([f"{b:02x}" for b in self.buttons])
        return f"<Machine({self.lights:02x}, {buttons}, {self.joltage})>"


def single_var_constraints(
    null_vecs: np.ndarray[int], sol_vec: np.ndarray[int], amx: int
) -> dict[Idx, tuple[int, int]]:
    constr: dict[Idx, list[int]] = {}
    for null_row, sol_val in zip(null_vecs, sol_vec):
        if np.all(null_row == 0):
            # No constraints in this row
            continue
        elif np.sum(null_row != 0) == 1:
            # The row will give a single constraint
            # Get the index of the non-zero coefficient
            idx = np.argwhere(null_row != 0).flat[0]
            # Get the coefficient
            coef = null_row[idx]
            # Calculate the limit value
            lim_val = -1 * sol_val // coef
            # Determine the comparison function
            lim_idx, cmp = (1, min) if coef < 0 else (0, max)
            # Get the limits for this index
            lim_set = constr.setdefault(idx, [-1 * amx, amx])
            # Set the limit
            lim_set[lim_idx] = cmp(lim_set[lim_idx], lim_val)
    return {k: (n, x) for k, (n, x, *_) in constr.items()}


def multi_var_constraints(
    null_vecs: np.ndarray[int],
    sol_vec: np.ndarray[int],
    svc: dict[Idx, tuple[int, int]],
    amx: int,
) -> dict[Idx, tuple[int, int]]:
    svc: dict[Idx, tuple[int, int]] = deepcopy(svc)
    msk = np.arange(null_vecs.shape[0])
    for i, (null_row, sol_val) in enumerate(zip(null_vecs, sol_vec)):
        # check to see if adding or subtracting this row from the remaining
        # rows results in any lone variables
        for sgn in (1,):
            # Add the current row (multiplied by `sgn`) to the remaining rows
            check_mat = null_vecs[msk != i, :] + sgn * null_row
            check_sol = sol_vec[msk != i] + sgn * sol_val
            # Loop over the rows
            for check_row, check_sol_val in zip(check_mat, check_sol):
                # If there's only one non-zero value, then we've struck gold
                if np.sum(check_row != 0) == 1:
                    # Get the index of the non-zero coefficient
                    idx: Idx = np.argwhere(check_row != 0).flat[0]
                    # Get the coefficient
                    coef = check_row[idx]
                    # Calculate the limit value
                    lim_val = -1 * check_sol_val // coef
                    # Get the existing limits (if any)
                    lim_set = list(svc.get(idx, (-1 * amx, amx)))
                    # Determine which limit we're setting and the correct comparison operator to use
                    lim_idx, cmp = (1, min) if coef < 0 else (0, max)
                    # Set the limit
                    lim_set[lim_idx] = cmp(lim_set[lim_idx], lim_val)
                    # Store the limits
                    svc[idx] = tuple(lim_set[:2])
    return svc


def solve(A: list[list[int]], b: list[int]) -> int | None:
    "Take a matrix (that may be over- or under-specified) and RHS vector, return the smallest interger solution"
    # Compute the Smith normal form of the input matrix
    #
    SNF, U, V = [
        np.array(m.to_list(), dtype=int)
        for m in smith_normal_decomp(DM(A, domain=ZZ).transpose())
    ]

    # Numpy version of A
    A: np.ndarray[int] = np.array(A, dtype=int).T
    # The B matrix is the same as the SNF (i.e., U @ A @ V), but we're only interested in the diagonal entries
    B: np.ndarray[int] = np.diag(SNF)
    # C is a Numpy version of the original righthand-side vector
    C: np.ndarray[int] = np.array([b], dtype=int).T
    # D is the product of the U matrix (from the Smith decomp) and the C vector
    D: np.ndarray[int] = U @ C

    # Determine the null space of A
    NULL_VECS = la.null_space(A)
    # This tells us how many rows a solution vector has to have and also how many free variables there are
    x_rows, n_free_vars = NULL_VECS.shape

    # For Diophantine equations, V @ y where y = [D[i]/B[i,i],...] is a solution to the original system
    # Here DoB is D/B.  We size this to have at least one column vector, but potentially as many column
    # vectors as there are in the null space
    DoB = np.zeros((x_rows, max(1, n_free_vars)), dtype=int)
    # To avoid divisions by zero, find where B is non-zero
    idxs = np.argwhere(B != 0)
    # The we only do the division of D by B where B is non-zero
    DoB[idxs, :] = D[idxs, :] / B[idxs, None]

    # The particular solution is given by V @ DoB[:, 0]
    X = V @ DoB[:, 0]

    # If there are no free variables, this must be the only solution
    if n_free_vars < 1:
        return X.sum()

    # If there are free variables, modify DoB so that we assume a value of
    # one for each of those
    for i in range(1, n_free_vars + 1):
        DoB[-i, -i] = 1

    # See how the solution changes with a change in each of the free variables
    dXdfv = V @ DoB - X[:, None]

    # Try to determine some limits for the free variables
    constraints = single_var_constraints(dXdfv, X, (x_n := np.abs(X).max()))
    constraints = multi_var_constraints(dXdfv, X, constraints, x_n)
    # Construct ranges over which the free variables will be varied
    # For simplicity we're just going vary each free variable from -1*maximum to maximum
    ranges = []
    for i in range(n_free_vars):
        n, x = constraints.get(i, (-1 * x_n, x_n))
        ranges.append(np.arange(n, x + 1))
    x_sum = None
    idxs = [r.flat for r in np.meshgrid(*ranges)]
    for vals in zip(*idxs):
        DoB[-n_free_vars:, 0] = vals
        X = V @ DoB[:, 0]
        if np.all(X >= 0):
            s = X.sum()
            x_sum = s if not x_sum else min(x_sum, s)
    return x_sum


def main(options):
    data: list[Machine] = []

    with open(options.DATA, "rt") as input_file:
        data: list[Machine] = [Machine.from_input(line) for line in input_file]

    pushes = 0
    for mach in data:
        allb = set(mach.buttons)
        cache: OrderedDict[frozenset[int], int] = OrderedDict(
            (frozenset((b,)), b) for b in mach.buttons
        )
        if mach.lights in cache.values():
            pushes += 1
            continue

        while cache:
            s, v = cache.popitem(last=False)
            for b in allb - s:
                nv = v ^ b
                if nv == mach.lights:
                    pushes += len(s) + 1
                    break
                cache[frozenset(s | set((b,)))] = nv
            else:
                continue
            break

    print(f"Part 1: {pushes}")

    push_cts: list[int] = []
    for i, mach in enumerate(data):
        if options.only and i != options.only:
            continue
        *rows, b = mach.btn_mtx()
        print(f"Processing machine {i}")
        push_cts.append(solve(rows, b))

    print(f"Matched: {sum(push_cts)}")
    print(f"Total: {len(data)}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 10")
    parser.add_argument("DATA", type=str, help="Path to data file")
    parser.add_argument(
        "-o",
        "--only",
        type=int,
        default=None,
        help="Process only the specified machine",
    )

    main(parser.parse_args())
