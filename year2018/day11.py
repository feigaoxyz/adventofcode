import sys
from copy import deepcopy

from common import load_input


def preprocess(raw):
    s = int(raw)
    grid = dict()
    ul = dict()
    ul[(0, 0)] = 0
    for i in range(301):
        ul[(i, 0)] = ul[(0, i)] = 0
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = power_level(x, y, s)
            ul[(x, y)] = (
                ul[(x - 1, y)] + ul[(x, y - 1)] - ul[(x - 1, y - 1)] + grid[(x, y)]
            )
    return grid, ul


def power_level(x, y, serial_no):
    rack_id = x + 10
    power = (rack_id * y + serial_no) * rack_id
    power = (power // 100) % 10
    return power - 5


def test_power_level():
    assert power_level(3, 5, 8) == 4
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4


def subgrid(ul, x, y, size=3):
    lx = x + size - 1
    ly = y + size - 1
    return (
        ul[(lx, ly)]
        + ul[(lx - size, ly - size)]
        - ul[(lx - size, ly)]
        - ul[(lx, ly - size)]
    )


def fn_p1(data):
    _, ul = data
    return max(
        [(x, y) for x in range(1, 298) for y in range(1, 298)],
        key=lambda k: subgrid(ul, *k),
    )


def fn_p2(data):
    _, ul = data
    return max(
        [
            (x, y, s)
            for s in range(1, 301)
            for x in range(1, 302 - s)
            for y in range(1, 302 - s)
        ],
        key=lambda k: subgrid(ul, *k),
    )


if __name__ == "__main__":
    raw_data = """42
    """.strip()
    # data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(deepcopy(data)))
    # print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer: 241,40
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 166,75,12
