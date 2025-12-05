import numpy as np


def main(options):
    ranges: list[tuple[int, range]] = []
    ids: list[int] = []
    maxe = 0
    with open(options.DATA, "rt") as data_file:
        for row in data_file:
            if "-" in row:
                s, _, e = row.strip().partition("-")
                s, e = int(s), int(e)
                ranges.append((s, range(s, e + 1)))
                maxe = max(e, maxe)
            elif i := row.strip():
                ids.append(int(i))

    ranges = sorted(ranges, key=lambda t: t[0])
    ct = 0
    for iid in ids:
        for _, rng in ranges:
            if iid in rng:
                ct += 1
                break
    print(f"Count: {ct}")

    # Build bitmask
    msk = 0
    for _, rng in ranges:
        for v in rng:
            msk |= 1 << v

    # Read out bitmask
    ct = 0
    while msk:
        if msk & 1:
            ct += 1
        msk >>= 1

    print(f"Total: {ct}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 5")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
