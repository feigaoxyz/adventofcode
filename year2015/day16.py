#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Sue 1: cars: 9, akitas: 3, goldfish: 0
# Sue 2: akitas: 9, children: 3, samoyeds: 9

with open('16.in', 'r') as f:
    lines = f.readlines()

known = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

sues = {}
for l in lines:
    name, prop = map(str.strip, l.split(':', 1))
    d = dict(p.strip().split(': ') for p in prop.split(','))
    for k, v in d.items():
        d[k] = int(v)
    sues[int(name.split()[1])] = d.copy()

knows = dict(l.strip().split(': ') for l in known.splitlines())
for k, v in knows.items():
    knows[k] = int(v)

ans1 = []
ans2 = []

for nid, props in sues.items():
    ok1 = True
    ok2 = True
    for k, v in knows.items():
        if k in props:
            thisv = props[k]
            if v != thisv:
                ok1 = False
            if k in {'cats', 'trees'}:
                if v >= thisv:
                    ok2 = False
            elif k in {'pomeranians', 'goldfish'}:
                if v <= thisv:
                    ok2 = False
            else:
                if v != thisv:
                    ok2 = False
    if ok1:
        ans1.append(nid)
    if ok2:
        ans2.append(nid)

print('One:', ans1)
print('Two:', ans2)
