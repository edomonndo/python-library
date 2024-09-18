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
  code: "def tim_sort(A: list[int]) -> list[int]:\n    def insert_sort(A: list[int],\
    \ l: int = 0, r: int = None):\n        if r is None:\n            r = len(A)\n\
    \        for i in range(l + 1, r):\n            tmp = A[i]\n            j = i\
    \ - 1\n            while j >= 0 and A[j] > tmp:\n                A[j + 1] = A[j]\n\
    \                j -= 1\n            A[j + 1] = tmp\n        return\n\n    def\
    \ merge_sort(A: list[int], l: int, m: int, r: int):\n        L, R = A[l : m +\
    \ 1], A[m + 1 : r + 1]\n        L.reverse()\n        R.reverse()\n        for\
    \ i in range(l, r + 1):\n            if len(L) == 0:\n                A[i] = R.pop()\n\
    \            elif len(R) == 0:\n                A[i] = L.pop()\n            elif\
    \ L[-1] <= R[-1]:\n                A[i] = L.pop()\n            else:\n       \
    \         A[i] = R.pop()\n\n    n = len(A)\n    if n < 64:\n        insert_sort(A)\n\
    \        return A\n    bucket_size = 64\n    for l in range(0, n, bucket_size):\n\
    \        r = min(l + bucket_size, n)\n        insert_sort(A, l, r)\n    size =\
    \ 64\n    while size < n:\n        for l in range(0, n, 2 * size):\n         \
    \   m = min(n - 1, l + size - 1)\n            r = min(n - 1, l + 2 * size - 1)\n\
    \            merge_sort(A, l, m, r)\n        size *= 2\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/tim_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/tim_sort.py
layout: document
title: "Tim\u30BD\u30FC\u30C8"
---
