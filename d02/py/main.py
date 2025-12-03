from typing import Sequence


def main(options):
    with open(options.DATA, "rt") as data:
        ranges = [rng.split("-") for rng in data.read().strip().split(",")]

    spans: dict[int, Sequence[int]] = {
        10: (5, 2),
        9: (3,),
        8: (4, 2),
        6: (3, 2),
        4: (2,),
    }

    tot_1 = 0
    tot_2 = 0
    for first, last in ranges:
        for v in range(int(first), int(last) + 1):
            sv = str(v)
            svl = len(sv)
            if svl < 2:
                continue
            spns = [1] + list(spans.get(svl, []))
            for spn in spns:
                if sv == (svl // spn) * sv[:spn]:
                    tot_2 += v
                    break
            if svl % 2 != 0:
                continue
            hl = svl // 2
            if sv[:hl] == sv[hl:]:
                tot_1 += v

    print(f"Part 1: {tot_1}")
    print(f"Part 2: {tot_2}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 2")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
