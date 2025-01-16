import sys
from copy import deepcopy
import numpy as np
import re


def load_input(fn: str) -> str:
    """Loading downloaded input."""
    try:
        with open(fn, "r") as fp:
            return fp.read()
    except FileNotFoundError:
        print("File not exists.")
        return ""


sample_raw_data = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()


def preprocess(raw: str):
    puzzles = list()
    for chunk in raw.split("\n\n"):
        puzzles.append([int(v) for v in re.findall(r"\d+", chunk)])
    # print(puzzles)
    return puzzles


def solve_linear_equations(a, b):
    """
    Solve the linear equations A * x = b.

    Parameters:
        a (2D array-like): Coefficient matrix (n x n).
        b (1D array-like): Values (n x 1).

    Returns:
        str or np.ndarray: Returns the solution as a numpy array if unique, or
                           a string indicating 'no solution' or 'infinite solutions'.
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)

    # Check if the matrix is square
    if a.shape[0] != a.shape[1]:
        return "Invalid input: Coefficient matrix must be square."

    try:
        # Attempt to compute the solution using numpy.linalg.solve
        x = np.linalg.solve(a, b)
        return x
    except np.linalg.LinAlgError as e:
        # Handle singular matrix case
        rank_a = np.linalg.matrix_rank(a)
        aug_matrix = np.hstack((a, b.reshape(-1, 1)))
        rank_aug = np.linalg.matrix_rank(aug_matrix)

        if rank_a < rank_aug:
            return "no"
        elif rank_a == rank_aug:
            return "inf"
        else:
            return "no"


def solve1_1(ax, ay, bx, by, px, py):
    sol = solve_linear_equations([[ax, bx], [ay, by]], [px, py])
    if type(sol) is str:
        if sol == "no":
            pass
        elif sol == "inf":
            temp = []
            if ax != 0:
                for pa in range(100):
                    rx, ry = px - ax * pa, py - ay * pa
                    if rx < 0 or ry < 0:
                        break
                    if bx != 0:
                        if rx % bx == 0:
                            temp.append([pa, rx // bx])
                    else:
                        if by != 0:
                            if ry % by == 0:
                                temp.append([pa, ry // by])
            else:
                pass
            return temp
    else:
        pa, pb = sol[0], sol[1]
        if pa >= 0 and pb >= 0 and abs(round(pa) - pa) + abs(round(pb) - pb) < 0.001:
            return [(round(pa), round(pb))]
    return []


def fn_p1(data):
    cost = 0
    for pz in data:
        sols = solve1_1(*pz[:6])
        if sols:
            cost += min([3 * pa + pb for (pa, pb) in sols])
    return cost


def solve1_2(ax, ay, bx, by, px, py):
    temp = []
    for pa in range(101):
        if ax * pa > px or ay * pa > py:
            break
        elif ax * pa == px and ay * pa == py:
            temp.append((pa, 0))
        else:
            if bx != 0:
                pb = (px - ax * pa) // bx
            elif by != 0:
                pb = (py - ay * pa) // by
            if ax * pa + bx * pb == px and ay * pa + by * pb == py:
                temp.append((pa, pb))
    return temp


def fn_p1v2(data):
    cost = 0
    for pz in data:
        sols = solve1_2(*pz[:6])
        if sols:
            cost += min([3 * pa + pb for (pa, pb) in sols])

    return cost


def debug(data):
    for pz in data:
        sols1 = solve1_1(*pz[:6])
        sols2 = solve1_2(*pz[:6])
        if len(sols1) != len(sols2):
            print(pz, sols1, sols2)


def fn_p2(data):
    cost = 0
    for pz in data:
        pz[4] += 10000000000000
        pz[5] += 10000000000000
        sols = solve1_1(*pz[:6])
        if sols:
            cost += min([3 * pa + pb for (pa, pb) in sols])

    return cost


if __name__ == "__main__":
    data = preprocess(sample_raw_data)
    print("Part 1 Example:", fn_p1v2(deepcopy(data)))  # answer: 480
    print("Part 2 Example:", fn_p2(deepcopy(data)))  # answer: 875318608908

    raw_data = load_input(
        sys.argv[1] if len(sys.argv) == 2 else (sys.argv[0].split(".")[0] + "_in.txt")
    ).strip()
    data = preprocess(raw_data)
    print("Part 1:", fn_p1(deepcopy(data)))  # answer: 35997
    # print("Part 1:", fn_p1v2(deepcopy(data)))  # answer: 35997
    # debug(deepcopy(data))
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 82510994362072
