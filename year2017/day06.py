from common import load_input

input_data = list(
    map(int, load_input(__file__.split('.')[0] + '_in.txt').split()))

PART1_DOC = """
Part 1: In each cycle, it finds the memory bank with the most blocks (ties won
by the lowest-numbered memory bank) and redistributes those blocks among the
banks.

The debugger would like to know how many redistributions can be done before a
blocks-in-banks configuration is produced that has been seen before.
"""


def redistribute(banks: list) -> int:
    seen = set()
    steps = 0

    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        steps += 1
        max_v = max_i = -1
        for i, v in enumerate(banks):
            if max_v < v:
                max_v = v
                max_i = i
        div, rem = divmod(max_v, len(banks))
        banks[max_i] = 0
        for i in range(len(banks)):
            if i < rem:
                banks[(max_i + i + 1) % len(banks)] += div + 1
            else:
                banks[(max_i + i + 1) % len(banks)] += div
        # print(steps, banks)

    return steps


fn_p1 = redistribute
assert fn_p1([0, 2, 7, 0]) == 5
# print("Part 1:", fn_p1(input_data[::]))  # 11137

PART2_DOC = """
Part 2: How many cycles are in the infinite loop that arises from the
configuration in your puzzle input?
"""


def redistribute_cycle(banks: list) -> int:
    seen = dict()
    steps = 0

    while True:
        if tuple(banks) not in seen:
            seen[tuple(banks)] = steps
        else:
            return steps - seen[tuple(banks)]
        steps += 1
        max_v = max_i = -1
        for i, v in enumerate(banks):
            if max_v < v:
                max_v = v
                max_i = i
        div, rem = divmod(max_v, len(banks))
        banks[max_i] = 0
        for i in range(len(banks)):
            if i < rem:
                banks[(max_i + i + 1) % len(banks)] += div + 1
            else:
                banks[(max_i + i + 1) % len(banks)] += div
        # print(steps, banks)


fn_p2 = redistribute_cycle
print(fn_p2([0, 2, 7, 0]), 4)
print("Part 2:", fn_p2(input_data[::]))
