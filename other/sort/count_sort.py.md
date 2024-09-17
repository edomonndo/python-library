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
  code: "def count_sort(A: list[int], max_value: int) -> list[int]:\n    cnt = [0]\
    \ * (max_value + 1)\n    n = len(A)\n    for a in A:\n        cnt[a] += 1\n  \
    \  for i in range(max_value):\n        cnt[i + 1] += cnt[i]\n    res = [None]\
    \ * n\n    for i in range(n - 1, -1, -1):\n        cnt[A[i]] -= 1\n        res[cnt[A[i]]]\
    \ = A[i]\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: other/sort/count_sort.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: other/sort/count_sort.py
layout: document
redirect_from:
- /library/other/sort/count_sort.py
- /library/other/sort/count_sort.py.html
title: other/sort/count_sort.py
---
