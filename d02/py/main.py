def main(options):
    with open(options.DATA, "rt") as data:
        ranges = [rng.split("-") for rng in data.read().strip().split(",")]

    tot = 0
    for first, last in ranges:
        for v in range(int(first), int(last) + 1):
            sv = str(v)
            svl = len(sv)
            if svl % 2 != 0:
                continue
            hl = svl // 2
            if sv[:hl] == sv[hl:]:
                tot += v

    print(tot)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 2")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
