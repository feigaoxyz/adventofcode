#!/usr/bin/env python3
# -*- coding: utf-8 -*-


puzzle = []
with open('23.in', 'r') as f:
    for line in f.readlines():
        puzzle.append(line.replace(',', '').split())

registers = {'a': 0, 'b': 0,}
instructions = {'hlf', 'tpl', 'inc', 'jmp', 'jie', 'jio'}


def run(prog, reg):
    ptr = 0
    while 0 <= ptr < len(prog):
        ins, *ops = prog[ptr]
        # print('Step', ptr, prog[ptr], end=' ')
        if ins not in instructions:
            break
        elif ins == 'hlf':
            reg[ops[0]] //= 2
            ptr += 1
        elif ins == 'tpl':
            reg[ops[0]] *= 3
            ptr += 1
        elif ins == 'inc':
            reg[ops[0]] += 1
            ptr += 1
        elif ins == 'jmp':
            ptr += int(ops[0])
        elif ins == 'jie':
            ptr += int(ops[1]) if reg[ops[0]] % 2 == 0 else 1
        elif ins == 'jio':
            ptr += int(ops[1]) if reg[ops[0]] == 1 else 1
        # print(reg, ptr)
    return reg


print('One:', run(puzzle, registers.copy()))
print('Two:', run(puzzle, {'a': 1, 'b': 0}))
