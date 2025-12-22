def ftrace(nodes: dict[str, list[str]], start: str, end: str, cache: dict):
    if start == end:
        return [[end]]
    paths = []
    for con in nodes[start]:
        con_p = (
            cache[con]
            if con in cache
            else cache.setdefault(con, ftrace(nodes, con, end, cache))
        )
        paths.extend([[start, *p] for p in con_p])
    return paths


def main(options):
    graph: dict[str, list[str]] = {"out": []}
    with open(options.DATA, "rt") as input_file:
        for row in input_file:
            lbl, _, con_lbls = row.partition(":")
            cons = list(con_lbls.strip().split())
            graph[lbl] = cons

    paths = ftrace(graph, options.start, options.out, {})
    print(f"Part 1: {len(paths)}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 11")
    parser.add_argument("DATA", type=str, help="Path to data file")
    parser.add_argument("-s", "--start", type=str, default="you", help="Starting Node")
    parser.add_argument("-o", "--out", type=str, default="out", help="Ending Node")

    main(parser.parse_args())
