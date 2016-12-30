import re
import sys

try:
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__.split('.')[0] + '_input.txt'

    lines = []

    with open(fn) as f:
        for line in f:
            nums = list(map(int, re.findall(r'\d+', line)))
            if nums:
                lines.append(nums)
except FileNotFoundError:
    pass


# for x, y, total, used, avail, perc in lines:
#     if total > 100 or used < 50:
#         print(x, y, total, used, avail)


def solution(*args, **kws):
    count = 0
    for line1 in lines:
        for line2 in lines:
            if line1[0:2] != line2[0:2] and line1[3] > 0 and line1[3] <= line2[4]:
                count += 1
    return count


r1 = solution()
print('Part One:', r1)  # 976


def solution2(*args, **kws):
    # blocks: 15<=x<=36, y=2
    # empty: (20,6)

    steps = 0
    # move "E" to (14,2)
    steps += abs(20 - 14) + abs(6 - 2)
    # move "E" to (35,0)
    steps += abs(35 - 14) + abs(0 - 2)
    # T(0,0) ... E(35,0) G(36,0)

    # shift EG to left 1 cell
    per_shift = 5

    steps += abs(35 - 1) * per_shift
    # T E G ...
    steps += 5 + 1

    return steps


r2 = solution2()
print('Part Two:', r2)  # 209
