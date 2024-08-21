---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: graph/bipartite_edge_coloring.py
    title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u306E\u8FBA\u5F69\u8272"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/bipartitematching.test.py
    title: Matching on Bipartite Graph
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import shuffle\n\n\ndef bipartite_matching(\n    n: int, m: int,\
    \ edges: list[tuple[int, int]]\n) -> list[tuple[int, int]]:\n\n    shuffle(edges)\n\
    \n    adj = [[] for _ in range(n)]\n    for u, v in edges:\n        adj[u].append(v)\n\
    \n    prev = [-1] * n\n    root = [-1] * n\n    p = [-1] * n\n    q = [-1] * m\n\
    \    updated = True\n    while updated:\n        updated = False\n        s =\
    \ []\n        for v in range(n):\n            if p[v] == -1:\n               \
    \ root[v] = v\n                s.append(v)\n        i = 0\n        while i < len(s):\n\
    \            v = s[i]\n            i += 1\n            if p[root[v]] != -1:\n\
    \                continue\n            for u in adj[v]:\n                if q[u]\
    \ == -1:\n                    while u != -1:\n                        q[u] = v\n\
    \                        p[v], u = u, p[v]\n                        v = prev[v]\n\
    \                    updated = True\n                    break\n             \
    \   u = q[u]\n                if prev[u] != -1:\n                    continue\n\
    \                prev[u] = v\n                root[u] = root[v]\n            \
    \    s.append(u)\n        if updated:\n            for v in range(n):\n      \
    \          prev[v] = -1\n                root[v] = -1\n    return p, q\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/bipartite_matching.py
  requiredBy:
  - graph/bipartite_edge_coloring.py
  timestamp: '2024-08-21 11:11:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/bipartitematching.test.py
documentation_of: graph/bipartite_matching.py
layout: document
title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u30DE\u30C3\u30C1\u30F3\u30B0"
---
