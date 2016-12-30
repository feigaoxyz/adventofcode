#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

with open('19.in', 'r') as f:
    lines = f.read().splitlines()
#
# lines = """e => H
# e => O
# H => HO
# H => OH
# O => HH
#
# HOHOHO""".splitlines()

trans = defaultdict(list)
for k, w in [l.split(' => ') for l in lines[:-2]]:
    trans[k].append(w)

med = lines[-1]


# print(trans.items())
# print(start)

def step(starter, tf):
    results = set()
    for k, vs in tf:
        p = -1
        while True:
            p = starter.find(k, p + 1)
            if p == -1:
                break
            for v in vs:
                results.add(starter[:p] + v + starter[p + len(k):])
    return results


# print('One:', len(step(med, trans.items())))


# Part Two: TODO: tle

retrans = defaultdict(list)
for k, vs in trans.items():
    for v in vs:
        retrans[v].append(k)

kvs = sorted([(k, v[0]) for k, v in retrans.items()], key=(lambda p: (len(p[0]), -len(p[1]))), reverse=True)
m1 = med[:]
s = 0
while True:
    for k, v in kvs:
        p = m1.rfind(k)
        if p != -1:
            m2 = m1[:p] + v + m1[p + len(k):]
            s += 1
            break
    if m1 == m2: break
    m1 = m2
    print(len(m1), m1)

print('Two:', s)  # 195
