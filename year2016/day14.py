import hashlib
import sys

from collections import defaultdict

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

try:
    with open(fn) as f:
        for line in f:
            items.append(line.split(','))
except:
    pass


def get_triple(s):
    try:
        for i in range(len(s)):
            if s[i] == s[i + 1] == s[i + 2]:
                return i, s[i]
    except IndexError:
        return -1, ''


def get_five(s):
    result = []
    try:
        for i in range(len(s)):
            if all(s[i] == s[i + j] for j in range(5)):
                result.append((i, s[i]))
    except IndexError:
        pass
    finally:
        return result


def part1(repeat=0):
    tuple3 = defaultdict(list)  # chr: idx
    tuple5 = defaultdict(list)  # chr: List[index]

    r1 = list()

    salt = "qzyelonm"  # "abc"  # "qzyelonm"

    count = index = 0
    while count < 75:
        hash = salt + str(index)
        for _ in range(repeat + 1):
            hash = hashlib.md5(hash.encode()).hexdigest()

        idx3, ch = get_triple(hash)
        if idx3 != -1:
            # print(index, hash)
            tuple3[ch].append(index)

        fives = get_five(hash)
        for _, ch in fives:
            # print(index, hash, ch)
            tr = []
            for idx3 in tuple3[ch]:
                if idx3 < index <= idx3 + 1000:
                    r1.append((idx3, ch, index))
                    tr.append(idx3)
                    count += 1
            for r in tr:
                tuple3[ch].remove(r)

        index += 1

    return r1


# print('Part One:', sorted(part1())[63])  # 15168
print('Part Two:', sorted(part1(repeat=2016))[63])
