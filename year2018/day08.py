import sys
from copy import deepcopy
from collections import namedtuple

from common import load_input

Node = namedtuple("Node", ["meta", "child"])


def preprocess(raw):
    data = list(map(int, raw.split()))

    def parse_node(payload):
        n_child, n_meta, *rest = payload
        children = []
        for _ in range(n_child):
            child, rest = parse_node(rest)
            children.append(child)
        meta, rest = rest[:n_meta], rest[n_meta:]
        return Node(meta=meta, child=children), rest

    tree, _ = parse_node(data)

    return tree


def fn_p1(data):
    def sum_meta(node):
        return sum(node.meta) + sum(sum_meta(child) for child in node.child)

    return sum_meta(data)


def fn_p2(data):
    def value(node):
        if not node.child:
            return sum(node.meta)
        else:
            return sum(
                value(node.child[t - 1]) for t in node.meta if 1 <= t <= len(node.child)
            )

    return value(data)


if __name__ == "__main__":
    raw_data = """
    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    """.strip()
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 35911
    print("Part 2:", fn_p2(deepcopy(data)))  # answer:
