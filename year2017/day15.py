from common import load_input

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


def generator(start_value, factor, mod=2147483647, predict=None):
    if predict is None:
        predict = lambda v: True
    value = start_value
    while True:
        value = ((value * factor) % mod)
        if predict(value):
            yield value
    return


def judge(ga, gb, round):
    mask = (1 << 16) - 1
    return sum(next(ga) & mask == next(gb) & mask for _ in range(round))


def fn_p1(raw: str):
    seed_a, seed_b = map(int,
                         [l.strip().split()[-1] for l in raw.splitlines()])
    fa, fb = 16807, 48271
    gen_a = generator(seed_a, factor=fa)
    gen_b = generator(seed_b, factor=fb)
    return judge(gen_a, gen_b, 40_000_000)


def fn_p2(raw: str):
    seed_a, seed_b = map(int,
                         [l.strip().split()[-1] for l in raw.splitlines()])
    fa, fb = 16807, 48271
    gen_a = generator(seed_a, factor=fa, predict=lambda v: v % 4 == 0)
    gen_b = generator(seed_b, factor=fb, predict=lambda v: v % 8 == 0)
    # return judge(gen_a, gen_b, 5_000_000)
    return judge(gen_a, gen_b, 5_000_000)


if __name__ == '__main__':
    example = """65
    8921
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example))  # 588
    # print("Part 1:", fn_p1(input_data))  # 569

    # print("Part 2 example:", fn_p2(example))  # 309
    print("Part 2:", fn_p2(input_data))  # 298
