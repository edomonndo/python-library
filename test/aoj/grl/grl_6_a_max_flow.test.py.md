---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/maxflow.py
    title: "\u6700\u5927\u30D5\u30ED\u30FC"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A\n\
    \nfrom graph.maxflow import MaxFlow\n\nn, m = map(int, input().split())\ng = MaxFlow(n)\n\
    for _ in range(m):\n    u, v, c = map(int, input().split())\n    g.add_edge(u,\
    \ v, c)\n\nans = g.flow(0, n - 1)\nprint(ans)\n"
  dependsOn:
  - graph/maxflow.py
  isVerificationFile: true
  path: test/aoj/grl/grl_6_a_max_flow.test.py
  requiredBy: []
  timestamp: '2024-08-27 15:46:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_6_a_max_flow.test.py
layout: document
title: "GRL6A \u6700\u5927\u6D41"
---

