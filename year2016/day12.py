import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

with open(fn) as f:
    for line in f:
        items.append(line.split())


def cpy(reg, pos, x, y):
    try:
        reg[y] = reg[x]
    except KeyError:
        reg[y] = int(x)
    return pos + 1


def inc(reg, pos, x):
    reg[x] += 1
    return pos + 1


def dec(reg, pos, x):
    reg[x] -= 1
    return pos + 1


def jnz(reg, pos, x, y):
    try:
        v = reg[x]
    except KeyError:
        v = int(x)
    if v:
        return pos + int(y)
    else:
        return pos + 1


s2f = {
    'cpy': cpy,
    'inc': inc,
    'dec': dec,
    'jnz': jnz,
}


def assembunny(registers):
    pos = 0
    length = len(items)
    while 0 <= pos < length:
        pos = s2f[items[pos][0]](registers, pos, *items[pos][1:])
    return registers['a']


def assembunny_str(registers):
    pos = 0
    while 0 <= pos < len(items):
        cmd, *par = items[pos]
        if cmd == 'cpy':
            x, y = par
            registers[y] = registers[x] if x in 'abcd' else int(x)
        elif cmd == 'inc':
            x = par[0]
            registers[x] += 1
        elif cmd == 'dec':
            x = par[0]
            registers[x] -= 1
        elif cmd == 'jnz':
            x, y = par
            if (registers[x] if x in registers else int(x)) != 0:
                pos += int(y)
                continue
        pos += 1
    return registers['a']


import time

t0 = time.time()

r1 = assembunny(dict(a=0, b=0, c=1, d=0))
t1 = time.time()
print('Part One:', r1, t1 - t0)  # 318003

r2 = assembunny_str(dict(a=0, b=0, c=1, d=0))
t2 = time.time()
print('Part Two:', r2, t2 - t1)  # 9227657
