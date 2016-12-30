import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = [(1, 17, 15),
(2, 3, 2),
(3, 19, 4),
(4, 13, 2),
(5, 7, 2),
(6, 5, 0),
(7, 11, 0)
]
#Disc #1 has 17 positions; at time=0, it is at position 15.
#Disc #2 has 3 positions; at time=0, it is at position 2.
#Disc #3 has 19 positions; at time=0, it is at position 4.
#Disc #4 has 13 positions; at time=0, it is at position 2.
#Disc #5 has 7 positions; at time=0, it is at position 2.
#Disc #6 has 5 positions; at time=0, it is at position 0.


def part1(items):
    n = 0
    while True:
        if all((n+h+f) % m == 0 for h, m, f in items):
            return n
        n += 1


#r1 = part1(items[:-1])
#r2 = part2(items)

import multiprocessing as mp

r1, r2 = mp.Pool().map(part1, (items[:-1], items))

print('Part One:', r1)  # 400589
print('Part Two:', r2)  # 3045959
