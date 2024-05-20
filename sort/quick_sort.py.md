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
  code: "import sys\n\nsys.setrecursionlimit(1000000)\n\n\ndef quick_sort(A: list[int])\
    \ -> list[int]:\n    n = len(A)\n    if n <= 1:\n        return A\n    pivot =\
    \ A[n // 2]\n    L, M, R = [], [], []\n    for a in A:\n        if a < pivot:\n\
    \            L.append(a)\n        elif a == pivot:\n            M.append(a)\n\
    \        else:\n            R.append(a)\n    return quick_sort(L) + M + quick_sort(R)\n"
  dependsOn: []
  isVerificationFile: false
  path: sort/quick_sort.py
  requiredBy: []
  timestamp: '2024-05-20 15:28:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: sort/quick_sort.py
layout: document
redirect_from:
- /library/sort/quick_sort.py
- /library/sort/quick_sort.py.html
title: sort/quick_sort.py
---
