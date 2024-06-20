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
  code: "from convolution.convolution import *\nfrom convolution.formal_power_series\
    \ import FPS\n\n\nclass ProductTree:\n    def __init__(self, a: list[int]):\n\
    \        self.a = a\n        self.sz = sz = len(a)\n        n = 1\n        while\
    \ n < sz:\n            n <<= 1\n        self.n = n\n        self.buf = buf = [[]\
    \ for _ in range(n << 1)]\n        self.l = l = [sz] * (n << 1)\n        self.r\
    \ = r = [sz] * (n << 1)\n        for i in range(sz):\n            l[i + n] = i\n\
    \            r[i + n] = i + 1\n            buf[i + n] = [-a[i] + 1, -a[i] - 1]\n\
    \        for i in range(n - 1, 0, -1):\n            f = []\n            l[i] =\
    \ l[i << 1 | 0]\n            r[i] = r[i << 1 | 1]\n            if not buf[i <<\
    \ 1 | 0]:\n                continue\n            if not buf[1 << 1 | 1]:\n   \
    \             buf[i] = buf[i << 1 | 0][:]\n                continue\n        \
    \    if len(buf[i << 1 | 0]) == len(buf[i << 1 | 1]):\n                buf[i]\
    \ = buf[i << 1 | 0][:]\n                ntt_doubling(buf[i])\n               \
    \ f = buf[i << 1 | 1][:]\n                ntt_doubling(f)\n            else:\n\
    \                buf[i] = buf[i << 1 | 0][:]\n                ntt_doubling(buf[i])\n\
    \                f = buf[i << 1 | 1][:]\n                intt(f)\n           \
    \     FPS.resize(f, len(buf[i]))\n                ntt(f)\n            for j in\
    \ range(len(buf[i])):\n                buf[i][j] = buf[i][j] * f[j] % MOD\n  \
    \      for i in range(n << 1):\n            intt(buf[i])\n            FPS.shrink(buf[i])\n"
  dependsOn:
  - convolution/convolution.py
  - convolution/formal_power_series.py
  isVerificationFile: false
  path: convolution/product_tree.py
  requiredBy: []
  timestamp: '2024-06-20 09:29:05+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: convolution/product_tree.py
layout: document
redirect_from:
- /library/convolution/product_tree.py
- /library/convolution/product_tree.py.html
title: convolution/product_tree.py
---
