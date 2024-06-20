from convolution.convolution import *
from math_.combination_mod import Comb


def tayler_shift(a: list[int], c: int) -> list[int]:
    n = len(a)
    C = Comb(n + 1)
    res = [x * C.fact[i] % MOD for i, x in enumerate(a)]
    res.reverse()
    b = [0] * n
    b[0] = 1
    for i in range(1, n):
        b[i] = (b[i - 1] * c % MOD) * C.inv[i] % MOD
    res = multiply(res, b)[:n]
    res.reverse()
    return [x * C.inv_fact[i] % MOD for i, x in enumerate(res)]
