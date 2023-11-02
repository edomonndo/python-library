---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_B\n\
    \nfrom graph.mincostflow import mcf_graph\n\nN, M, F = map(int, input().split())\n\
    G = mcf_graph(N)\nfor _ in range(M):\n    u, v, c, d = map(int, input().split())\n\
    \    G.add_edge(u, v, c, d)\n\nf, c = G.flow(0, N - 1, F)\nprint(c if f == F else\
    \ -1)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_6_b_min_cost_flow.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_6_b_min_cost_flow.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_6_b_min_cost_flow.test.py
- /verify/test/aoj/grl_6_b_min_cost_flow.test.py.html
title: test/aoj/grl_6_b_min_cost_flow.test.py
---
