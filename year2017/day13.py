from common import load_input
import itertools

PART1_DOC = """Part 1:
the depth of each layer and the range of scanning area.
Within each layer, a security scanner moves back and forth within its range.
Each picosecond, the packet moves one layer forward (its first move takes
it into layer 0), and then the scanners move one step. If there is a scanner
at the top of the layer as your packet enters it, you are caught.

The severity of getting caught on a layer is equal to its depth multiplied
by its range.
"""

PART2_DOC = """Part 2:
What is the fewest number of picoseconds that you need to delay the packet
to pass through the firewall without being caught?
"""

example = """
0: 3
1: 2
4: 4
6: 4
""".strip()
input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()


def is_caught(depth: int, height: int, delay: int = 0) -> bool:
    return (depth + delay) % (height * 2 - 2) == 0


def fn_p1(raw: str) -> int:
    severity = 0
    for line in raw.splitlines():
        depth, height = map(int, line.split(':'))
        severity += depth * height * is_caught(depth, height)
    return severity


print("Part 1 example:", fn_p1(example))
print("Part 1:", fn_p1(input_data))  # 648


def fn_p2(raw: str) -> int:
    lines = [(int(l.split(':')[0]), int(l.split(':')[1]))
             for l in raw.splitlines()]
    return next(itertools.dropwhile(
                lambda t: any(is_caught(d, r, t) for (d, r) in lines),
                itertools.count()))


print("Part 2 example:", fn_p2(example))
print("Part 2:", fn_p2(input_data))  # 3933124
