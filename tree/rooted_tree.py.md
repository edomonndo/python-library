---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: tree/count_stable_set.py
    title: "\u6728\u306E\u5B89\u5B9A\u96C6\u5408\u306E\u500B\u6570"
  - icon: ':warning:'
    path: tree/maximum_matching.py
    title: "\u6728\u306E\u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0"
  - icon: ':warning:'
    path: tree/maximum_stable_set.py
    title: "\u6728\u306E\u6700\u5927\u5B89\u5B9A\u96C6\u5408"
  - icon: ':warning:'
    path: tree/maximum_weighted_stable_set.py
    title: "\u6728\u306E\u91CD\u307F\u4ED8\u304D\u6700\u5927\u5B89\u5B9A\u96C6\u5408"
  - icon: ':warning:'
    path: tree/minimum_edge_cover.py
    title: "\u6728\u306E\u6700\u5C0F\u8FBA\u88AB\u8986"
  - icon: ':warning:'
    path: tree/minimum_vertex_cover.py
    title: "\u6728\u306E\u6700\u5C0F\u9802\u70B9\u88AB\u8986"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def rooted_tree(adj: list[list[int]], r: int = 0) -> tuple[list[list[int]],\
    \ list[int]]:\n    n = len(adj)\n    children = [[] for _ in range(n)]\n    parent\
    \ = [-1] * n\n    seen = [0] * n\n    seen[r] = 1\n    stack = [r]\n    while\
    \ stack:\n        v = stack.pop()\n        for u in adj[v]:\n            if not\
    \ seen[u]:\n                seen[u] = 1\n                children[v].append(u)\n\
    \                parent[u] = v\n                stack.append(u)\n    return children,\
    \ parent\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/rooted_tree.py
  requiredBy:
  - tree/count_stable_set.py
  - tree/maximum_stable_set.py
  - tree/minimum_edge_cover.py
  - tree/maximum_matching.py
  - tree/maximum_weighted_stable_set.py
  - tree/minimum_vertex_cover.py
  timestamp: '2024-04-30 11:25:39+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/rooted_tree.py
layout: document
title: "\u6839\u4ED8\u304D\u6728"
---

無向グラフから根を$r$としたときの根付き木を作成する．