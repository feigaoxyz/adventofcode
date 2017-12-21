from common import load_input

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


def subgrid2by2(grid: list) -> list:
    ans = []
    for first_row, second_row in zip(grid[::2], grid[1::2]):
        ans.append([])
        for i in range(0, len(first_row), 2):
            ans[-1].append(first_row[i:i + 2] + '/' + second_row[i:i + 2])
    return ans


def subgrid3by3(grid: list) -> list:
    ans = []
    for first_row, second_row, third_row in zip(grid[::3], grid[1::3],
                                                grid[2::3]):
        ans.append([])
        for i in range(0, len(first_row), 3):
            ans[-1].append(first_row[i:i + 3] + '/' + second_row[i:i + 3] + '/'
                           + third_row[i:i + 3])
    return ans


def subgrid(grid, size):
    if size == 2:
        return subgrid2by2(grid)
    else:
        return subgrid3by3(grid)


def restore_grid(grid):
    ans = []
    for row in grid:
        for one in zip(*[sub.split('/') for sub in row]):
            ans.append(''.join(one))
    return ans


def test_subgrid():
    g6 = ['##.##.', '#..#..', '......', '##.##.', '#..#..', '......']
    g2 = subgrid2by2(g6)
    assert len(g2) == 3
    assert len(g2[0]) == 3
    assert len(g2[0][0]) == 5
    assert restore_grid(g2) == g6
    g3 = subgrid3by3(g6)
    assert len(g3) == 2
    assert len(g3[0]) == 2
    assert len(g3[0][0]) == 11
    assert restore_grid(g3) == g6


def rotate(s: list, size) -> list:
    t = s.copy()
    for i in range(size):
        t[i::size] = s[size * (size - i - 1):size * (size - i)]
    # print('in rotate', s, t)
    return t


def flip(s: list, size) -> list:
    t = s.copy()
    for i in range(size):
        t[i * size:(i + 1) * size] = s[size * (size - i - 1):size * (size - i)]
    # print('in flip', s, t)
    return t


def transform(pattern: str, size: int = 2):
    start = []
    ans = []
    for row in pattern.split('/'):
        start.extend(list(row))
    temp = start.copy()
    for _ in range(4):
        temp = rotate(temp, size)
        for _ in range(2):
            temp = flip(temp, size)
            s = ''.join(temp)
            if size == 3:
                ans.append('/'.join([s[:3], s[3:6], s[6:]]))
            else:
                ans.append('/'.join([s[:2], s[2:]]))
    # print('in tranform', pattern, ans)
    return ans


def test_tranform():
    g4 = list(range(4))
    g9 = list(range(1, 10))
    assert rotate(g4, 2) == [2, 0, 3, 1]
    assert flip(g4, 2) == [2, 3, 0, 1]
    assert rotate(g9, 3) == [7, 4, 1, 8, 5, 2, 9, 6, 3]
    assert flip(g9, 3) == [7, 8, 9, 4, 5, 6, 1, 2, 3]


def enhance(grid, size, rules: dict):
    ans = []
    for row in grid:
        ans.append([])
        for sub in row:
            # print('tranform', grid, sub)
            for p in transform(sub, size):
                # print('tranform', grid, sub, p)
                if p in rules:
                    ans[-1].append(rules[p])
                    break
    return ans


def fn_p1(starter, rule_raw: str, round: int = 5):
    grid = starter[::]
    rules = dict([line.split(' => ') for line in rule_raw.splitlines()])
    # print(grid, rules)
    for _ in range(round):
        size = 2 if len(grid) % 2 == 0 else 3
        sub = subgrid(grid, size)
        # print('sub', sub)
        larger = enhance(sub, size, rules)
        # print('enhanced', larger)
        grid = restore_grid(larger)
        # print('grid:\n', '\n'.join(grid))
    return sum(row.count('#') for row in grid)


if __name__ == '__main__':
    starter = [".#.", "..#", "###"]
    example = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    print("Part 1 example:", fn_p1(starter, example))
    print("Part 1:", fn_p1(starter, input_data))  # 173

    # print("Part 2 example:", fn_p2(example))
    print("Part 2:", fn_p1(starter, input_data, 18))  # 2456178
