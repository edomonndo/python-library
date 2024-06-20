---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/polynomial/multipoint_evaluation_geometric_sequence.test.py
    title: test/library_checker/polynomial/multipoint_evaluation_geometric_sequence.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution.convolution import *\n\n\ndef chirp_z(f: list[int], W: int,\
    \ N: int = -1, A: int = 1) -> list[int]:\n    if N == -1:\n        N = len(f)\n\
    \    if not f or N == 0:\n        return []\n    M = len(f)\n    if A != -1:\n\
    \        x = 1\n        for i in range(M):\n            f[i] = f[i] * x % MOD\n\
    \            x = x * A % MOD\n    if W == 0:\n        F = [f[0]] * N\n       \
    \ F[0] = sum(f) % MOD\n        return F\n    wc = [0] * (N + M)\n    iwc = [0]\
    \ * max(N, M)\n    ws = 1\n    iW = pow(W, MOD - 2, MOD)\n    iws = 1\n    wc[0]\
    \ = iwc[0] = 1\n    tmp = 1\n    for i in range(1, N + M):\n        wc[i] = tmp\
    \ = ws * tmp % MOD\n        ws = ws * W % MOD\n    tmp = 1\n    for i in range(1,\
    \ max(N, M)):\n        iwc[i] = tmp = iws * tmp % MOD\n        iws = iws * iW\
    \ % MOD\n    for i, x in enumerate(f):\n        f[i] = x * iwc[i] % MOD\n    f.reverse()\n\
    \    g = multiply(f, wc)\n    F = [0] * N\n    for i, x in enumerate(iwc):\n \
    \       if i == N:\n            break\n        F[i] = g[M - 1 + i] * x % MOD\n\
    \    return F\n"
  dependsOn:
  - convolution/convolution.py
  isVerificationFile: false
  path: convolution/chirp_z.py
  requiredBy: []
  timestamp: '2024-06-20 10:59:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/polynomial/multipoint_evaluation_geometric_sequence.test.py
documentation_of: convolution/chirp_z.py
layout: document
redirect_from:
- /library/convolution/chirp_z.py
- /library/convolution/chirp_z.py.html
title: convolution/chirp_z.py
---
