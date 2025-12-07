def main(options):
    grid: list[list[float]] = []

    with open(options.DATA, "rt") as input_file:
        for line in input_file:
            grid.append(
                [-1 if c == "^" else 1 if c == "S" else 0 for c in line.strip()]
            )

    ct = 0

    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v > 0 and i + 1 < len(grid):
                if grid[i + 1][j] == 0:
                    grid[i + 1][j] = v
                elif grid[i + 1][j] < 0:
                    ct += 1
                    grid[i + 1][j - 1] += v
                    grid[i + 1][j + 1] += v
                else:
                    grid[i + 1][j] += v

    print(f"Splits: {ct}")
    print(f"Histories: {sum(grid[-1])}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 7")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
