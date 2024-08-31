---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/extreme_vertex_set.py
    title: "\u6975\u70B9\u96C6\u5408"
  - icon: ':heavy_check_mark:'
    path: graph/tree/hld_lazysegtree.py
    title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u9045\u5EF6\u30BB\u30B0\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/global_minimum_cut_of_dynamic_star_augmented_graph
    links:
    - https://judge.yosupo.jp/problem/global_minimum_cut_of_dynamic_star_augmented_graph
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/global_minimum_cut_of_dynamic_star_augmented_graph\n\
    \n\nimport sys\n\ninput = sys.stdin.readline\n\nfrom graph.extreme_vertex_set\
    \ import extreme_vertex_set\nfrom graph.tree.hld_lazysegtree import HldLazySegTree\n\
    \n\ndef mapping(x, f):\n    return x + f\n\n\ndef composition(f, g):\n    return\
    \ f + g\n\n\nn, m, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\
    edges = [tuple(map(int, input().split())) for _ in range(m)]\n\nnew_edges = extreme_vertex_set(n,\
    \ edges)\nsz = 2 * n - 1\ninf = float(\"inf\")\nseg = HldLazySegTree(\n    min,\
    \ inf, mapping, composition, 0, [0] * sz, sz, new_edges, sz - 1, True\n)\nfor\
    \ u, v, w in new_edges:\n    seg.path_apply(u, v, w, True)\n\ncur = [0] * n\n\
    for i in range(n):\n    seg.path_apply(i, sz - 1, A[i] - cur[i], False)\n    cur[i]\
    \ = A[i]\n\nfor _ in range(q):\n    x, y = map(int, input().split())\n    seg.path_apply(x,\
    \ sz - 1, y - cur[x], False)\n    cur[x] = y\n    print(seg.all_prod())\n"
  dependsOn:
  - graph/extreme_vertex_set.py
  - graph/tree/hld_lazysegtree.py
  isVerificationFile: true
  path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph2.test.py
  requiredBy: []
  timestamp: '2024-09-01 02:12:38+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph2.test.py
layout: document
title: Global Minimum Cut of Dynamic Star Augmented Graph
---

