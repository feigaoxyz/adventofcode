import operator as op

_max = (1<<16) - 1  # 65535

with open('07.in', 'r') as f:
    lines = f.readlines()

lines.sort(key=lambda l: (len(l.split()), l))

maps = {}
wires = {}

for line in lines:
    words = line.split()
    maps[words[-1]] = words[:-2]

def calc(symb):
    try:
        return wires[symb]
    except KeyError:
        pass
    try:
        v = int(symb)
        wires[symb] = v
        return v
    except ValueError:
        pass
    ws = maps[symb]
    if len(ws) == 1:  # 123 or x
        v = calc(ws[0])
    elif ws[0] == 'NOT':  # not x
        v = (~ calc(ws[1])) & _max
    elif ws[1] == 'AND':
        v = (calc(ws[0]) & calc(ws[2]))
    elif ws[1] == 'OR':
        v = (calc(ws[0]) | calc(ws[2]))
    elif ws[1] == 'LSHIFT':
        v = ((calc(ws[0]) << calc(ws[2])) & _max)
    elif ws[1] == 'RSHIFT':
        v = ((calc(ws[0]) >> calc(ws[2])) & _max)
    wires[symb] = v
    return v

print("One:", calc('a'))  # 956

wires = {'b': 956}
print('Two:', calc('a'))

