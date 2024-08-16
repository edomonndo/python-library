---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/mincost_arborescence.py
    title: "\u6700\u5C0F\u5168\u57DF\u6709\u5411\u6728"
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
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_2_B


    from graph.mincost_arborescence import MinCostArborescence


    N, M, r = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(M)]

    MCA = MinCostArborescence(N, edges, r)

    print(MCA.calc_min_cost())

    '
  dependsOn:
  - graph/mincost_arborescence.py
  isVerificationFile: true
  path: test/aoj/grl/grl_2_b_minimum_cost_arborescence.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_2_b_minimum_cost_arborescence.test.py
layout: document
title: "GRL2B \u6700\u5C0F\u5168\u57DF\u6709\u5411\u6728"
---
