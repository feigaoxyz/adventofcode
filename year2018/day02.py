import sys
from collections import Counter
from common import load_input


def fn_p1(raw: str):
    two_three = [
        (2 in c.values(), 3 in c.values()) for c in map(Counter, raw.splitlines())
    ]
    return len([x for x in two_three if x[0] == True]) * len(
        [x for x in two_three if x[1] == True]
    )


def fn_p2(raw: str):
    lines = raw.splitlines()
    for i in range(len(lines[0]) - 1):
        seen = set()
        for line in lines:
            cut = line[:i] + line[i + 1 :]
            if cut in seen:
                return cut
            else:
                seen.add(cut)
    return ""


if __name__ == "__main__":
    example = """
    """.strip()
    # print("Part 1 example:", fn_p1(example))
    # print("Part 2 example:", fn_p2(example))

    input_data = load_input(sys.argv[1]).strip()
    print("Part 1:", fn_p1(input_data))  # 5478
    print("Part 2:", fn_p2(input_data))  # qyzphxoiseldjrntfygvdmanu
