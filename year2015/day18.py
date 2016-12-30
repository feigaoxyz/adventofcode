#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('18.in', 'r') as f:
    lines = f.read().splitlines()


def trans(bd):
    lr, lc = len(bd), len(bd[0])
    nex = [list(r)[:] for r in bd]
    for r in range(lr):
        for c in range(lc):
            nb = [bd[rr][cc] for rr, cc
                  in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                      (r, c - 1), (r, c + 1),
                      (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
                  if 0 <= rr < lr and 0 <= cc < lc]
            if bd[r][c] == '#':
                if nb.count('#') in {2, 3}:
                    nex[r][c] = '#'
                else:
                    nex[r][c] = '.'
            else:
                if nb.count('#') in {3}:
                    nex[r][c] = '#'
                else:
                    nex[r][c] = '.'
    return nex


def test():
    s = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
    print(s)
    cur = s.splitlines()
    for _ in range(4):
        cur = trans(cur)
        print('step ', _)
        print('\n'.join(''.join(r) for r in cur))


# test()

# for _ in range(100):
#     lines = trans(lines)
#
# print('One:', sum(row.count('#') for row in lines))


with open('18.in', 'r') as f:
    lines = f.read().splitlines()
lines = [list(l) for l in lines]
lines[0][0] = lines[0][99] = lines[99][0] = lines[99][99] = '#'
for _ in range(100):
    lines = trans(lines)
    lines[0][0] = lines[0][99] = lines[99][0] = lines[99][99] = '#'

print('Two:', sum(row.count('#') for row in lines))
