---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_5_B\n\
    \nfrom graph.tree.tree_dp import TreeDp\n\nN = int(input())\nG = [[] for _ in\
    \ range(N)]\nW = dict()\nfor _ in range(N - 1):\n    u, v, w = map(int, input().split())\n\
    \    G[u].append(v)\n    G[v].append(u)\n    W[(u, v)] = w\n    W[(v, u)] = w\n\
    \nTDP = TreeDp(N, G)\ne = 0\nmerge = lambda a, b: max(a, b)\nadj_bu = lambda a,\
    \ v, p: a + W[(v, p)]\nadj_td = lambda a, v, p: a + W[(v, p)]\nadj_fin = lambda\
    \ a, v: a\n\nres = TDP.rerooting(e, merge, adj_bu, adj_td, adj_fin)\nprint(*res,\
    \ sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl/grl_5_b_tree_height.test.py
  requiredBy: []
  timestamp: '2024-06-20 09:29:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_b_tree_height.test.py
layout: document
title: "GRL5B \u6728\u306E\u9AD8\u3055"
---

