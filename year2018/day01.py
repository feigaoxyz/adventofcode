from common import load_input


def fn_p1(raw: str):
    lines = raw.splitlines()
    return sum(int(l) for l in lines)
    pass


def fn_p2(raw: str):
    freqs = [int(l) for l in raw.splitlines()]
    seen = set()
    curr = 0
    idx = 0
    while curr not in seen:
        seen.add(curr)
        curr += freqs[idx % len(freqs)]
        idx += 1
    return curr


if __name__ == "__main__":
    example = """
    """.strip()
    input_data = load_input(__file__.split(".")[0] + "_in.txt").strip()

    # print("Part 1 example:", fn_p1(example))
    print("Part 1:", fn_p1(input_data))

    # print("Part 2 example:", fn_p2(example))
    print("Part 2:", fn_p2(input_data))
