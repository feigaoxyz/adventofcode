import sys
from copy import deepcopy

from common import load_input


class Cart:
    def __init__(self, x, y, direction, crashed=False):
        self.x = x
        self.y = y
        self.dx, self.dy = direction
        self.crashed = crashed
        self.next_turn = 0

    def turn(self, corner=False):
        if self.next_turn % 3 == 0:
            # turn left
            self.turn_left()
        elif self.next_turn % 3 == 1:
            # go straight
            pass
        elif self.next_turn % 3 == 2:
            # turn right
            self.turn_right()
        # increment the counter only not at corner
        if not corner:
            self.next_turn += 1

    def turn_left(self):
        self.dx, self.dy = self.dy, -self.dx

    def turn_right(self):
        self.dx, self.dy = -self.dy, self.dx

    def __repr__(self):
        return f"Cart(({self.x}, {self.y}), ({self.dx}, {self.dy}))"

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def step(self, track):
        self.x += self.dx
        self.y += self.dy
        cell = track[self.y][self.x]
        if cell == "+":
            self.turn()
        elif cell == "/":
            # up -> right, down -> left
            if self.dx == 0:
                self.turn_right()
            else:
                self.turn_left()
        elif cell == "\\":
            if self.dy == 0:
                self.turn_right()
            else:
                self.turn_left()

    @property
    def position(self):
        return (self.x, self.y)


def preprocess(raw):
    carts = []
    track = [list(line) for line in raw.splitlines()]
    for y, row in enumerate(track):
        for x, cell in enumerate(row):
            if cell == ">":
                carts.append(Cart(x, y, (1, 0)))
                track[y][x] = "-"
            elif cell == "<":
                carts.append(Cart(x, y, (-1, 0)))
                track[y][x] = "-"
            elif cell == "^":
                carts.append(Cart(x, y, (0, -1)))
                track[y][x] = "|"
            elif cell == "v":
                carts.append(Cart(x, y, (0, 1)))
                track[y][x] = "|"
    return track, carts


def fn_p1(data):
    track, carts = data
    # print(carts)
    for _ in range(1500):
        carts.sort()
        old_pos = set([cart.position for cart in carts])
        new_pos = set()
        for cart in carts:
            old_pos.remove(cart.position)
            cart.step(track)
            if cart.position in old_pos or cart.position in new_pos:
                return cart.position
            new_pos.add(cart.position)


def fn_p2(data):
    track, carts = data
    # print(carts)
    while True:
        # for _ in range(5500):
        carts = sorted([cart for cart in carts if not cart.crashed])
        if len(carts) == 1:
            return carts[0].position

        old_pos = set([cart.position for cart in carts])
        new_pos = set()
        for cart in carts:
            if cart.crashed:
                continue
            old_pos.remove(cart.position)
            cart.step(track)
            if cart.position in old_pos or cart.position in new_pos:
                for c2 in carts:
                    if c2.position == cart.position:
                        c2.crashed = True
            new_pos.add(cart.position)
    return carts


if __name__ == "__main__":
    raw_data = r"""/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/"""
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    )
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 46,18
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 124,103
