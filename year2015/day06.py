with open('06.in', 'r') as f:
    lines = f.readlines()

lights = [[0 for col in range(1000)] for row in range(1000)]

for line in lines:
    words = line.split()
    x1, y1 = map(int, words[-3].split(','))
    x2, y2 = map(int, words[-1].split(','))
    if words[0] == 'toggle':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = 1 - lights[x][y]
    elif words[1] == 'on':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = 1
    elif words[1] == 'off':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = 0

print('One:', sum(map(sum, lights)))

lights = [[0 for col in range(1000)] for row in range(1000)]

for line in lines:
    words = line.split()
    x1, y1 = map(int, words[-3].split(','))
    x2, y2 = map(int, words[-1].split(','))
    if words[0] == 'toggle':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = 2 + lights[x][y]
    elif words[1] == 'on':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = 1 + lights[x][y]
    elif words[1] == 'off':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lights[x][y] = max(0, lights[x][y] - 1)

print('Two:', sum(map(sum, lights)))

