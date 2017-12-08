from common import load_input

PART1_DOC = """Part 1:
What is the largest value in any register after completing the instructions in
your puzzle input?
"""

PART2_DOC = """Part 2:

"""

input_data = load_input(__file__.split('.')[0] + '_in.txt')
example = """
"""

fn_p1 = print
print("Part 1 example:", fn_p1(example))
print("Part 1:", fn_p1(input_data))

# fn_p2 = print
# print("Part 2 example:", fn_p2(example))
# print("Part 2:", fn_p2(input_data))
