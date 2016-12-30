import math
import sys
from collections import defaultdict
from collections import deque

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

with open(fn) as f:
    for line in f:
        items.append(line.split(','))

import functools


@functools.lru_cache(maxsize=1024)
def is_open(x, y):
    # fav = 10
    fav = 1358

    if x < 0 or y < 0:
        return False
    s = x * x + 3 * x + 2 * x * y + y + y * y
    s += fav
    bits = bin(s).count('1')
    if bits % 2 == 0:
        return True
    else:
        return False


# for y in range(7):
#     print(''.join('.' if is_open(x, y) else '#' for x in range(10)))

dis = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def part1(tx, ty):
    cx, cy = 1, 1
    distance = defaultdict(lambda: math.inf)
    distance[(cx, cy)] = 0
    q = deque()
    q.append((cx, cy))

    while True:
        # print(q)
        cx, cy = q.popleft()
        for dx, dy in dis:
            nx, ny = cx + dx, cy + dy
            if is_open(nx, ny):
                d = distance[(cx, cy)] + 1
                if d < distance[(nx, ny)]:
                    q.append((nx, ny))
                    distance[(nx, ny)] = d
                if (nx, ny) == (tx, ty):
                    return d


r1 = part1(31, 39)


def part2(step):
    cx, cy = 1, 1
    distance = defaultdict(lambda: math.inf)
    distance[(cx, cy)] = 0
    q = deque()
    q.append((cx, cy))
    count = 1

    while q:
        # print(q)
        cx, cy = q.popleft()
        for dx, dy in dis:
            nx, ny = cx + dx, cy + dy
            if is_open(nx, ny):
                d = distance[(cx, cy)] + 1
                if d < distance[(nx, ny)] and d <= step:
                    q.append((nx, ny))
                    distance[(nx, ny)] = d
                    count += 1

    return count


r2 = part2(50)

print('Part One:', r1)
print('Part Two:', r2)
