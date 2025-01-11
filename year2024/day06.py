import sys
from copy import deepcopy


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


rotates = [(0, -1), (1, 0), (0, 1), (-1, 0)][::-1]


def preprocess(raw: str):
    lns = [list(row) for row in raw.split()]
    m = len(lns)
    n = len(lns[0])
    for r in range(m):
        for c in range(n):
            ch = lns[r][c]
            if ch == "^":
                return (lns, (r, c, 0))


def run(mp, init_st, visited=None):
    (r, c, d) = init_st
    m, n = len(mp), len(mp[0])

    if visited is None:
        visited = list()

    while (r, c, d) not in visited:
        visited.append((r, c, d))
        nr, nc, nd = r + rotates[d][0], c + rotates[d][1], (d + 1) % 4
        if (0 <= nr < m) and (0 <= nc < n):  # in board
            if mp[nr][nc] == "#":  # next step is obstacle
                # -> turn right
                d = nd
            else:  # next step is not obstacle
                # -> step forward
                r, c = nr, nc
        else:  # step out of board
            return True, visited
    # loop
    return False, visited


def fn_p1(data):
    mp, (r, c, d) = data
    return len(set([(r, c) for (r, c, _) in run(mp, (r, c, d))[1]]))


def fn_p2(data):
    mp, st = data
    visited = run(mp, st)[1]

    tested = set()
    result = 0

    for i in range(1, len(visited)):
        r, c, d = visited[i - 1]
        nr, nc, _ = visited[i]
        if (nr, nc) in tested:
            continue
        else:
            tested.add((nr, nc))

            mp2 = deepcopy(mp)
            mp2[nr][nc] = "#"
            visited2 = deepcopy(visited[: i - 1])
            if not run(mp2, (r, c, d), visited2)[0]:
                # print(nr, nc)
                result += 1

    return result


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 41
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 6

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 4973
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1482
