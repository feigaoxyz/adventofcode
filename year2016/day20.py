import sys

try:
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__.split('.')[0] + '_input.txt'

    lines = []

    with open(fn) as f:
        for line in f:
            lines.append(line.split('-'))
except FileNotFoundError:
    pass


def solution(*args, **kws):
    segs = [(int(low), int(high)) for (low, high) in args[0]]
    segs.sort()
    allow_lowest = float('inf')
    allow = 0
    allow_count = 0
    allow = 0
    for low, high in segs:
        if allow < low:
            allow_lowest = min(allow, allow_lowest)
            allow_count += low - allow
            allow = high + 1
        elif low <= allow:
            allow = max(high + 1, allow)
    allow_count += (4294967295 + 1 - allow)
    return allow_lowest, allow_count


r1, r2 = solution(lines)
print('Part One:', r1)  # 4793564
print('Part Two:', r2)  # 146
