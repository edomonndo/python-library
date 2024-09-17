---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/maximum_independent_set.test.py
    title: Maximum Independent Set
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def maximum_independnet_set(\n    n: int, edges: list[tuple[int, int]]\n\
    ) -> tuple[int, list[int]]:\n    adj = [0] * n\n    for u, v in edges:\n     \
    \   if u > v:\n            u, v = v, u\n        adj[u] |= 1 << v\n\n    dp = {0:\
    \ 0}\n    for i in range(n):\n        nex = dict()\n        for S, val in dp.items():\n\
    \            if S >> i & 1 == 0:\n                S1 = S | adj[i]\n          \
    \      nv = (val + (1 << n)) | (1 << i)\n                if S1 in nex:\n     \
    \               if nex[S1] < nv:\n                        nex[S1] = nv\n     \
    \           else:\n                    nex[S1] = nv\n            S2 = S & ~(1\
    \ << i)\n            if S2 in nex:\n                if nex[S2] < val:\n      \
    \              nex[S2] = val\n            else:\n                nex[S2] = val\n\
    \        dp = nex\n\n    size, bitset = divmod(dp[0], 1 << n)\n    res = [i for\
    \ i in range(n) if bitset >> i & 1]\n    return size, res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/maximum_independent_set.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/maximum_independent_set.test.py
documentation_of: graph/maximum_independent_set.py
layout: document
redirect_from:
- /library/graph/maximum_independent_set.py
- /library/graph/maximum_independent_set.py.html
title: graph/maximum_independent_set.py
---
