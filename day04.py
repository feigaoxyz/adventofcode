import hashlib

data = 'bgvyzdsv'

pre = 1
while True:
    s = data + str(pre)
    m = hashlib.md5(s.encode()).hexdigest()
    if m.startswith('00000'):
        break
    pre += 1
print("part one:", pre)

while True:
    s = data + str(pre)
    m = hashlib.md5(s.encode()).hexdigest()
    if m.startswith('000000'):
        break
    pre += 1
print("part two:", pre)

