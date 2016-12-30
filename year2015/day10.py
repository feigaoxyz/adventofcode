

def look_and_say(s):
    from itertools import groupby
    r = []
    for g in groupby(s):
        r.extend([len(list(g[1])), g[0]])
    return ''.join(map(str, r))


start = '1321131112'
#  start = '1'

for _ in range(40):
    start = look_and_say(start)
    #  print(start)

print('One:', len(start))

for _ in range(10):
    start = look_and_say(start)
    #  print(start)

print('Two:', len(start))
