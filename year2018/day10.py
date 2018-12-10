import sys
from copy import deepcopy
import re

from common import load_input


class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def step(self, seconds=1):
        self.x += seconds * self.dx
        self.y += seconds * self.dy

    def __str__(self):
        return f"Point({self.x, self.y, self.dx, self.dy})"

    def __repr__(self):
        return str(self)


class Cloud:
    def __init__(self, points):
        self.points = points
        self.timer = 0
        self.draw = set()
        self.min_x = self.min_y = 10 ** 6
        self.max_x = self.max_y = -10 ** 6
        self.step(0)

    def step(self, seconds=1):
        self.draw = set()
        self.min_x = self.min_y = 10 ** 6
        self.max_x = self.max_y = -10 ** 6
        for p in self.points:
            p.step(seconds)
            self.min_x = min(self.min_x, p.x)
            self.max_x = max(self.max_x, p.x)
            self.min_y = min(self.min_y, p.y)
            self.max_y = max(self.max_y, p.y)
            self.draw.add((p.x, p.y))
        self.timer += seconds
        self.width = self.max_x - self.min_x + 1
        self.height = self.max_y - self.min_y + 1

    def __str__(self):
        return "\n".join(
            "".join(
                "#" if (x, y) in self.draw else "."
                for x in range(self.min_x, self.max_x + 1)
            )
            for y in range(self.min_y, self.max_y + 1)
        )


def preprocess(raw):
    points = [Point(*map(int, re.findall(r"-?\d+", line))) for line in raw.splitlines()]
    # print(points)
    return Cloud(list(points))


def fn_p1(data):
    timer = 0
    # while True:
    #     try:
    #         dt = int(input("Time Diff:"))
    #         data.step(dt)
    #         timer += dt
    #         print("Timer:", timer, data.width, data.height)
    #         if input("Draw? (y/n)") == "y":
    #             print(data)
    #     except KeyboardInterrupt:
    #         break
    while True:
        if data.height < 200:
            print(timer)
            print(data)
            input()
        timer += 1
        data.step(1)

    return timer


def fn_p2(data):
    return


if __name__ == "__main__":
    raw_data = """
    position=< 9,  1> velocity=< 0,  2>
    position=< 7,  0> velocity=<-1,  0>
    position=< 3, -2> velocity=<-1,  1>
    position=< 6, 10> velocity=<-2, -1>
    position=< 2, -4> velocity=< 2,  2>
    position=<-6, 10> velocity=< 2, -2>
    position=< 1,  8> velocity=< 1, -1>
    position=< 1,  7> velocity=< 1,  0>
    position=<-3, 11> velocity=< 1, -2>
    position=< 7,  6> velocity=<-1, -1>
    position=<-2,  3> velocity=< 1,  0>
    position=<-4,  3> velocity=< 2,  0>
    position=<10, -3> velocity=<-1,  1>
    position=< 5, 11> velocity=< 1, -2>
    position=< 4,  7> velocity=< 0, -1>
    position=< 8, -2> velocity=< 0,  1>
    position=<15,  0> velocity=<-2,  0>
    position=< 1,  6> velocity=< 1,  0>
    position=< 8,  9> velocity=< 0, -1>
    position=< 3,  3> velocity=<-1,  1>
    position=< 0,  5> velocity=< 0, -1>
    position=<-2,  2> velocity=< 2,  0>
    position=< 5, -2> velocity=< 1,  2>
    position=< 1,  4> velocity=< 2,  1>
    position=<-2,  7> velocity=< 2, -2>
    position=< 3,  6> velocity=<-1, -1>
    position=< 5,  0> velocity=< 1,  0>
    position=<-6,  0> velocity=< 2,  0>
    position=< 5,  9> velocity=< 1, -2>
    position=<14,  7> velocity=<-2,  0>
    position=<-3,  6> velocity=< 2, -1>
    """.strip()
    data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: ERCXLAJL at 10813 seconds
    # print("Part 2:", fn_p2(deepcopy(data)))  # answer: 10813
