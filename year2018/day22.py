import sys
from copy import deepcopy
from functools import lru_cache
import networkx as nx

from common import load_input


def preprocess(raw):
    depth, tx, ty = map(int, raw.split())
    mx, my = int(tx * 20), int(ty * 2)
    grid = [[0 for _ in range(my + 1)] for _ in range(mx + 1)]

    # geologic index
    grid[0][0] = 0
    for ix in range(mx):
        for iy in range(my):
            if (ix, iy) in [(0, 0), (tx, ty)]:
                grid[ix][iy] = 0
            elif iy == 0:
                grid[ix][0] = ix * 16807 % 20183
            elif ix == 0:
                grid[0][iy] = iy * 48271 % 20183
            else:
                grid[ix][iy] = (
                    (grid[ix - 1][iy] + depth) * (grid[ix][iy - 1] + depth) % 20183
                )

    # erosion level = (geologic index + depth ) % 20183
    # type = erosion level % 3
    for ix in range(mx):
        for iy in range(my):
            grid[ix][iy] = (grid[ix][iy] + depth) % 20183 % 3
    return grid, tx, ty


def fn_p1(data):
    grid, tx, ty = data
    risk_level = 0
    for ix in range(0, tx + 1):
        for iy in range(0, ty + 1):
            risk_level += grid[ix][iy]
    return risk_level


def fn_p2(data):
    grid, tx, ty = data
    # neither = 0, gear = 2, torch = 1
    # draw = {0: ".", 1: "=", 2: "|"}
    # for row in grid[:30]:
    #     print("".join(draw[c] for c in row[:30]))
    tools = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    mx, my = len(grid), len(grid[0])
    g = nx.Graph()
    for x in range(mx):
        for y in range(my):
            t1, t2 = tools[grid[x][y]]
            g.add_node((x, y, t1))
            g.add_node((x, y, t2))
            g.add_edge((x, y, t1), (x, y, t2), weight=7)
            if x > 0:
                cx, cy = x - 1, y
                if grid[x][y] == grid[cx][cy]:
                    g.add_edge((cx, cy, t1), (x, y, t1), weight=1)
                    g.add_edge((cx, cy, t2), (x, y, t2), weight=1)
                else:
                    t = 3 - (grid[x][y] + grid[cx][cy])
                    g.add_edge((cx, cy, t), (x, y, t), weight=1)
            if y > 0:
                cx, cy = x, y - 1
                if grid[x][y] == grid[cx][cy]:
                    g.add_edge((cx, cy, t1), (x, y, t1), weight=1)
                    g.add_edge((cx, cy, t2), (x, y, t2), weight=1)
                else:
                    t = 3 - (grid[x][y] + grid[cx][cy])
                    g.add_edge((cx, cy, t), (x, y, t), weight=1)
    shortest = nx.shortest_path_length(
        g, source=(0, 0, 1), target=(tx, ty, 1), weight="weight"
    )
    # sp = nx.shortest_path(g, source=(0, 0, 1), target=(tx, ty, 1), weight="weight")
    # print([(x, y, t, grid[x][y]) for x, y, t in sp[:100]])
    return shortest


def main():
    raw_data = """510 10 10""".strip()
    data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = "8103 9 758".strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 7743
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1029


if __name__ == "__main__":
    main()
