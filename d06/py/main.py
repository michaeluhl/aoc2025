from functools import reduce
from operator import add, mul
from typing import Callable


OP_MAP: dict[str, Callable] = {"+": add, "*": mul}


def main(options):
    operands: list[list[int]] = []
    operators: list[Callable] = []

    with open(options.DATA, "rt") as input_file:
        for line in input_file:
            if "+" in line:
                operators: list[Callable] = [OP_MAP[v] for v in line.strip().split()]
            else:
                operands.append([int(v) for v in line.strip().split()])

    tot = 0
    operands.append(operators)

    for *args, op in zip(*operands):
        tot += reduce(op, args)

    print(f"Total {tot}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 6")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
