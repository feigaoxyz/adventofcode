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


sample1 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""".strip()

sample2 = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip()

sample_raw_data = sample2


def preprocess(raw: str):
    [box, attempts, *_] = raw.split("\n\n")
    box = [list(b.strip()) for b in box.split()]
    attempts = "".join(attempts.split())
    return (box, attempts)


def print_box(box):
    print("\n".join(["".join(r) for r in box]))


direction = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


def move(box, curr, attempt):
    cr, cc = curr
    nr, nc = cr + direction[attempt][0], cc + direction[attempt][1]

    if box[nr][nc] == "#":
        return False
    if box[nr][nc] in "[]O":
        if move(box, (nr, nc), attempt) is False:
            return False
    if box[nr][nc] == ".":
        box[nr][nc], box[cr][cc] = box[cr][cc], box[nr][nc]
        return True


def fn_p1(data):
    box, attempts = data

    (row, col) = (None, None)
    for r in range(len(box)):
        if row is not None:
            break
        else:
            for c in range(len(box[r])):
                if box[r][c] == "@":
                    row, col = r, c
                    break

    cr, cc = row, col
    for attempt in attempts:
        nr, nc = cr + direction[attempt][0], cc + direction[attempt][1]
        move(box, (cr, cc), attempt)
        if box[cr][cc] == "@":
            pass
        elif box[nr][nc] == "@":
            cr, cc = nr, nc
        else:
            print("error")
        # print_box(box)

    gps = 0
    for r in range(len(box)):
        for c in range(len(box[r])):
            if box[r][c] == "O":
                gps += 100 * r + c
    return gps


def move2(box, curr, attempt):
    cr, cc = curr
    nr, nc = cr + direction[attempt][0], cc + direction[attempt][1]
    backup = deepcopy(box)
    if box[nr][nc] == "#":
        return False, box
    if box[nr][nc] in "[]":
        if attempt in "<>":
            if not move(box, (nr, nc), attempt):
                return False, backup
            else:
                pass
        else:
            nc2 = nc + (1 if backup[nr][nc] == "[" else -1)
            (r1, box) = move2(box, (nr, nc), attempt)
            if not r1:
                return False, backup
            (r2, box) = move2(box, (nr, nc2), attempt)
            if not r2:
                return False, backup
            # return move2(box, curr, attempt)
    if box[nr][nc] == ".":
        box[nr][nc], box[cr][cc] = box[cr][cc], box[nr][nc]
        return True, box
        # if box[cr][cc] == "@":
        #     box[nr][nc], box[cr][cc] = box[cr][cc], box[nr][nc]
        #     return True, box
        # if box[cr][cc] in "[]":
        #     nc2 = nc + (1 if box[cr][cc] == "[" else -1)
        #     if box[nr][nc2] == ".":
        #         box[nr][nc], box[cr][cc] = box[cr][cc], box[nr][nc]
        #         box[nr][nc2], box[cr][nc2] = box[cr][nc2], box[nr][nc2]
        #         return True, box
    return False, backup


def fn_p2(data):
    box, attempts = data

    next_box = []
    for row in box:
        next_box.append([])
        for ch in row:
            if ch == "#":
                next_box[-1].extend("##")
            elif ch == "O":
                next_box[-1].extend("[]")
            elif ch == ".":
                next_box[-1].extend("..")
            elif ch == "@":
                next_box[-1].extend("@.")
    box = next_box
    # print_box(box)

    (row, col) = (None, None)
    for r in range(len(box)):
        if row is not None:
            break
        else:
            for c in range(len(box[r])):
                if box[r][c] == "@":
                    row, col = r, c
                    break

    cr, cc = row, col
    for (i, attempt) in enumerate(attempts):
        # print_box(box)
        # print("move", i, attempt, (cr, cc))
        backup = deepcopy(box)
        r, box = move2(box, (cr, cc), attempt)
        if r:
            cr, cc = cr + direction[attempt][0], cc + direction[attempt][1]
        else:
            box = backup
        # print_box(box)
        # print("@", (cr, cc))
        assert box[cr][cc] == "@"
    # print_box(box)

    gps = 0
    for r in range(len(box)):
        for c in range(len(box[r])):
            if box[r][c] == "[":
                gps += 100 * r + c
    return gps


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: 10092
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer:

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 1412971
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 1429299
