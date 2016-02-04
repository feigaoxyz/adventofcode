
data = input()

def move(d, x, y):
    if d == '>':
        x += 1
    elif d == '<':
        x -= 1
    elif d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    return x, y

x, y = 0, 0
hist = {(x, y)}
for d in data:
    x, y = move(d, x, y)
    hist.add((x, y))
print('Part One:', len(hist))

x, y = 0, 0
hist = {(x, y)}
for d in data[::2]:
    x, y = move(d, x, y)
    hist.add((x, y))
x, y = 0, 0
for d in data[1::2]:
    x, y = move(d, x, y)
    hist.add((x, y))
print('Part Two:', len(hist))
