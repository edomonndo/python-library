---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/maxflow.py
    title: "\u6700\u5927\u30D5\u30ED\u30FC"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A\n\
    \nfrom graph.maxflow import mf_graph\n\nX, Y, M = map(int, input().split())\n\
    N = X + Y\nG = mf_graph(N + 2)\nfor _ in range(M):\n    x, y = map(int, input().split())\n\
    \    G.add_edge(x, y + X, 1)\nfor i in range(N):\n    if i < X:\n        G.add_edge(N,\
    \ i, 1)\n    else:\n        G.add_edge(i, N + 1, 1)\n\nf = G.flow(N, N + 1)\n\
    print(f)\n"
  dependsOn:
  - graph/maxflow.py
  isVerificationFile: true
  path: test/aoj/grl_7_a_bipartite_matching.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_7_a_bipartite_matching.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_7_a_bipartite_matching.test.py
- /verify/test/aoj/grl_7_a_bipartite_matching.test.py.html
title: test/aoj/grl_7_a_bipartite_matching.test.py
---
