import logging
import sys
from collections import Counter, deque
from itertools import permutations

logging.basicConfig(level=logging.DEBUG)

try:
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__.split('.')[0] + '_input.txt'

    grid = []

    with open(fn) as f:
        for line in f:
            grid.append(line)
except FileNotFoundError:
    pass

logging.info(Counter(''.join(grid)).most_common())  # numbers: 0 - 7

locations = dict()
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit():
            locations[ch] = (r, c)

logging.info(locations)


def one2all(start):
    start_pos = locations[start]

    seen = {start_pos}
    queue = deque([(locations[start], 0)])
    result = dict()

    while queue:
        (r, c), dis = queue.popleft()
        ch = grid[r][c]
        if ch.isdigit():
            result[ch] = dis
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = dr + r, dc + c
            ch = grid[nr][nc]  # type: str
            if ch != '#' and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append(((nr, nc), dis + 1))

    return result


distances = dict()
for start in locations:
    distances[start] = one2all(start)

logging.info(distances['0'])


def solution(back=False):
    keys = list(locations.keys())
    keys.remove('0')
    best_dis = float('inf')
    best_route = None
    for seq in permutations(keys):
        dis = sum(distances[a][b] for a, b in
                  zip(('0',) + seq,
                      seq + ('0',) if back else seq))
        if dis < best_dis:
            best_dis = dis
            best_route = seq
    return best_dis, best_route


r1 = solution()
print('Part One:', r1)  # 518

r2 = solution(back=True)
print('Part Two:', r2)  # 716
