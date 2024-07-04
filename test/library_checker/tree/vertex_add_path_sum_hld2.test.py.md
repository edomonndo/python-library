---
data:
  _extendedDependsOn: []
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
    \nfrom graph.tree.hld_segtree import HldSegTree\n\n\nn, q = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\nedges = [tuple(map(int, input().split()))\
    \ for _ in range(n - 1)]\nseg = HldSegTree(lambda x, y: x + y, 0, A, n, edges,\
    \ 0)\n\nfor _ in range(q):\n    t, a, b = map(int, input().split())\n    if t\
    \ == 0:\n        seg.set(a, b + seg.get(a))\n    else:\n        print(seg.path_prod(a,\
    \ b))\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_path_sum_hld2.test.py
  requiredBy: []
  timestamp: '2024-07-02 12:00:00+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_path_sum_hld2.test.py
layout: document
title: Vertex Add Path Sum (HLD)
---