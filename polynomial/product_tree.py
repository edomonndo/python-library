from convolution.convolution import *
from polynomial.formal_power_series import FPS


class ProductTree:
    def __init__(self, xs: list[int]):
        self.xs = xs
        self.sz = sz = len(xs)
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
            buf[i + n] = [-xs[i] + 1, -xs[i] - 1]
        for i in range(n - 1, 0, -1):
            f = []
            l[i] = l[i << 1 | 0]
            r[i] = r[i << 1 | 1]
            if not buf[i << 1 | 0]:
                continue
            if not buf[i << 1 | 1]:
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

    @staticmethod
    def _modinv(a: int, m: int) -> int:
        b, u, v = m, 1, 0
        while b:
            t = a // b
            a, b = b, a - t * b
            u, v = v, u - t * v
        u %= m
        return u

    def _inner_multipoint_evaluation(self, f: list[int]) -> list[int]:
        res = []
        st = [(f, 1)]
        while st:
            a, idx = st.pop()
            if self.l[idx] == self.r[idx]:
                continue
            a = FPS.mod(a, self.buf[idx])
            if len(a) <= 64:
                for i in range(self.l[idx], self.r[idx]):
                    res.append(FPS.eval(a, self.xs[i]))
                continue
            st += [(a, idx << 1 | 1), (a, idx << 1 | 0)]
        return res

    def multipoint_evaluation(self, f: list[int]) -> list[int]:
        if not f:
            return [0] * self.sz
        return self._inner_multipoint_evaluation(f)

    def polynomial_interpolation(self, ys: list[int]) -> list[int]:
        # assert len(xs) == len(ys)
        w = FPS.fps_diff(self.buf[1])
        vs = self._inner_multipoint_evaluation(w)
        res = [[] for _ in range(self.n << 1)]
        for i in range(self.n):
            if i < len(self.xs):
                res[self.n + i] = [ys[i] * self._modinv(vs[i], MOD) % MOD]
            else:
                res[self.n + i] = [1]
        for i in range(self.n - 1, 0, -1):
            if not self.buf[i << 1 | 0]:
                res[i] = []
            elif not self.buf[i << 1 | 1]:
                res[i] = res[i << 1 | 0]
            else:
                res[i] = FPS.add(
                    multiply(res[i << 1 | 0], self.buf[i << 1 | 1]),
                    multiply(res[i << 1 | 1], self.buf[i << 1 | 0]),
                )
        return res[1]
