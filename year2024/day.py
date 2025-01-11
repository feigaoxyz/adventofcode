import sys
from copy import deepcopy


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """

""".strip()


def preprocess(raw: str):
    return raw


def fn_p1(data):
    return


def fn_p2(data):
    return


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer:
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer:

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    # data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer:
    # print("Part 2:", fn_p2(deepcopy(data)))  # answer:
