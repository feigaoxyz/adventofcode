with open('14.in', 'r') as f:
    lines = f.read().splitlines()

import re

reindeers = {}
for l in lines:
    ws = l.split()
    reindeers[ws[0]] = list(map(int, re.findall(r'\d+', l)))

ttime = 2503

def dist(ttime):
    dist = {}

    for r, v in reindeers.items():
        p = v[1] + v[2]
        d1 = v[0] * v[1] * (ttime // p)
        rem = ttime % p
        d2 = v[0] * v[1] if rem >= v[1] else v[0] * rem
        dist[r] = d1 + d2
    return dist

print('One:', max(dist(ttime).values()))

pts = {d: 0 for d in reindeers}

for t in range(ttime):
    ds = dist(t+1)
    b = max(ds.values())
    for d, v in ds.items():
        if v == b:
            pts[d] += 1

print('Two:', max(pts.values()))

