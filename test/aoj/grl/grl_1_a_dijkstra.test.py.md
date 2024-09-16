---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/dijkstra.py
    title: "Dijkstra\uFF08\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A\n\
    \nfrom graph.dijkstra import dijkstra\n\nINF = float(\"inf\")\nN, M, r = map(int,\
    \ input().split())\nG = [[] for _ in range(N)]\nfor _ in range(M):\n    u, v,\
    \ w = map(int, input().split())\n    G[u].append((w, v))\n\ndist, _ = dijkstra(G,\
    \ r)\nfor i in range(N):\n    print(dist[i] if dist[i] != INF else \"INF\")\n"
  dependsOn:
  - graph/dijkstra.py
  isVerificationFile: true
  path: test/aoj/grl/grl_1_a_dijkstra.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_1_a_dijkstra.test.py
layout: document
title: "GRL1A \u5358\u4E00\u59CB\u70B9\u6700\u77ED\u7D4C\u8DEF"
---
