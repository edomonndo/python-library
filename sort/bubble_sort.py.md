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
  code: "def bubble_sort(A: list[int]) -> list[int]:\n    n = len(A)\n    ok = False\n\
    \    for i in range(n):\n        if ok:\n            break\n        ok = True\n\
    \        for j in range(n - i - 1):\n            if A[j] < A[j + 1]:\n       \
    \         A[j], A[j + 1] = A[j + 1], A[j]\n                ok = False\n    return\
    \ A\n"
  dependsOn: []
  isVerificationFile: false
  path: sort/bubble_sort.py
  requiredBy: []
  timestamp: '2024-05-20 15:28:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: sort/bubble_sort.py
layout: document
title: "\u30D0\u30D6\u30EB\u30BD\u30FC\u30C8"
---
