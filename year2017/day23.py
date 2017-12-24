from common import load_input
from collections import defaultdict


def get_value(reg: dict, key):
    try:
        return int(key)
    except ValueError:
        return reg[key]


def fn_p1(raw: str):
    registers = defaultdict(int)
    mul_counter = 0
    lines = raw.splitlines()
    pos = 0
    while 0 <= pos < len(lines):
        op, p1, p2 = lines[pos].split()
        if op == 'set':
            registers[p1] = get_value(registers, p2)
        elif op == 'sub':
            registers[p1] -= get_value(registers, p2)
        elif op == 'mul':
            registers[p1] *= get_value(registers, p2)
            mul_counter += 1
        elif op == 'jnz':
            if get_value(registers, p1):
                pos += get_value(registers, p2) - 1
        pos += 1
    return mul_counter


def is_prime(num):
    if num % 2 == 0:
        return False
    d = 3
    while d * d <= num:
        if num % d == 0:
            return False
        d += 2
    return True


def fn_p2(raw: str):
    """Number of non-primes between 109_900 and 126_900, step 17
    """
    h = 0
    b = 99 * 100 - (-100000)
    c = b - (-17000)
    while True:
        if not is_prime(b):
            h += 1
        if b == c:
            break
        else:
            b += 17
    return h


if __name__ == '__main__':
    example = """
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example))
    # print("Part 1:", fn_p1(input_data))  # 9409

    # print("Part 2 example:", fn_p2(example))
    print("Part 2:", fn_p2(input_data))  # 913
