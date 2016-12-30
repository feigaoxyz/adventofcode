import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'


items = []

with open(fn) as f:
    for line in f:
        line = line.replace('[', ' ').replace(']', ' ')
        # print(line)
        items.append(line.split())

r1 = 0
r2 = 0


def abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    else:
        return False


def aba(s, xyx):
    return s.find(xyx) != -1


from functools import partial, reduce
from itertools import product


def solution1():
    for row in items:
        if any(map(abba, row[::2])) and not any(map(abba, row[1::2])):
            r1 += 1
        if any(any(map(partial(aba, xyx=a+b+a), row[::2])) and any(map(partial(aba, xyx=b+a+b), row[1::2])) for a, b in product(set(''.join(row)), repeat=2) if a != b):
            r2 += 1

    print('Part One:', r1)  # 105
    print('Part Two:', r2)  # 258


def find_abba(s):
    r = []
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            r.append((s[i], s[i+1]))
    return r


def find_aba(s, reverse=False):
    r = []
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            if not reverse:
                r.append((s[i], s[i+1]))
            else:
                r.append((s[i+1], s[i]))
    return r

def solution2():
    r1 = r2 = 0
    for row in items:
        if any(map(find_abba, row[::2])) and not any(map(find_abba, row[1::2])):
            r1 += 1
        outside, inside = (reduce(set.union, (set(find_aba(s, r)) for s in p), set()) for p,r in zip((row[::2], row[1::2]), (False, True)))
        if inside & outside:
            r2 += 1

    return r1, r2

print(solution2())

