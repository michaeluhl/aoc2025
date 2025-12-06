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

    data_lines: list[str] = []
    operators: list[Callable] = []
    splits: list[int] = []

    with open(options.DATA, "rt") as input_file:
        for line in input_file:
            if "+" not in line:
                data_lines.append(line.strip("\n"))
            else:
                for i, c in enumerate(line.strip("\n")):
                    if c != " ":
                        splits.append(i)
                        operators.append(OP_MAP[c])
                splits.append(len(line))
    # Calculate the field widths
    splits = [e - s for s, e in zip(splits[:-1], splits[1:])]

    iblocks: list[list[str]] = []

    for d_line in data_lines:
        row: list[str] = []
        for l in splits:
            row.append(d_line[:l])
            d_line = d_line[l:]
        iblocks.append(row)

    tot = 0
    for *chunk, op in zip(*iblocks, operators):
        args: list[int] = []
        for d_chars in zip(*chunk):
            if all([c == " " for c in d_chars]):
                continue
            args.append(int("".join(d_chars).strip()))
        tot += reduce(op, args)

    print(f"Total: {tot}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 6")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
