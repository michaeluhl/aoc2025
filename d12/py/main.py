def main(options):
    pieces: list[tuple[int, list[list[int]]]] = []
    spaces: list[tuple[tuple[int, int], tuple[int, ...]]] = []
    chunks: list[list[str]] = []

    with open(options.DATA, "rt") as input_file:
        chunk: list[str] = []
        for line in input_file:
            if l := line.strip():
                chunk.append(l)
            if not l and chunk:
                chunks.append(chunk)
                chunk = []
        else:
            if chunk:
                chunks.append(chunk)
    for chunk in chunks:
        if "x" in chunk[0]:
            for row in chunk:
                area, _, counts = row.partition(":")
                w, _, l = area.partition("x")
                icounts: list[int] = [int(v) for v in counts.strip().split()]
                spaces.append(((int(w), int(l)), tuple(icounts)))
        else:
            piece: list[list[int]] = []
            for row in chunk:
                if ":" in row:
                    continue
                piece.append([1 if c == "#" else 0 for c in row.strip()])
            area: int = sum([sum(r) for r in piece])
            pieces.append((area, piece))

    fails = 0
    passes = 0
    for (w, l), counts in spaces:
        area = w * l
        parea: int = sum([ct * a for ct, (a, _) in zip(counts, pieces)])
        if parea > area:
            fails += 1
        if 9 * sum(counts) <= (w - (w % 3)) * (l - (l % 3)):
            passes += 1
    print(f"Fails: {fails}")
    print(f"Passes: {passes}")
    print(f"Total: {len(spaces)}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 12")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
