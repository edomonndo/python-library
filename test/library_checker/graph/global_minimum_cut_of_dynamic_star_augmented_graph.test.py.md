---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  - icon: ':heavy_check_mark:'
    path: graph/extreme_vertex_set.py
    title: "\u6975\u70B9\u96C6\u5408"
  - icon: ':heavy_check_mark:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
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
    \ import extreme_vertex_set\nfrom graph.tree.heavy_light_decomposition import\
    \ HeavyLightDecomposition\nfrom data_structure.segtree.lazy_segment_tree import\
    \ LazySegtree\n\n\ndef mapping(x, f):\n    return x + f\n\n\ndef composition(f,\
    \ g):\n    return f + g\n\n\nn, m, q = map(int, input().split())\nA = [int(x)\
    \ for x in input().split()]\nedges = [tuple(map(int, input().split())) for _ in\
    \ range(m)]\n\nnew_edges = extreme_vertex_set(n, edges)\nsz = 2 * n - 1\nhld =\
    \ HeavyLightDecomposition(sz, new_edges, sz - 1, True)\nvs = [0] * sz\nfor i in\
    \ range(sz):\n    for v, ei in hld.adj[i]:\n        vs[hld.into[v]] = new_edges[ei][2]\n\
    inf = float(\"inf\")\nseg = LazySegtree(vs, min, inf, mapping, composition, 0)\n\
    \n\ndef update(v: int, cost: int):\n    # assert 0 <= v < n\n    hld.path_query(v,\
    \ sz - 1, (lambda l, r: seg.apply(l, r, cost - cur[v])))\n    cur[v] = cost\n\n\
    \ncur = [0] * n\nfor i in range(n):\n    update(i, A[i])\n\nfor _ in range(q):\n\
    \    x, y = map(int, input().split())\n    update(x, y)\n    print(seg.all_prod())\n"
  dependsOn:
  - graph/extreme_vertex_set.py
  - graph/tree/heavy_light_decomposition.py
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
  requiredBy: []
  timestamp: '2024-09-01 17:50:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
layout: document
title: Global Minimum Cut of Dynamic Star Augmented Graph
---

