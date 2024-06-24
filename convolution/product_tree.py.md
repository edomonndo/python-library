---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  - icon: ':heavy_check_mark:'
    path: convolution/formal_power_series.py
    title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/multipoint_evaluation_pt.test.py
    title: test/library_checker/polynomial/multipoint_evaluation_pt.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/polynomial_interpolation.test.py
    title: test/library_checker/polynomial/polynomial_interpolation.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution.convolution import *\nfrom convolution.formal_power_series\
    \ import FPS\n\n\nclass ProductTree:\n    def __init__(self, xs: list[int]):\n\
    \        self.xs = xs\n        self.sz = sz = len(xs)\n        n = 1\n       \
    \ while n < sz:\n            n <<= 1\n        self.n = n\n        self.buf = buf\
    \ = [[] for _ in range(n << 1)]\n        self.l = l = [sz] * (n << 1)\n      \
    \  self.r = r = [sz] * (n << 1)\n        for i in range(sz):\n            l[i\
    \ + n] = i\n            r[i + n] = i + 1\n            buf[i + n] = [-xs[i] + 1,\
    \ -xs[i] - 1]\n        for i in range(n - 1, 0, -1):\n            f = []\n   \
    \         l[i] = l[i << 1 | 0]\n            r[i] = r[i << 1 | 1]\n           \
    \ if not buf[i << 1 | 0]:\n                continue\n            if not buf[i\
    \ << 1 | 1]:\n                buf[i] = buf[i << 1 | 0][:]\n                continue\n\
    \            if len(buf[i << 1 | 0]) == len(buf[i << 1 | 1]):\n              \
    \  buf[i] = buf[i << 1 | 0][:]\n                ntt_doubling(buf[i])\n       \
    \         f = buf[i << 1 | 1][:]\n                ntt_doubling(f)\n          \
    \  else:\n                buf[i] = buf[i << 1 | 0][:]\n                ntt_doubling(buf[i])\n\
    \                f = buf[i << 1 | 1][:]\n                intt(f)\n           \
    \     FPS.resize(f, len(buf[i]))\n                ntt(f)\n            for j in\
    \ range(len(buf[i])):\n                buf[i][j] = buf[i][j] * f[j] % MOD\n  \
    \      for i in range(n << 1):\n            intt(buf[i])\n            FPS.shrink(buf[i])\n\
    \n    @staticmethod\n    def _modinv(a: int, m: int) -> int:\n        b, u, v\
    \ = m, 1, 0\n        while b:\n            t = a // b\n            a, b = b, a\
    \ - t * b\n            u, v = v, u - t * v\n        u %= m\n        return u\n\
    \n    def _inner_multipoint_evaluation(self, f: list[int]) -> list[int]:\n   \
    \     res = []\n        st = [(f, 1)]\n        while st:\n            a, idx =\
    \ st.pop()\n            if self.l[idx] == self.r[idx]:\n                continue\n\
    \            a = FPS.mod(a, self.buf[idx])\n            if len(a) <= 64:\n   \
    \             for i in range(self.l[idx], self.r[idx]):\n                    res.append(FPS.eval(a,\
    \ self.xs[i]))\n                continue\n            st += [(a, idx << 1 | 1),\
    \ (a, idx << 1 | 0)]\n        return res\n\n    def multipoint_evaluation(self,\
    \ f: list[int]) -> list[int]:\n        if not f:\n            return [0] * self.sz\n\
    \        return self._inner_multipoint_evaluation(f)\n\n    def polynomial_interpolation(self,\
    \ ys: list[int]) -> list[int]:\n        # assert len(xs) == len(ys)\n        w\
    \ = FPS.fps_diff(self.buf[1])\n        vs = self._inner_multipoint_evaluation(w)\n\
    \        res = [[] for _ in range(self.n << 1)]\n        for i in range(self.n):\n\
    \            if i < len(self.xs):\n                res[self.n + i] = [ys[i] *\
    \ self._modinv(vs[i], MOD) % MOD]\n            else:\n                res[self.n\
    \ + i] = [1]\n        for i in range(self.n - 1, 0, -1):\n            if not self.buf[i\
    \ << 1 | 0]:\n                res[i] = []\n            elif not self.buf[i <<\
    \ 1 | 1]:\n                res[i] = res[i << 1 | 0]\n            else:\n     \
    \           res[i] = FPS.add(\n                    multiply(res[i << 1 | 0], self.buf[i\
    \ << 1 | 1]),\n                    multiply(res[i << 1 | 1], self.buf[i << 1 |\
    \ 0]),\n                )\n        return res[1]\n"
  dependsOn:
  - convolution/convolution.py
  - convolution/formal_power_series.py
  isVerificationFile: false
  path: convolution/product_tree.py
  requiredBy: []
  timestamp: '2024-06-20 12:15:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/polynomial/multipoint_evaluation_pt.test.py
  - test/library_checker/polynomial/polynomial_interpolation.test.py
documentation_of: convolution/product_tree.py
layout: document
redirect_from:
- /library/convolution/product_tree.py
- /library/convolution/product_tree.py.html
title: convolution/product_tree.py
---
