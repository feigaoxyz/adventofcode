
puzzle = 'vzbxkghb'
LEN = 8

from string import ascii_lowercase

l2d = dict(zip(ascii_lowercase, range(26)))
d2l = dict(zip(range(26), ascii_lowercase))

def s2a(s):
    return [l2d[x] for x in s]

def a2s(a):
    return ''.join([d2l[v] for v in a])

def a2v(a):
    return sum([v * (26 ** (LEN - i - 1)) for i,v in enumerate(a)])

def v2a(v):
    return [(v // (26 ** (LEN - i - 1))) % 26 for i in range(LEN)]

assert puzzle == a2s(v2a(a2v(s2a(puzzle))))

def inc(puzzle):
    val = a2v(s2a(puzzle))
    while True:
        val += 1
        s = a2s(v2a(val))
        if sum(s.count(p3) for p3 in [x+x for x in ascii_lowercase]) < 2:
            continue
        if any(s.count(p2) > 0 for p2 in 'iol'):
            continue
        if all(s.count(p1) == 0 for p1 in [ascii_lowercase[i:i+3] for i in range(26-2)]):
            continue
        break
    return s

#  assert inc('abcdefgh') == 'abcdffaa'
#  assert inc('ghijklmn') == 'ghjaabcc'

answer1 = inc('vzbxkghb')
print('One:', answer1)
answer2 = inc(answer1)
print('Two:', answer2)
