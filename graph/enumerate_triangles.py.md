---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/enumerate_triangles.test.py
    title: Enumerate Triangles
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\n\ndef enumerate_triangles(\n\
    \    n: int,\n    edges: tuple[int, int],\n    calc: Callable[[T, T], T],\n  \
    \  merge: Callable[[T, T], T],\n    e: T = 0,\n) -> T:\n    adj = [[] for _ in\
    \ range(n)]\n    deg = [0] * n\n    for u, v in edges:\n        adj[u].append(v)\n\
    \        adj[v].append(u)\n        deg[u] += 1\n        deg[v] += 1\n\n    tmp\
    \ = [[] for _ in range(n)]\n    for u in range(n):\n        for v in adj[u]:\n\
    \            if deg[u] > deg[v] or (deg[u] == deg[v] and u > v):\n           \
    \     tmp[u].append(v)\n\n    used = [0] * n\n    res = e\n    for u in range(n):\n\
    \        for v in tmp[u]:\n            used[v] = 1\n        for v in tmp[u]:\n\
    \            for w in tmp[v]:\n                if used[w]:\n                 \
    \   res = merge(res, calc(u, v, w))\n        for v in tmp[u]:\n            used[v]\
    \ = 0\n    return res\n\n\nMOD = 998244353\n\n\ndef calc(u: int, v: int, w: int)\
    \ -> int:\n    return X[u] * X[v] % MOD * X[w] % MOD\n\n\ndef merge(x: int, y:\
    \ int) -> int:\n    return (x + y) % MOD\n\n\nn, m = map(int, input().split())\n\
    X = [int(x) for x in input().split()]\nedges = [tuple(map(int, input().split()))\
    \ for _ in range(m)]\nprint(enumerate_triangles(n, edges, calc, merge, 0))\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/enumerate_triangles.py
  requiredBy: []
  timestamp: '2024-07-19 16:23:17+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/enumerate_triangles.test.py
documentation_of: graph/enumerate_triangles.py
layout: document
redirect_from:
- /library/graph/enumerate_triangles.py
- /library/graph/enumerate_triangles.py.html
title: graph/enumerate_triangles.py
---
