---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    \nfrom data_structure.segtree.segment_tree import Segtree\n\nMOD = 998244353\n\
    mask = (1 << 30) - 1\n\n\ndef op(x, y):\n    a, b = x >> 30, x & mask\n    c,\
    \ d = y >> 30, y & mask\n    e, f = a * c % MOD, (c * b + d) % MOD\n    return\
    \ e << 30 | f\n\n\ne = 1 << 30\n\nN, Q = map(int, input().split())\nA = [tuple(map(int,\
    \ input().split())) for _ in range(N)]\ng = Segtree([a << 30 | b for a, b in A],\
    \ op, e)\nfor _ in range(Q):\n    t, l, r, x = map(int, input().split())\n   \
    \ if t == 0:\n        g.set(l, r << 30 | x)\n    else:\n        ab = g.prod(l,\
    \ r)\n        a, b = ab >> 30, ab & mask\n        print((a * x + b) % MOD)\n"
  dependsOn:
  - data_structure/segtree/segment_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/point_set_range_composite.test.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/point_set_range_composite.test.py
layout: document
title: Point Set Range Composite
---
