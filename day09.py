
with open('09.in', 'r') as f:
    lines = f.read().splitlines()

dist = {}
cities = set()
for line in lines:
    ws = line.split()
    c1, c2, d = ws[0], ws[2], int(ws[4])
    dist[(c1, c2)] = dist[(c2, c1)] = d
    cities.update({c1, c2})
cities = list(cities)

from itertools import permutations

min_dis = sum(dist.values())
min_route = []
max_dis = 0
max_route = []

for route in permutations(cities):
    dis = sum(dist[(c1, c2)] for c1, c2 in zip(route[:-1], route[1:]))
    if dis < min_dis:
        min_dis = dis
        min_route = route[:]
    if dis > max_dis:
        max_dis = dis
        max_route = route[:]

print('One:', min_dis)

print('Two:', max_dis)
