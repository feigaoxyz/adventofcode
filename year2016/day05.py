import hashlib
import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

items = []

with open(fn) as f:
    for line in f:
        items.append(line)

puzzle = 'reyedfim'


def sol_1():
    length = 1

    r1 = []
    r1idx = []
    r2 = [None for _ in range(length)]
    r2idx = []

    i = 1e7
    while len(r2idx) < length or len(r2idx) < length:
        md5 = hashlib.md5((puzzle + str(i)).encode()).hexdigest()  # type: str
        # if all(x == '0' for x in md5[:5]):
        if md5.startswith('00000'):
            r1.append(md5[5])
            r1idx.append(i)

            idx = int(md5[5], 16)
            if 0 <= idx < length and r2[idx] is None:
                r2[idx] = md5[6]
                r2idx.append(i)
        i += 1

    print('Part One:', ''.join(r1[:length]), r1idx)
    # f97c354d [797564, 938629, 1617991, 2104453, 2564359, 2834991, 3605750]

    print('Part Two:', ''.join(r2), r2idx)
    # 863dde27 [1617991, 2564359, 2834991, 3605750, 12187005, 13432325, 21679503, 25067104]


sol_1()
