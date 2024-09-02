---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  - icon: ':question:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D\n\
    \nfrom data_structure.fenwick_tree.fenwick_tree import FenwickTree\nfrom graph.tree.heavy_light_decomposition\
    \ import HLD\n\nn = int(input())\ng = [[] for _ in range(n)]\npar = [-1] * n\n\
    for v in range(n):\n    k, *us = map(int, input().split())\n    for u in us:\n\
    \        g[v].append(u)\n        par[u] = v\nhld = HLD(n, g, is_undirect=False)\n\
    bit = FenwickTree(n)\nq = int(input())\nfor _ in range(q):\n    t, *qu = map(int,\
    \ input().split())\n    if t == 0:\n        v, w = qu\n        for l, r in hld.path_query(par[v],\
    \ v, True):\n            bit.add(l, w)\n    else:\n        u = qu[0]\n       \
    \ ans = 0\n        for l, r in hld.path_query(0, u, True):\n            ans +=\
    \ bit.sum(l, r)\n        print(ans)\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld.test.py
  requiredBy: []
  timestamp: '2024-09-03 08:35:19+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld.test.py
layout: document
title: GRL5D Range Query on a Tree
---

