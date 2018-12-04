import sys

from common import load_input


def preprocess(raw):
    return raw


def fn_p1(data):
    return


def fn_p2(data):
    return


if __name__ == "__main__":
    raw_data = """
    """.strip()
    data = preprocess(raw_data)
    # print("Part 1 Example:", fn_p1(raw_data))
    # print("Part 2 Example:", fn_p2(raw_data))

    raw_data = load_input(sys.argv[1]).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(data))  # answer:
    print("Part 2:", fn_p2(data))  # answer:
