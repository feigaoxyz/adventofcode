import sys
import re
from copy import deepcopy
from collections import namedtuple
from functools import lru_cache

import networkx as nx

from common import load_input

Bot = namedtuple("Bot", "x y z r".split())


def preprocess(raw):
    pts = [Bot(*map(int, re.findall(r"([0-9\-]+)", line))) for line in raw.splitlines()]
    return pts


@lru_cache(1024 * 1024)
def dist(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y) + abs(p1.z - p2.z)


def fn_p1(pts):
    big = max(pts, key=lambda p: p.r)
    count = 0
    for p in pts:
        if dist(p, big) <= big.r:
            count += 1
    return count


def fn_p2(pts):
    pass


if __name__ == "__main__":
    raw_data = """
pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5""".strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 232
    print("Part 2:", fn_p2(deepcopy(data)))  # answer:
