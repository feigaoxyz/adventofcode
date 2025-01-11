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
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()


def preprocess(raw: str):
    lns = raw.split()
    m = len(lns)
    n = len(lns[0])
    mp = defaultdict(list)
    for r, ln in enumerate(lns):
        for c, chr in enumerate(ln):
            if chr != ".":
                mp[chr].append((r, c))
    return (m, n, mp)


def fn_p1(data):
    m, n, mp = data
    antinodes = set()
    for ch in mp:
        locs = mp[ch]
        for i in range(len(locs) - 1):
            ri, ci = locs[i]
            for j in range(i + 1, len(locs)):
                rj, cj = locs[j]
                r1, c1 = 2 * ri - rj, 2 * ci - cj
                if 0 <= r1 < m and 0 <= c1 < n:
                    antinodes.add((r1, c1))
                r1, c1 = 2 * rj - ri, 2 * cj - ci
                if 0 <= r1 < m and 0 <= c1 < n:
                    antinodes.add((r1, c1))
    return len(antinodes)


def fn_p2(data):
    m, n, mp = data
    antinodes = set()
    for ch in mp:
        locs = mp[ch]
        for i in range(len(locs) - 1):
            ri, ci = locs[i]
            antinodes.add((ri, ci))
            for j in range(i + 1, len(locs)):
                rj, cj = locs[j]
                dr, dc = rj - ri, cj - ci
                r1, c1 = ri, ci
                while 0 <= r1 < m and 0 <= c1 < n:
                    antinodes.add((r1, c1))
                    r1 += dr
                    c1 += dc
                r1, c1 = ri, ci
                while 0 <= r1 < m and 0 <= c1 < n:
                    antinodes.add((r1, c1))
                    r1 -= dr
                    c1 -= dc

    return len(antinodes)


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 14
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 34

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 269
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 949
