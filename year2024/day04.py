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


def get_primary_diagonals(matrix):
    """
    Returns all top-left to bottom-right diagonals of a 2D matrix.
    Diagonals are grouped by (column - row) offsets.
    """
    from collections import defaultdict

    n = len(matrix)
    m = len(matrix[0])
    diagonals = defaultdict(list)

    for i in range(n):
        for j in range(m):
            offset = j - i
            diagonals[offset].append(matrix[i][j])

    # Sort by offset to preserve a clear left-to-right ordering
    sorted_offsets = sorted(diagonals.keys())
    return [diagonals[offset] for offset in sorted_offsets]


def get_secondary_diagonals(matrix):
    """
    Returns all top-right to bottom-left diagonals of a 2D matrix.
    Diagonals are grouped by (row + column) sums.
    """
    from collections import defaultdict

    n = len(matrix)
    m = len(matrix[0])
    diagonals = defaultdict(list)

    for i in range(n):
        for j in range(m):
            offset = i + j
            diagonals[offset].append(matrix[i][j])

    # Sort by offset to preserve a top-to-bottom ordering
    sorted_offsets = sorted(diagonals.keys())
    return [diagonals[offset] for offset in sorted_offsets]


def preprocess(raw: str):
    return raw.split()


def fn_p1(matrix) -> int:
    # rows
    rt = [matrix]
    # columns
    rt.append([list(row) for row in zip(*matrix)])
    # diag
    rt.append(get_primary_diagonals(matrix))
    # anti-diag
    rt.append(get_secondary_diagonals(matrix))

    # reverse order of rows, columns, diagonals, anti_diag
    rt.extend([[r[::-1] for r in m] for m in rt])

    data = [["".join(r) for r in m] for m in rt]
    rt = 0
    for m in data:
        for r in m:
            rt += r.count("XMAS")
            # rt += r.count("SAMX")
    return rt


def fn_p1_v2(m: str) -> int:
    lr = len(m)
    lc = len(m[0])
    # print(lr, lc)
    rt = 0
    dirs = [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1] if (a, b) != (0, 0)]
    # print(dirs, len(dirs))

    for r in range(lr):
        for c in range(lc):
            # if m[r][c] == "X":
            for dr, dc in dirs:
                if 0 <= r + dr * 3 < lr and 0 <= c + dc * 3 < lc:
                    t4 = tuple(m[r + dr * i][c + dc * i] for i in range(4))
                    if "".join(t4) == "XMAS":
                        rt += 1

    return rt


def fn_p2(m):
    lr = len(m)
    lc = len(m[0])

    rt = 0
    for r in range(1, lr - 1):
        for c in range(1, lc - 1):
            if m[r][c] == "A":
                diag1 = "".join([m[r - 1][c - 1], m[r][c], m[r + 1][c + 1]])
                diag2 = "".join([m[r - 1][c + 1], m[r][c], m[r + 1][c - 1]])
                if (diag1 == "MAS" or diag1 == "SAM") and (
                    diag2 == "MAS" or diag2 == "SAM"
                ):
                    rt += 1

    return rt


raw_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()

if __name__ == "__main__":
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # 18
    print("Part 1 Example:", fn_p1_v2(deepcopy(data)))  # 18
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer:
    print("Part 1:", fn_p1_v2(deepcopy(data)))  # answer: 2532
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1941
