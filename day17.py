#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sizes = list(map(int, """33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42""".split()))

sizes.sort(reverse=True)

ways1 = 0
ways = []

def solve(egg, cont, sol=None):
    if egg == 0:
        ways.append(sol[:])
        return
    if not cont:
        return
    if egg >= cont[0]:
        solve(egg - cont[0], cont[1:], sol + cont[0:1])
    solve(egg, cont[1:], sol)


solve(150, sizes, [])

print('One:', len(ways))

minlen = min(map(len, ways))
print('Two:', sum([1 for l in ways if len(l) == minlen]))
