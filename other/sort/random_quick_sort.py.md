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
  code: "from random import randrange\nimport sys\n\nsys.setrecursionlimit(1000000)\n\
    \n\ndef quick_sort(A: list[int]) -> list[int]:\n    n = len(A)\n    if n <= 1:\n\
    \        return A\n    x = randrange(0, n)\n    pivot = A[x]\n    L, R = [], []\n\
    \    for i, a in enumerate(A):\n        if i == x:\n            continue\n   \
    \     if a < pivot:\n            L.append(a)\n        elif a > pivot:\n      \
    \      R.append(a)\n        elif randrange(0, 2) == 1:\n            L.append(a)\n\
    \        else:\n            R.append(a)\n\n    return quick_sort(L) + pivot +\
    \ quick_sort(R)\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/random_quick_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/random_quick_sort.py
layout: document
title: "\u4E71\u629E\u30AF\u30A4\u30C3\u30AF\u30BD\u30FC\u30C8"
---