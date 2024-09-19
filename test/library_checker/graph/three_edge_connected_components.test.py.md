---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/three_edge_connected_components.py
    title: "\u4E09\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/three_edge_connected_components
    links:
    - https://judge.yosupo.jp/problem/three_edge_connected_components
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/three_edge_connected_components\n\
    \nfrom graph.three_edge_connected_components import three_edge_connected_components\n\
    \n\nn, m = map(int, input().split())\ng = [[] for _ in range(n)]\nfor _ in range(m):\n\
    \    u, v = map(int, input().split())\n    g[u].append(v)\n    g[v].append(u)\n\
    \ngroups = three_edge_connected_components(g)\nprint(len(groups))\nfor group in\
    \ groups:\n    print(len(group), *group)\n"
  dependsOn:
  - graph/three_edge_connected_components.py
  isVerificationFile: true
  path: test/library_checker/graph/three_edge_connected_components.test.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/three_edge_connected_components.test.py
layout: document
title: Three-Edge-Connected Components
---

