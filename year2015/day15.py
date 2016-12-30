# Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
# Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
# Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
# Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8


with open('15.in', 'r') as f:
    lines = f.readlines()

prop = []
for l in lines:
    ws = [w.strip(',:') for w in l.split()]
    prop.append(list(map(int, ws[2::2])))

# cheating here
from operator import mul
from functools import reduce

vals = []
for x in range(101):
    for y in range(101 - x):
        for z in range(101 - x - y):
            w = 100 - x - y - z
            num = [x, y, z, w]
            vals.append( reduce(mul, [max(0, sum(num[i] * prop[i][p] for i in range(4))) for p in range(4)], 1) )

print('One:', max(vals))


vals = []
for x in range(101):
    for y in range(101 - x):
        for z in range(101 - x - y):
            w = 100 - x - y - z
            num = [x, y, z, w]
            cal = sum(num[i] * prop[i][-1] for i in range(4))
            if cal == 500:
                vals.append( reduce(mul, [max(0, sum(num[i] * prop[i][p] for i in range(4))) for p in range(4)], 1) )

print('Two:', max(vals))
