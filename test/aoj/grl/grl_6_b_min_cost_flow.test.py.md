---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/mincostflow.py
    title: graph/mincostflow.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B\n\
    \nfrom graph.mincostflow import MinCostFlow\n\nn, m, limit = map(int, input().split())\n\
    g = MinCostFlow(n)\nfor _ in range(m):\n    u, v, c, d = map(int, input().split())\n\
    \    g.add_edge(u, v, c, d)\n\nf, c = g.flow(0, n - 1, limit)\nprint(c if f ==\
    \ limit else -1)\n"
  dependsOn:
  - graph/mincostflow.py
  isVerificationFile: true
  path: test/aoj/grl/grl_6_b_min_cost_flow.test.py
  requiredBy: []
  timestamp: '2024-08-27 15:46:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_6_b_min_cost_flow.test.py
layout: document
title: "GRL6B \u6700\u5C0F\u8CBB\u7528\u6D41"
---

