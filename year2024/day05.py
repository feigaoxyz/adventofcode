from collections import defaultdict
import sys
from copy import deepcopy
from typing import Any, List


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


def preprocess(raw: str) -> tuple[List[tuple[int, int]], List[List[int]]]:
    [p1, p2, *_] = raw.split("\n\n")
    after = defaultdict(list)
    # r1 = [(int(a), int(b)) for [a, b, *_] in p1.split()]
    for l in p1.split():
        [a, b, *_] = l.split("|")
        after[(int(b))].append(int(a))
    r2 = [[int(a) for a in l.split(",")] for l in p2.split()]
    return (after, r2)


def fn_p1(data: tuple[any, List[List[int]]]):
    before, lines = data
    result = 0
    for ln in lines:
        ok = True
        for i, k in enumerate(ln):
            if k in before.keys():
                for v in before[k]:
                    try:
                        if ln.index(v) > i:
                            ok = False
                            break
                    except ValueError:
                        pass
            if not ok:
                break
        if ok:
            result += ln[len(ln) // 2]
    return result


def fn_p2(data: tuple[Any, List[List[int]]]) -> int:
    before, lines = data
    result = 0
    for ln in lines:
        ok = True
        i = 0
        while i < len(ln):
            k = ln[i]
            if k in before.keys():
                for v in before[k]:
                    try:
                        j = ln.index(v)
                        if j > i:
                            ok = False
                            ln[i], ln[j] = v, k
                            i -= 1
                            break
                    except ValueError:
                        continue
            i += 1
        if not ok:
            result += ln[len(ln) // 2]
    return result


raw_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()


if __name__ == "__main__":
    data = preprocess(raw_data)
    print(data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 143
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 4790
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 6319
