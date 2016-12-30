#!/usr/bin/env python3
# -*- coding: utf-8 -*-

puzzle = 29000000


# find min n s.t. sum(d for d in n.divisors()) >= puzzle

def divisors(n):
    from math import sqrt
    ds = {1, n}
    for d in range(2, int(sqrt(n))):
        if n % d == 0:
            ds.update({d, n // d})
        if d * d > n:
            break
    return ds


one = 0

# slow
# for n in range(1000, puzzle):
#     if sum(divisors(n)) >= puzzle:
#         one = n
#         break

# sums1 = [i * 10 for i in range(puzzle // 10 + 1)]
# for n in range(2, len(sums1)):
#     if sums1[n] >= puzzle:
#         one = n
#         break
#     for m in range(n * 2, len(sums1), n):
#         sums1[m] += n * 10
#
# print('One:', one)  # 665280

two = 0
sums2 = [i * 11 for i in range(puzzle // 11 + 1)]
for n in range(2, puzzle):
    if sums2[n] >= puzzle:
        two = n
        break
    for m in range(n * 2, min(51 * n, len(sums2)), n):
        sums2[m] += n * 11

print('Two:', two)  # 705600
