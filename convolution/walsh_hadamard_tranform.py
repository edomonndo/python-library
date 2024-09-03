MOD = 998244353


def walsh_hadamard_tranform(buf: list[int], inv: bool = False):
    i, n = 1, len(buf)
    while i < n:
        for j in range(0, n, i << 1):
            for k in range(i):
                s, t = buf[j + k], buf[j + k + i]
                buf[j + k], buf[j + k + i] = (s + t) % MOD, (s - t) % MOD
        i <<= 1
    if inv:
        inv_n = pow(n, -1, MOD)
        for i in range(n):
            buf[i] = (buf[i] * inv_n) % MOD


def bitwise_xor_conv(f: list[int], g: list[int]):
    n = len(f)
    assert n == len(g)
    walsh_hadamard_tranform(f, False)
    walsh_hadamard_tranform(g, False)
    for i in range(n):
        f[i] = (f[i] * g[i]) % MOD
    walsh_hadamard_tranform(f, True)
