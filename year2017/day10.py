from common import load_input
from functools import reduce
from operator import xor

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


def knot_hash_one_round(lengths: list,
                        knot: list,
                        offset: int = 0,
                        skip_size=0) -> (list, int, int):
    if knot is None:
        knot = list(range(256))
    list_len = len(knot)
    for length in lengths:
        if length > list_len:
            continue
        else:
            knot = knot[length:] + knot[:length][::-1]
            skip_size %= list_len
            if skip_size:
                knot = knot[skip_size:] + knot[:skip_size]
            offset -= (length + skip_size)
            skip_size += 1
            # print(length, knot, skip_size, offset)
    return (knot, offset % list_len, skip_size % list_len)


def knot_hash_full(data):
    rev_lens = list(map(ord, data.replace(' ', ''))) + [17, 31, 73, 47, 23]
    knot, offset, skip_size = list(range(256)), 0, 0
    for _ in range(64):
        knot, offset, skip_size = knot_hash_one_round(rev_lens, knot, offset,
                                                      skip_size)
    if offset:
        knot = knot[offset:] + knot[:offset]
    result = ''
    for i in range(16):
        result += '{:02x}'.format(reduce(xor, knot[i*16:(i+1)*16], 0))
    return result


def main():
    example = "3, 4, 1, 5"
    input_data = load_input(__file__.split('.')[0] + '_in.txt')

    fn_p1 = knot_hash_one_round
    print("Part 1 example:", fn_p1([3, 4, 1, 5], list(range(5))))  # 12
    knot, offset, _ = fn_p1(map(int, input_data.split(',')), None)
    print("Part 1:", knot[offset] * knot[offset + 1])  # 38628

    fn_p2 = knot_hash_full
    print("Part 2 example:", fn_p2(""))
    print("Part 2 example:", fn_p2("1,2,3"))
    print("Part 2:", fn_p2(input_data.strip().replace(
        ' ', '')))  # e1462100a34221a7f0906da15c1c979a


if __name__ == '__main__':
    main()
