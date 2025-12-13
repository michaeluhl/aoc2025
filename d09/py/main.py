def inrect(rect, pt):
    c1, c2 = rect
    xs, ys = zip(c1, c2)
    xs, ys = sorted(xs), sorted(ys)
    return (xs[0] <= pt[0] <= xs[1]) and (ys[0] <= pt[1] <= ys[1])


def area(rect):
    c1, c2 = rect
    xs, ys = zip(c1, c2)
    xs, ys = sorted(xs), sorted(ys)
    return (xs[1] - xs[0] + 1) * (ys[1] - ys[0] + 1)


def main(options):
    points = []
    with open(options.DATA, "rt") as input_file:
        for line in input_file:
            points.append(tuple([int(v) for v in line.strip().split(",")]))

    areas = {}
    cpoints = points[:]
    while cpoints:
        c1 = cpoints.pop(0)
        for c2 in cpoints:
            legs = [abs(x2 - x1) + 1 for x1, x2 in zip(c2, c1)]
            areas[frozenset([c1, c2])] = legs[0] * legs[1]

    print(f"Part 1: {max(areas.values())}")

    lengths = [
        abs(e[0] - s[0]) + abs(e[1] - s[1]) for s, e in zip(points[:-1], points[1:])
    ]
    mxidxs = sorted(range(len(lengths)), key=lengths.__getitem__, reverse=True)

    p1, p2 = points[mxidxs[0]], points[mxidxs[0] + 1]
    p3, p4 = points[mxidxs[1]], points[mxidxs[1] + 1]

    c1 = max([p1, p2], key=lambda t: t[0])
    c2 = max([p3, p4], key=lambda t: t[0])

    c1, c2 = sorted([c1, c2], key=lambda t: t[1])

    areas = {}
    lr = [p for p in points if (c1[0] - 100 <= p[0] <= c1[0]) and p[1] < c1[1]]
    print(f"{lr=}")
    lr = max(lr, key=lambda t: t[1])
    print(f"{lr=}")
    ll = [p for p in points if (lr[1] <= p[1] <= c1[1] and p[0] < 50000)]
    print(f"{ll=}")
    ll = min(ll, key=lambda t: t[1])
    print(f"{ll=}")
    areas[frozenset((c1, ll))] = area((c1, ll))

    ur = [p for p in points if (c2[0] - 100 <= p[0] <= c2[0]) and p[1] > c2[1]]
    print(f"{ur=}")
    ur = min(ur, key=lambda t: t[1])
    print(f"{ur=}")
    ul = [p for p in points if (c2[1] <= p[1] <= ur[1]) and p[0] < 50000]
    print(f"{ul=}")
    ul = min(sorted(ul, key=lambda t: t[1])[-2:], key=lambda t: t[0])
    print(f"{ul=}")
    areas[frozenset((c2, ul))] = area((c2, ul))

    print(areas)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 9")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
