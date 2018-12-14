import sys
from copy import deepcopy

from common import load_input


def c2b(c):
    return c == "#"


def preprocess(raw):
    init_raw, _, *rules_raw = raw.splitlines()
    init_raw = init_raw.split()[-1]
    init_state = tuple(i for i, c in enumerate(map(c2b, init_raw)) if c)
    rules = dict()
    for line in rules_raw:
        source, target = line.split(" => ")
        rules[tuple(map(c2b, source))] = c2b(target)
    return init_state, rules


def step(state, rules):
    new_state = []
    for p in range(min(state) - 2, max(state) + 3):
        key = tuple(p + i in state for i in range(-2, 3))
        if rules.get(key, False):
            new_state.append(p)
    return tuple(new_state)


def state_repr(state):
    return "".join(
        "#" if state.get(k, False) else "." for k in range(min(state), max(state) + 1)
    )


def fn_p1(data):
    state, rules = data
    # print(state_repr(state))
    for _ in range(20):
        state = step(state, rules)
        # print(state_repr(state))
    return sum(state)


def fn_p2_experiment(data):
    state, rules = data
    records = {state: 0}
    cycle_len = None
    i = 0
    while i < (50000000000):
        if i % 1000 == 0:
            print(i, state)
        i += 1
        state = step(state, rules)
        if state in records:
            if not cycle_len:
                cycle_len = i - records[state]
            else:
                while i + cycle_len < 50000000000:
                    i += cycle_len
        else:
            records[state] = i
    return sum(state)


def fn_p2(data):
    """
    0 (0, 1, 2, 5, 9, 10, 11, 12, 14, 17, 18, 19, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 41, 42, 44, 45, 46, 47, 48, 50, 51, 53, 54, 57, 58, 59, 64, 69, 70, 74, 75, 79, 80, 82, 85, 86, 87, 90,92, 96, 99)
1000 (947, 955, 966, 971, 976, 981, 986, 994, 999, 1004, 1009, 1017, 1024, 1029, 1035, 1040, 1045, 1053, 1058, 1063, 1072, 1079, 1084, 1089, 1094, 1099)
2000 (1947, 1955, 1966, 1971, 1976, 1981, 1986, 1994, 1999, 2004, 2009, 2017, 2024, 2029, 2035, 2040, 2045, 2053, 2058, 2063, 2072, 2079, 2084, 2089, 2094, 2099)
    3000 (2947, 2955, 2966, 2971, 2976, 2981, 2986, 2994, 2999, 3004, 3009, 3017, 3024, 3029, 3035, 3040, 3045, 3053, 3058, 3063, 3072, 3079, 3084, 3089, 3094, 3099)
    """
    count, state = (
        3000,
        (
            2947,
            2955,
            2966,
            2971,
            2976,
            2981,
            2986,
            2994,
            2999,
            3004,
            3009,
            3017,
            3024,
            3029,
            3035,
            3040,
            3045,
            3053,
            3058,
            3063,
            3072,
            3079,
            3084,
            3089,
            3094,
            3099,
        ),
    )
    target = 50000000000
    return sum(state) + (target - count) * len(state)


if __name__ == "__main__":
    raw_data = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
    """.strip()
    data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(deepcopy(data)))
    # print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer: 3051
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1300000000669
