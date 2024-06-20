from convolution.convolution import *


class FPS:
    @staticmethod
    def shrink(a: list[int]) -> None:
        while a and not a[-1]:
            a.pop()

    @staticmethod
    def resize(a: list[int], size: int, val: int = 0) -> None:
        a[size:] = []
        a[len(a) :] = [val] * (size - len(a))

    @staticmethod
    def add(a: list[int], b: list[int]) -> list[int]:
        if len(a) < len(b):
            res = b[::]
            for i, x in enumerate(a):
                res[i] += x
        else:
            res = a[::]
            for i, x in enumerate(b):
                res[i] += x
        return [x % MOD for x in res]

    @staticmethod
    def add_scalar(a: list[int], k: int) -> list[int]:
        res = a[:]
        res[0] = (res[0] + k) % MOD
        return res

    @classmethod
    def sub(cls, a: list[int], b: list[int]) -> list[int]:
        if len(a) < len(b):
            res = b[::]
            for i, x in enumerate(a):
                res[i] -= x
            res = cls.neg(res)
        else:
            res = a[::]
            for i, x in enumerate(b):
                res[i] -= x
        return [x % MOD for x in res]

    @classmethod
    def sub_scalar(cls, a: list[int], k: int) -> list[int]:
        return cls.add_scalar(a, -k)

    @staticmethod
    def neg(a: list[int]) -> list[int]:
        return [MOD - x if x else 0 for x in a]

    @staticmethod
    def mul_scalar(a: list[int], k: int) -> list[int]:
        return [x * k % MOD for x in a]

    @staticmethod
    def matmul(a: list[int], b: list[int]) -> list[int]:
        return [x * b[i] % MOD for i, x in enumerate(a)]

    @classmethod
    def div(cls, a: list[int], b: list[int]) -> list[int]:
        if len(a) < len(b):
            return []
        n = len(a) - len(b) + 1
        cnt = 0
        if len(b) > 64:
            return multiply(a[::-1][:n], cls.inv(b[::-1], n))[:n][::-1]
        f, g = a[::], b[::]
        while g and not g[-1]:
            g.pop()
            cnt += 1
        coef = pow(g[-1], MOD - 2, MOD)
        g = cls.mul_scalar(g, coef)
        deg = len(f) - len(g) + 1
        gs = len(g)
        quo = [0] * deg
        for i in range(deg)[::-1]:
            quo[i] = x = f[i + gs - 1] % MOD
            for j, y in enumerate(g):
                f[i + j] -= x * y
        return cls.mul_scalar(quo, coef) + [0] * cnt

    @classmethod
    def mod(cls, a: list[int], b: list[int]) -> list[int]:
        res = cls.sub(a, multiply(cls.div(a, b), b))
        while res and not res[-1]:
            res.pop()
        return res

    @classmethod
    def divmod(cls, a: list[int], b: list[int]) -> tuple[list[int], list[int]]:
        q = cls.div(a, b)
        r = cls.sub(a, multiply(q, b))
        while r and not r[-1]:
            r.pop()
        return q, r

    @staticmethod
    def mod_sqrt(a: int, p: int) -> int:
        "x s.t. x**2 == a (mod p) if exist else -1"
        if a < 2:
            return a
        if pow(a, (p - 1) >> 1, p) != 1:
            return -1
        b = 1
        while pow(b, (p - 1) >> 1, p) == 1:
            b += 1
        m = p - 1
        e = 0
        while not m & 1:
            m >>= 1
            e += 1
        x = pow(a, (m - 1) >> 1, p)
        y = (a * x % p) * x % p
        x = a * x % p
        z = pow(b, m, p)
        while y != 1:
            j = 0
            t = y
            while t != 1:
                j += 1
                t = t * t % p
            z = pow(z, 1 << (e - j - 1), p)
            x = x * z % p
            z = z * z % p
            y = y * z % p
            e = j
        return x

    @classmethod
    def sqrt(cls, a: list[int], deg=-1) -> list[int]:
        if deg == -1:
            deg = len(a)
        if len(a) == 0:
            return [0] * deg
        if a[0] == 0:
            for i in range(1, len(a)):
                if a[i] != 0:
                    if i & 1:
                        return []
                    if deg - (i >> 1) <= 0:
                        break
                    ret = cls.sqrt(a[i:], deg - (i >> 1))
                    if not ret:
                        return []
                    ret[:0] = [0] * (i >> 1)
                    if len(ret) < deg:
                        ret[len(ret) :] = [0] * (deg - len(ret))
                    return ret
            return [0] * deg
        sqr = cls.mod_sqrt(a[0], MOD)
        if sqr == -1:
            return []
        ret = [sqr]
        inv2 = 499122177
        i = 1
        while i < deg:
            i <<= 1
            ret = cls.mul_scalar(cls.add(ret, multiply(a[:i], cls.inv(ret, i))), inv2)
        return ret[:deg]

    @staticmethod
    def eval(a: list[int], x: int) -> int:
        r = 0
        w = 1
        for v in a:
            r += w * v % MOD
            w = w * x % MOD
        return r % MOD

    @staticmethod
    def inv(a: list[int], deg: int = -1) -> list[int]:
        # assert(self[0] != 0)
        if deg == -1:
            deg = len(a)
        res = [0] * deg
        res[0] = pow(a[0], MOD - 2, MOD)
        d = 1
        while d < deg:
            f = [0] * (d << 1)
            tmp = min(len(a), d << 1)
            f[:tmp] = a[:tmp]
            g = [0] * (d << 1)
            g[:d] = res[:d]
            ntt(f)
            ntt(g)
            for i, x in enumerate(g):
                f[i] = f[i] * x % MOD
            intt(f)
            f[:d] = [0] * d
            ntt(f)
            for i, x in enumerate(g):
                f[i] = f[i] * x % MOD
            intt(f)
            for j in range(d, min(d << 1, deg)):
                if f[j]:
                    res[j] = MOD - f[j]
                else:
                    res[j] = 0
            d <<= 1
        return res

    @classmethod
    def pow(cls, a: list[int], k: int, deg=-1) -> list[int]:
        n = len(a)
        if deg == -1:
            deg = n
        if k == 0:
            if not deg:
                return []
            res = [0] * deg
            res[0] = 1
            return res
        for i, x in enumerate(a):
            if x:
                rev = pow(x, MOD - 2, MOD)
                res = cls.mul_scalar(
                    cls.exp(
                        cls.mul_scalar(cls.log(cls.mul_scalar(a, rev)[i:], deg), k), deg
                    ),
                    pow(x, k, MOD),
                )
                res[:0] = [0] * (i * k)
                if len(res) < deg:
                    res[len(res) :] = [0] * (deg - len(res))
                    return res
                return res[:deg]
            if (i + 1) * k >= deg:
                break
        return [0] * deg

    @staticmethod
    def exp(a: list[int], deg=-1) -> list[int]:
        # assert(not self or self[0] == 0)
        if deg == -1:
            deg = len(a)
        inv = [0, 1]

        def inplace_integral(F: list[int]) -> list[int]:
            n = len(F)
            while len(inv) <= n:
                j, k = divmod(MOD, len(inv))
                inv.append((-inv[k] * j) % MOD)
            return [0] + [x * inv[i + 1] % MOD for i, x in enumerate(F)]

        def inplace_diff(F: list[int]) -> list[int]:
            return [x * i % MOD for i, x in enumerate(F) if i]

        b = [1, (a[1] if 1 < len(a) else 0)]
        c = [1]
        z1 = []
        z2 = [1, 1]
        m = 2
        while m < deg:
            y = b + [0] * m
            ntt(y)
            z1 = z2
            z = [y[i] * p % MOD for i, p in enumerate(z1)]
            intt(z)
            z[: m >> 1] = [0] * (m >> 1)
            ntt(z)
            for i, p in enumerate(z1):
                z[i] = z[i] * (-p) % MOD
            intt(z)
            c[m >> 1 :] = z[m >> 1 :]
            z2 = c + [0] * m
            ntt(z2)
            tmp = min(len(a), m)
            x = a[:tmp] + [0] * (m - tmp)
            x = inplace_diff(x)
            x.append(0)
            ntt(x)
            for i, p in enumerate(x):
                x[i] = y[i] * p % MOD
            intt(x)
            for i, p in enumerate(b):
                if not i:
                    continue
                x[i - 1] -= p * i % MOD
            x += [0] * m
            for i in range(m - 1):
                x[m + i], x[i] = x[i], 0
            ntt(x)
            for i, p in enumerate(z2):
                x[i] = x[i] * p % MOD
            intt(x)
            x.pop()
            x = inplace_integral(x)
            x[:m] = [0] * m
            for i in range(m, min(len(a), m << 1)):
                x[i] += a[i]
            ntt(x)
            for i, p in enumerate(y):
                x[i] = x[i] * p % MOD
            intt(x)
            b[m:] = x[m:]
            m <<= 1
        return b[:deg]

    @classmethod
    def log(cls, a: list[int], deg=-1) -> list[int]:
        # assert(a[0] == 1)
        if deg == -1:
            deg = len(a)
        return cls.integral(multiply(cls.fps_diff(a), cls.inv(a, deg))[: deg - 1])

    @staticmethod
    def integral(a: list[int]) -> list[int]:
        n = len(a)
        res = [0] * (n + 1)
        if n:
            res[1] = 1
        for i in range(2, n + 1):
            j, k = divmod(MOD, i)
            res[i] = (-res[k] * j) % MOD
        for i, x in enumerate(a):
            res[i + 1] = res[i + 1] * x % MOD
        return res

    @staticmethod
    def fps_diff(a: list[int]) -> list[int]:
        return [i * x % MOD for i, x in enumerate(a) if i]
