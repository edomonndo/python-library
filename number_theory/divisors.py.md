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
  code: "def make_divisors(n: int) -> list[int]:\n    lower_divisors, upper_divisors\
    \ = [], []\n    i = 1\n    while i * i <= n:\n        if n % i == 0:\n       \
    \     lower_divisors.append(i)\n            if i != n // i:\n                upper_divisors.append(n\
    \ // i)\n        i += 1\n    return lower_divisors + upper_divisors[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/divisors.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/divisors.py
layout: document
redirect_from:
- /library/number_theory/divisors.py
- /library/number_theory/divisors.py.html
title: number_theory/divisors.py
---
