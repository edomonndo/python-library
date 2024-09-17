---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/bipartite_edge_coloring.py
    title: graph/bipartite_edge_coloring.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bipartite_edge_coloring
    links:
    - https://judge.yosupo.jp/problem/bipartite_edge_coloring
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartite_edge_coloring



    from graph.bipartite_edge_coloring import *


    l, r, m = map(int, input().split())

    edges = [tuple(map(int, input().split())) for _ in range(m)]

    rg = RegularBipartiteGlaph(l, r, edges)

    bec = BipartiteEdgeColoring(rg)

    bec.solve()


    print(rg.k)

    print(*bec.color[:m], sep="\n")

    '
  dependsOn:
  - graph/bipartite_edge_coloring.py
  isVerificationFile: true
  path: test/library_checker/graph/bipartite_edge_coloring.test.py
  requiredBy: []
  timestamp: '2024-08-21 14:04:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/bipartite_edge_coloring.test.py
layout: document
title: Edge Coloring of Bipartite Graph
---

