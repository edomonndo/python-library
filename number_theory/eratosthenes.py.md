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
  code: "def eratosthenes(N: int) -> list[bool]:\n    isprime = [True] * (N + 1)\n\
    \n    isprime[0], isprime[1] = False, False\n\n    for p in range(2, N + 1):\n\
    \        if not isprime[p]:\n            continue\n\n        q = p * 2\n     \
    \   while q <= N:\n            isprime[q] = False\n            q += p\n\n    return\
    \ isprime\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/eratosthenes.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/eratosthenes.py
layout: document
redirect_from:
- /library/number_theory/eratosthenes.py
- /library/number_theory/eratosthenes.py.html
title: number_theory/eratosthenes.py
---
