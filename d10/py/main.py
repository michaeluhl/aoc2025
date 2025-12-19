from collections import OrderedDict
from typing import Self


class Machine:
    def __init__(
        self,
        lights: int,
        nlights: int,
        buttons: tuple[int, ...],
        joltage: tuple[int, ...],
    ):
        self.lights = lights
        self.nlights = nlights
        self.buttons = buttons
        self.joltage = joltage

    @classmethod
    def from_input(cls, line: str) -> Self:
        lights: int = 0
        nlights: int = 0
        buttons: list[int] = []
        joltage: tuple[int, ...] = tuple()

        for section in line.strip().split(" "):
            if "[" in section:
                for i, c in enumerate(section.strip("[]")):
                    if c == "#":
                        lights |= 1 << i
                    nlights += 1
            elif "(" in section:
                button = 0
                for i, v in enumerate(section.strip("()").split(",")):
                    button |= 1 << int(v)
                buttons.append(button)
            elif "{" in section:
                joltage = tuple([int(v) for v in section[1:-1].split(",")])
        return cls(lights, nlights, tuple(buttons), joltage)

    def btn_mtx(self) -> list[list[int]]:
        mtx: list[list[int]] = []
        for btn in self.buttons:
            row = self.nlights * [0]
            for i in range(self.nlights):
                if btn & (1 << i):
                    row[i] = 1
            mtx.append(row)
        mtx.append(list(self.joltage))
        return mtx

    def __repr__(self) -> str:
        buttons = ",".join([f"{b:02x}" for b in self.buttons])
        return f"<Machine({self.lights:02x}, {buttons}, {self.joltage})>"


def main(options):
    data: list[Machine] = []

    with open(options.DATA, "rt") as input_file:
        data: list[Machine] = [Machine.from_input(line) for line in input_file]

    pushes = 0
    for mach in data:
        allb = set(mach.buttons)
        cache: OrderedDict[frozenset[int], int] = OrderedDict(
            (frozenset((b,)), b) for b in mach.buttons
        )
        if mach.lights in cache.values():
            pushes += 1
            continue

        while cache:
            s, v = cache.popitem(last=False)
            for b in allb - s:
                nv = v ^ b
                if nv == mach.lights:
                    pushes += len(s) + 1
                    break
                cache[frozenset(s | set((b,)))] = nv
            else:
                continue
            break

    print(f"Part 1: {pushes}")

    push_cts: list[int] = []
    for mach in data:
        print(mach)
        *rows, b = mach.btn_mtx()
        queue: OrderedDict[tuple[int, ...], int] = OrderedDict({tuple(b): 0})
        startrows: dict[tuple[int, ...], list[list[int]]] = {tuple(b): rows}
        while queue:
            counters, pushes = queue.popitem(last=False)
            zeros: list[int] = [i for i, c in enumerate(counters) if c == 0]
            srows = startrows.pop(counters)
            srows: list[list[int]] = [r for r in srows if all(r[z] == 0 for z in zeros)]

            for row in srows:
                res: tuple[int, ...] = tuple([c - v for c, v in zip(counters, row)])
                if any(r < 0 for r in res):
                    continue
                elif all(r == 0 for r in res):
                    # Found solution
                    push_cts.append(pushes + 1)
                    print("Found solution")
                    break
                elif res in queue:
                    continue
                else:
                    queue[res] = pushes + 1
                    startrows[res] = srows
            else:
                continue
            break
        else:
            print("Found no solution")
    print(f"Part 2: {sum(push_cts)}")


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description="AoC 2025 Day 10")
    parser.add_argument("DATA", type=str, help="Path to data file")

    main(parser.parse_args())
