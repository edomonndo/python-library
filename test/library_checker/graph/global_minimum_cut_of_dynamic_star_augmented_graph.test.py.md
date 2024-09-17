---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: data_structure/segtree/lazy_segment_tree.py
  - icon: ':heavy_check_mark:'
    path: graph/extreme_vertex_set.py
    title: graph/extreme_vertex_set.py
  - icon: ':heavy_check_mark:'
    path: graph/tree/heavy_light_decomposition.py
    title: graph/tree/heavy_light_decomposition.py
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
    \ HLD\nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\n\n\n\
    def mapping(x, f):\n    return x + f\n\n\ndef composition(f, g):\n    return f\
    \ + g\n\n\nn, m, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\
    edges = [tuple(map(int, input().split())) for _ in range(m)]\n\ng = extreme_vertex_set(n,\
    \ edges)\nsz = 2 * n - 1\nhld = HLD(sz, g, root=sz - 1, has_weight=True, is_undirect=False)\n\
    vs = [0] * sz\nfor i in range(sz):\n    for v, w in hld.adj[i]:\n        vs[hld.into[v]]\
    \ = w\ninf = float(\"inf\")\nseg = LazySegtree(vs, min, inf, mapping, composition,\
    \ 0)\n\n\ndef update(v: int, cost: int):\n    # assert 0 <= v < n\n    hld.path_query(v,\
    \ sz - 1, (lambda l, r: seg.apply(l, r, cost - cur[v])))\n    cur[v] = cost\n\n\
    \ncur = [0] * n\nfor i in range(n):\n    for l, r in hld.path_query(i, sz - 1,\
    \ False):\n        seg.apply(l, r, A[i] - cur[i])\n    cur[i] = A[i]\n\nfor _\
    \ in range(q):\n    x, y = map(int, input().split())\n    for l, r in hld.path_query(x,\
    \ sz - 1, False):\n        seg.apply(l, r, y - cur[x])\n    cur[x] = y\n    print(seg.all_prod())\n"
  dependsOn:
  - graph/extreme_vertex_set.py
  - graph/tree/heavy_light_decomposition.py
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
  requiredBy: []
  timestamp: '2024-09-03 08:35:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
layout: document
title: Global Minimum Cut of Dynamic Star Augmented Graph
---

