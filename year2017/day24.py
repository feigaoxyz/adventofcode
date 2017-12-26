from common import load_input


BEST_SCORE = 0


def dfs(nodes, path, score, port):
    global BEST_SCORE
    for i, (p0, p1) in enumerate(nodes):
        if i in path:
            continue
        if p0 == port:
            cur_score = score + p0 + p1
            BEST_SCORE = max(BEST_SCORE, cur_score)
            dfs(nodes, path | {i}, cur_score, p1)
        elif p1 == port:
            cur_score = score + p0 + p1
            BEST_SCORE = max(BEST_SCORE, cur_score)
            dfs(nodes, path | {i}, cur_score, p0)


def fn_p1(raw: str):
    lines = [line.strip() for line in raw.strip().splitlines()]
    nodes = []
    for idx, line in enumerate(lines):
        p1, p2 = map(int, line.split('/'))
        nodes.append((p1, p2))
    dfs(nodes, set(), 0, 0)
    return BEST_SCORE


LONGEST = 0
BEST_STRENGTH = 0


def dfs_p2(nodes, path, score, port):
    global LONGEST
    global BEST_STRENGTH
    for i, (p0, p1) in enumerate(nodes):
        if i in path:
            continue
        argument = False
        if p0 == port:
            argument = True
            new_port = p1
        elif p1 == port:
            argument = True
            new_port = p0
        if argument:
            new_score = score + p0 + p1
            new_path = path | {i}
            if len(new_path) > LONGEST:
                LONGEST = len(new_path)
                BEST_STRENGTH = new_score
            elif len(new_path) == LONGEST:
                BEST_STRENGTH = max(BEST_STRENGTH, new_score)
            dfs_p2(nodes, new_path, new_score, new_port)


def fn_p2(raw: str):
    lines = [line.strip() for line in raw.strip().splitlines()]
    nodes = []
    for idx, line in enumerate(lines):
        p1, p2 = map(int, line.split('/'))
        nodes.append((p1, p2))
    dfs_p2(nodes, set(), 0, 0)
    return BEST_STRENGTH


if __name__ == '__main__':
    example = """
    0/2
    2/2
    2/3
    3/4
    3/5
    0/1
    10/1
    9/10
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example))  # 31
    # print("Part 1:", fn_p1(input_data))  # 1656

    print("Part 2 example:", fn_p2(example))  # 19
    print("Part 2:", fn_p2(input_data))  # 1642
