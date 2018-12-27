import sys
from copy import deepcopy

from common import load_input

OPEN, TREE, LUMBER = ".", "|", "#"


def preprocess(raw):
    grid = dict()
    for r, row in enumerate(raw.splitlines()):
        for c, cell in enumerate(row):
            grid[(r, c)] = cell
    return grid


def neighbors(grid, r, c):
    return [
        grid[(r + dr, c + dc)]
        for dr in [-1, 0, 1]
        for dc in [-1, 0, 1]
        if not (dr == 0 == dc) and (r + dr, c + dc) in grid
    ]


def fn_p1(grid):
    time = 10
    for _ in range(time):
        new_grid = dict()
        for (r, c) in grid:
            cell = grid[(r, c)]
            nbs = neighbors(grid, r, c)
            if cell == OPEN:
                new_cell = TREE if nbs.count(TREE) >= 3 else cell
            elif cell == TREE:
                new_cell = LUMBER if nbs.count(LUMBER) >= 3 else cell
            elif cell == LUMBER:
                new_cell = (
                    LUMBER if nbs.count(LUMBER) >= 1 and nbs.count(TREE) >= 1 else OPEN
                )
            new_grid[(r, c)] = new_cell
        grid = deepcopy(new_grid)
    cells = list(grid.values())
    return cells.count(TREE) * cells.count(LUMBER)


def fn_p2(grid):
    # time = 1000000000
    time = 496
    records = dict()
    for step in range(time):
        kvs = list(grid.items())
        kvs.sort()
        pattern = "".join(v for _, v in kvs)
        if pattern not in records:
            records[pattern] = [step]
        else:
            records[pattern].append(step)
            print(records[pattern])

        new_grid = dict()
        for (r, c) in grid:
            cell = grid[(r, c)]
            nbs = neighbors(grid, r, c)
            if cell == OPEN:
                new_cell = TREE if nbs.count(TREE) >= 3 else cell
            elif cell == TREE:
                new_cell = LUMBER if nbs.count(LUMBER) >= 3 else cell
            elif cell == LUMBER:
                new_cell = (
                    LUMBER if nbs.count(LUMBER) >= 1 and nbs.count(TREE) >= 1 else OPEN
                )
            new_grid[(r, c)] = new_cell
        grid = deepcopy(new_grid)
    # same pattern repeats after 471 with cycle length 56
    # so 1000000000 is same as 496
    cells = list(grid.values())
    return cells.count(TREE) * cells.count(LUMBER)


if __name__ == "__main__":
    raw_data = """
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.""".strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    # print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 466125
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 207998
