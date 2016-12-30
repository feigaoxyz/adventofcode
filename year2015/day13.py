with open('13.in', 'r') as f:
    lines = f.read().splitlines()

from collections import defaultdict
dist = defaultdict(int)
ppl = set()

for l in lines:
    ws = l.strip('.').split()
    p1, p2, v = ws[0], ws[-1], int(ws[3]) * (1 - ws.count('lose') * 2)
    dist[(p1, p2)] += v
    dist[(p2, p1)] += v
    ppl.update({p1, p2})

ppl = list(ppl)

p1, *rest = ppl

from itertools import permutations

best = 0
for plan in permutations(rest):
    plan = [p1] + list(plan)
    score = sum(dist[(plan[i], plan[i-1])] for i in range(len(ppl)))
    best = max(best, score)

print('One:', best)

best2 = 0
for plan in permutations(ppl):
    score = sum(dist[(plan[i], plan[i+1])] for i in range(len(ppl) - 1))
    best2 = max(best2, score)

print('Two:', best2)


