---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: tree/hld_segtree.py
    title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u30BB\u30B0\u6728\uFF08\u53EF\u63DB\u30AF\
      \u30A8\u30EA\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_add_subtree_sum
    links:
    - https://judge.yosupo.jp/problem/vertex_add_subtree_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum\n\
    \nfrom tree.hld_segtree import HldSegtree\n\nn, q = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\nP = [int(x) for x in input().split()]\n\
    edges = []\nfor i, p in enumerate(P, 1):\n    edges.append((i, p))\n\nseg = HldSegtree(lambda\
    \ x, y: x + y, 0, A, n, edges, 0)\n\nfor _ in range(q):\n    t, *a = map(int,\
    \ input().split())\n    if t == 0:\n        v, x = a\n        seg.set(v, x)\n\
    \    else:\n        print(seg.subtree_prod(a[0]))\n"
  dependsOn:
  - tree/hld_segtree.py
  isVerificationFile: true
  path: test/library_checker/tree/vertex_add_subtree_sum_hld2.test.py
  requiredBy: []
  timestamp: '2024-07-02 08:45:17+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/tree/vertex_add_subtree_sum_hld2.test.py
layout: document
title: Vertex Add Subtree Sum (HLD)
---
