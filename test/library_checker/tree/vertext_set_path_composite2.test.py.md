---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/tree/hld_segtree_noncommutative.py
    title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u30BB\u30B0\u6728\uFF08\u975E\u53EF\u63DB\
      \u30D1\u30B9\u30AF\u30A8\u30EA\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/vertex_set_path_composite
    links:
    - https://judge.yosupo.jp/problem/vertex_set_path_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite\n\
    \nfrom graph.tree.hld_segtree_noncommutative import HldSegTree\n\nMOD = 998244353\n\
    msk = (1 << 32) - 1\n\n\ndef op(x, y):\n    x1, x2 = x >> 32, x & msk\n    y1,\
    \ y2 = y >> 32, y & msk\n    z1 = x1 * y1 % MOD\n    z2 = (x2 * y1 % MOD + y2)\
    \ % MOD\n    return (z1 << 32) + z2\n\n\nn, q = map(int, input().split())\nA =\
    \ [0] * n\nB = [0] * n\nfor i in range(n):\n    A[i], B[i] = map(int, input().split())\n\
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]\nV = [None] *\
    \ n\nfor i, (a, b) in enumerate(zip(A, B)):\n    V[i] = (a << 32) + b\n\nseg =\
    \ HldSegTree(op, 1 << 32, V, n, edges, 0)\nfor _ in range(q):\n    t, a, b, c\
    \ = map(int, input().split())\n    if t == 0:\n        seg.set(a, (b << 32) +\
    \ c)\n    else:\n        res = seg.prod(a, b)\n        a, b = res >> 32, res &\
    \ msk\n        print((a * c + b) % MOD)\n"
  dependsOn:
  - graph/tree/hld_segtree_noncommutative.py
  isVerificationFile: true
  path: test/library_checker/tree/vertext_set_path_composite2.test.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertext_set_path_composite2.test.py
layout: document
title: Vertex Set Path Composite
---