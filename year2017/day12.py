from common import load_input
from collections import defaultdict

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""

example = """
0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
""".strip()
input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()


def group_of_seed(neighbor: dict, seed: str = '0') -> int:
    group = set()
    front = {seed}
    while front:
        v = front.pop()
        group.add(v)
        for t in neighbor[v]:
            if t not in group:
                front.add(t)
    return group


def build_neighbor(raw):
    neighbor = defaultdict(list)
    for line in raw.splitlines():
        l, r = line.split(' <-> ')
        r = r.split(', ')
        neighbor[l] = r
    return neighbor


def fn_p1(raw):
    neighbor = build_neighbor(raw)
    return len(group_of_seed(neighbor, '0'))


print("Part 1 example:", fn_p1(example))
print("Part 1:", fn_p1(input_data))  # 152


def fn_p2(raw: str) -> int:
    neighbor = build_neighbor(raw)
    ids = set(neighbor.keys())
    count = 0
    while ids:
        pick = ids.pop()
        group = group_of_seed(neighbor, pick)
        ids -= group
        count += 1
    return count


print("Part 2 example:", fn_p2(example))
print("Part 2:", fn_p2(input_data))  # 186
