from common import load_input
from string import ascii_lowercase

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""

LEN = 0


def spin_v0(c2i, i2c, offset):
    for c in c2i:
        np = (c2i[c] + offset) % len(c2i)
        c2i[c] = np
        i2c[np] = c


def exchange_v0(c2i, i2c, pa, pb):
    ca, cb = i2c[pa], i2c[pb]
    c2i[ca], c2i[cb] = pb, pa
    i2c[pa], i2c[pb] = cb, ca


def partner_v0(c2i, i2c, ca, cb):
    ia, ib = c2i[ca], c2i[cb]
    c2i[ca], c2i[cb] = ib, ia
    i2c[ia], i2c[ib] = cb, ca


def one_dance_v0(c2i, i2c, ops):
    for fn, *param in ops:
        globals().get(fn.__name__ + '_v0')(c2i, i2c, *param)
        # fn(c2i, i2c, *param)


def fn_p1_v0(raw: str, num=16):
    global LEN
    LEN = num
    c2i = dict(zip(ascii_lowercase, range(num)))
    i2c = dict(zip(range(num), ascii_lowercase))
    one_dance_v0(c2i, i2c, map(op_parser, raw.split(',')))
    last = ''
    for i in range(num):
        last += i2c[i]
    return last


def spin(positions, letters, offset):
    np = {}
    for p in positions:
        # positions[p] = (positions[p] - offset) % LEN
        np[(p + offset) % LEN] = positions[p]
    positions.update(np)


def exchange(positions, letters, pa, pb):
    positions[pa], positions[pb] = positions[pb], positions[pa]


def partner(positions, letters, ca, cb):
    letters[ca], letters[cb] = letters[cb], letters[ca]


def op_parser(op: str) -> tuple:
    if op[0] == 's':
        return spin, int(op[1:])
    elif op[0] == 'x':
        i1, i2 = map(int, op[1:].split('/'))
        return exchange, i1, i2
    elif op[0] == 'p':
        c1, c2 = op[1:].split('/')
        return partner, c1, c2
    else:
        raise ValueError


def one_dance(positions, letters, ops):
    for fn, *param in ops:
        fn(positions, letters, *param)


def recover_string(positions, letters):
    letters_rev = dict((v, k) for k, v in letters.items())
    last = ['' for _ in range(LEN)]
    for i in range(LEN):
        last[i] = letters_rev[chr(ord('a') + positions[i])]
    return ''.join(last)


def fn_p1(raw: str, num=16):
    global LEN
    LEN = num
    positions = dict(zip(range(num), range(num)))
    letters = dict(zip(ascii_lowercase[:num], ascii_lowercase[:num]))
    one_dance(positions, letters, map(op_parser, raw.split(',')))
    # print(positions, letters)
    return recover_string(positions, letters)


def debug_p1(example, data):
    # print(fn_p1_v0(example, 5))
    # print(fn_p1(example, 5))

    for l in range(1, 1500):
        data_ = ','.join(data.split(',')[:l])
        ro = (fn_p1_v0(data_, 16))
        rn = (fn_p1(data_, 16))
        if ro != rn:
            print('--\n', data_, '\n', ro, '\n', rn)
            break


def compose(ma, mb):
    mc = {}
    for k in mb:
        mc[k] = ma[mb[k]]
    return mc


def fn_p2(raw: str, num, round=10**9):
    global LEN
    LEN = num
    positions = dict(zip(range(num), range(num)))
    letters = dict(zip(ascii_lowercase[:num], ascii_lowercase[:num]))

    one_dance(positions, letters, map(op_parser, raw.split(',')))

    positions_acc = dict(zip(range(num), range(num)))
    letters_acc = dict(zip(ascii_lowercase[:num], ascii_lowercase[:num]))
    while round:
        if round & 1:
            positions_acc = compose(positions_acc, positions)
            letters_acc = compose(letters_acc, letters)
        positions = compose(positions, positions)
        letters = compose(letters, letters)
        round >>= 1

    # print(positions, letters)
    return recover_string(positions_acc, letters_acc)


if __name__ == '__main__':
    example = """s1,x3/4,pe/b
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example, 5))  # baedc
    # print("Part 1:", fn_p1(input_data))  # lbdiomkhgcjanefp
    # debug_p1(example, input_data)

    print("Part 2 example:", fn_p2(example, 5, 2))  # ceadb
    print("Part 2:", fn_p2(input_data, 16, 10**9))  # ejkflpgnamhdcboi
