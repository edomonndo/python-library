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
  code: "def insert_sort(A: list[int]) -> list[int]:\n    n = len(A)\n    for i in\
    \ range(1, n):\n        tmp = A[i]\n        j = i - 1\n        while j >= 0 and\
    \ A[j] > tmp:\n            A[j + 1] = A[j]\n            j -= 1\n        A[j +\
    \ 1] = tmp\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/insert_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/insert_sort.py
layout: document
title: "\u633F\u5165\u30BD\u30FC\u30C8"
---