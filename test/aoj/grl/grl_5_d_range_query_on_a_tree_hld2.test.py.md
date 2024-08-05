---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/hld_segtree.py
    title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u30BB\u30B0\u6728\uFF08\u53EF\u63DB\u30AF\
      \u30A8\u30EA\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D\n\
    \nfrom graph.tree.hld_segtree import HldSegTree\n\nn = int(input())\nedges = []\n\
    par = [-1] * n\nfor v in range(n):\n    k, *us = map(int, input().split())\n \
    \   for u in us:\n        edges.append((v, u))\n        par[u] = v\nseg = HldSegTree(lambda\
    \ x, y: x + y, 0, [0] * n, n, edges)\nq = int(input())\nfor _ in range(q):\n \
    \   t, *qu = map(int, input().split())\n    if t == 0:\n        v, w = qu\n  \
    \      seg.set(v, seg.get(v) + w)\n    else:\n        u = qu[0]\n        print(seg.path_prod(0,\
    \ u))\n"
  dependsOn:
  - graph/tree/hld_segtree.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
layout: document
title: GRL5D Range Query on a Tree
---

