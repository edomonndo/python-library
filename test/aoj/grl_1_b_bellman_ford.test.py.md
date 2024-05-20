---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/bellman_ford.py
    title: "\u30D9\u30EB\u30DE\u30F3\u30D5\u30A9\u30FC\u30C9"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B\n\
    \nfrom graph.bellman_ford import BellmanFord\n\ninf = float(\"inf\")\nn, m, r\
    \ = map(int, input().split())\ng = BellmanFord(n)\nfor _ in range(m):\n    u,\
    \ v, w = map(int, input().split())\n    g.add_edge(u, v, w)\n\ndist = g.solve_sssp(r)\n\
    if dist == -1:\n    print(\"NEGATIVE CYCLE\")\n    exit()\n\nfor d in dist:\n\
    \    if d == inf:\n        print(\"INF\")\n    else:\n        print(d)\n"
  dependsOn:
  - graph/bellman_ford.py
  isVerificationFile: true
  path: test/aoj/grl_1_b_bellman_ford.test.py
  requiredBy: []
  timestamp: '2024-04-19 07:43:56+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_1_b_bellman_ford.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_1_b_bellman_ford.test.py
- /verify/test/aoj/grl_1_b_bellman_ford.test.py.html
title: test/aoj/grl_1_b_bellman_ford.test.py
---
