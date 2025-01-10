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


def preprocess(raw):
    left = []
    right = []

    for l in raw.splitlines():
        a, b = map(int, l.split())
        left.append(a)
        right.append(b)
        
    left.sort()
    right.sort()

    return left, right



def fn_p1(data):
    left, right = data

    r1 = 0
    for a, b in zip(left, right):
        r1 += abs(a - b)
    return r1


def fn_p2(data):
    left, right = data
    r2 = 0
    for a, b in zip(left, right):
        r2 += a * right.count(a)
    return r2


raw_data = """3   4
4   3
2   5
1   3
3   9
3   3
""".strip()


if __name__ == "__main__":
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer:
    print("Part 2:", fn_p2(deepcopy(data)))  # answer:
