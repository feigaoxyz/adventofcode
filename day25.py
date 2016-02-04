#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_idx(row, col):
    diag = row + col - 1
    base = diag * (diag - 1) // 2
    idx = base + col
    return idx


print('\nindex')
for r in range(1, 5):
    print([get_idx(r, c) for c in range(1, 5)])

idx = get_idx(3010, 3019)
b, e, m = 20151125, 252533, 33554393


def fast_exp_mod(a, b, m):
    """a**b % m"""
    p = 1
    r = 1
    while p <= b:
        if b & p:
            r = (r * a) % m
        a = (a * a) % m
        p = p * 2
    return r % m


print('\na**b%m:', [fast_exp_mod(2, i, 10) for i in range(11)])


def code(row, col):
    return b * fast_exp_mod(e, get_idx(row, col) - 1, m) % m


print('\ncode')
for row in range(1, 5):
    print([code(row, col) for col in range(1, 5)])

# Part One
print('Part One:', 3010, 3019, code(3010, 3019))
