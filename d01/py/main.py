def main(options):
    start = options.start
    ct = 0

    ops = []

    with open(options.DATA, "rt") as instructions:
        for inst in instructions:
            d, n = inst[0], int(inst[1:])
            turns = [n % 100] + (n // 100) * [100] if options.pt2 else [n]
            s = 1 if d == "R" else -1
            ops.extend([s * v for v in turns])

    for n in ops:
        nxt = start + n
        if options.pt2 and not start == 0:
            if nxt < 0 or nxt > 100:
                ct += 1
        start = nxt % 100
        if start == 0:
            ct += 1

    print(ct)


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 1")
    parser.add_argument("-s", "--start", type=int, default=50, help="Starting Value")
    parser.add_argument("-p", "--pt2", action="store_true", help="Part 2 procedure")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
