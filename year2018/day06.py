import sys
from functools import partial
from itertools import chain

from common import load_input, sorted2


def preprocess(raw):
    return [(i, list(map(int, l.split(",")))) for (i, l) in enumerate(raw.splitlines())]


def ham_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def fn_p1(data):
    marks = [0 for _ in data]
    counter = 0
    size = max(chain.from_iterable(p[1] for p in data)) + 1
    for y in range(size):
        for x in [0, size]:
            dists = sorted2([(i, ham_dist([x, y], p2)) for (i, p2) in data])
            marks[dists[0][0]] = -size * size
    for x in range(size):
        for y in [0, size]:
            dists = sorted2([(i, ham_dist([x, y], p2)) for (i, p2) in data])
            marks[dists[0][0]] = -size * size
    for x in range(size):
        for y in range(size):
            dists = sorted2([(i, ham_dist([x, y], p2)) for (i, p2) in data])
            if dists[0][1] < dists[1][1]:
                marks[dists[0][0]] += 1
            if sum(d for _, d in dists) < 10000:
                counter += 1
    return max(marks), counter


def fn_p2(data):
    return


if __name__ == "__main__":
    raw_data = """
    1, 1
    1, 6
    8, 3
    3, 4
    5, 5
    8, 9
    """.strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(data))
    print("Part 2 Example:", fn_p2(data))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(data))  # answer: 3223
    print("Part 2:", fn_p2(data))  # answer: 40495
