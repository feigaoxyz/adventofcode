from common import load_input

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


def routing(raw: str):
    grid = [list(line) for line in raw.splitlines()]
    rows = len(grid)
    cols = max(map(len, grid))
    for row in grid:
        while len(row) < cols:
            row.append(' ')
    for ci, ch in enumerate(grid[0]):
        if ch != ' ':
            entry = (0, ci)
            break
    face = (1, 0)
    route = [entry]
    letters = []
    while True:
        sr, sc = route[-1]
        if grid[sr][sc] not in "+-|":
            letters.append(grid[sr][sc])
        if grid[sr][sc] == '+':
            # print('debug2:', rows, cols, face, sr, sc, grid[sr][sc+1])
            if face[0] != 0:
                if 0 <= sc + 1 < cols and grid[sr][sc + 1] != ' ':
                    face = (0, 1)
                elif 0 <= sc - 1 and grid[sr][sc - 1] != ' ':
                    face = (0, -1)
            else:
                if sr + 1 < rows and grid[sr + 1][sc] != ' ':
                    face = (1, 0)
                elif 0 <= sr - 1 and grid[sr - 1][sc] != ' ':
                    face = (-1, 0)
        nr, nc = sr + face[0], sc + face[1]
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != ' ':
            route.append((nr, nc))
        else:
            break

    return ''.join(letters), len(route)


def fn_p1(raw):
    return routing(raw)[0]

def fn_p2(raw: str):
    return routing(raw)[1]


if __name__ == '__main__':
    example = """\
     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
    """
    input_data = load_input(__file__.split('.')[0] + '_in.txt')

    print("Part 1 example:", fn_p1(example))  # ABCDEF
    print("Part 1:", fn_p1(input_data))  # GINOWKYXH

    print("Part 2 example:", fn_p2(example))  # 38
    print("Part 2:", fn_p2(input_data))  # 16636
