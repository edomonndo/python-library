---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  - icon: ':heavy_check_mark:'
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
    PROBLEM: https://judge.yosupo.jp/problem/vertex_set_path_composite
    links:
    - https://judge.yosupo.jp/problem/vertex_set_path_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite\n\
    \nfrom graph.tree.template import Tree\nfrom data_structure.segtree.segment_tree\
    \ import Segtree\nfrom graph.tree.heavy_light_decomposition import HeavyLightDecomposition\n\
    \nMOD = 998244353\nmsk = (1 << 32) - 1\n\n\ndef op1(x, y):\n    x1, x2 = x >>\
    \ 32, x & msk\n    y1, y2 = y >> 32, y & msk\n    z1 = x1 * y1 % MOD\n    z2 =\
    \ (x2 * y1 % MOD + y2) % MOD\n    return (z1 << 32) + z2\n\n\ndef op2(x, y):\n\
    \    return op1(y, x)\n\n\nn, q = map(int, input().split())\nA = [0] * n\nB =\
    \ [0] * n\nfor i in range(n):\n    A[i], B[i] = map(int, input().split())\ng =\
    \ Tree.from_input(n, 0)\nhld = HeavyLightDecomposition(n, g)\nP = hld.build_list([A[i]\
    \ << 32 | B[i] for i in range(n)])\ne = 1 << 32\nseg1 = Segtree(P, op1, e)\nseg2\
    \ = Segtree(P, op2, e)\n\nfor _ in range(q):\n    t, a, b, c = map(int, input().split())\n\
    \    if t == 0:\n        p = hld.index(a)\n        seg1.set(p, (b << 32) + c)\n\
    \        seg2.set(p, (b << 32) + c)\n    else:\n        path = hld.path_query_noncommutative(a,\
    \ b, False)\n        res = e\n        for l, r, is_rev in path:\n            if\
    \ is_rev:\n                res = op1(res, seg2.prod(l, r))\n            else:\n\
    \                res = op1(res, seg1.prod(l, r))\n        s, t = res >> 32, res\
    \ & msk\n        ans = (s * c % MOD + t) % MOD\n        print(ans)\n"
  dependsOn:
  - graph/tree/template.py
  - data_structure/segtree/segment_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: true
  path: test/library_checker/tree/vertext_set_path_composite.test.py
  requiredBy: []
  timestamp: '2024-09-02 11:34:25+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/tree/vertext_set_path_composite.test.py
layout: document
title: Vertex Set Path Composite
---
