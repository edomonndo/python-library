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
  code: "from heapq import *\n\n\ndef heap_sort(A: list[int]) -> list[int]:\n    pq\
    \ = heapify(A[:])\n    n = len(A)\n    return [heappop(pq) for _ in range(n)]\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/heap_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/heap_sort.py
layout: document
redirect_from:
- /library/other/sort/heap_sort.py
- /library/other/sort/heap_sort.py.html
title: other/sort/heap_sort.py
---
