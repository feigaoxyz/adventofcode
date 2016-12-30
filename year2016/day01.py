import sys

with open(sys.argv[1]) as f:
    raw_data = f.read()

data = raw_data.strip()

position = 0j
heading = 1j

history = set((0,0))
revisit = None

for x in data.strip().split(','):
    x = x.strip()
    turn, steps = x[0], int(x[1:])
    if turn == 'R':
        heading = heading / 1j
    elif turn == 'L':
        heading = heading * 1j
    for i in range(steps):
        position = position + heading
        x, y = int(position.real), int(position.imag)
        if revisit is None and (x, y) in history:
            revisit = (x, y)
        else:
            history.add((x, y))

print('Part One:', int(abs(position.real) + abs(position.imag)))
print('Part Two:', sum(map(abs, revisit)))
