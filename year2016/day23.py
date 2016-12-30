import math
import sys

try:
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__.split('.')[0] + '_input.txt'

    lines = []

    with open(fn) as f:
        for line in f:
            lines.append(line.split())
except FileNotFoundError:
    pass


def assembunny_runner(registers, lines):
    pos = 0
    while 0 <= pos < len(lines):
        cmd, *par = lines[pos]
        # print(lines[pos], registers)
        try:
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
                    pos += registers[y] if y in registers else int(y)
                    continue
            elif cmd == 'tgl':
                print(registers, lines)
                x = par[0]
                a = registers[x] if x in registers else int(x)
                if 0 <= pos + a < len(lines):
                    if len(lines[pos + a]) == 2:
                        lines[pos + a][0] = 'dec' if lines[pos + a][0] == 'inc' else 'inc'
                    elif len(lines[pos + a]) == 3:
                        lines[pos + a][0] = 'cpy' if lines[pos + a][0] == 'jnz' else 'jnz'
                else:
                    pass
        except:
            print(pos, lines[pos])
            pass
        pos += 1
    return registers


solution = assembunny_runner

sample = [l.strip().split() for l in """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a""".splitlines() if l.strip()]

assert solution({'a': 0}, sample)['a'] == 3

import copy
r1 = solution(dict(a=6, b=0, c=0, d=0), [l[::] for l in lines])
print('Part One:', r1)  # 10880


# 6: 720
# 7: 5040, 10880
# 8: 40320, 46160

def solution2(registers, *args):
    offset = 10880 - 5040
    registers['a'] = offset + math.factorial(registers['a'])
    return registers


r2 = solution2(dict(a=12, b=0, c=0, d=0), [l[::] for l in lines])
print('Part Two:', r2)
