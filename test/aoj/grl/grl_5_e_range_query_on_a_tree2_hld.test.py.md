---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: data_structure/fenwick_tree/range_add_range_sum.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':x:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_E\n\
    \nfrom graph.tree.heavy_light_decomposition import HeavyLightDecomposition\nfrom\
    \ data_structure.fenwick_tree.range_add_range_sum import RangeAddRangeSum\n\n\n\
    def f(l, r):\n    seg.add(l, r, w)\n\n\ndef g(l, r):\n    global ans\n    ans\
    \ += seg.sum(l, r)\n\n\nn = int(input())\nedges = []\nfor v in range(n):\n   \
    \ k, *us = map(int, input().split())\n    for u in us:\n        edges.append((v,\
    \ u))\nT = HeavyLightDecomposition(n, edges)\nseg = RangeAddRangeSum([0] * n)\n\
    q = int(input())\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        v, w = qu\n        T.path_query(0, v, f)\n    else:\n\
    \        u = qu[0]\n        ans = 0\n        T.path_query(0, u, g)\n        print(ans)\n"
  dependsOn:
  - graph/tree/heavy_light_decomposition.py
  - data_structure/fenwick_tree/range_add_range_sum.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
- /verify/test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py.html
title: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
---