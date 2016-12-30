with open('08.in', 'r') as f:
    lines = list(map(str.strip, f.read().split()))


def count_delete(l):
    return len(l) - len(eval(l))


print(count_delete('""'))
print(count_delete('"abc"'))
print(count_delete('"aaa\\\"aaa"'))
print(count_delete('"\\x27"'))

print('One:', sum([count_delete(l) for l in lines]))  # 1350


def count_add(l):
    return l.count('"') + l.count('\\') + 2


print(count_add('""'))

print('Two:', sum(count_add(l) for l in lines))  # 2085
