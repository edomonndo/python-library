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
  code: "import sys\n\nsys.setrecursionlimit(1000000)\n\n\ndef merge_sort(A: list[int])\
    \ -> list[int]:\n    n = len(A)\n    if n <= 1:\n        return A\n    m = n >>\
    \ 1\n    L = merge_sort(A[:m])\n    R = merge_sort(A[m:])\n    res = []\n    i,\
    \ j = 0, 0\n    while i < len(L) and j < len(R):\n        if L[i] <= R[j]:\n \
    \           res.append(L[i])\n            i += 1\n        else:\n            res.append(R[j])\n\
    \            j += 1\n    if i < len(L):\n        res += L[i:]\n    if j < len(R):\n\
    \        res += R[j:]\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: sort/merge_sort.py
  requiredBy: []
  timestamp: '2024-06-13 11:50:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: sort/merge_sort.py
layout: document
title: "\u30DE\u30FC\u30B8\u30BD\u30FC\u30C8"
---
