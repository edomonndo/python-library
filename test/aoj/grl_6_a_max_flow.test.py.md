---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_6_A\n\
    \nfrom graph.maxflow import mf_graph\n\nN, M = map(int, input().split())\nG =\
    \ mf_graph(N)\nfor _ in range(M):\n    u, v, c = map(int, input().split())\n \
    \   G.add_edge(u, v, c)\n\nans = G.flow(0, N - 1)\nprint(ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_6_a_max_flow.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_6_a_max_flow.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_6_a_max_flow.test.py
- /verify/test/aoj/grl_6_a_max_flow.test.py.html
title: test/aoj/grl_6_a_max_flow.test.py
---
