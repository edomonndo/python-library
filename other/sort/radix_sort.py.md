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
  code: "def radix_sort(A: list[int], max_value: int) -> list[int]:\n    n = len(A)\n\
    \    mask = 0xFF\n    tmp = [None] * n\n    for bit in range(0, 32, 8):\n    \
    \    cnt = [0] * (max_value + 1)\n        for i in range(n):\n            cnt[A[i]\
    \ >> bit & mask] += 1\n        for i in range(max_value):\n            cnt[i +\
    \ 1] += cnt[i]\n        for i in range(n - 1, -1, -1):\n            j = A[i] >>\
    \ bit & mask\n            cnt[j] -= 1\n            tmp[cnt[j]] = A[i]\n      \
    \  for i in range(n):\n            A[i] = tmp[i]\n    return A\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/radix_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/radix_sort.py
layout: document
redirect_from:
- /library/other/sort/radix_sort.py
- /library/other/sort/radix_sort.py.html
title: other/sort/radix_sort.py
---
