import itertools
import math
from common import validation, neighbors

PART1_DOC = """
## [Day 03: Spiral Memory](http://adventofcode.com/2017/day/3)

### Part 1

Compute the Manhatten distance between a number and 1 in spiraling grid:
```
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
```
"""


def spiral_to_xy(num) -> (int, int):
    """Return the (x, y) coordinate of number `num`.
    Number `1` at (0, 0).
    """
    n2 = int(math.sqrt(num))
    if n2 % 2 == 0:
        n2 -= 1
    side = n2 + 1
    r = n2 // 2

    # print(num, n2)
    if n2**2 == num:
        return (r, -r)

    x, y = r + 1, -r - 1
    remain = num - n2**2

    if remain > side:
        y += side
        remain -= side
    else:
        return (x, y + remain)

    if remain > side:
        x -= side
        remain -= side
    else:
        return (x - remain, y)

    if remain > side:
        y -= side
        remain -= side
    else:
        return (x, y - remain)

    if remain > side:
        x += side
        remain -= side
    else:
        return (x + remain, y)

    assert False


def distance_spiral(a, b=1) -> int:
    ax, ay = spiral_to_xy(a)
    return abs(ax) + abs(ay)


def test_spiral_to_xy():
    fn = spiral_to_xy
    validation(fn, (1, ), (0, 0))
    validation(fn, (9, ), (1, -1))
    validation(fn, (2, ), (1, 0))
    validation(fn, (3, ), (1, 1))
    validation(fn, (4, ), (0, 1))
    validation(fn, (8, ), (0, -1))
    validation(fn, (23, ), (0, -2))
    print("Pass")


def test_distance_spiral():
    fn = distance_spiral
    validation(fn, (1, ), 0)
    validation(fn, (12, ), 3)
    validation(fn, (23, ), 2)
    validation(fn, (1024, ), 31)
    print("Part 1: Pass")


input_data = 289326
print("Part 1:", distance_spiral(input_data))

PART2_DOC = """
### Part 2

With the same spiral shape, now write down the sum of known adjacents of
current location. The first few values look like:
```
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
```

Return the first value written that is larger than puzzle input.
"""


def spiral_adj_sum_seq(bound) -> iter:
    grid = {(0, 0): 1}
    for num in itertools.count(2):
        loc = spiral_to_xy(num)
        value = 0
        for nb in neighbors(loc, 8):
            value += grid.get(nb, 0)
        if value > bound:
            return value
        grid[loc] = value


def test_spiral_adj_sum_seq():
    fn = spiral_adj_sum_seq
    validation(fn, (1, ), 2)
    validation(fn, (2, ), 4)
    validation(fn, (20, ), 23)
    validation(fn, (100, ), 122)


print("Part 2:", spiral_adj_sum_seq(input_data))
