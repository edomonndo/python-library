---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_a_diameter.test.py
    title: test/aoj/grl/grl_5_a_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/tree_diameter.test.py
    title: test/library_checker/tree/tree_diameter.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def diameter(N: int, G: list[list[tuple[int, int]]], get_path: bool = False):\n\
    \    def dfs(start: int):\n        dist = [-1 for _ in range(N)]\n        dist[start]\
    \ = 0\n        stack = [start]\n        while stack:\n            v = stack.pop()\n\
    \            for u, d in G[v]:\n                if dist[u] != -1:\n          \
    \          continue\n                dist[u] = dist[v] + d\n                stack.append(u)\n\
    \        max_v = -1\n        max_d = -1\n        for v, d in enumerate(dist):\n\
    \            if d > max_d:\n                max_d = d\n                max_v =\
    \ v\n        return max_v, dist\n\n    s, _ = dfs(0)\n    v, dist = dfs(s)\n \
    \   diam = dist[v]\n    if not get_path:\n        return diam\n    path = [v]\n\
    \    while v != s:\n        for u, d in G[v]:\n            if dist[u] + d == dist[v]:\n\
    \                path.append(u)\n                v = u\n                break\n\
    \    return diam, path\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/diameter.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/tree/tree_diameter.test.py
  - test/aoj/grl/grl_5_a_diameter.test.py
documentation_of: tree/diameter.py
layout: document
title: "\u6728\u306E\u76F4\u5F84"
---

木を２回dfsすることで木の直径を求める．返り値はタプルで，`(直径，直径を通るパス)`となっている．