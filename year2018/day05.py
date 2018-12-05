import sys
from string import ascii_lowercase

from common import load_input


def preprocess(raw):
    return raw


def fn_p1(data):
    stack = []
    diff = abs(ord("a") - ord("A"))
    for u in data:
        if stack and abs(ord(stack[-1]) - ord(u)) == diff:
            stack.pop()
        else:
            stack.append(u)
    return len(stack)


def fn_p2(data):
    return min(
        fn_p1(s)
        for s in [data.replace(c, "").replace(c.upper(), "") for c in ascii_lowercase]
    )


if __name__ == "__main__":
    raw_data = """dabAcCaCBAcCcaDA
    """.strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(raw_data))
    print("Part 2 Example:", fn_p2(raw_data))

    raw_data = load_input(sys.argv[1]).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(data))  # answer: 10804
    print("Part 2:", fn_p2(data))  # answer: 6650
