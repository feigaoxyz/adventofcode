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

import functools


@functools.lru_cache()
def is_trap(left=False, center=False, right=False):
    return ((left == True == center and right == False)
            or (center == True == right and left == False)
            or (left == True and center == False == right)
            or (right == True and center == False == left))


@functools.lru_cache()
def next_row(row: str):
    traps = [False] + [c == '^' for c in row] + [False]
    new_traps = [is_trap(*traps[i:i + 3]) for i in range(len(row))]
    new_row = ''.join('^' if c else '.' for c in new_traps)
    return new_row


assert next_row('..^^.') == '.^^^^'

INPUT = '.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^'


def solution(*args, **kws):
    row = INPUT
    total_safe = row.count('.')
    for _ in range(args[0] - 1):
        row = next_row(row)
        total_safe += row.count('.')
    return total_safe


r1 = solution(40)
print('Part One:', r1)  # 1989

r2 = solution(400000)
print('Part Two:', r2)  # 19999894
