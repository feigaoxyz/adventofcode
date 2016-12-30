with open('05.in', 'r') as f:
    lines = f.readlines()


def is_nice_p1(s):
    counting = lambda s, l: [s.count(x) for x in l]
    if sum(counting(s, 'aeiou')) < 3:
        return False
    if sum(counting(s, [x+x for x in set(s)])) < 1:
        return False
    if sum(counting(s, ['ab', 'cd', 'pq', 'xy'])) > 0:
        return False
    return True

print('One:', sum(map(is_nice_p1, lines)))

def is_nice_p2(s):
    if max([s.count(p) for p in [s[i:i+2] for i in range(len(s) - 2)]]) < 2:
        return False
    if not any(s[i] == s[i+2] for i in range(len(s) - 3)):
        return False
    return True

print('Two:', sum(map(is_nice_p2, lines)))



