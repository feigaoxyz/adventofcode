from common import load_input

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


def spinlock(step, round):
    spin = [0]
    for k in range(1, round + 1):
        p = step % k
        spin = spin[p:] + spin[:p]
        spin.append(k)
        # print(spin)
    return spin


def fn_p1(raw: str, round=2017):
    step = int(raw)
    spin = spinlock(step, round)
    return spin[0]


def fn_p2(raw: str, round=50000000):
    step = int(raw)
    remainder = 0
    result = None
    for k in range(1, round + 1):
        remainder = (remainder + step) % k + 1
        if remainder == 1:
            result = k
    return result


if __name__ == '__main__':
    example = 3
    input_data = 386

    # print("Part 1 example:", fn_p1(example))  # 638
    # print("Part 1:", fn_p1(input_data))  # 419

    # print("Part 2 example:", fn_p2(example, 2017))
    print("Part 2:", fn_p2(input_data))  # 46038988
