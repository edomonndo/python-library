---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/mincostflow.py
    title: "\u6700\u5C0F\u30B3\u30B9\u30C8\u30D5\u30ED\u30FC"
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
    \nfrom graph.mincostflow import mcf_graph\n\nN, M, F = map(int, input().split())\n\
    G = mcf_graph(N)\nfor _ in range(M):\n    u, v, c, d = map(int, input().split())\n\
    \    G.add_edge(u, v, c, d)\n\nf, c = G.flow(0, N - 1, F)\nprint(c if f == F else\
    \ -1)\n"
  dependsOn:
  - graph/mincostflow.py
  isVerificationFile: true
  path: test/aoj/grl/grl_6_b_min_cost_flow.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_6_b_min_cost_flow.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_6_b_min_cost_flow.test.py
- /verify/test/aoj/grl/grl_6_b_min_cost_flow.test.py.html
title: test/aoj/grl/grl_6_b_min_cost_flow.test.py
---
