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


def preprocess(raw):
    return raw


def fn_p1(data):
    return sum(
        int(a) * int(b)
        for _, a, b in re.findall(r"""(mul\((\d{1,3}),(\d{1,3})\))""", data)
    )


def fn_p2(data):
    r = 0
    d = True
    matches = re.findall(
        r"""((mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\)))""", data
    )
    for terms in matches:
        if terms[0].startswith("mul"):
            if d:
                r += int(terms[2]) * int(terms[3])
        elif terms[0].startswith("don"):
            d = False
        else:
            d = True
    return r


raw_data = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))


if __name__ == "__main__":
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # 161
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # 48

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 178794710
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 76729637
