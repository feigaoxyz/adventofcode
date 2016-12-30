import sys

try:
    if len(sys.argv) > 1:
        fn = sys.argv[1]
    else:
        fn = __file__.split('.')[0] + '_input.txt'

    lines = []

    with open(fn) as f:
        for line in f:
            lines.append(line.split())
except FileNotFoundError:
    pass


def str2func(words):
    if words[0:2] == ['swap', 'position']:
        x, y = int(words[2]), int(words[5])

        def swap_pos(lst):
            lst[x], lst[y] = lst[y], lst[x]
            return lst

        return swap_pos

    elif words[0:2] == ['swap', 'letter']:
        x, y = words[2], words[5]

        def swap_letter(lst):
            for i, c in enumerate(lst):
                if c == x:
                    lst[i] = y
                elif c == y:
                    lst[i] = x
            return lst

        return swap_letter

    elif words[0] == 'rotate':
        if words[1] == 'left':
            def rotate_left(lst):
                offset = int(words[2]) % len(lst)
                return lst[offset:] + lst[:offset]

            return rotate_left
        elif words[1] == 'right':
            def rotate_right(lst):
                offset = int(words[2]) % len(lst)
                return lst[-offset:] + lst[:-offset]

            return rotate_right
        elif words[1] == 'based':
            x = words[-1]

            def rotate_letter(lst: list):
                offset = lst.index(x)
                s = 'rotate right {}'.format(offset + 1 + (1 if offset >= 4 else 0))
                return str2func(s.split())(lst)

            return rotate_letter

    elif words[0] == 'reverse':
        x, y = int(words[2]), int(words[4])
        x, y = min(x, y), max(x, y)

        def reverse(lst):
            return lst[:x] + lst[x:y + 1][::-1] + lst[y + 1:]

        return reverse

    elif words[0] == 'move':
        x, y = int(words[2]), int(words[5])

        def move(lst: list):
            lst.insert(y, lst.pop(x))
            return lst

        return move


def solution(*args, **kws):
    lines = args[0]
    passwd = list(args[1])
    for line in lines:
        passwd = str2func(line)(passwd)
    return ''.join(passwd)


assert solution(['swap position 4 with position 0'.split()], 'abcde') == 'ebcda'
assert solution(['swap letter d with letter b'.split()], 'ebcda') == 'edcba'
assert solution(['reverse positions 0 through 4'.split()], 'edcba') == 'abcde'
assert solution(['rotate left 1 step'.split()], 'abcde') == 'bcdea'
assert solution(['move position 1 to position 4'.split()], 'bcdea') == 'bdeac'
assert solution(['move position 3 to position 0'.split()], 'bdeac') == 'abdec'
assert solution(['rotate based on position of letter b'.split()], 'abdec') == 'ecabd'
assert solution(['rotate based on position of letter d'.split()], 'ecabd') == 'decab'

r1 = solution(lines, 'abcdefgh')
print('Part One:', r1)  # bfheacgd


def solution2(*args, **kws):
    passwd = args[0]
    from itertools import permutations
    for plain in permutations(sorted(list(passwd))):
        if solution(lines, plain) == passwd:
            return ''.join(plain)
    return None


r2 = solution2('fbgdceah')
print('Part Two:', r2)  # gcehdbfa
