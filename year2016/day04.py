import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

print(fn)

items = []

with open(fn) as f:
    for line in f:
        items.append(line.split('-'))

r1 = 0
r2 = 0

from collections import Counter


def shift(x, n):
    for i in range(n):
        x = chr((ord(x) - ord('a') + 1) % 26 + ord('a'))
    return x


for row in items:
    letters = ''.join(row[:-1])
    sec = int(row[-1].split('[')[0])
    check = row[-1].split('[')[1].split(']')[0]

    c = Counter(letters)
    c = list(c.items())
    c = sorted(c, key=(lambda a: (-a[1], a[0])))
    if set([x for x, _ in c[:5]]) == set(check):
        r1 += sec

    dec = ''.join(shift(x, sec % 26) for x in letters)
    if 'north' in dec:
        r2 = sec

print('Part One:', r1)
print('Part Two:', r2)
