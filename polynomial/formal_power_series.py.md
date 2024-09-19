---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: polynomial/composition.py
    title: Composition
  - icon: ':heavy_check_mark:'
    path: polynomial/multipoint_evaluation.py
    title: Multipoint Evaluation
  - icon: ':heavy_check_mark:'
    path: polynomial/product_tree.py
    title: Product Tree
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/division_of_polynomials.test.py
    title: Division of Polynomials
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/exp_of_formal_power_series.test.py
    title: Exp of Formal Power Series
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/exp_of_formal_power_series_sparse.test.py
    title: Exp of Formal Power Series (Sparse)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/inv_of_formal_power_series.test.py
    title: Inv of Formal Power Series
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/inv_of_formal_power_series_sparse.test.py
    title: Inv of Formal Power Series (Sparse)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/log_of_formal_power_series.test.py
    title: Log of Formal Power Series
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/log_of_formal_power_series_sparse.test.py
    title: Log of Formal Power Series (Sparse)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/pow_of_formal_power_series.test.py
    title: Pow of Formal Power Series
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/pow_of_formal_power_series_sparse.test.py
    title: Pow of Formal Power Series (Sparse)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/product_of_polynomial_sequence.test.py
    title: Product of Polynomial Sequence
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/sqrt_of_formal_power_series.test.py
    title: Sqrt of Formal Power Series
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/sqrt_of_formal_power_series_sparse.test.py
    title: Sqrt of Formal Power Series (Sparse)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution.convolution import *\n\n\nclass FPS:\n    @staticmethod\n\
    \    def shrink(a: list[int]) -> None:\n        while a and not a[-1]:\n     \
    \       a.pop()\n\n    @staticmethod\n    def resize(a: list[int], size: int,\
    \ val: int = 0) -> None:\n        a[size:] = []\n        a[len(a) :] = [val] *\
    \ (size - len(a))\n\n    @staticmethod\n    def add(a: list[int], b: list[int])\
    \ -> list[int]:\n        if len(a) < len(b):\n            res = b[::]\n      \
    \      for i, x in enumerate(a):\n                res[i] += x\n        else:\n\
    \            res = a[::]\n            for i, x in enumerate(b):\n            \
    \    res[i] += x\n        return [x % MOD for x in res]\n\n    @staticmethod\n\
    \    def add_scalar(a: list[int], k: int) -> list[int]:\n        res = a[:]\n\
    \        res[0] = (res[0] + k) % MOD\n        return res\n\n    @classmethod\n\
    \    def sub(cls, a: list[int], b: list[int]) -> list[int]:\n        if len(a)\
    \ < len(b):\n            res = b[::]\n            for i, x in enumerate(a):\n\
    \                res[i] -= x\n            res = cls.neg(res)\n        else:\n\
    \            res = a[::]\n            for i, x in enumerate(b):\n            \
    \    res[i] -= x\n        return [x % MOD for x in res]\n\n    @classmethod\n\
    \    def sub_scalar(cls, a: list[int], k: int) -> list[int]:\n        return cls.add_scalar(a,\
    \ -k)\n\n    @staticmethod\n    def neg(a: list[int]) -> list[int]:\n        return\
    \ [MOD - x if x else 0 for x in a]\n\n    @staticmethod\n    def mul_scalar(a:\
    \ list[int], k: int) -> list[int]:\n        return [x * k % MOD for x in a]\n\n\
    \    @staticmethod\n    def matmul(a: list[int], b: list[int]) -> list[int]:\n\
    \        return [x * b[i] % MOD for i, x in enumerate(a)]\n\n    @classmethod\n\
    \    def div(cls, a: list[int], b: list[int]) -> list[int]:\n        if len(a)\
    \ < len(b):\n            return []\n        n = len(a) - len(b) + 1\n        cnt\
    \ = 0\n        if len(b) > 64:\n            return multiply(a[::-1][:n], cls.inv(b[::-1],\
    \ n))[:n][::-1]\n        f, g = a[::], b[::]\n        while g and not g[-1]:\n\
    \            g.pop()\n            cnt += 1\n        coef = pow(g[-1], MOD - 2,\
    \ MOD)\n        g = cls.mul_scalar(g, coef)\n        deg = len(f) - len(g) + 1\n\
    \        gs = len(g)\n        quo = [0] * deg\n        for i in range(deg)[::-1]:\n\
    \            quo[i] = x = f[i + gs - 1] % MOD\n            for j, y in enumerate(g):\n\
    \                f[i + j] -= x * y\n        return cls.mul_scalar(quo, coef) +\
    \ [0] * cnt\n\n    @classmethod\n    def mod(cls, a: list[int], b: list[int])\
    \ -> list[int]:\n        res = cls.sub(a, multiply(cls.div(a, b), b))\n      \
    \  cls.shrink(res)\n        return res\n\n    @classmethod\n    def divmod(cls,\
    \ a: list[int], b: list[int]) -> tuple[list[int], list[int]]:\n        q = cls.div(a,\
    \ b)\n        r = cls.sub(a, multiply(q, b))\n        while r and not r[-1]:\n\
    \            r.pop()\n        return q, r\n\n    @staticmethod\n    def mod_sqrt(a:\
    \ int, p: int) -> int:\n        \"x s.t. x**2 == a (mod p) if exist else -1\"\n\
    \        if a < 2:\n            return a\n        if pow(a, (p - 1) >> 1, p) !=\
    \ 1:\n            return -1\n        b = 1\n        while pow(b, (p - 1) >> 1,\
    \ p) == 1:\n            b += 1\n        m = p - 1\n        e = 0\n        while\
    \ not m & 1:\n            m >>= 1\n            e += 1\n        x = pow(a, (m -\
    \ 1) >> 1, p)\n        y = (a * x % p) * x % p\n        x = a * x % p\n      \
    \  z = pow(b, m, p)\n        while y != 1:\n            j = 0\n            t =\
    \ y\n            while t != 1:\n                j += 1\n                t = t\
    \ * t % p\n            z = pow(z, 1 << (e - j - 1), p)\n            x = x * z\
    \ % p\n            z = z * z % p\n            y = y * z % p\n            e = j\n\
    \        return x\n\n    @classmethod\n    def sqrt(cls, a: list[int], deg=-1)\
    \ -> list[int]:\n        if deg == -1:\n            deg = len(a)\n        if len(a)\
    \ == 0:\n            return [0] * deg\n        if a[0] == 0:\n            for\
    \ i in range(1, len(a)):\n                if a[i] != 0:\n                    if\
    \ i & 1:\n                        return []\n                    if deg - (i >>\
    \ 1) <= 0:\n                        break\n                    ret = cls.sqrt(a[i:],\
    \ deg - (i >> 1))\n                    if not ret:\n                        return\
    \ []\n                    ret[:0] = [0] * (i >> 1)\n                    if len(ret)\
    \ < deg:\n                        ret[len(ret) :] = [0] * (deg - len(ret))\n \
    \                   return ret\n            return [0] * deg\n        sqr = cls.mod_sqrt(a[0],\
    \ MOD)\n        if sqr == -1:\n            return []\n        ret = [sqr]\n  \
    \      inv2 = 499122177\n        i = 1\n        while i < deg:\n            i\
    \ <<= 1\n            ret = cls.mul_scalar(cls.add(ret, multiply(a[:i], cls.inv(ret,\
    \ i))), inv2)\n        return ret[:deg]\n\n    @staticmethod\n    def eval(a:\
    \ list[int], x: int) -> int:\n        r = 0\n        w = 1\n        for v in a:\n\
    \            r += w * v % MOD\n            w = w * x % MOD\n        return r %\
    \ MOD\n\n    @staticmethod\n    def inv(a: list[int], deg: int = -1) -> list[int]:\n\
    \        # assert(self[0] != 0)\n        if deg == -1:\n            deg = len(a)\n\
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
    \   @classmethod\n    def pow(cls, a: list[int], k: int, deg=-1) -> list[int]:\n\
    \        n = len(a)\n        if deg == -1:\n            deg = n\n        if k\
    \ == 0:\n            if not deg:\n                return []\n            res =\
    \ [0] * deg\n            res[0] = 1\n            return res\n        for i, x\
    \ in enumerate(a):\n            if x:\n                rev = pow(x, MOD - 2, MOD)\n\
    \                res = cls.mul_scalar(\n                    cls.exp(\n       \
    \                 cls.mul_scalar(cls.log(cls.mul_scalar(a, rev)[i:], deg), k),\
    \ deg\n                    ),\n                    pow(x, k, MOD),\n         \
    \       )\n                res[:0] = [0] * (i * k)\n                if len(res)\
    \ < deg:\n                    res[len(res) :] = [0] * (deg - len(res))\n     \
    \               return res\n                return res[:deg]\n            if (i\
    \ + 1) * k >= deg:\n                break\n        return [0] * deg\n\n    @staticmethod\n\
    \    def exp(a: list[int], deg=-1) -> list[int]:\n        # assert(not self or\
    \ self[0] == 0)\n        if deg == -1:\n            deg = len(a)\n        inv\
    \ = [0, 1]\n\n        def inplace_integral(F: list[int]) -> list[int]:\n     \
    \       n = len(F)\n            while len(inv) <= n:\n                j, k = divmod(MOD,\
    \ len(inv))\n                inv.append((-inv[k] * j) % MOD)\n            return\
    \ [0] + [x * inv[i + 1] % MOD for i, x in enumerate(F)]\n\n        def inplace_diff(F:\
    \ list[int]) -> list[int]:\n            return [x * i % MOD for i, x in enumerate(F)\
    \ if i]\n\n        b = [1, (a[1] if 1 < len(a) else 0)]\n        c = [1]\n   \
    \     z1 = []\n        z2 = [1, 1]\n        m = 2\n        while m < deg:\n  \
    \          y = b + [0] * m\n            ntt(y)\n            z1 = z2\n        \
    \    z = [y[i] * p % MOD for i, p in enumerate(z1)]\n            intt(z)\n   \
    \         z[: m >> 1] = [0] * (m >> 1)\n            ntt(z)\n            for i,\
    \ p in enumerate(z1):\n                z[i] = z[i] * (-p) % MOD\n            intt(z)\n\
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
    \   def log(cls, a: list[int], deg=-1) -> list[int]:\n        # assert(a[0] ==\
    \ 1)\n        if deg == -1:\n            deg = len(a)\n        return cls.integral(multiply(cls.fps_diff(a),\
    \ cls.inv(a, deg))[: deg - 1])\n\n    @staticmethod\n    def integral(a: list[int])\
    \ -> list[int]:\n        n = len(a)\n        res = [0] * (n + 1)\n        if n:\n\
    \            res[1] = 1\n        for i in range(2, n + 1):\n            j, k =\
    \ divmod(MOD, i)\n            res[i] = (-res[k] * j) % MOD\n        for i, x in\
    \ enumerate(a):\n            res[i + 1] = res[i + 1] * x % MOD\n        return\
    \ res\n\n    @staticmethod\n    def fps_diff(a: list[int]) -> list[int]:\n   \
    \     return [i * x % MOD for i, x in enumerate(a) if i]\n"
  dependsOn:
  - convolution/convolution.py
  isVerificationFile: false
  path: polynomial/formal_power_series.py
  requiredBy:
  - polynomial/composition.py
  - polynomial/multipoint_evaluation.py
  - polynomial/product_tree.py
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/polynomial/exp_of_formal_power_series.test.py
  - test/library_checker/polynomial/product_of_polynomial_sequence.test.py
  - test/library_checker/polynomial/division_of_polynomials.test.py
  - test/library_checker/polynomial/inv_of_formal_power_series_sparse.test.py
  - test/library_checker/polynomial/inv_of_formal_power_series.test.py
  - test/library_checker/polynomial/sqrt_of_formal_power_series.test.py
  - test/library_checker/polynomial/log_of_formal_power_series_sparse.test.py
  - test/library_checker/polynomial/pow_of_formal_power_series_sparse.test.py
  - test/library_checker/polynomial/sqrt_of_formal_power_series_sparse.test.py
  - test/library_checker/polynomial/pow_of_formal_power_series.test.py
  - test/library_checker/polynomial/log_of_formal_power_series.test.py
  - test/library_checker/polynomial/exp_of_formal_power_series_sparse.test.py
documentation_of: polynomial/formal_power_series.py
layout: document
title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
---
