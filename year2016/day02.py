import sys

with open(sys.argv[1]) as f:
    raw_data = f.read()

result1 = []
result2 = []

def move(num, di):
    if di == 'U':
        if num >= 4:
            return num - 3
    elif di == 'D':
        if num <= 6:
            return num + 3
    elif di == 'L':
        if num not in {1, 4, 7}:
            return num - 1
    elif di == 'R':
        if num not in {3, 6, 9}:
            return num + 1
    return num


grid2 = [[0,0,1,0,0],
        [0,2,3,4,0],
        [5, 6,7,8,9],
        [0,'A', 'B', 'C', 0],
        [0,0,'D',0,0]
        ]

def move2(r, c, di):
    val = grid2[r][c]
    nr, nc = r, c
    if di == 'U':
        nr -= 1
    elif di == 'D':
        nr += 1
    elif di == 'L':
        nc -= 1
    elif di == 'R':
        nc += 1

    try:
        if 0<=nr<=4 and 0<=nc<=4 and grid2[nr][nc] != 0:
            return nr, nc
        else:
            return r, c
    except:
        return r, c


for line in raw_data.splitlines():
    line = line.strip()
    num = 5
    r, c = 2, 0
    for di in line:
        num = move(num, di)
        r, c = move2(r, c, di)
    result1.append(num)
    result2.append(grid2[r][c])


print('Part One:', result1)
print('Part Two:', result2)
