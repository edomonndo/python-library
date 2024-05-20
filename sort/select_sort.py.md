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
  code: "def select_sort(A: list[int]) -> list[int]:\n    n = len(A)\n    for i in\
    \ range(n):\n        k = i\n        for j in range(i + 1, n):\n            if\
    \ A[j] < A[k]:\n                k = j\n        A[i], A[k] = A[k], A[i]\n    return\
    \ A\n"
  dependsOn: []
  isVerificationFile: false
  path: sort/select_sort.py
  requiredBy: []
  timestamp: '2024-05-20 15:28:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: sort/select_sort.py
layout: document
redirect_from:
- /library/sort/select_sort.py
- /library/sort/select_sort.py.html
title: sort/select_sort.py
---
