def trace(nodes: dict[str, list[str]], node: str, hist: list[str]) -> list[list[str]]:
    hist = [*hist, node]
    paths = []
    for con in nodes[node]:
        if con not in hist:
            paths.extend(trace(nodes, con, hist))
    return (
        paths
        if paths
        else [
            hist,
        ]
    )


def main(options):
    graph: dict[str, list[str]] = {"out": []}
    with open(options.DATA, "rt") as input_file:
        for row in input_file:
            lbl, _, con_lbls = row.partition(":")
            cons = list(con_lbls.strip().split())
            graph[lbl] = cons

    paths = trace(graph, options.start, [])
    print(f"Part 1: {len(paths)}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 11")
    parser.add_argument("DATA", type=str, help="Path to data file")
    parser.add_argument("-s", "--start", type=str, default="you", help="Starting Node")

    main(parser.parse_args())
