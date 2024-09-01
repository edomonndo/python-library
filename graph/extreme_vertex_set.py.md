---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
    title: Global Minimum Cut of Dynamic Star Augmented Graph
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph2.test.py
    title: Global Minimum Cut of Dynamic Star Augmented Graph
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import *\nfrom typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\
    \ndef extreme_vertex_set(\n    n: int, edges: list[tuple[int, int, T]]\n) -> list[tuple[int,\
    \ int, T]]:\n    # for u, v, w in edges:\n    #    assert 0 <= u < n\n    #  \
    \  assert 0 <= v < n\n    #    assert u != v\n    #    assert 0 <= w\n\n    res\
    \ = []\n    uf = list(range(n))\n    cur = [0] * (2 * n - 1)\n    leaf = [1] *\
    \ n + [0] * (n - 1)\n\n    pq = []\n    for t in range(n - 1):\n        g = [[]\
    \ for _ in range(2 * n - 1)]\n        cost = [0] * (2 * n - 1)\n        for i\
    \ in range(len(edges)):\n            u, v, w = edges[i]\n            u = uf[u]\n\
    \            v = uf[v]\n            if u != v:\n                cost[u] += w\n\
    \                cost[v] += w\n                g[u].append((v, w))\n         \
    \       g[v].append((u, w))\n        for i in range(2 * n - 1):\n            if\
    \ leaf[i]:\n                cur[i] = cost[i]\n                heappush(pq, (cost[i],\
    \ i))\n        x = y = -1\n        while pq:\n            _, v = heappop(pq)\n\
    \            if cur[v] == -1:\n                continue\n            cur[v] =\
    \ -1\n            x, y = v, x\n            for u, w in g[v]:\n               \
    \ if cur[u] != -1:\n                    cur[u] -= w\n                    heappush(pq,\
    \ (cur[u], u))\n        z = n + t\n        res += [(z, x, cost[x]), (z, y, cost[y])]\n\
    \        for i in range(n):\n            if uf[i] == x or uf[i] == y:\n      \
    \          uf[i] = z\n        leaf[x] = leaf[y] = 0\n        leaf[z] = 1\n   \
    \ return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/extreme_vertex_set.py
  requiredBy: []
  timestamp: '2024-08-27 13:47:08+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
  - test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph2.test.py
documentation_of: graph/extreme_vertex_set.py
layout: document
title: "\u6975\u70B9\u96C6\u5408"
---
