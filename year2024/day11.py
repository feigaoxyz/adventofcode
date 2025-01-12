import sys
from copy import deepcopy


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """
125 17
""".strip()


def preprocess(raw: str):
    return [int(v) for v in raw.split()]

seen = dict()

def blink(v: int, n: int):
    if (v, n) in seen:
        return seen[(v, n)]
    if n == 0:
        r = 1
    else:
        if v == 0:
            r =  blink(1, n - 1)
        elif len(str(v)) % 2 == 0:
            s = str(v)
            v1, v2 = int(s[: len(s) // 2]), int(s[len(s) // 2 :])
            r = blink(v1, n - 1) + blink(v2, n - 1)
        else:
            r = blink(v * 2024, n - 1)
    seen[(v, n)] = r
    return r


def fn_p1(data):
    print("data", data)
    return sum([blink(v, 25) for v in data])
    # for _ in range(25):
        # stones = []
        # # blink
        # for v in data:
        #     if v == 0:
        #         stones.append(1)
        #     elif len(str(v)) % 2 == 0:
        #         s = str(v)
        #         s1, s2 = s[: len(s) // 2], s[len(s) // 2 :]
        #         stones.append(int(s1))
        #         stones.append(int(s2))
        #     else:
        #         stones.append(v * 2024)
        # data = stones[::]
    # return len(data)


def fn_p2(data):
    return sum([blink(v, 75) for v in data])


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 55312
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 65601038650482

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 186203
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 221291560078593
