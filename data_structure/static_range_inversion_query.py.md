---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_inversion_query.test.py
    title: Static Range Inversion Query
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def StaticRangeInversionQuery(\n    A: list[int], queries: list[tuple[int,\
    \ int]]\n) -> list[int]:\n    n, q = len(A), len(queries)\n    # \u5EA7\u5727\n\
    \    dA = {a: i for i, a in enumerate(sorted(set(A)))}\n    A = [dA[a] for a in\
    \ A]\n\n    L, R = [0] * q, [0] * q\n    for i, (l, r) in enumerate(queries):\n\
    \        L[i], R[i] = l, r\n    d = int(n**0.5)\n    order = sorted(\n       \
    \ range(q),\n        key=lambda i: (\n            (L[i] // d) << 20 | R[i] if\
    \ (L[i] // d) & 1 else ((L[i] // d) << 20) - R[i]\n        ),\n    )\n\n    bit\
    \ = [0] * (n + 1)\n    l = r = score = 0\n    ans = [0] * q\n    for i in order:\n\
    \        # Add\n        while L[i] < l:\n            l -= 1\n            idx =\
    \ A[l] + 1\n            while idx <= n:\n                bit[idx] += 1\n     \
    \           idx += idx & -idx\n            idx = A[l]\n            while idx:\n\
    \                score += bit[idx]\n                idx -= idx & -idx\n      \
    \  while r < R[i]:\n            score += r - l\n            idx = A[r] + 1\n \
    \           while idx:\n                score -= bit[idx]\n                idx\
    \ -= idx & -idx\n            idx = A[r] + 1\n            while idx <= n:\n   \
    \             bit[idx] += 1\n                idx += idx & -idx\n            r\
    \ += 1\n        # Remove\n        while L[i] > l:\n            idx = A[l]\n  \
    \          while idx:\n                score -= bit[idx]\n                idx\
    \ -= idx & -idx\n            idx = A[l] + 1\n            while idx <= n:\n   \
    \             bit[idx] -= 1\n                idx += idx & -idx\n            l\
    \ += 1\n        while r > R[i]:\n            r -= 1\n            idx = A[r] +\
    \ 1\n            while idx <= n:\n                bit[idx] -= 1\n            \
    \    idx += idx & -idx\n            score -= r - l\n            idx = A[r] + 1\n\
    \            while idx:\n                score += bit[idx]\n                idx\
    \ -= idx & -idx\n        ans[i] = score\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/static_range_inversion_query.py
  requiredBy: []
  timestamp: '2024-05-28 15:29:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/static_range_inversion_query.test.py
documentation_of: data_structure/static_range_inversion_query.py
layout: document
redirect_from:
- /library/data_structure/static_range_inversion_query.py
- /library/data_structure/static_range_inversion_query.py.html
title: data_structure/static_range_inversion_query.py
---
