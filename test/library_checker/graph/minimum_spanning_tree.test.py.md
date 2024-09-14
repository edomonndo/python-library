---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/minimum_spanning_tree
    links:
    - https://judge.yosupo.jp/problem/minimum_spanning_tree
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/minimum_spanning_tree\n\
    \nfrom graph.connectivity.unionfind import UnionFind\n\nn, m = map(int, input().split())\n\
    edges = []\nfor i in range(m):\n    u, v, w = map(int, input().split())\n    edges.append((u,\
    \ v, w, i))\n\nedges.sort(key=lambda x: x[2])\nuf = UnionFind(n)\n\nX = 0\nes\
    \ = []\nfor u, v, w, i in edges:\n    if uf.same(u, v):\n        continue\n  \
    \  uf.merge(u, v)\n    X += w\n    es.append(i)\n\nes.sort()\nprint(X)\nprint(*es)\n"
  dependsOn:
  - graph/connectivity/unionfind.py
  isVerificationFile: true
  path: test/library_checker/graph/minimum_spanning_tree.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/minimum_spanning_tree.test.py
layout: document
title: Minimum Spanning Tree
---

