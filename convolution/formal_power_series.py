from convolution import *


class FPS:
    @staticmethod
    def shrink(a: list) -> None:
        while a and not a[-1]:
            a.pop()

    @staticmethod
    def add(a: list, b: list) -> list:
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
    def add_scalar(a: list, k: int) -> list:
        res = a[:]
        res[0] = (res[0] + k) % MOD
        return res

    @classmethod
    def sub(cls, a: list, b: list) -> list:
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
    def sub_scalar(cls, a: list, k: int) -> list:
        return cls.add_scalar(a, -k)

    @staticmethod
    def neg(a: list) -> list:
        return [MOD - x if x else 0 for x in a]

    @staticmethod
    def mul_scalar(a: list, k: int) -> list:
        return [x * k % MOD for x in a]

    @staticmethod
    def matmul(a: list, b: list) -> list:
        "not verified"
        return [x * b[i] % MOD for i, x in enumerate(a)]

    @classmethod
    def div(cls, a: list, b: list) -> list:
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
    def mod(cls, a: list, b: list) -> list:
        res = cls.sub(a, multiply(cls.div(a, b), b))
        while res and not res[-1]:
            res.pop()
        return res

    @classmethod
    def divmod(cls, a: list, b: list):
        q = cls.div(a, b)
        r = cls.sub(a, multiply(q, b))
        while r and not r[-1]:
            r.pop()
        return q, r

    @staticmethod
    def mod_sqrt(a: int, p: int):
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
    def sqrt(cls, a: list, deg=-1) -> list:
        if deg == -1:
            deg = len(a)
        if len(a) == 0:
            return [0] * deg
        if a[0] == 0:
            for i in range(1, len(a)):
                if a[i] != 0:
                    if i & 1:
                        return []
                    if deg - i // 2 <= 0:
                        break
                    ret = cls.sqrt(a[i:], deg - i // 2)
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
    def eval(a: list, x: int) -> int:
        r = 0
        w = 1
        for v in a:
            r += w * v % MOD
            w = w * x % MOD
        return r % MOD

    @staticmethod
    def inv(a: list, deg: int = -1) -> list:
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
    def pow(cls, a: list, k: int, deg=-1) -> list:
        n = len(a)
        if deg == -1:
            deg = n
        if k == 0:
            if not deg:
                return []
            ret = [0] * deg
            ret[0] = 1
            return ret
        for i, x in enumerate(a):
            if x:
                rev = pow(x, MOD - 2, MOD)
                ret = cls.mul_scalar(
                    cls.exp(
                        cls.mul_scalar(cls.log(cls.mul_scalar(a, rev)[i:], deg), k), deg
                    ),
                    pow(x, k, MOD),
                )
                ret[:0] = [0] * (i * k)
                if len(ret) < deg:
                    ret[len(ret) :] = [0] * (deg - len(ret))
                    return ret
                return ret[:deg]
            if (i + 1) * k >= deg:
                break
        return [0] * deg

    @staticmethod
    def exp(a: list, deg=-1) -> list:
        # assert(not self or self[0] == 0)
        if deg == -1:
            deg = len(a)
        inv = [0, 1]

        def inplace_integral(F: list) -> list:
            n = len(F)
            while len(inv) <= n:
                j, k = divmod(MOD, len(inv))
                inv.append((-inv[k] * j) % MOD)
            return [0] + [x * inv[i + 1] % MOD for i, x in enumerate(F)]

        def inplace_diff(F: list) -> list:
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
    def log(cls, a: list, deg=-1) -> list:
        # assert(a[0] == 1)
        if deg == -1:
            deg = len(a)
        return cls.integral(multiply(cls.fps_diff(a), cls.inv(a, deg))[: deg - 1])

    @staticmethod
    def integral(a: list) -> list:
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
    def fps_diff(a: list) -> list:
        return [i * x % MOD for i, x in enumerate(a) if i]

    @staticmethod
    def composition(a: list, b: list) -> list:
        deg = min(len(a), len(b))
        k = int(deg**0.5 + 1)
        d = (deg + k) // k

        X = [[] for _ in range(k + 1)]
        X[0] = [1]
        for i, x in enumerate(X):
            if i == k:
                break
            X[i + 1] = multiply(x, b)[: deg + 1]

        Y = [[0] * len(X[-1]) for _ in range(k)]
        X[d + 1 :] = []
        xd = X.pop()
        for i, y in enumerate(Y):
            for j, x in enumerate(X):
                if i * d + j >= deg:
                    break
                for t in range(min(deg + 1, len(x))):
                    if t < len(y):
                        y[t] += x[t] * a[i * d + j] % MOD

        F = [0] * (deg + 1)
        Z = [1]
        for i, y in enumerate(Y):
            tmp = multiply(y, Z)[: deg + 1]
            for j, yy in enumerate(tmp):
                F[j] += yy
            Z = multiply(Z, xd)[: deg + 1]
        res = [x % MOD for x in F]
        res.pop()
        return res

    @staticmethod
    def chirp_z(f: list, W: int, N: int = -1, A: int = 1) -> list:
        if N == -1:
            N = len(f)
        if not f or N == 0:
            return []
        M = len(f)
        if A != -1:
            x = 1
            for i in range(M):
                f[i] = f[i] * x % MOD
                x = x * A % MOD
        if W == 0:
            F = [f[0]] * N
            F[0] = sum(f) % MOD
            return F
        wc = [0] * (N + M)
        iwc = [0] * max(N, M)
        ws = 1
        iW = pow(W, MOD - 2, MOD)
        iws = 1
        wc[0] = iwc[0] = 1
        tmp = 1
        for i in range(1, N + M):
            wc[i] = tmp = ws * tmp % MOD
            ws = ws * W % MOD
        tmp = 1
        for i in range(1, max(N, M)):
            iwc[i] = tmp = iws * tmp % MOD
            iws = iws * iW % MOD
        for i, x in enumerate(f):
            f[i] = x * iwc[i] % MOD
        f.reverse()
        g = multiply(f, wc)
        F = [0] * N
        for i, x in enumerate(iwc):
            if i == N:
                break
            F[i] = g[M - 1 + i] * x % MOD
        return F

    @staticmethod
    def multivariate_multiplication(f: list, g: list, base: list) -> list:
        n = len(f)
        s = len(base)
        W = 1
        if s == 0:
            return [f[0] * g[0] % MOD]
        while W < n << 1:
            W <<= 1
        chi = [0] * n
        for i in range(n):
            x = i
            for j in range(s - 1):
                x //= base[j]
                chi[i] += x
            chi[i] %= s
        F = [[0] * W for _ in range(s)]
        G = [[0] * W for _ in range(s)]
        for i, j in enumerate(chi):
            F[j][i] = f[i]
            G[j][i] = g[i]
        for i in range(s):
            ntt(F[i])
            ntt(G[i])
        for k in range(W):
            a = [0] * s
            for i, f in enumerate(F):
                tmp = f[k]
                for j, g in enumerate(G):
                    a[i + j - (s if i + j >= s else 0)] += tmp * g[k] % MOD
            for i, f in enumerate(F):
                f[k] = a[i] % MOD
        for f in F:
            intt(f)
        return [F[j][i] for i, j in enumerate(chi)]

    @classmethod
    def multipoint_evaluation(cls, f: list, xs: list) -> list:
        s = len(xs)
        N = 1 << (s - 1).bit_length() if s != 1 else 2
        if not f or not xs:
            return [0] * s
        buf = [[] for _ in range(N << 1)]
        for i in range(N):
            n = -xs[i] if i < s else 0
            buf[i + N] = [n + 1, n - 1]
        for i in range(N - 1, 0, -1):
            g = buf[i << 1 | 0]
            h = buf[i << 1 | 1]
            n = len(g)
            m = n << 1
            buf[i][n:] = []
            buf[i][len(buf[i]) :] = [0] * (n - len(buf[i]))
            for j in range(n):
                buf[i][j] = g[j] * h[j] % MOD - 1
            if i != 1:
                ntt_doubling(buf[i])
                buf[i][len(buf[i]) :] = [0] * (m - len(buf[i]))
                for j in range(m):
                    buf[i][j] += 1 if j < n else -1
        fs = len(f)
        root = buf[1]
        intt(root)
        root.append(1)
        root.reverse()
        tmp = cls.inv(root, fs)
        tmp.reverse()
        root = multiply(tmp, f)
        root[: fs - 1] = []
        root[N:] = []
        root[len(root) :] = [0] * (N - len(root))

        ans = [0] * s

        def calc(i: int, l: int, r: int, g: list) -> None:
            if i >= N:
                ans[i - N] = g[0]
                return
            length = len(g)
            m = l + r >> 1
            ntt(g)
            tmp = buf[i << 1 | 1]
            for j in range(length):
                tmp[j] = tmp[j] * g[j] % MOD
            intt(tmp)
            calc(i << 1, l, m, tmp[length >> 1 :])
            if m >= s:
                return
            tmp = buf[i << 1 | 0]
            for j in range(length):
                tmp[j] = tmp[j] * g[j] % MOD
            intt(tmp)
            calc(i << 1 | 1, m, r, tmp[length >> 1 :])

        calc(1, 0, N, root)
        return ans
