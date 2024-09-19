---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/enumerate_triangles.test.py
    title: Enumerate Triangles
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
    \ = 0\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/enumerate_triangles.py
  requiredBy: []
  timestamp: '2024-07-19 17:06:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/enumerate_triangles.test.py
documentation_of: graph/enumerate_triangles.py
layout: document
title: Enumerate Triangles
---
