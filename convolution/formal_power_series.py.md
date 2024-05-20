---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution import *\n\n\nclass FPS:\n    @staticmethod\n    def shrink(a:\
    \ list) -> None:\n        while a and not a[-1]:\n            a.pop()\n\n    @staticmethod\n\
    \    def add(a: list, b: list) -> list:\n        if len(a) < len(b):\n       \
    \     res = b[::]\n            for i, x in enumerate(a):\n                res[i]\
    \ += x\n        else:\n            res = a[::]\n            for i, x in enumerate(b):\n\
    \                res[i] += x\n        return [x % MOD for x in res]\n\n    @staticmethod\n\
    \    def add_scalar(a: list, k: int) -> list:\n        res = a[:]\n        res[0]\
    \ = (res[0] + k) % MOD\n        return res\n\n    @classmethod\n    def sub(cls,\
    \ a: list, b: list) -> list:\n        if len(a) < len(b):\n            res = b[::]\n\
    \            for i, x in enumerate(a):\n                res[i] -= x\n        \
    \    res = cls.neg(res)\n        else:\n            res = a[::]\n            for\
    \ i, x in enumerate(b):\n                res[i] -= x\n        return [x % MOD\
    \ for x in res]\n\n    @classmethod\n    def sub_scalar(cls, a: list, k: int)\
    \ -> list:\n        return cls.add_scalar(a, -k)\n\n    @staticmethod\n    def\
    \ neg(a: list) -> list:\n        return [MOD - x if x else 0 for x in a]\n\n \
    \   @staticmethod\n    def mul_scalar(a: list, k: int) -> list:\n        return\
    \ [x * k % MOD for x in a]\n\n    @staticmethod\n    def matmul(a: list, b: list)\
    \ -> list:\n        \"not verified\"\n        return [x * b[i] % MOD for i, x\
    \ in enumerate(a)]\n\n    @classmethod\n    def div(cls, a: list, b: list) ->\
    \ list:\n        if len(a) < len(b):\n            return []\n        n = len(a)\
    \ - len(b) + 1\n        cnt = 0\n        if len(b) > 64:\n            return multiply(a[::-1][:n],\
    \ cls.inv(b[::-1], n))[:n][::-1]\n        f, g = a[::], b[::]\n        while g\
    \ and not g[-1]:\n            g.pop()\n            cnt += 1\n        coef = pow(g[-1],\
    \ MOD - 2, MOD)\n        g = cls.mul_scalar(g, coef)\n        deg = len(f) - len(g)\
    \ + 1\n        gs = len(g)\n        quo = [0] * deg\n        for i in range(deg)[::-1]:\n\
    \            quo[i] = x = f[i + gs - 1] % MOD\n            for j, y in enumerate(g):\n\
    \                f[i + j] -= x * y\n        return cls.mul_scalar(quo, coef) +\
    \ [0] * cnt\n\n    @classmethod\n    def mod(cls, a: list, b: list) -> list:\n\
    \        res = cls.sub(a, multiply(cls.div(a, b), b))\n        while res and not\
    \ res[-1]:\n            res.pop()\n        return res\n\n    @classmethod\n  \
    \  def divmod(cls, a: list, b: list):\n        q = cls.div(a, b)\n        r =\
    \ cls.sub(a, multiply(q, b))\n        while r and not r[-1]:\n            r.pop()\n\
    \        return q, r\n\n    @staticmethod\n    def mod_sqrt(a: int, p: int):\n\
    \        \"x s.t. x**2 == a (mod p) if exist else -1\"\n        if a < 2:\n  \
    \          return a\n        if pow(a, (p - 1) >> 1, p) != 1:\n            return\
    \ -1\n        b = 1\n        while pow(b, (p - 1) >> 1, p) == 1:\n           \
    \ b += 1\n        m = p - 1\n        e = 0\n        while not m & 1:\n       \
    \     m >>= 1\n            e += 1\n        x = pow(a, (m - 1) >> 1, p)\n     \
    \   y = (a * x % p) * x % p\n        x = a * x % p\n        z = pow(b, m, p)\n\
    \        while y != 1:\n            j = 0\n            t = y\n            while\
    \ t != 1:\n                j += 1\n                t = t * t % p\n           \
    \ z = pow(z, 1 << (e - j - 1), p)\n            x = x * z % p\n            z =\
    \ z * z % p\n            y = y * z % p\n            e = j\n        return x\n\n\
    \    @classmethod\n    def sqrt(cls, a: list, deg=-1) -> list:\n        if deg\
    \ == -1:\n            deg = len(a)\n        if len(a) == 0:\n            return\
    \ [0] * deg\n        if a[0] == 0:\n            for i in range(1, len(a)):\n \
    \               if a[i] != 0:\n                    if i & 1:\n               \
    \         return []\n                    if deg - i // 2 <= 0:\n             \
    \           break\n                    ret = cls.sqrt(a[i:], deg - i // 2)\n \
    \                   if not ret:\n                        return []\n         \
    \           ret[:0] = [0] * (i >> 1)\n                    if len(ret) < deg:\n\
    \                        ret[len(ret) :] = [0] * (deg - len(ret))\n          \
    \          return ret\n            return [0] * deg\n        sqr = cls.mod_sqrt(a[0],\
    \ MOD)\n        if sqr == -1:\n            return []\n        ret = [sqr]\n  \
    \      inv2 = 499122177\n        i = 1\n        while i < deg:\n            i\
    \ <<= 1\n            ret = cls.mul_scalar(cls.add(ret, multiply(a[:i], cls.inv(ret,\
    \ i))), inv2)\n        return ret[:deg]\n\n    @staticmethod\n    def eval(a:\
    \ list, x: int) -> int:\n        r = 0\n        w = 1\n        for v in a:\n \
    \           r += w * v % MOD\n            w = w * x % MOD\n        return r %\
    \ MOD\n\n    @staticmethod\n    def inv(a: list, deg: int = -1) -> list:\n   \
    \     # assert(self[0] != 0)\n        if deg == -1:\n            deg = len(a)\n\
    \        res = [0] * deg\n        res[0] = pow(a[0], MOD - 2, MOD)\n        d\
    \ = 1\n        while d < deg:\n            f = [0] * (d << 1)\n            tmp\
    \ = min(len(a), d << 1)\n            f[:tmp] = a[:tmp]\n            g = [0] *\
    \ (d << 1)\n            g[:d] = res[:d]\n            ntt(f)\n            ntt(g)\n\
    \            for i, x in enumerate(g):\n                f[i] = f[i] * x % MOD\n\
    \            intt(f)\n            f[:d] = [0] * d\n            ntt(f)\n      \
    \      for i, x in enumerate(g):\n                f[i] = f[i] * x % MOD\n    \
    \        intt(f)\n            for j in range(d, min(d << 1, deg)):\n         \
    \       if f[j]:\n                    res[j] = MOD - f[j]\n                else:\n\
    \                    res[j] = 0\n            d <<= 1\n        return res\n\n \
    \   @classmethod\n    def pow(cls, a: list, k: int, deg=-1) -> list:\n       \
    \ n = len(a)\n        if deg == -1:\n            deg = n\n        if k == 0:\n\
    \            if not deg:\n                return []\n            ret = [0] * deg\n\
    \            ret[0] = 1\n            return ret\n        for i, x in enumerate(a):\n\
    \            if x:\n                rev = pow(x, MOD - 2, MOD)\n             \
    \   ret = cls.mul_scalar(\n                    cls.exp(\n                    \
    \    cls.mul_scalar(cls.log(cls.mul_scalar(a, rev)[i:], deg), k), deg\n      \
    \              ),\n                    pow(x, k, MOD),\n                )\n  \
    \              ret[:0] = [0] * (i * k)\n                if len(ret) < deg:\n \
    \                   ret[len(ret) :] = [0] * (deg - len(ret))\n               \
    \     return ret\n                return ret[:deg]\n            if (i + 1) * k\
    \ >= deg:\n                break\n        return [0] * deg\n\n    @staticmethod\n\
    \    def exp(a: list, deg=-1) -> list:\n        # assert(not self or self[0] ==\
    \ 0)\n        if deg == -1:\n            deg = len(a)\n        inv = [0, 1]\n\n\
    \        def inplace_integral(F: list) -> list:\n            n = len(F)\n    \
    \        while len(inv) <= n:\n                j, k = divmod(MOD, len(inv))\n\
    \                inv.append((-inv[k] * j) % MOD)\n            return [0] + [x\
    \ * inv[i + 1] % MOD for i, x in enumerate(F)]\n\n        def inplace_diff(F:\
    \ list) -> list:\n            return [x * i % MOD for i, x in enumerate(F) if\
    \ i]\n\n        b = [1, (a[1] if 1 < len(a) else 0)]\n        c = [1]\n      \
    \  z1 = []\n        z2 = [1, 1]\n        m = 2\n        while m < deg:\n     \
    \       y = b + [0] * m\n            ntt(y)\n            z1 = z2\n           \
    \ z = [y[i] * p % MOD for i, p in enumerate(z1)]\n            intt(z)\n      \
    \      z[: m >> 1] = [0] * (m >> 1)\n            ntt(z)\n            for i, p\
    \ in enumerate(z1):\n                z[i] = z[i] * (-p) % MOD\n            intt(z)\n\
    \            c[m >> 1 :] = z[m >> 1 :]\n            z2 = c + [0] * m\n       \
    \     ntt(z2)\n            tmp = min(len(a), m)\n            x = a[:tmp] + [0]\
    \ * (m - tmp)\n            x = inplace_diff(x)\n            x.append(0)\n    \
    \        ntt(x)\n            for i, p in enumerate(x):\n                x[i] =\
    \ y[i] * p % MOD\n            intt(x)\n            for i, p in enumerate(b):\n\
    \                if not i:\n                    continue\n                x[i\
    \ - 1] -= p * i % MOD\n            x += [0] * m\n            for i in range(m\
    \ - 1):\n                x[m + i], x[i] = x[i], 0\n            ntt(x)\n      \
    \      for i, p in enumerate(z2):\n                x[i] = x[i] * p % MOD\n   \
    \         intt(x)\n            x.pop()\n            x = inplace_integral(x)\n\
    \            x[:m] = [0] * m\n            for i in range(m, min(len(a), m << 1)):\n\
    \                x[i] += a[i]\n            ntt(x)\n            for i, p in enumerate(y):\n\
    \                x[i] = x[i] * p % MOD\n            intt(x)\n            b[m:]\
    \ = x[m:]\n            m <<= 1\n        return b[:deg]\n\n    @classmethod\n \
    \   def log(cls, a: list, deg=-1) -> list:\n        # assert(a[0] == 1)\n    \
    \    if deg == -1:\n            deg = len(a)\n        return cls.integral(multiply(cls.fps_diff(a),\
    \ cls.inv(a, deg))[: deg - 1])\n\n    @staticmethod\n    def integral(a: list)\
    \ -> list:\n        n = len(a)\n        res = [0] * (n + 1)\n        if n:\n \
    \           res[1] = 1\n        for i in range(2, n + 1):\n            j, k =\
    \ divmod(MOD, i)\n            res[i] = (-res[k] * j) % MOD\n        for i, x in\
    \ enumerate(a):\n            res[i + 1] = res[i + 1] * x % MOD\n        return\
    \ res\n\n    @staticmethod\n    def fps_diff(a: list) -> list:\n        return\
    \ [i * x % MOD for i, x in enumerate(a) if i]\n\n    @staticmethod\n    def composition(a:\
    \ list, b: list) -> list:\n        deg = min(len(a), len(b))\n        k = int(deg**0.5\
    \ + 1)\n        d = (deg + k) // k\n\n        X = [[] for _ in range(k + 1)]\n\
    \        X[0] = [1]\n        for i, x in enumerate(X):\n            if i == k:\n\
    \                break\n            X[i + 1] = multiply(x, b)[: deg + 1]\n\n \
    \       Y = [[0] * len(X[-1]) for _ in range(k)]\n        X[d + 1 :] = []\n  \
    \      xd = X.pop()\n        for i, y in enumerate(Y):\n            for j, x in\
    \ enumerate(X):\n                if i * d + j >= deg:\n                    break\n\
    \                for t in range(min(deg + 1, len(x))):\n                    if\
    \ t < len(y):\n                        y[t] += x[t] * a[i * d + j] % MOD\n\n \
    \       F = [0] * (deg + 1)\n        Z = [1]\n        for i, y in enumerate(Y):\n\
    \            tmp = multiply(y, Z)[: deg + 1]\n            for j, yy in enumerate(tmp):\n\
    \                F[j] += yy\n            Z = multiply(Z, xd)[: deg + 1]\n    \
    \    res = [x % MOD for x in F]\n        res.pop()\n        return res\n\n   \
    \ @staticmethod\n    def chirp_z(f: list, W: int, N: int = -1, A: int = 1) ->\
    \ list:\n        if N == -1:\n            N = len(f)\n        if not f or N ==\
    \ 0:\n            return []\n        M = len(f)\n        if A != -1:\n       \
    \     x = 1\n            for i in range(M):\n                f[i] = f[i] * x %\
    \ MOD\n                x = x * A % MOD\n        if W == 0:\n            F = [f[0]]\
    \ * N\n            F[0] = sum(f) % MOD\n            return F\n        wc = [0]\
    \ * (N + M)\n        iwc = [0] * max(N, M)\n        ws = 1\n        iW = pow(W,\
    \ MOD - 2, MOD)\n        iws = 1\n        wc[0] = iwc[0] = 1\n        tmp = 1\n\
    \        for i in range(1, N + M):\n            wc[i] = tmp = ws * tmp % MOD\n\
    \            ws = ws * W % MOD\n        tmp = 1\n        for i in range(1, max(N,\
    \ M)):\n            iwc[i] = tmp = iws * tmp % MOD\n            iws = iws * iW\
    \ % MOD\n        for i, x in enumerate(f):\n            f[i] = x * iwc[i] % MOD\n\
    \        f.reverse()\n        g = multiply(f, wc)\n        F = [0] * N\n     \
    \   for i, x in enumerate(iwc):\n            if i == N:\n                break\n\
    \            F[i] = g[M - 1 + i] * x % MOD\n        return F\n\n    @staticmethod\n\
    \    def multivariate_multiplication(f: list, g: list, base: list) -> list:\n\
    \        n = len(f)\n        s = len(base)\n        W = 1\n        if s == 0:\n\
    \            return [f[0] * g[0] % MOD]\n        while W < n << 1:\n         \
    \   W <<= 1\n        chi = [0] * n\n        for i in range(n):\n            x\
    \ = i\n            for j in range(s - 1):\n                x //= base[j]\n   \
    \             chi[i] += x\n            chi[i] %= s\n        F = [[0] * W for _\
    \ in range(s)]\n        G = [[0] * W for _ in range(s)]\n        for i, j in enumerate(chi):\n\
    \            F[j][i] = f[i]\n            G[j][i] = g[i]\n        for i in range(s):\n\
    \            ntt(F[i])\n            ntt(G[i])\n        for k in range(W):\n  \
    \          a = [0] * s\n            for i, f in enumerate(F):\n              \
    \  tmp = f[k]\n                for j, g in enumerate(G):\n                   \
    \ a[i + j - (s if i + j >= s else 0)] += tmp * g[k] % MOD\n            for i,\
    \ f in enumerate(F):\n                f[k] = a[i] % MOD\n        for f in F:\n\
    \            intt(f)\n        return [F[j][i] for i, j in enumerate(chi)]\n\n\
    \    @classmethod\n    def multipoint_evaluation(cls, f: list, xs: list) -> list:\n\
    \        s = len(xs)\n        N = 1 << (s - 1).bit_length() if s != 1 else 2\n\
    \        if not f or not xs:\n            return [0] * s\n        buf = [[] for\
    \ _ in range(N << 1)]\n        for i in range(N):\n            n = -xs[i] if i\
    \ < s else 0\n            buf[i + N] = [n + 1, n - 1]\n        for i in range(N\
    \ - 1, 0, -1):\n            g = buf[i << 1 | 0]\n            h = buf[i << 1 |\
    \ 1]\n            n = len(g)\n            m = n << 1\n            buf[i][n:] =\
    \ []\n            buf[i][len(buf[i]) :] = [0] * (n - len(buf[i]))\n          \
    \  for j in range(n):\n                buf[i][j] = g[j] * h[j] % MOD - 1\n   \
    \         if i != 1:\n                ntt_doubling(buf[i])\n                buf[i][len(buf[i])\
    \ :] = [0] * (m - len(buf[i]))\n                for j in range(m):\n         \
    \           buf[i][j] += 1 if j < n else -1\n        fs = len(f)\n        root\
    \ = buf[1]\n        intt(root)\n        root.append(1)\n        root.reverse()\n\
    \        tmp = cls.inv(root, fs)\n        tmp.reverse()\n        root = multiply(tmp,\
    \ f)\n        root[: fs - 1] = []\n        root[N:] = []\n        root[len(root)\
    \ :] = [0] * (N - len(root))\n\n        ans = [0] * s\n\n        def calc(i: int,\
    \ l: int, r: int, g: list) -> None:\n            if i >= N:\n                ans[i\
    \ - N] = g[0]\n                return\n            length = len(g)\n         \
    \   m = l + r >> 1\n            ntt(g)\n            tmp = buf[i << 1 | 1]\n  \
    \          for j in range(length):\n                tmp[j] = tmp[j] * g[j] % MOD\n\
    \            intt(tmp)\n            calc(i << 1, l, m, tmp[length >> 1 :])\n \
    \           if m >= s:\n                return\n            tmp = buf[i << 1 |\
    \ 0]\n            for j in range(length):\n                tmp[j] = tmp[j] * g[j]\
    \ % MOD\n            intt(tmp)\n            calc(i << 1 | 1, m, r, tmp[length\
    \ >> 1 :])\n\n        calc(1, 0, N, root)\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: convolution/formal_power_series.py
  requiredBy: []
  timestamp: '2023-09-16 18:27:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: convolution/formal_power_series.py
layout: document
title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
---
