from common import load_input
from collections import defaultdict
import operator as op

PART1_DOC = """Part 1:
What is the largest value in any register after completing the instructions in
your puzzle input?
"""

PART2_DOC = """Part 2:
the highest value held in any register during this process
"""

OPS = {
    '>': op.gt,
    '<': op.lt,
    '>=': op.ge,
    '<=': op.le,
    '==': op.eq,
    '!=': op.ne
}


def execute_line(line: str, variables: dict) -> dict:
    parts = line.split()
    # b inc 5 if a > 1
    if OPS[parts[5]](variables[parts[4]], int(parts[6])):
        if parts[1] == 'inc':
            variables[parts[0]] += int(parts[2])
        elif parts[1] == 'dec':
            variables[parts[0]] -= int(parts[2])
    return variables


def find_largest_after_execution(lines: str) -> int:
    variables = defaultdict(int)
    for line in lines.splitlines():
        variables = execute_line(line, variables)
    return max(variables.values())


example = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

input_data = load_input(__file__.split('.')[0] + '_in.txt')

# fn_p1 = find_largest_after_execution
# print("Part 1:", fn_p1(example))
# print("Part 1:", fn_p1(input_data))  # 4416


def find_largest_during_execution(lines: str) -> int:
    variables = defaultdict(int)
    highest = 0
    for line in lines.splitlines():
        variables = execute_line(line, variables)
        highest = max(highest, max(variables.values()))
    return highest


fn_p2 = find_largest_during_execution
print("Part 2 example:", fn_p2(example))
print("Part 2:", fn_p2(input_data))
