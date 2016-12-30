import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

with open(fn) as f:
    raw_data = f.read()

lines = raw_data.splitlines()

nums = []

t1 = 0
t2 = 0

for line in lines:
    line = line.strip()
    a, b, c = map(int, line.split())
    nums.append([a, b, c])

    a, b, c = sorted([a, b, c])
    if a + b > c:
        t1 += 1

for i in range(len(nums) // 3):
    for j in range(3):
        a, b, c = nums[i * 3][j], nums[i * 3 + 1][j], nums[i * 3 + 2][j]
        a, b, c = sorted([a, b, c])
        if a + b > c:
            t2 += 1

print('Part One:', t1)
print('Part Two:', t2)
