MOD = 998244353


def sup_zeta_transform(buf: list[int]) -> None:
    i, n = 1, len(buf)
    while i < n:
        for j in range(n):
            if i & j == 0:
                buf[j] = (buf[j] + buf[i | j]) % MOD
        i <<= 1


def sup_moebius_transform(buf: list[int]) -> None:
    i, n = 1, len(buf)
    while i < n:
        for j in range(n):
            if i & j == 0:
                buf[j] = (buf[j] - buf[i | j]) % MOD
        i <<= 1


def sub_zeta_transform(buf: list[int]) -> None:
    i, n = 1, len(buf)
    while i < n:
        for j in range(0, n, i << 1):
            for k in range(i):
                buf[j + k + i] = (buf[j + k + i] + buf[j + k]) % MOD
        i <<= 1


def sub_moebius_transform(buf: list[int]) -> None:
    i, n = 1, len(buf)
    while i < n:
        for j in range(0, n, i << 1):
            for k in range(i):
                buf[j + k + i] = (buf[j + k + i] - buf[j + k]) % MOD
        i <<= 1


def bitwize_and_conv(f: list[int], g: list[int]) -> None:
    n = len(f)
    assert n == len(g)
    sup_zeta_transform(f)
    sup_zeta_transform(g)
    for i in range(n):
        f[i] = f[i] * g[i] % MOD
    sup_moebius_transform(f)


def bitwize_and_conv(f: list[int], g: list[int]) -> None:
    n = len(f)
    assert n == len(g)
    sub_zeta_transform(f)
    sub_zeta_transform(g)
    for i in range(n):
        f[i] = f[i] * g[i] % MOD
    sub_moebius_transform(f)
