---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/eulerian_trail.py
    title: "\u30AA\u30A4\u30E9\u30FC\u8DEF"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/eulerian_trail_undirected
    links:
    - https://judge.yosupo.jp/problem/eulerian_trail_undirected
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/eulerian_trail_undirected\n\
    \nfrom graph.eulerian_trail import EulerianTrail\n\n\nT = int(input())\nfor _\
    \ in range(T):\n    n, m = map(int, input().split())\n    edges = [tuple(map(int,\
    \ input().split())) for _ in range(m)]\n    g = EulerianTrail(n, edges, True)\n\
    \    start, eids = g.get_edge_order()\n    if start == -1:\n        print(\"No\"\
    )\n    else:\n        print(\"Yes\")\n        path = g.get_verticle_order(start,\
    \ eids)\n        print(*path)\n        print(*eids)\n"
  dependsOn:
  - graph/eulerian_trail.py
  isVerificationFile: true
  path: test/library_checker/graph/eulerian_trail_undirected.test.py
  requiredBy: []
  timestamp: '2024-07-19 12:35:18+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/graph/eulerian_trail_undirected.test.py
layout: document
title: Eulerian Trail (Undirected)
---

