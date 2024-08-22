---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/number_theory/rational_approximation.test.py
    title: Rational Approximation
  - icon: ':heavy_check_mark:'
    path: test/library_checker/number_theory/stern_brocot_tree.test.py
    title: "Stern\u2013Brocot Tree"
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SternBrocotTree:\n    @staticmethod\n    def encode(a: int, b: int)\
    \ -> list[tuple[bool, int]]:\n        path = []\n        q, r = divmod(a, b)\n\
    \        if q > 0:\n            path.append((True, q))\n\n        a, b = b, r\n\
    \        is_right = False\n        while b:\n            q, r = divmod(a, b)\n\
    \            path.append((is_right, q))\n            a, b = b, r\n           \
    \ is_right ^= True\n\n        is_right, k = path.pop()\n        if k > 1:\n  \
    \          path.append((is_right, k - 1))\n        return path\n\n    @staticmethod\n\
    \    def _decode_interval(code: list[tuple[bool, int]]) -> tuple[int, int, int,\
    \ int]:\n        p, q, r, s = 0, 1, 1, 0\n        for is_right, k in code:\n \
    \           if is_right:\n                p += k * r\n                q += k *\
    \ s\n            else:\n                r += k * p\n                s += k * q\n\
    \        return p, q, r, s\n\n    @classmethod\n    def decode(cls, code: list[tuple[bool,\
    \ int]]) -> tuple[int, int]:\n        p, q, r, s = cls._decode_interval(code)\n\
    \        return p + r, q + s\n\n    @classmethod\n    def lca(cls, a: int, b:\
    \ int, c: int, d: int) -> tuple[int, int]:\n        if (a, b) == (1, 1) or (c,\
    \ d) == (1, 1):\n            return (1, 1)\n\n        code1 = cls.encode(a, b)\n\
    \        code2 = cls.encode(c, d)\n        if code1[0][0] != code2[0][0]:\n  \
    \          return (1, 1)\n\n        lca_code = []\n        for (t, k), (_, l)\
    \ in zip(code1, code2):\n            lca_code.append((t, min(k, l)))\n       \
    \     if k != l:\n                break\n        return cls.decode(lca_code)\n\
    \n    @classmethod\n    def depth(cls, a: int, b: int) -> int:\n        code =\
    \ cls.encode(a, b)\n        return sum(k for _, k in code)\n\n    @classmethod\n\
    \    def ancestor(cls, a: int, b: int, k: int, default=None) -> tuple[int, int]:\n\
    \        code = []\n        for is_right, l in cls.encode(a, b):\n           \
    \ l = min(k, l)\n            code.append((is_right, l))\n            k -= l\n\
    \            if k == 0:\n                return cls.decode(code)\n        else:\n\
    \            return default\n\n    @classmethod\n    def range(cls, a: int, b:\
    \ int) -> tuple[int, int, int, int]:\n        return cls._decode_interval(cls.encode(a,\
    \ b))\n\n    @staticmethod\n    def approx(n: int, x: int, y: int) -> tuple[int,\
    \ int, int, int]:\n        real = [0, 1]\n        imag = [1, 0]\n        while\
    \ y and real[-1] <= n and imag[-1] <= n:\n            t, r = divmod(x, y)\n  \
    \          real.append(real[-1] * t + real[-2])\n            imag.append(imag[-1]\
    \ * t + imag[-2])\n            x, y = y, r\n        if real[-1] <= n and imag[-1]\
    \ <= n:\n            return real[-1], imag[-1], real[-1], imag[-1]\n        a,\
    \ b = real[-2], imag[-2]\n        t = n\n        if a > 0:\n            t = min(t,\
    \ (n - imag[-3]) // b)\n        if b > 0:\n            t = min(t, (n - real[-3])\
    \ // a)\n        c, d = real[-3] + t * a, imag[-3] + t * b\n        if a * d >\
    \ c * b:\n            a, b, c, d = c, d, a, b\n        return a, b, c, d\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/stern_brocot_tree.py
  requiredBy: []
  timestamp: '2024-08-22 11:09:04+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/library_checker/number_theory/stern_brocot_tree.test.py
  - test/library_checker/number_theory/rational_approximation.test.py
documentation_of: number_theory/stern_brocot_tree.py
layout: document
title: Stern Brocot tree
---

https://tjkendev.github.io/procon-library/python/math/stern-brocot-tree.html