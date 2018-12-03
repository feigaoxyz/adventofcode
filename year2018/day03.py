from common import load_input


def preprocess(raw):
    result = []
    max_width = 0
    max_height = 0
    for line in raw.splitlines():
        (claim_id, at_sign, left_top, wh) = line.split()
        left, top = map(int, left_top[:-1].split(","))
        width, height = map(int, wh.split("x"))
        max_width = max(max_width, left + width)
        max_height = max(max_height, top + height)
        result.append((left, top, width, height, int(claim_id[1:])))
    grid = [[[] for _ in range(max_width)] for _ in range(max_height)]
    for l, t, w, h, s in result:
        for i in range(w):
            for j in range(h):
                grid[t + j][l + i].append(s)
    return grid


def fn_p1(raw: str):
    grid = preprocess(raw)
    count = 0
    for row in grid:
        for cell in row:
            if len(cell) > 1:
                count += 1
    return count


def fn_p2(raw: str):
    grid = preprocess(raw)
    all_id = set()
    over_id = set()
    for row in grid:
        for cell in row:
            scell = set(cell)
            all_id.update(scell)
            if len(cell) >= 2:
                over_id.update(scell)
    return all_id.difference(over_id).pop()


if __name__ == "__main__":
    example = """
    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2
    """.strip()
    input_data = load_input(__file__.split(".")[0] + "_in.txt").strip()

    print("Part 1 example:", fn_p1(example))
    print("Part 1:", fn_p1(input_data))  # 110383

    print("Part 2 example:", fn_p2(example))
    print("Part 2:", fn_p2(input_data))  # 129
