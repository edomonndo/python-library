---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/maxflow.py
    title: "\u6700\u5927\u30D5\u30ED\u30FC"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_7_A\n\
    \nfrom graph.maxflow import maxflow\n\nx, y, m = map(int, input().split())\nn\
    \ = x + y\ng = MaxFlow(n + 2)\nfor _ in range(m):\n    u, v = map(int, input().split())\n\
    \    g.add_edge(u, v + x, 1)\nfor i in range(n):\n    if i < x:\n        g.add_edge(n,\
    \ i, 1)\n    else:\n        g.add_edge(i, n + 1, 1)\n\nf = g.flow(n, n + 1)\n\
    print(f)\n"
  dependsOn:
  - graph/maxflow.py
  isVerificationFile: true
  path: test/aoj/grl/grl_7_a_bipartite_matching.test.py
  requiredBy: []
  timestamp: '2024-08-27 15:46:23+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl/grl_7_a_bipartite_matching.test.py
layout: document
title: "GRL7A 2\u90E8\u30DE\u30C3\u30C1\u30F3\u30B0"
---

