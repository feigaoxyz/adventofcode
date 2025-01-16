import sys
from copy import deepcopy
import re


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()


def preprocess(raw: str):
    robots = list()
    for ln in raw.split("\n"):
        robots.append(tuple(int(v) for v in re.findall(r"-?\d+", ln)))
    return robots


def fn_p1(robots, dims):
    quant = [[0, 0], [0, 0]]
    (width, height) = dims
    hw, hh = width // 2, height // 2
    for robot in robots:
        x = ((robot[0] + 100 * robot[2]) % width + width) % width
        y = ((robot[1] + 100 * robot[3]) % height + height) % height
        # print(robot, x, y)
        if x == hw or y == hh:
            pass
        else:
            quant[x > hw][y > hh] += 1
    return quant[0][0] * quant[0][1] * quant[1][0] * quant[1][1]


def fn_p2(robots, dims):
    (width, height) = dims
    for second in range(width * height):
        xw = [0 for _ in range(width)]
        yw = [0 for _ in range(height)]

        for robot in robots:
            x = ((robot[0] + second * robot[2]) % width + width) % width
            y = ((robot[1] + second * robot[3]) % height + height) % height
            xw[x] += 1
            yw[y] += 1

        if max(xw) > 25 and max(yw) > 20:
            mat = [["." for _ in range(width)] for _ in range(height)]
            for robot in robots:
                x = ((robot[0] + second * robot[2]) % width + width) % width
                y = ((robot[1] + second * robot[3]) % height + height) % height
                mat[y][x] = "#"

            print("\n".join(["".join(r) for r in mat]))
            print("second", second)
            # break
    return None


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    # print(data)
    print("Part 1 Example:", fn_p1(deepcopy(data), (11, 7)))  # answer: 12
    # print("Part 2 Example:", fn_p2(deepcopy(data), (11, 7)))  # answer:

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data), (101, 103)))  # answer: 218433348
    print("Part 2:", fn_p2(deepcopy(data), (101, 103)))  # answer: 6512
