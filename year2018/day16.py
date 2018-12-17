import sys
import re
from copy import deepcopy
import operator as op
from collections import defaultdict

from common import load_input, line2ints


def preprocess(raw):
    lines = raw.splitlines()
    p1, p2 = lines[:3096], lines[3096:]
    p1_r = []
    for i in range(0, len(p1), 4):
        reg1 = list(map(int, re.findall(r"\d+", p1[i])))
        ops = list(map(int, re.findall(r"\d+", p1[i + 1])))
        reg2 = list(map(int, re.findall(r"\d+", p1[i + 2])))
        p1_r.append((reg1, ops, reg2))
    p2_r = []
    for line in p2:
        ints = line2ints(line)
        if ints:
            p2_r.append(ints)
    return p1_r, p2_r


def factory(func, ri):
    def wrapped(register, params):
        result = register.copy()
        result[params[2]] = func(
            (register[params[0]] if ri[0] == "r" else params[0]),
            (register[params[1]] if ri[1] == "r" else params[1]),
        )
        return result

    return wrapped


functions = {
    "addr": factory(op.add, "rr"),
    "addi": factory(op.add, "ri"),
    "mulr": factory(op.mul, "rr"),
    "muli": factory(op.mul, "ri"),
    "banr": factory(op.and_, "rr"),
    "bani": factory(op.and_, "ri"),
    "borr": factory(op.or_, "rr"),
    "bori": factory(op.or_, "ri"),
    "setr": factory((lambda a, b: a), "ri"),
    "seti": factory((lambda a, b: a), "ii"),
    "gtir": factory((lambda a, b: 1 if a > b else 0), "ir"),
    "gtri": factory((lambda a, b: 1 if a > b else 0), "ri"),
    "gtrr": factory((lambda a, b: 1 if a > b else 0), "rr"),
    "eqir": factory((lambda a, b: 1 if a == b else 0), "ir"),
    "eqri": factory((lambda a, b: 1 if a == b else 0), "ri"),
    "eqrr": factory((lambda a, b: 1 if a == b else 0), "rr"),
}


def fn_p1(data):
    p1, _ = data
    count = 0
    for reg1, ops, reg2 in p1:
        curr = 0
        for func in functions.values():
            if reg2 == func(reg1, ops[1:]):
                curr += 1
        if curr >= 3:
            count += 1
    return count


def matching(graph):
    result = dict()
    while True:
        any_remove = False
        for k, v in graph.items():
            if len(v) == 1:
                result[k] = v = v.pop()
                any_remove = True
                for k2 in graph:
                    graph[k2].discard(v)
                break
        if not any_remove:
            break
    # print(result.items(), graph.items())
    return dict((v, k) for k, v in result.items())


def fn_p2(data):
    p1, p2 = data
    possibles = defaultdict(set)
    for reg1, ops, reg2 in p1:
        curr = 0
        for name, func in functions.items():
            if reg2 == func(reg1, ops[1:]):
                possibles[name].add(ops[0])
    op2func = matching(possibles)
    reg = [0, 0, 0, 0]
    for line in p2:
        reg = functions[op2func[line[0]]](reg, line[1:])
    return reg


if __name__ == "__main__":
    #     raw_data = """
    # Before: [3, 2, 1, 1]
    # 9 2 1 2
    # After:  [3, 2, 2, 1]
    #     """.strip()
    #     data = preprocess(raw_data)
    #     print("Part 1 Example:", fn_p1(deepcopy(data)))
    #     print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer: 517
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 667
