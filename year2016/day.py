import sys

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


def solution(*args, **kws):
    return 0


r1 = solution()
print('Part One:', r1)


def solution2(*args, **kws):
    return 1


r2 = solution2()
print('Part Two:', r2)
