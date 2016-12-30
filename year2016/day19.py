n_elves = 3005290


def drop(row, start, step):
    return row[start::step], len(row) % step


def solution(elves):
    # f(n,k) = (f(n-1,k) + k) % n
    fn, n = 0, 1
    while n < elves:
        # print(fn, n)
        fn1, n = fn, n + 1
        fn = (fn1 + 2) % n
    return fn + 1


assert solution(5) == 3
assert solution(6) == 5

r1 = solution(n_elves)
print('Part One:', r1)  # 1816277


def solution2(elves):
    from collections import deque
    len1 = (elves + 1) // 2
    len2 = elves - len1

    left = deque(list(range(len1)))
    right = deque(list(range(len1, elves)))

    while len1 > 1 and len2 > 0:
        # assert len2 <= len1 <= len2 +1
        if len1 > len2:
            left.pop()
            len1 -= 1
        else:
            right.popleft()
            len2 -= 1
        right.append(left.popleft())
        left.append(right.popleft())
    return left[0] + 1


assert solution2(5) == 2

r2 = solution2(n_elves)
print('Part Two:', r2)  # 1410967
