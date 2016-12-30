wrapping = 0
ribbon = 0

while True:
    try:
        data = input()
    except EOFError:
        break
    x, y, z = map(int, data.split('x'))
    area = [x*y, x*z, y*z]
    wrapping += sum(area) * 2 + min(area)
    sides = [x + y, x + z, y + z]
    ribbon += min(sides) * 2 + x * y * z


print('Part One Answer:', wrapping)
print('Part Two Answer:', ribbon)
