import sys
from copy import deepcopy
from collections import defaultdict

from common import load_input


def dist(p1, p2):
    return sum(abs(x - y) for x, y in zip(p1, p2))


def preprocess(raw):
    pts = [list(map(int, line.split(","))) for line in raw.splitlines()]
    return pts


def fn_p1(data):
    close = defaultdict(set)
    for i1 in range(len(data)):
        for i2 in range(i1 + 1, len(data)):
            if dist(data[i1], data[i2]) <= 3:
                close[i1].add(i2)
                close[i2].add(i1)
    components = []
    seen = set()
    unseen = set(range(len(data)))
    while unseen:
        p = unseen.pop()
        front = set([p])
        cons = set()
        while front:
            p = front.pop()
            seen.add(p)
            cons.add(p)
            for q in close[p]:
                if q in unseen:
                    unseen.remove(q)
                    front.add(q)
        components.append(cons)
    return len(components)


def fn_p2(data):
    return


if __name__ == "__main__":
    raw_data = """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
    """.strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 399
    print("Part 2:", fn_p2(deepcopy(data)))  # answer:
