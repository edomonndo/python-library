---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/range_add_range_sum.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E\n\
    \nfrom graph.tree.heavy_light_decomposition import HLD\nfrom data_structure.fenwick_tree.range_add_range_sum\
    \ import RangeAddRangeSum\n\nn = int(input())\ng = [[] for _ in range(n)]\nfor\
    \ v in range(n):\n    k, *us = map(int, input().split())\n    for u in us:\n \
    \       g[v].append(u)\nhld = HLD(n, g, is_undirect=False)\nseg = RangeAddRangeSum([0]\
    \ * n)\nq = int(input())\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        v, w = qu\n        for l, r in hld.path_query(0, v, True):\n\
    \            seg.add(l, r, w)\n    else:\n        u = qu[0]\n        ans = 0\n\
    \        for l, r in hld.path_query(0, u, True):\n            ans += seg.sum(l,\
    \ r)\n        print(ans)\n"
  dependsOn:
  - graph/tree/heavy_light_decomposition.py
  - data_structure/fenwick_tree/range_add_range_sum.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
  requiredBy: []
  timestamp: '2024-09-03 08:35:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
layout: document
title: GRL5E Range Query on a Tree II
---

