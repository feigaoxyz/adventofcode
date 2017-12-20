from common import load_input
from typing import List
import numpy as np
import re
from collections import defaultdict

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


class Particle:
    def __init__(self, p, v, a, uid):
        self.p = p
        self.v = v
        self.a = a
        self.uid = uid

    def travel(self, time):
        return self.p + self.v * time + self.a * (time + 1) * time / 2

    def step(self):
        self.v += self.a
        self.p += self.v

    @property
    def position(self):
        return tuple(self.p)

    def __hash__(self):
        return self.uid

    def __str__(self):
        return f"[UID={self.uid}, p=<{self.p}>, v=<{self.v}>, a=<{self.a}>]"

    def __repr__(self):
        return self.__str__()


def parser(raw: str) -> List[Particle]:
    particles = []
    for idx, line in enumerate(raw.splitlines()):
        nums = list(map(int, re.findall(r'[-\d]+', line)))
        p = np.array(nums[:3])
        v = np.array(nums[3:6])
        a = np.array(nums[6:])
        particles.append(Particle(p, v, a, idx))
    return particles


def fn_p1(raw: str):
    particles = parser(raw)
    time = 10**8
    min_dist = None
    for p in particles:
        loc = p.travel(time)
        dist = np.sum(np.abs(loc))
        if min_dist is None or dist < min_dist[0]:
            min_dist = (dist, p.uid)
    return min_dist[1]


def same_way(p: Particle):
    for i in range(3):
        if p.a[i] > 0 and (p.v[i] <= 0 or p.p[i] <= 0):
            return False
        if p.a[i] == 0 and (p.v[i] != 0 and p.v[i] * p.p[i] <= 0):
            return False
        if p.a[i] < 0 and (p.v[i] >= 0 or p.p[i] >= 0):
            return False
    return True


def fn_p2(raw: str):
    particles = parser(raw)
    survivals = set(particles)
    while True:
        collide = False
        positions = defaultdict(set)
        for p in survivals:
            positions[p.position].add(p)
        for pos in positions:
            if len(positions[pos]) > 1:
                collide = True
                survivals.difference_update(positions[pos])
        # for p in survivals:
        #     print(p, same_way(p))
        if collide is False and all(same_way(p) for p in survivals):
            break
        for p in survivals:
            p.step()
    return len(survivals)


if __name__ == '__main__':
    example = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
    p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example))
    # print("Part 1:", fn_p1(input_data))  # 144

    example2 = """
    p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
    p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
    p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
    p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>
    """.strip()
    print("Part 2 example:", fn_p2(example2))  # 1
    print("Part 2:", fn_p2(input_data))  # 477
