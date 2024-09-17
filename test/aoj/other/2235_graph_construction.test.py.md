---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/dynamic_connectivity.py
    title: graph/connectivity/dynamic_connectivity.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2235
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2235
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2235\n\
    \nfrom graph.connectivity.dynamic_connectivity import DynamicConnectivity\n\n\
    n, q = map(int, input().split())\ndc = DynamicConnectivity(n, lambda _, __: 0,\
    \ 0)\nfor _ in range(q):\n    t, u, v = map(int, input().split())\n    if t ==\
    \ 1:\n        dc.link(u, v)\n    elif t == 2:\n        dc.cut(u, v)\n    else:\n\
    \        print(\"YES\" if dc.same(u, v) else \"NO\")\n"
  dependsOn:
  - graph/connectivity/dynamic_connectivity.py
  isVerificationFile: true
  path: test/aoj/other/2235_graph_construction.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/other/2235_graph_construction.test.py
layout: document
title: 2235 Graph Construction
---

