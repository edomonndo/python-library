---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/low_link.py
    title: graph/low_link.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B\n\
    \nfrom graph.low_link import LowLink\n\nn, m = map(int, input().split())\ng =\
    \ [[] for _ in range(n)]\nfor _ in range(m):\n    u, v = map(int, input().split())\n\
    \    g[u].append(v)\n    g[v].append(u)\n\nL = LowLink(g)\nbridges = L.get_bridge()\n\
    for u, v in sorted(bridges):\n    print(u, v)\n"
  dependsOn:
  - graph/low_link.py
  isVerificationFile: true
  path: test/aoj/grl/grl_3_b_bridges.test.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_3_b_bridges.test.py
layout: document
title: "GRL3B \u6A4B"
---

