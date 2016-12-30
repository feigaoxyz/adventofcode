import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

print(fn)

items = []

with open(fn) as f:
    for line in f:
        items.append(line.split())

r1 = 0
r2 = 0

height = 6
width = 50

screen = [[False for c in range(width)] for r in range(height)]


def rect(a, b):
    for r in range(b):
        for c in range(a):
            screen[r][c] = True


def rotate_row(a, b):
    tmp = screen[a][::]
    for c in range(width):
        screen[a][(c + b) % width] = tmp[c]


def rotate_column(a, b):
    tmp = [screen[i][a] for i in range(height)]
    for r in range(height):
        screen[(r + b) % height][a] = tmp[r]


for row in items:
    if 'rect' in row:
        rect(*map(int, row[1].split('x')))
    elif 'row' in row:
        p1, p2 = row[2], row[4]
        p1 = int(p1.split('=')[1])
        p2 = int(p2)
        rotate_row(p1, p2)
    elif 'column' in row:
        p1, p2 = row[2].split('=')[1], row[4]
        rotate_column(*map(int, (p1, p2)))

r1 = sum(sum(r) for r in screen)

print('Part One:', r1)  # 106

print('\n'.join(''.join('*' if c else ' ' for c in r) for r in screen))
print('Part Two:', r2)  # CFLELOYFCS
