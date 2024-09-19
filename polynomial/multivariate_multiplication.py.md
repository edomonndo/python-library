---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
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
  code: "from convolution.convolution import *\n\n\ndef multivariate_multiplication(\n\
    \    f: list[int], g: list[int], base: list[int]\n) -> list[int]:\n    n = len(f)\n\
    \    s = len(base)\n    W = 1\n    if s == 0:\n        return [f[0] * g[0] % MOD]\n\
    \    while W < n << 1:\n        W <<= 1\n    chi = [0] * n\n    for i in range(n):\n\
    \        x = i\n        for j in range(s - 1):\n            x //= base[j]\n  \
    \          chi[i] += x\n        chi[i] %= s\n    F = [[0] * W for _ in range(s)]\n\
    \    G = [[0] * W for _ in range(s)]\n    for i, j in enumerate(chi):\n      \
    \  F[j][i] = f[i]\n        G[j][i] = g[i]\n    for i in range(s):\n        ntt(F[i])\n\
    \        ntt(G[i])\n    for k in range(W):\n        a = [0] * s\n        for i,\
    \ f in enumerate(F):\n            tmp = f[k]\n            for j, g in enumerate(G):\n\
    \                a[i + j - (s if i + j >= s else 0)] += tmp * g[k] % MOD\n   \
    \     for i, f in enumerate(F):\n            f[k] = a[i] % MOD\n    for f in F:\n\
    \        intt(f)\n    return [F[j][i] for i, j in enumerate(chi)]\n"
  dependsOn:
  - convolution/convolution.py
  isVerificationFile: false
  path: polynomial/multivariate_multiplication.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: polynomial/multivariate_multiplication.py
layout: document
title: Multivariate Multiplication
---
