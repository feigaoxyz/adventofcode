import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

from collections import defaultdict

bot = defaultdict(list)
output = defaultdict(list)
rule = defaultdict(list)

with open(fn) as f:
    for line in f:
        row = line.split()
        if row[0] == 'value':
            # value x goes to bot y
            bot[row[-1]].append(row[1])
        else:
            # bot x gives low to bot y and high to bot z
            rule[row[1]].extend(row[5:7] + row[-2:])

r1 = 0
r2 = 0
target = {'61', '17'}

while True:
    for b in bot:
        if len(bot[b]) == 2:
            if set(bot[b]) == target:
                r1 = b
            low, high = sorted(map(int, bot[b]))
            if rule[b][0] == 'bot':
                bot[rule[b][1]].append(str(low))
            elif rule[b][0] == 'output':
                output[rule[b][1]].append(str(low))
            if rule[b][2] == 'bot':
                bot[rule[b][3]].append(str(high))
            elif rule[b][2] == 'output':
                output[rule[b][3]].append(str(high))
            bot[b] = list()
            break
    else:
        break


def prod(*it, start=1):
    """
    Return the product of a 'start' value (default: 1) multiplies an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    """
    from operator import mul
    from functools import reduce
    if len(it) == 1:
        it = it[0]
    return reduce(mul, it, start)


r2 = prod(prod(map(int, output[x])) for x in '012')

print('Part One:', r1)  # 56
print('Part Two:', r2)  # 7847
