---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  - icon: ':question:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  - icon: ':question:'
    path: graph/tree/template.py
    title: graph/tree/template.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/past202010-open/tasks/past202010_m
    links:
    - https://atcoder.jp/contests/past202010-open/tasks/past202010_m
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/past202010-open/tasks/past202010_m\n\
    \nfrom graph.tree.template import Tree\nfrom graph.tree.heavy_light_decomposition\
    \ import HeavyLightDecomposition\nfrom data_structure.segtree.lazy_segment_tree\
    \ import LazySegtree\n\n\nn, q = map(int, input().split())\nedges = [tuple(map(lambda\
    \ x: int(x) - 1, input().split())) for _ in range(n - 1)]\ng = [[] for _ in range(n)]\n\
    for u, v in edges:\n    g[u].append(v)\n    g[v].append(u)\nhld = HeavyLightDecomposition(n,\
    \ g)\n\ninf = float(\"inf\")\nmapping = lambda f, x: x if f == ID else f\ncomposition\
    \ = lambda f, g: g if f == ID else f\nID = inf\nseg = LazySegtree([0] * n, min,\
    \ inf, mapping, composition, ID)\n\nfor _ in range(q):\n    u, v, c = map(int,\
    \ input().split())\n    u -= 1\n    v -= 1\n    for l, r in hld.path_query(u,\
    \ v, True):\n        seg.apply(l, r, c)\n\n\nfor u, v in edges:\n    ans = None\n\
    \    for l, r in hld.path_query(u, v, True):\n        ans = seg.prod(l, r)\n \
    \   print(ans)\n"
  dependsOn:
  - graph/tree/template.py
  - graph/tree/heavy_light_decomposition.py
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/atcoder/past/past4m_hld.test.py
  requiredBy: []
  timestamp: '2024-09-02 08:53:18+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/atcoder/past/past4m_hld.test.py
layout: document
title: "M - \u7B46\u5857\u308A"
---
