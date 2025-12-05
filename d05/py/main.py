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

    ranges = sorted(ranges, key=lambda t: t[0])
    consolidated = [ranges.pop(0)[-1]]

    while ranges:
        _, r = ranges.pop(0)
        if r.start in consolidated[-1]:
            if r.stop in consolidated[-1]:
                pass
            e = consolidated.pop()
            consolidated.append(range(e.start, max(e.stop, r.stop)))
        else:
            consolidated.append(r)

    ct = sum(len(r) for r in consolidated)

    print(f"Total: {ct}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 5")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
