---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure_basic/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_A\n\
    \nfrom data_structure_basic.unionfind import UnionFind\n\nN, M = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(M)]\nedges.sort(key=lambda\
    \ x: x[2])\nG = UnionFind(N)\nans = 0\nfor u, v, w in edges:\n    if G.same(u,\
    \ v):\n        continue\n    G.merge(u, v)\n    ans += w\n\nprint(ans)\n"
  dependsOn:
  - data_structure_basic/unionfind.py
  isVerificationFile: true
  path: test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
  requiredBy: []
  timestamp: '2024-05-02 15:05:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
- /verify/test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py.html
title: test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
---
