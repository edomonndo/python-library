from number_theory.kth_root import KthRoot


def count_squarefree(n: int) -> int:
    def get_mobius(n: int) -> list[int]:
        sieve = [1] * (n + 1)
        mu = [1] * (n + 1)
        for i in range(2, n + 1):
            if sieve[i] == 0:
                continue
            mu[i] = -1
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
            for j in range(i * 2, n + 1, i):
                mu[j] = -mu[j]
            for j in range(i * i, n + 1, i * i):
                mu[j] = 0
        return mu

    res = 0
    if n <= 4000:
        mu = get_mobius(n + 1)
        i = 1
        while i * i <= n:
            res += n // (i * i) * mu[i]
            i += 1
        return res

    I = KthRoot.floor(n, 5)
    D = KthRoot.floor(n // (I + 1), 2)
    mu = get_mobius(D + 1)
    Mf = [0] * (D + 1)
    for i in range(1, D + 1):
        Mf[i] = Mf[i - 1] + mu[i]
    Md = [0] * (I + 1)
    for i in range(I, 0, -1):
        m = 1
        x = KthRoot.floor(n // i, 2)
        Dx = KthRoot.floor(x, 2)
        Rx = x // (Dx + 1)
        r = 2
        while i * r * r <= I:
            m -= Md[i * r * r]
            r += 1
        while r <= Rx:
            m -= Mf[x // r]
            r += 1
        for d in range(1, Dx + 1):
            m -= mu[d] * (x // d - Rx)
        Md[i] = m
        res += m
    for i in range(1, D + 1):
        res += mu[i] * (n // (i * i) - I)
    return res
