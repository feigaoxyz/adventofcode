from collections import defaultdict
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
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()


def preprocess(raw: str):
    mat = raw.split()
    mp = defaultdict(set)
    for r, ln in enumerate(mat):
        for c, x in enumerate(ln):
            mp[x].add((r, c))
    # print(mat, mp)
    return mat, mp


dd = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def fn_p1(data):
    mat, mp = data
    m = len(mat)
    n = len(mat[0])
    st = [[set() for _ in range(n)] for _ in range(m)]
    for tr, tc in mp["9"]:
        st[tr][tc].add((tr, tc))

    for num in range(8, -1, -1):
        for r, c in mp[str(num)]:
            for dr, dc in dd:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == str(num + 1):
                    st[r][c] |= st[nr][nc]
    rt = 0
    for r, c in sorted(mp["0"]):
        # print(r, c, len(st[r][c]), st[r][c])
        rt += len(st[r][c])

    # for r in range(5, 8):
    #     for c in range(4):
    #         print("debug:", r, c, mat[r][c], st[r][c])
    return rt


def fn_p2(data):
    mat, mp = data
    m = len(mat)
    n = len(mat[0])
    st = [[set() for _ in range(n)] for _ in range(m)]
    for tr, tc in mp["9"]:
        st[tr][tc].add(((tr, tc),))

    for num in range(8, -1, -1):
        for r, c in mp[str(num)]:
            for dr, dc in dd:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == str(num + 1):
                    for trail in st[nr][nc]:
                        st[r][c].add(((r,c), *trail))
    rt = 0
    for r, c in sorted(mp["0"]):
        # print(r, c, len(st[r][c]), st[r][c])
        rt += len(st[r][c])

    # for r in range(5, 8):
    #     for c in range(4):
    #         print("debug:", r, c, mat[r][c], st[r][c])
    return rt


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 36
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 81

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer: 798
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1816
