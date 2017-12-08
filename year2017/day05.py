from common import load_input

input_data = load_input(__file__.split('.')[0] + '_in.txt')

PART1_DOC = """
The goal is to follow the jumps until one leads outside the list.
In addition, these instructions are a little strange; after each jump, the
offset of that instruction increases by 1.

Part 1: How many steps does it take to reach the exit?
"""


def jump_offsets(offsets: list) -> int:
    p = 0
    steps = 0
    while 0 <= p < len(offsets):
        offsets[p] += 1
        p += offsets[p] - 1
        steps += 1
    return steps


input_data = list(map(int, input_data.splitlines()))
print("Part 1:", jump_offsets(input_data[::]))  # 376976


def test_part1():
    assert jump_offsets([0, 3, 0, 1, -3]) == 5


PART2_DOC = """
Part 2:
"""


def jump_offsets_part2(offsets: list) -> int:
    p = 0
    steps = 0
    while 0 <= p < len(offsets):
        jump = offsets[p]
        if (jump) >= 3:
            offsets[p] -= 1
        else:
            offsets[p] += 1
        p += jump
        steps += 1
    # print(offsets)
    return steps


def test_part2():
    assert jump_offsets_part2([0, 3, 0, 1, -3]) == 10


print("Part 2:", jump_offsets_part2(input_data[::]))  # 29227751
