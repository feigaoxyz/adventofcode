a = 1
b = c = 99
d = e = f = g = h = 0

# L_5
# b = b * 100 + 100_000
b = 199_000
# c = b + 17_000
c = 216_000

while True:
    # L_9
    f = 1
    d = 2
    while True:
        # L_11
        e = 2

        # while True:
        #     # L_12
        #     g = d * e - b
        #     if d * e == b:
        #         f = 0
        #     # L_17
        #     e += 1
        #     g = e - b
        #     if e == b:
        #         break
        if d != b and b % d == 0:
            f = 0
        e = b

        d += 1
        g = d - b
        if d == b:
            break
    e = b
    d = b
    f = 1  # if b is prime
    f = 0  # if b is not prime

    if f == 0:
        # b is not prime
        h += 1
    g = b - c
    if c == b:
        exit()
    b += 17

print(h)

# h = no. of non-primes in between 199_000 to 216_000 step 17
