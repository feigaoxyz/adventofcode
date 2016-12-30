import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

with open(fn) as f:
    for line in f:
        items.append(line.split(','))

r1 = 0
r2 = 0

for row in items:
    for col in row:
        pass

print('Part One:', r1)  # 31
print('Part Two:', r2)  # 55
