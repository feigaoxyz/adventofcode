import sys

if len(sys.argv) > 1:
    fn = sys.argv[1]
else:
    fn = __file__.split('.')[0] + '_input.txt'

with open(fn) as f:
    line = f.read().strip()


def decompress_len(s: str, recursive: bool = True) -> int:
    left, right = map(lambda d: str.find(*d), [(s, '('), (s, ')')])
    if left == -1:
        return len(s)
    head, marker, remain = s[:left], s[left + 1:right], s[right + 1:]
    length, repeat = map(int, marker.split('x'))
    data, remain = remain[:length], remain[length:]

    assert s == head + '({}x{})'.format(length, repeat) + data + remain

    return (len(head)
            + repeat * (decompress_len(data, recursive) if recursive  # recursively decompress data part
                        else len(data))
            + decompress_len(remain, recursive))


r1 = decompress_len(line[::], False)
r2 = decompress_len(line[::], True)

print('Part One:', r1)  # 150914
print('Part Two:', r2)  # 11052855125

assert r1 == 150914
assert r2 == 11052855125
