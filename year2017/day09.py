from common import load_input

PART1_DOC = """Part 1:
group = {thing*,}
thing = group | garbage
garbage = < any char including "{" "}" and "<" >
inside garbage, *any* char after "!" is ignored

Your goal is to find the total score for all groups in your input.
Each group is assigned a score which is one more than the score of
the group that immediately contains it.
(The outermost group gets a score of 1.)
"""

PART2_DOC = """Part 2:

"""

example = """
"""
input_data = load_input(__file__.split('.')[0] + '_in.txt')


def group_scores(group_str: str) -> int:
    ignore = False
    total_score = cur_score = 0
    in_garbage = False
    for cur in group_str:
        if ignore:
            ignore = False
            continue
        elif cur == '!':
            ignore = True
            continue
        elif in_garbage:
            if cur == '>' and not ignore:
                in_garbage = False
        else:
            if cur == '{':
                cur_score += 1
            elif cur == '}':
                total_score += cur_score
                cur_score -= 1
            elif cur == '<':
                in_garbage = True
    return total_score


fn_p1 = group_scores
print("Part 1 example:", fn_p1("{}"))
print("Part 1 example:", fn_p1("{{},{}}"))
print("Part 1 example:", fn_p1("{{{}}}"))
print("Part 1 example:", fn_p1("{{{},{},{{}}}}"))
print("Part 1 example:", fn_p1("{{<ab>},{<ab>},{<ab>},{<ab>}}"))
print("Part 1 example:", fn_p1("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
print("Part 1 example:", fn_p1("{{<a!>},{<a!>},{<a!>},{<ab>}}"))
print("Part 1:", fn_p1(input_data))  # 14212


def counting_garbage_char(group_str: str) -> int:
    ignore = False
    garbage_char = 0
    in_garbage = False
    for cur in group_str:
        if ignore:
            ignore = False
            continue
        elif cur == '!':
            ignore = True
            continue
        elif in_garbage:
            if cur == '>' and not ignore:
                in_garbage = False
            else:
                garbage_char += 1
        elif cur == '<':
            in_garbage = True
    return garbage_char


fn_p2 = counting_garbage_char
print("Part 2 example:", fn_p2("<>"))
print("Part 2 example:", fn_p2("<<<<>"))
print("Part 2 example:", fn_p2('<{o"i!a,<{i<a>'))
print("Part 2:", fn_p2(input_data))  # 6569
