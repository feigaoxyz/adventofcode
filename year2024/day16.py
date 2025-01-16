import sys
from copy import deepcopy


def load_input(filename: str) -> str:
    """Load input data from a file."""
    try:
        with open(filename, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print("File not found.")
        return ""


def bfs(maze):
    """Breadth-First Search to calculate shortest paths in the maze."""
    start = next(
        (r, c)
        for r, row in enumerate(maze)
        for c, cell in enumerate(row)
        if cell == "S"
    )
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    todo = {(start, 0)}
    status = {(start, 0): 0}

    while todo:
        cur_pos, cur_dir = todo.pop()
        cur_cost = status[(cur_pos, cur_dir)]

        for next_pos, next_dir, cost_diff in [
            (cur_pos, (cur_dir + 1) % 4, 1000),
            (cur_pos, (cur_dir + 3) % 4, 1000),
            (
                (
                    cur_pos[0] + directions[cur_dir][0],
                    cur_pos[1] + directions[cur_dir][1],
                ),
                cur_dir,
                1,
            ),
        ]:
            if maze[next_pos[0]][next_pos[1]] == "#":
                continue

            next_cost = status.get((next_pos, next_dir), float("inf"))
            if cur_cost + cost_diff < next_cost:
                status[(next_pos, next_dir)] = cur_cost + cost_diff
                todo.add((next_pos, next_dir))

    return status


def preprocess(raw: str):
    """Prepare the maze and compute BFS results."""
    maze = [list(line) for line in raw.splitlines()]
    status = bfs(maze)
    return maze, status


def find_end(maze):
    """Locate the end position 'E' in the maze."""
    return next(
        (r, c)
        for r, row in enumerate(maze)
        for c, cell in enumerate(row)
        if cell == "E"
    )


def fn_p1(data):
    """Compute the minimum cost to reach the end."""
    maze, status = data
    end = find_end(maze)
    return min(status.get((end, d), float("inf")) for d in range(4))


def fn_p2(data):
    """Compute the size of the area with optimal paths."""
    maze, status = data
    end = find_end(maze)

    best_cost = min(status.get((end, d), float("inf")) for d in range(4))
    optimal_todo = {
        (end, d) for d in range(4) if status.get((end, d), float("inf")) == best_cost
    }
    optimal_positions = {end}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while optimal_todo:
        cur_pos, cur_dir = optimal_todo.pop()
        for prev_pos, prev_dir, cost_diff in [
            (cur_pos, (cur_dir + 1) % 4, 1000),
            (cur_pos, (cur_dir + 3) % 4, 1000),
            (
                (
                    cur_pos[0] - directions[cur_dir][0],
                    cur_pos[1] - directions[cur_dir][1],
                ),
                cur_dir,
                1,
            ),
        ]:
            if (
                status.get((prev_pos, prev_dir), float("inf")) + cost_diff
                == status[(cur_pos, cur_dir)]
            ):
                optimal_todo.add((prev_pos, prev_dir))
                optimal_positions.add(prev_pos)

    return len(optimal_positions)


s1 = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()

s2 = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
""".strip()

sample_raw_data = s1

if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))  # answer: s1: 7036; s2: 11048
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: s1: 45; s2: 64

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) > 1 else sys.argv[0].split(".")[0] + "_in.txt"
    )
    if raw_data:
        data = preprocess(raw_data)
        print("Part 1:", fn_p1(deepcopy(data)))  # answer: 115500
        print("Part 2:", fn_p2(deepcopy(data)))  # answer: 679
