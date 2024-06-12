from random import randrange

from math_.factorize import factorize


def primitive_root(p: int) -> int:
    # assert is_prime(p)
    if p == 2:
        return 1
    pf = factorize(p - 1)
    res = 2
    cnt = 0
    while True:
        for pi in pf.keys():
            if pow(res, (p - 1) // pi, p) != 1:
                cnt += 1
            else:
                cnt = 0
                break
        if cnt == len(pf):
            break
        res = randrange(3, p - 1)
    return res
