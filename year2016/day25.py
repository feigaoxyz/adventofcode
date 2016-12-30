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


def assembunny_runner(registers, cmds):
    pos = 0
    while 0 <= pos < len(cmds):
        cmd, *par = cmds[pos]
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
                # print(registers, cmds)
                x = par[0]
                a = registers[x] if x in registers else int(x)
                if 0 <= pos + a < len(cmds):
                    if len(cmds[pos + a]) == 2:
                        cmds[pos + a][0] = 'dec' if cmds[pos + a][0] == 'inc' else 'inc'
                    elif len(cmds[pos + a]) == 3:
                        cmds[pos + a][0] = 'cpy' if cmds[pos + a][0] == 'jnz' else 'jnz'
                else:
                    pass
            elif cmd == 'out':
                x = par[0]
                v = registers[x] if x in registers else int(x)
                yield v
        except Exception as ex:
            # print(pos, cmds[pos])
            print(ex)
        pos += 1
        # return registers


def solution(*args, **kws):
    ans = 0
    while True:
        it = assembunny_runner(dict(a=ans, b=0, c=0, d=0), lines)
        lst = [next(it) for _ in range(20)]
        # print(ans, lst)
        if set(lst[::2]) == {0} and set(lst[1::2]) == {1}:
            return ans
        ans += 1


r1 = solution()
print('Part One:', r1)  # 198


def solution2(*args, **kws):
    return 1


r2 = solution2()
print('Part Two:', r2)
