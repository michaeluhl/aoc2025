def main(options):
    grid = []

    with open(options.DATA, "rt") as input_file:
        for row in input_file:
            grid.append([0] + [1 if c == "@" else 0 for c in row.strip()] + [0])

    gw = len(grid[0])
    grid.insert(0, gw * [0])
    grid.append(grid[0])

    stencil = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    ct = 0
    removable = [(0, 0)]
    while removable:
        for r, c in removable:
            grid[r][c] = 0
        removable = []
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[1]) - 1):
                if grid[r][c] != 1:
                    continue
                n = sum([grid[r + dr][c + dc] for dr, dc in stencil])
                if n < 4:
                    ct += 1
                    removable.append((r, c))
        if not options.part2:
            break

    print(f"Removed: {ct}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 4")
    parser.add_argument("DATA", type=str, help="Path to data file")
    parser.add_argument("-2", "--part2", action="store_true", help="Do Part 2")

    main(parser.parse_args())
