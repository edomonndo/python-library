from convolution.convolution import *
from convolution.formal_power_series import FPS


class ProductTree:
    def __init__(self, a: list[int]):
        self.a = a
        self.sz = sz = len(a)
        n = 1
        while n < sz:
            n <<= 1
        self.n = n
        self.buf = buf = [[] for _ in range(n << 1)]
        self.l = l = [sz] * (n << 1)
        self.r = r = [sz] * (n << 1)
        for i in range(sz):
            l[i + n] = i
            r[i + n] = i + 1
            buf[i + n] = [-a[i] + 1, -a[i] - 1]
        for i in range(n - 1, 0, -1):
            f = []
            l[i] = l[i << 1 | 0]
            r[i] = r[i << 1 | 1]
            if not buf[i << 1 | 0]:
                continue
            if not buf[1 << 1 | 1]:
                buf[i] = buf[i << 1 | 0][:]
                continue
            if len(buf[i << 1 | 0]) == len(buf[i << 1 | 1]):
                buf[i] = buf[i << 1 | 0][:]
                ntt_doubling(buf[i])
                f = buf[i << 1 | 1][:]
                ntt_doubling(f)
            else:
                buf[i] = buf[i << 1 | 0][:]
                ntt_doubling(buf[i])
                f = buf[i << 1 | 1][:]
                intt(f)
                FPS.resize(f, len(buf[i]))
                ntt(f)
            for j in range(len(buf[i])):
                buf[i][j] = buf[i][j] * f[j] % MOD
        for i in range(n << 1):
            intt(buf[i])
            FPS.shrink(buf[i])
