from common import load_input

input_data = load_input(__file__.split('.')[0] + '_in.txt')

PART1_DOC = """
## [Day 02: Corruption Checksum](http://adventofcode.com/2017/day/2)

### Part 1:

The **checksum** of spreadsheet is the sum of differences between the largest
value and the smallest value on each row.
"""


def spreadsheet_checksum(lines: str) -> int:
    res = 0
    for row in lines.splitlines():
        nums = sorted(map(int, row.split()))
        res += nums[-1] - nums[0]
    return res


def test_spreadsheet_checksum():
    sample = "5 1 9 5\n7 5 3\n2 4 6 8"
    assert spreadsheet_checksum(sample) == 18
    print("Part 1: Pass")


print(spreadsheet_checksum(input_data))

PART2_DOC = """
### Part 2

For each row, find the only two numbers that one evenly divides the other.
The task is to find those numbers on each line, divide them, and add up each
line's result.
"""


def divided_sum(lines: str) -> int:
    res = 0
    for line in lines.splitlines():
        nums = sorted(map(int, line.split()))
        for a in nums:
            found = False
            for b in reversed(nums):
                if a >= b:
                    break
                elif b % a == 0:
                    res += b // a
                    found = True
                    break
            if found:
                break
    return res


def test_divided_sum():
    sample = "5 9 2 8\n9 4 7 3\n3 8 6 5"
    assert divided_sum(sample) == 9
    print("Part 2: Pass")


print(divided_sum(input_data))
