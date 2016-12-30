steps = input()

# Part One
print('Final Step:', len(steps) - steps.count(')') * 2)

# Part Two
cur = 0
for p, d in enumerate(steps):
    if d == '(':
        cur += 1
    else:
        cur -= 1
    if cur == -1:
        print('Position:', p + 1)
        break
else:
    print('Never enter basement')