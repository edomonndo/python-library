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
  code: "def bucket_sort(A: list[int], max_value: int) -> list[int]:\n    # asserr\
    \ len(A) == len(set(A))\n    n = len(A)\n    bin = [None] * (max_value + 1)\n\
    \    for a in A:\n        bin[a] = a\n    j = 0\n    for i in range(max_value\
    \ + 1):\n        if bin[i] is not None:\n            A[j] = bin[i]\n         \
    \   j += 1\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/bucket_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/bucket_sort.py
layout: document
title: "\u30D0\u30B1\u30C3\u30C8\u30BD\u30FC\u30C8"
---
