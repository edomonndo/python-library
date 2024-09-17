---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: data_structure/fenwick_tree/fenwick_tree.py
  - icon: ':heavy_check_mark:'
    path: graph/tree/heavy_light_decomposition.py
    title: graph/tree/heavy_light_decomposition.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    \nfrom data_structure.fenwick_tree.fenwick_tree import FenwickTree\nfrom graph.tree.heavy_light_decomposition\
    \ import HLD\n\nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\
    P = [int(x) for x in input().split()]\ng = [[] for _ in range(n)]\nfor i, p in\
    \ enumerate(P, 1):\n    g[p].append(i)\nhld = HLD(n, g, is_undirect=False)\nL\
    \ = hld.build_list(A)\nbit = FenwickTree(n)\nfor i, p in enumerate(L):\n    bit.add(i,\
    \ p)\n\nfor _ in range(q):\n    t, *a = map(int, input().split())\n    if t ==\
    \ 0:\n        v, x = a\n        bit.add(hld.index(v), x)\n    else:\n        l,\
    \ r = hld.subtree_query(a[0])\n        print(bit.sum(l, r))\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
  requiredBy: []
  timestamp: '2024-09-03 08:35:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
layout: document
title: Vertex Add Subtree Sum (HLD)
---
