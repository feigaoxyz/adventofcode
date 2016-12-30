import sys

init = '11101000110010100'

def tran(a):
    b = ''
    for x in a[::-1]:
        b += '1' if x == '0' else '0'
    return a + '0' + b
    
#print(tran('0'))

def check(s):
    while len(s) % 2 == 0:
        s = ''.join('1' if a == b else '0' for a, b in zip(s[::2], s[1::2]))
    return s
    
    
#print(check('110010110100'))


def part1(seed, length):
    while len(seed) < length:
        seed = tran(seed)
    return check(seed[:length])
    
    
#r1 = part1(init, 272)
#print('Part One:', r1)

r2 = part1(init, 35651584)
print('Part Two:', r2)
