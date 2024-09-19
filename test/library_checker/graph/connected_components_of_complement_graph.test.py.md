---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connected_components_complement.py
    title: "\u88DC\u30B0\u30E9\u30D5\u306E\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/connected_components_of_complement_graph
    links:
    - https://judge.yosupo.jp/problem/connected_components_of_complement_graph
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/connected_components_of_complement_graph\n\
    \nfrom graph.connected_components_complement import get_ccc\n\nn, m = map(int,\
    \ input().split())\ng = [[] for _ in range(n)]\nfor _ in range(m):\n    u, v =\
    \ map(int, input().split())\n    g[u].append(v)\n    g[v].append(u)\n\ncc = get_ccc(g)\n\
    print(len(cc))\nfor group in cc:\n    print(len(group), *group)\n"
  dependsOn:
  - graph/connected_components_complement.py
  isVerificationFile: true
  path: test/library_checker/graph/connected_components_of_complement_graph.test.py
  requiredBy: []
  timestamp: '2024-08-02 11:42:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/connected_components_of_complement_graph.test.py
layout: document
title: Connected Components of Complement Graph
---

