import math
import random

from math_.miller_rabin import miller_rabin


def find_prime_factor(n):
    b = n.bit_length() - 1
    b = (b >> 2) << 2
    m = 2 * int(2 ** (b / 8))

    while True:
        c = random.randrange(1, n)
        f = lambda a: (pow(a, 2, n) + c) % n
        y = 0
        g = q = r = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = math.gcd(abs(x - y), n)
        if g == n:
            continue
        if miller_rabin(g):
            return g
        elif miller_rabin(n // g):
            return n // g
        else:
            n = g


def factorize(n):
    res = {}
    for p in range(2, 1000):
        if p * p > n:
            break
        if n % p:
            continue
        s = 0
        while n % p == 0:
            n //= p
            s += 1
        res[p] = s

    while not miller_rabin(n) and n > 1:
        p = find_prime_factor(n)
        s = 0
        while n % p == 0:
            n //= p
            s += 1
        res[p] = s
    if n > 1:
        res[n] = 1
    return res
