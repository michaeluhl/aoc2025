def main(options): ...


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day {day}")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
