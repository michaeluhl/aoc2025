def main(options):
    banks = []

    with open(options.DATA, "rt") as data:
        for line in data:
            banks.append([int(c) for c in line.strip()])

    joltage = 0
    for bank in banks:
        i, d0 = sorted(enumerate(bank[:-1]), key=lambda t: t[1], reverse=True)[0]
        d1 = max(bank[i + 1 :])
        joltage += d0 * 10 + d1

    print(f"Part 1: {joltage}")

    joltage = 0
    for bank in banks:
        buff = []
        s = 0
        l = len(bank)
        for e in reversed(range(12)):
            bseg = bank[s : l - 1 * e]
            i = max(range(len(bseg)), key=bseg.__getitem__)
            buff.append(str(bank[s + i]))
            s += i + 1
        joltage += int("".join(buff))

    print(f"Part 2: {joltage}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 3")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
