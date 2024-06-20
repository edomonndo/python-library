---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/topological_sort.py
    title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_4_A\n\
    \nfrom graph.topological_sort import topological_sort\n\nN, M = map(int, input().split())\n\
    G = [[] for _ in range(N)]\ndeg = [0] * N\nfor _ in range(M):\n    u, v = map(int,\
    \ input().split())\n    G[u].append(v)\n    deg[v] += 1\n\nans = topological_sort(G,\
    \ deg)\nprint(1 if ans == -1 else 0)\n"
  dependsOn:
  - graph/topological_sort.py
  isVerificationFile: true
  path: test/aoj/grl/grl_4_a_cycle_detection.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_4_a_cycle_detection.test.py
layout: document
title: "GRL4A \u6709\u5411\u30B0\u30E9\u30D5\u306E\u9589\u8DEF\u691C\u67FB"
---

