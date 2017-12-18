from common import load_input

PART1_DOC = """Part 1:

"""

PART2_DOC = """Part 2:

"""


def fn_p1(raw: str):
    def get_value(s):
        try:
            return int(s)
        except ValueError:
            if s not in registers:
                registers[s] = 0
            return registers[s]

    lines = [line.strip().split() for line in raw.splitlines()]
    pos = 0
    last_sound = None
    registers = dict()
    while 0 <= pos < len(lines):
        fn, *param = lines[pos]
        if fn == 'set':
            registers[param[0]] = get_value(param[1])
            pos += 1
        elif fn == 'add':
            registers[param[0]] = get_value(param[0]) + get_value(param[1])
            pos += 1
        elif fn == 'mul':
            registers[param[0]] = get_value(param[0]) * get_value(param[1])
            pos += 1
        elif fn == 'mod':
            registers[param[0]] = get_value(param[0]) % get_value(param[1])
            pos += 1
        elif fn == 'snd':
            last_sound = get_value(param[0])
            pos += 1
        elif fn == 'rcv':
            if get_value(param[0]):
                break
            pos += 1
        elif fn == 'jgz':
            if get_value(param[0]) > 0:
                pos += get_value(param[1])
            else:
                pos += 1
    return last_sound


def fn_p2(raw: str):
    def get_value(s, prog):
        try:
            return int(s)
        except ValueError:
            if s not in prog:
                prog[s] = 0
            return prog[s]

    lines = [line.strip().split() for line in raw.splitlines()]
    progs = {
        0: {
            'p': 0,
            'rcv': [],
            'snd': 0,
            'wait': False,
            'pos': 0
        },
        1: {
            'p': 1,
            'rcv': [],
            'snd': 0,
            'wait': False,
            'pos': 0
        }
    }

    def in_range(p):
        return 0 <= p < len(lines)

    def execute(prog, other):
        while prog['wait'] is False and in_range(prog['pos']):
            fn, *param = lines[prog['pos']]
            if fn == 'set':
                prog[param[0]] = get_value(param[1], prog)
                prog['pos'] += 1
            elif fn == 'add':
                prog[param[0]] = get_value(param[0], prog) + get_value(
                    param[1], prog)
                prog['pos'] += 1
            elif fn == 'mul':
                prog[param[0]] = get_value(param[0], prog) * get_value(
                    param[1], prog)
                prog['pos'] += 1
            elif fn == 'mod':
                prog[param[0]] = get_value(param[0], prog) % get_value(
                    param[1], prog)
                prog['pos'] += 1
            elif fn == 'jgz':
                if get_value(param[0], prog) > 0:
                    prog['pos'] += get_value(param[1], prog)
                else:
                    prog['pos'] += 1
            elif fn == 'snd':
                other['rcv'].append(get_value(param[0], prog))
                other['wait'] = False
                prog['snd'] += 1
                prog['pos'] += 1
            elif fn == 'rcv':
                if len(prog['rcv']) > 0:
                    prog[param[0]] = prog['rcv'].pop(0)
                    prog['pos'] += 1
                else:
                    prog['wait'] = True

    while True:
        execute(progs[0], progs[1])
        execute(progs[1], progs[0])
        if ((progs[0]['wait'] and progs[1]['wait'])
                or (not in_range(progs[0]['pos']) and not in_range(progs[1]['pos']))):
            break

    return progs[1]['snd']


if __name__ == '__main__':
    example = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2
    """.strip()
    input_data = load_input(__file__.split('.')[0] + '_in.txt').strip()

    # print("Part 1 example:", fn_p1(example))  # 4
    # print("Part 1:", fn_p1(input_data))  # 4601

    example2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

    print("Part 2 example:", fn_p2(example2))  # 3
    print("Part 2:", fn_p2(input_data))  # 6858
