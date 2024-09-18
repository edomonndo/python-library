---
data:
  _extendedDependsOn: []
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
    \nfrom data_structure.basic.unionfind import UnionFind\n\nN, M = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(M)]\nedges.sort(key=lambda\
    \ x: x[2])\nG = UnionFind(N)\nans = 0\nfor u, v, w in edges:\n    if G.same(u,\
    \ v):\n        continue\n    G.merge(u, v)\n    ans += w\n\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl/grl_2_a_minimum_spanning_tree_kruskal.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_2_a_minimum_spanning_tree_kruskal.test.py
layout: document
title: "GRL2A \u6700\u5C0F\u5168\u57DF\u6728\uFF08\u30AF\u30E9\u30B9\u30AB\u30EB\uFF09"
---

