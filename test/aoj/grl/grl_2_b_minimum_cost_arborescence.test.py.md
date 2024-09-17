---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/directed_mst.py
    title: graph/directed_mst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_B\n\
    \nfrom graph.directed_mst import directed_mst\n\nn, m, r = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(m)]\neis = directed_mst(n,\
    \ edges, r)\nans = 0\nfor ei in eis:\n    ans += edges[ei][2]\nprint(ans)\n"
  dependsOn:
  - graph/directed_mst.py
  isVerificationFile: true
  path: test/aoj/grl/grl_2_b_minimum_cost_arborescence.test.py
  requiredBy: []
  timestamp: '2024-08-26 12:24:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_2_b_minimum_cost_arborescence.test.py
layout: document
title: "GRL2B \u6700\u5C0F\u5168\u57DF\u6709\u5411\u6728"
---

