---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/convolution.py
    title: "\u7573\u307F\u8FBC\u307F $mod=998244353$"
  - icon: ':warning:'
    path: enumerative_combinatorics/combination_mod.py
    title: "\u4E8C\u9805\u4FC2\u6570(mod)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/polynomial/polynomial_tayler_shift.test.py
    title: test/library_checker/polynomial/polynomial_tayler_shift.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from convolution.convolution import *\nfrom enumerative_combinatorics.combination_mod\
    \ import Comb\n\n\ndef tayler_shift(a: list[int], c: int) -> list[int]:\n    n\
    \ = len(a)\n    C = Comb(n + 1)\n    res = [x * C.fact[i] % MOD for i, x in enumerate(a)]\n\
    \    res.reverse()\n    b = [0] * n\n    b[0] = 1\n    for i in range(1, n):\n\
    \        b[i] = (b[i - 1] * c % MOD) * C.inv[i] % MOD\n    res = multiply(res,\
    \ b)[:n]\n    res.reverse()\n    return [x * C.inv_fact[i] % MOD for i, x in enumerate(res)]\n"
  dependsOn:
  - convolution/convolution.py
  - enumerative_combinatorics/combination_mod.py
  isVerificationFile: false
  path: polynomial/tayler_shift.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/polynomial/polynomial_tayler_shift.test.py
documentation_of: polynomial/tayler_shift.py
layout: document
redirect_from:
- /library/polynomial/tayler_shift.py
- /library/polynomial/tayler_shift.py.html
title: polynomial/tayler_shift.py
---
