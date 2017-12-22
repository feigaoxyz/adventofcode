from common import load_input
from collections import defaultdict


class Virus:
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.direction = d

    def forward(self):
        dr, dc = Virus.DIRECTIONS[self.direction]
        self.r += dr
        self.c += dc
        return self.position

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1 + 4) % 4

    def turn_reverse(self):
        self.direction = (self.direction + 2) % 4

    @property
    def position(self):
        return (self.r, self.c)

    def burst(self, infected: defaultdict):
        change = 0
        if infected[self.position] == 2:
            self.turn_right()
            infected[self.position] = 0
            change = -1
        else:
            self.turn_left()
            infected[self.position] = 2
            change = 1
        self.forward()
        return change, infected

    def burst_v2(self, world):
        new_infect = False
        status = world[self.position]
        if status == 0:
            # clean -> weakened
            world[self.position] = 1
            self.turn_left()
        elif status == 1:
            # weakened -> infected
            world[self.position] = 2
            new_infect = True
        elif status == 2:
            # infected -> flagged
            world[self.position] = 3
            self.turn_right()
        elif status == 3:
            # flagged -> clean
            world[self.position] = 0
            self.turn_reverse()
        self.forward()
        return new_infect, world


def parse_input(map_str: str):
    infected = defaultdict(int)
    lines = map_str.splitlines()
    for r, row in enumerate(lines):
        for c, char in enumerate(row):
            if char == '#':
                infected[(r, c)] = 2

    return infected, Virus(r=len(lines) // 2, c=len(lines[0]) // 2, d=0)


def fn_p1(raw: str, rounds=10000):
    infected, virus = parse_input(raw)
    # print(infected, virus.position)
    infection = 0
    for _ in range(rounds):
        change, infected = virus.burst(infected)
        if change == 1:
            infection += 1
    return infection


def fn_p2(raw: str, rounds=10000000):
    infected, virus = parse_input(raw)
    # print(infected, virus.position)
    infection = 0
    for _ in range(rounds):
        change, infected = virus.burst_v2(infected)
        if change:
            infection += 1
    return infection


if __name__ == '__main__':
    example = '\n'.join(["..#", "#..", "..."])
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example, 70))  # 41
    # print("Part 1:", fn_p1(input_data))  # 5330

    print("Part 2 example:", fn_p2(example, 100))  # 26
    # print("Part 2:", fn_p2(input_data))  # 2512103
