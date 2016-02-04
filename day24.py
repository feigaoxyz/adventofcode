#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
from operator import mul

weights = list(map(int, "1 3 5 11 13 17 19 23 29 31 37 41 43 47 \
            53 59 67 71 73 79 83 89 97 101 103 107 109 113".split()))


# print(len(weights), sum(weights))


def knapsack(target, weights, depth):
    solutions = []

    def dfs(target, weights, partial, depth):
        # print(target, weights, partial, depth)
        if target == 0:
            solutions.append(partial)
            return
        if not weights or len(partial) > depth or target < 0:
            return
        if target >= weights[0]:
            dfs(target - weights[0], weights[1:], partial + weights[0:1], depth)
        dfs(target, weights[1:], partial, depth)

    dfs(target, weights, [], depth)
    return solutions


sols1 = knapsack(sum(weights) // 3, sorted(weights, reverse=True), 6)
print('One', min(reduce(mul, sol) for sol in sols1))  # 10439961859

sols2 = knapsack(sum(weights) // 4, sorted(weights, reverse=True), 5)
print('Two', min(reduce(mul, sol) for sol in sols2))  # 72050269
