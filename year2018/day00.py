import sys

from common import load_input


def fn_p1(raw: str):
    pass


def fn_p2(raw: str):
    pass


if __name__ == "__main__":
    example = """
    """.strip()
    # print("Part 1 example:", fn_p1(example))
    # print("Part 2 example:", fn_p2(example))

    input_data = load_input(sys.argv[1]).strip()
    print("Part 1:", fn_p1(input_data))  # answer:
    print("Part 2:", fn_p2(input_data))  # answer:
