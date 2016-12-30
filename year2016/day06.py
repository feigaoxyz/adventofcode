import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

with open(fn) as f:
    for line in f:
        items.append(list(line))


cols = ['' for c in items[0]]

for row in items:
    for idx, col in enumerate(row):
        cols[idx] += (col)

r1 = ''
r2 = ''
for x in cols:
    s = sorted(x, key=(lambda v: x.count(v)), reverse=True)
    r1 += (s[0])
    r2 +=  s[-1]



print('Part One:', r1)
print('Part Two:', r2)
