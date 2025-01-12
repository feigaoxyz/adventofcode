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
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()


def preprocess(raw: str):
    mt = raw.split()
    return mt


d4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def fn_p1(mt):
    # print(mt)
    m = len(mt)
    n = len(mt[0])
    seen = set()
    regions = list()
    for r in range(m):
        for c in range(n):
            if (r, c) not in seen:
                todo = [(r, c)]
                reg = []
                while todo:
                    (i, j), *todo = todo
                    if (i, j) in seen:
                        continue
                    reg.append((i, j))
                    seen.add((i, j))
                    for di, dj in d4:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            if mt[i][j] == mt[ni][nj] and (ni, nj) not in todo:
                                todo.append((ni, nj))
                regions.append(reg)
    # print("regs", regions)

    result = 0
    for reg in regions:
        area = len(reg)
        perimeter = 4 * area
        for r1, c1 in reg:
            for r2, c2 in reg:
                if abs(r1 - r2) + abs(c1 - c2) == 1:
                    perimeter -= 1
        result += area * perimeter
    return result


def n4(r, c):
    return [((r + dr), (c + dc)) for (dr, dc) in d4]


def fn_p2(mt):
    # print(mt)
    m = len(mt)
    n = len(mt[0])
    seen = set()
    regions = list()
    for r in range(m):
        for c in range(n):
            if (r, c) not in seen:
                todo = [(r, c)]
                reg = []
                while todo:
                    (i, j), *todo = todo
                    if (i, j) in seen:
                        continue
                    reg.append((i, j))
                    seen.add((i, j))
                    for di, dj in d4:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            if mt[i][j] == mt[ni][nj] and (ni, nj) not in todo:
                                todo.append((ni, nj))
                regions.append(reg)
    # print("regs", regions)

    result = 0
    for reg in regions:
        area = len(reg)
        sides = 0
        bounds = set()
        for r, c in reg:
            for nr, nc in n4(r, c):
                if (nr, nc) not in reg:
                    bounds.add((r, c, nr, nc))
        # print(reg, bounds)
        while bounds:
            (ri, ci, ro, co) = bounds.pop()
            sides += 1
            todo = [(ri, ci, ro, co)]
            while todo:
                (r1, c1, r2, c2), *todo = todo
                if r1 == r2:
                    nt = (r1 + 1, c1, r2 + 1, c2)
                    if nt in bounds:
                        bounds.remove(nt)
                        todo.append(nt)
                    nt = (r1 - 1, c1, r2 - 1, c2)
                    if nt in bounds:
                        bounds.remove(nt)
                        todo.append(nt)
                elif c1 == c2:
                    nt = (r1, c1 + 1, r2, c2 + 1)
                    if nt in bounds:
                        bounds.remove(nt)
                        todo.append(nt)
                    nt = (r1, c1 - 1, r2, c2 - 1)
                    if nt in bounds:
                        bounds.remove(nt)
                        todo.append(nt)
        result += area * sides
        # print(reg, sides)
    return result


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 1930
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 1206

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer: 1363484
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 838988
