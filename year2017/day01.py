import itertools
from common import load_input

input_data = load_input(__file__.split('.')[0] + '_in.txt')

PART1_DOC = """
## [Day 01: Inverse Captcha](http://adventofcode.com/2017/day/1)

In Part 1, we are asked to review a sequence of digits and find the **sum** of
all digits that match the *next* digit in the list. The list is circular, so
the digit after last is the first one in the list.
"""

PART2_DOC = """
Part 2:

In Part 2, we consider the digit *halfway around* the circular list,
instead of *next* digit.
"""


def matching_sum(digits: str, offset=1) -> int:
    """Returns the sum of digits that matching offset
    steps ahead in circular.

    :param digits: a string of digits
    :param offset: offset between matching pair
    """

    p1, p2 = itertools.tee(map(int, digits))
    p2 = itertools.islice(itertools.cycle(p2), offset, offset + len(digits))
    return sum(d1 if d1 == d2 else 0 for d1, d2 in zip(p1, p2))


def test_matching_sum_p1():
    assert matching_sum("1122") == 3
    assert matching_sum("1111") == 4
    assert matching_sum("1234") == 0
    assert matching_sum("91212129") == 9
    print("Part 1: Pass")


def test_matching_sum_p2():
    assert matching_sum("1212", 2) == 6
    assert matching_sum("1221", 2) == 0
    assert matching_sum("123425", 3) == 4
    assert matching_sum("123123", 3) == 12
    assert matching_sum("12131415", 4) == 4
    print("Part 2: Pass")


fn_p1 = matching_sum
print("Part 1:", fn_p1(input_data))

fn_p2 = matching_sum
print("Part 2:", fn_p2(input_data, len(input_data) // 2))
