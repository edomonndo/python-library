---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/dual_segment_tree.py
    title: "\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dual Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_affine_point_get
    links:
    - https://judge.yosupo.jp/problem/range_affine_point_get
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_point_get\n\
    \nfrom data_structure.segtree.dual_segment_tree import DualSegtree\n\nMOD = 998244353\n\
    mask = (1 << 30) - 1\nID = 1 << 30\n\n\ndef mapping(F, x):\n    a, b = F >> 30,\
    \ F & mask\n    c, d = x >> 30, x & mask\n    e, f = (a * c + b * d) % MOD, d\n\
    \    return e << 30 | f\n\n\ndef composition(F, G):\n    a, b = F >> 30, F & mask\n\
    \    c, d = G >> 30, G & mask\n    e, f = a * c % MOD, (a * d + b) % MOD\n   \
    \ return e << 30 | f\n\n\nN, Q = map(int, input().split())\nA = [int(x) for x\
    \ in input().split()]\ng = DualSegtree([(a << 30) | 1 for a in A], mapping, composition,\
    \ ID)\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n    if t ==\
    \ 0:\n        l, r, b, c = q\n        g.apply(l, r, b << 30 | c)\n    else:\n\
    \        i = q[0]\n        ab = g.get(i)\n        a, b = ab >> 30, ab & mask\n\
    \        print(a)\n"
  dependsOn:
  - data_structure/segtree/dual_segment_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_affine_point_get.test.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_affine_point_get.test.py
layout: document
title: Range Affine Point Get
---