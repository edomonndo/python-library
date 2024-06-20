---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  - icon: ':question:'
    path: convolution/formal_power_series.py
    title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/multipoint_evaluation.test.py
    title: test/library_checker/polynomial/multipoint_evaluation.test.py
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
    \ import FPS\n\n\ndef multipoint_evaluation(f: list[int], xs: list[int]) -> list[int]:\n\
    \    s = len(xs)\n    N = 1 << (s - 1).bit_length() if s != 1 else 2\n    if not\
    \ f or not xs:\n        return [0] * s\n    buf = [[] for _ in range(N << 1)]\n\
    \    for i in range(N):\n        n = -xs[i] if i < s else 0\n        buf[i + N]\
    \ = [n + 1, n - 1]\n    for i in range(N - 1, 0, -1):\n        g = buf[i << 1\
    \ | 0]\n        h = buf[i << 1 | 1]\n        n = len(g)\n        m = n << 1\n\
    \        buf[i][n:] = []\n        buf[i][len(buf[i]) :] = [0] * (n - len(buf[i]))\n\
    \        for j in range(n):\n            buf[i][j] = g[j] * h[j] % MOD - 1\n \
    \       if i != 1:\n            ntt_doubling(buf[i])\n            buf[i][len(buf[i])\
    \ :] = [0] * (m - len(buf[i]))\n            for j in range(m):\n             \
    \   buf[i][j] += 1 if j < n else -1\n    fs = len(f)\n    root = buf[1]\n    intt(root)\n\
    \    root.append(1)\n    root.reverse()\n    tmp = FPS.inv(root, fs)\n    tmp.reverse()\n\
    \    root = multiply(tmp, f)\n    root[: fs - 1] = []\n    root[N:] = []\n   \
    \ root[len(root) :] = [0] * (N - len(root))\n\n    res = [0] * s\n\n    def calc(i:\
    \ int, l: int, r: int, g: list[int]) -> None:\n        if i >= N:\n          \
    \  res[i - N] = g[0]\n            return\n        length = len(g)\n        m =\
    \ (l + r) >> 1\n        ntt(g)\n        tmp = buf[i << 1 | 1]\n        for j in\
    \ range(length):\n            tmp[j] = tmp[j] * g[j] % MOD\n        intt(tmp)\n\
    \        calc(i << 1, l, m, tmp[length >> 1 :])\n        if m >= s:\n        \
    \    return\n        tmp = buf[i << 1 | 0]\n        for j in range(length):\n\
    \            tmp[j] = tmp[j] * g[j] % MOD\n        intt(tmp)\n        calc(i <<\
    \ 1 | 1, m, r, tmp[length >> 1 :])\n\n    calc(1, 0, N, root)\n    return res\n"
  dependsOn:
  - convolution/convolution.py
  - convolution/formal_power_series.py
  isVerificationFile: false
  path: convolution/multipoint_evaluation.py
  requiredBy: []
  timestamp: '2024-06-20 12:15:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/polynomial/multipoint_evaluation.test.py
documentation_of: convolution/multipoint_evaluation.py
layout: document
redirect_from:
- /library/convolution/multipoint_evaluation.py
- /library/convolution/multipoint_evaluation.py.html
title: convolution/multipoint_evaluation.py
---
