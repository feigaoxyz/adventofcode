from common import load_input
from day10 import knot_hash_full

PART1_DOC = """Part 1:
For i in 0..127, how many '1' in 128 knot hashes (day 10) of
strings "INPUT-$i"?
"""

PART2_DOC = """Part 2:
Return number of connected components (4-direction) of 1's
"""


def disk_grid_recover(raw: str) -> list:
    grid = []
    for i in range(128):
        hash = knot_hash_full('{}-{}'.format(raw, i))
        grid.append([int(c) for c in '{:0>128b}'.format(int('0x' + hash, 16))])
    return grid


def fn_p1(raw):
    return sum(map(sum, disk_grid_recover(raw)))


def fn_p2(raw):
    grid = disk_grid_recover(raw)
    return len(connected_components(grid))


def connected_components(grid):
    remain: set = set([(r, c)
                       for r in range(len(grid)) for c in range(len(grid[r]))
                       if grid[r][c] == 1])
    marked: set = set()
    ccs = []
    while remain:
        ccs.append(set())
        p = remain.pop()
        working = {p}
        while working:
            t = working.pop()
            marked.add(t)
            ccs[-1].add(t)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = t[0] + dr, t[1] + dc
                if (r, c) in remain:
                    remain.remove((r, c))
                    working.add((r, c))
    # print(len(marked), len(ccs))
    return ccs


def test_connected_component():
    assert len(connected_components([[1, 0], [0, 1]])) == 2
    assert len(connected_components([[1, 1], [0, 1]])) == 1
    assert len(connected_components([[1, 1, 1], [0, 0, 1], [0, 1, 1]])) == 1
    pass


if __name__ == '__main__':
    example = """flqrgnkx
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example))  # 8108
    # print("Part 1:", fn_p1(input_data))  # 8216

    print("Part 2 example:", fn_p2(example))  # 1242
    print("Part 2:", fn_p2(input_data))  # 1139
