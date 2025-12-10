from functools import reduce
from operator import mul


def main(options):
    count = 10 if options.test else 1000
    points: list[tuple[int, int, int]] = []
    with open(options.DATA, "rt") as input_file:
        for line in input_file:
            points.append(tuple(int(v) for v in line.strip().split(",")))

    dists: dict[tuple, int] = {}
    pqueue = points[:]
    while pqueue:
        pt = pqueue.pop()
        for op in pqueue:
            key = (pt, op)
            dist = sum((p - o) ** 2 for p, o in zip(pt, op))
            dists[key] = dist

    dists: list[tuple[int, tuple]] = sorted((v, k) for k, v in dists.items())

    circuits: list[set] = [set((p,)) for p in points]
    for _ in range(count):
        d, c = dists.pop(0)
        c = set(c)
        cts = [ct for ct in circuits if ct & c]
        nct = set().union(*cts)
        circuits.append(nct)
        for ct in cts:
            circuits.remove(ct)

    res = reduce(mul, sorted([len(s) for s in circuits], reverse=True)[:3])
    print(f"Part 1: {res}")

    while True:
        d, c = dists.pop(0)
        c = set(c)
        cts = [ct for ct in circuits if ct & c]
        nct = set().union(*cts)
        circuits.append(nct)
        for ct in cts:
            circuits.remove(ct)
        if len(circuits) == 1:
            (x1, _, _), (x2, _, _) = c
            print(f"Part 2: {x1}, {x2}, {x1 * x2}")
            break


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 8")
    parser.add_argument("DATA", type=str, help="Path to data file")
    parser.add_argument("-t", "--test", action="store_true", help="Test mode")

    main(parser.parse_args())
