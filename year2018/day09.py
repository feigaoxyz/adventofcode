import sys
from copy import deepcopy
import re
from collections import deque

from common import load_input, aggregateby


def preprocess(raw):
    return map(int, re.findall(r"\d+", raw))


def play(max_marbles):
    circle = deque([0])
    scores = []
    for t in range(1, max_marbles + 1):
        if t % 23 == 0:
            circle.rotate(7)
            scores.append((t, t + circle[-1]))
            circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(t)
    return scores


def fn_p1(data):
    players, marbles = data
    # print(sorted(scores))
    scores = play(marbles)
    return max(map(sum, aggregateby(scores, key=lambda x: x % players).values()))


def fn_p2(data):
    players, marbles = data
    # print(sorted(scores))
    scores = play(marbles * 100)
    return max(map(sum, aggregateby(scores, key=lambda x: x % players).values()))


if __name__ == "__main__":
    raw_data = """10 1618
    """.strip()
    data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(deepcopy(data)))
    # print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)  # 435, 71184
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 412959
    # print("Part 2:", fn_p2(deepcopy(data)))  # answer: 3333662986
