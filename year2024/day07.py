import sys
from copy import deepcopy
from typing import List


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()


def preprocess(raw: str) -> tuple[int, List[int]]:
    rt = []
    for ln in raw.splitlines():
        p1, p2 = ln.strip().split(":")
        p2 = [int(v) for v in p2.strip().split()]
        rt.append((int(p1), p2))
    # print(rt)
    return rt


def is_solvable1(target, numbers):
    if not numbers:
        if target == 0:
            return True
        else:
            return False
    elif len(numbers) == 1:
        return target == numbers[-1]
    else:  # len >= 2
        if target < numbers[-1]:
            return False
        if is_solvable1(target - numbers[-1], numbers[:-1]):
            return True
        elif target % numbers[-1] == 0:
            return is_solvable1(target // numbers[-1], numbers[:-1])
        return False


def fn_p1(data):
    return sum([t for (t, ns) in data if is_solvable1(t, ns)])


def is_solvable2(target, numbers):
    if not numbers:
        return target == 0
    elif len(numbers) == 1:
        return target == numbers[-1]
    else:  # len >= 2
        *rest, last = numbers
        if target < last:
            return False
        # plus
        if is_solvable2(target - last, rest):
            return True
        # mul
        if target % last == 0 and is_solvable2(target // last, rest):
            return True
        # cat
        if str(target).endswith(str(last)):
            try:
                return is_solvable2(int(str(target)[: -len(str(last))]), rest)
            except ValueError:
                pass
    return False


def fn_p2(data):
    return sum([t for (t, ns) in data if is_solvable2(t, ns)])


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 3749
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 11387

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 2299996598890
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 362646859298554
