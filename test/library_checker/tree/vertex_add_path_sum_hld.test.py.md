---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  - icon: ':question:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  - icon: ':heavy_check_mark:'
    path: graph/tree/template.py
    title: graph/tree/template.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_path_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_path_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum\n\
    \n\nfrom graph.tree.template import Tree\nfrom data_structure.fenwick_tree.fenwick_tree\
    \ import FenwickTree\nfrom graph.tree.heavy_light_decomposition import HeavyLightDecomposition\n\
    \nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\ng =\
    \ Tree.from_input(n, 0)\nhld = HeavyLightDecomposition(n, g)\nP = hld.build_list(A)\n\
    bit = FenwickTree(n)\nfor i, p in enumerate(P):\n    bit.add(i, p)\n\nfor _ in\
    \ range(q):\n    t, a, b = map(int, input().split())\n    if t == 0:\n       \
    \ bit.add(hld.index(a), b)\n    else:\n        ans = 0\n        for l, r in hld.path_query(a,\
    \ b, False):\n            ans += bit.sum(l, r)\n        print(ans)\n"
  dependsOn:
  - graph/tree/template.py
  - data_structure/fenwick_tree/fenwick_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_path_sum_hld.test.py
  requiredBy: []
  timestamp: '2024-09-02 11:05:26+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_path_sum_hld.test.py
layout: document
title: Vertex Add Path Sum (HLD)
---
