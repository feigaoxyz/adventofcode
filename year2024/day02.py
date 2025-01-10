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
    data = []
    for line in raw.splitlines():
        data.append([int(v) for v in line.split()])
    return data


def is_safe(line):
    line_diff = [a - b for a, b in zip(line, line[1:])]
    return all(1 <= v <= 3 for v in line_diff) or all(-3 <= v <= -1 for v in line_diff)


def fn_p1(data):
    return sum(map(is_safe, data))


def fn_p2(data):
    r = 0
    for line in data:
        if is_safe(line):
            r += 1
        else:
            for e in range(len(line)):
                ln = line[:e] + line[e + 1 :]
                assert len(ln) == len(line) - 1
                if is_safe(ln):
                    r += 1
                    break
                # print(line, e, ln)
    return r


raw_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
1 2 3 10
""".strip()


if __name__ == "__main__":
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 402
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 455
