from common import load_input
import math
import collections

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""

example = """
"""
input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

dir2pos = {
    'ne': (1, 0),
    'n': (0, 1),
    'nw': (-1, 1),
    's': (0, -1),
    'sw': (-1, 0),
    'se': (1, -1)
}


def hex_distance(steps: str, init_pos: (int, int) = (0, 0)) -> (int, (int, int)):
    # print(collections.Counter(steps.split(',')))
    x, y = init_pos
    for step in steps.split(','):
        dx, dy = dir2pos[step]
        x += dx
        y += dy
    if x * y >= 0:
        return (abs(x) + abs(y), (x, y))
    else:
        return max(abs(x), abs(y)), (x, y)


fn_p1 = hex_distance
print("Part 1 example:", fn_p1("ne,ne,ne"))
print("Part 1 example:", fn_p1("ne,ne,sw,sw"))
print("Part 1 example:", fn_p1("ne,ne,s,s"))
print("Part 1 example:", fn_p1("se,sw,se,sw,sw"))
print("Part 1:", fn_p1(input_data))  # 682


def furthest(steps: str) -> int:
    pos = (0, 0)
    max_dist = 0
    for step in steps.split(','):
        dist, pos = hex_distance(step, pos)
        if dist > max_dist:
            max_dist = dist
    return max_dist


fn_p2 = furthest
# print("Part 2 example:", fn_p2(example))
print("Part 2:", fn_p2(input_data))  # 1406
