import sys
from collections import deque

try:
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__.split('.')[0] + '_input.txt'

    lines = []

    with open(fn) as f:
        for line in f:
            lines.append(line.split(','))
except FileNotFoundError:
    pass

# passcode = 'kglvqrro'

passcode = 'bwnlcvfs'

from hashlib import md5
from functools import lru_cache


@lru_cache(maxsize=1024)
def doors_open(path: str):
    hash = md5(path.encode())
    hash = hash.hexdigest()[:4]
    is_open = lambda c: True if c > 'a' else False
    return dict((d, is_open(c)) for d, c in zip('UDLR', hash))


# print(doors_open(passcode))


def solution(*args, **kws):
    position = 0, 0
    target = 3, 3

    queue = deque([])
    queue.append((passcode, *position))

    dxy = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    while queue:
        path, cx, cy = queue.popleft()
        if (cx, cy) == target:
            return path[len(passcode):]
        doors = doors_open(path)
        for d in doors:
            if doors[d]:
                dx, dy = dxy[d]
                nx, ny = cx + dx, cy + dy
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    queue.append((path + d, nx, ny))


r1 = solution()
print('Part One:', r1)  # DDURRLRRDD


def solution2(*args, **kws):
    position = 0, 0
    target = 3, 3
    longest = 0

    queue = deque([])
    queue.append((passcode, *position))

    dxy = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    while queue:
        path, cx, cy = queue.popleft()
        if (cx, cy) == target:
            longest = max(longest, len(path) - len(passcode))
            continue
        doors = doors_open(path)
        for d in doors:
            if doors[d]:
                dx, dy = dxy[d]
                nx, ny = cx + dx, cy + dy
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    queue.append((path + d, nx, ny))
    return longest


r2 = solution2()
print('Part Two:', r2)  # 436
