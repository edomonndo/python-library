---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: data_structure/segtree/lazy_segment_tree.py
  - icon: ':warning:'
    path: data_structure/segtree/monoids_action/range_add_range_product_sum.py
    title: data_structure/segtree/monoids_action/range_add_range_product_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':grey_question:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abc357/tasks/abc357_f
    links:
    - https://atcoder.jp/contests/abc357/tasks/abc357_f
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abc357/tasks/abc357_f\n\
    \nfrom data_structure.segtree.monoids_action.range_add_range_product_sum import\
    \ *\nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\n\n\nn,\
    \ q = map(int, input().split())\nA = [int(x) for x in input().split()]\nB = [int(x)\
    \ for x in input().split()]\nseg = LazySegtree(\n    [S(a, b, a * b, 1) for a,\
    \ b in zip(A, B)],\n    op,\n    S(0, 0, 0, 0),\n    mapping,\n    composition,\n\
    \    F(0, 0),\n)\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 3:\n        l, r = qu\n        print(seg.prod(l - 1, r).ab)\n   \
    \ else:\n        l, r, x = qu\n        f = F(x, 0) if t == 1 else F(0, x)\n  \
    \      seg.apply(l - 1, r, f)\n"
  dependsOn:
  - data_structure/segtree/monoids_action/range_add_range_product_sum.py
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc357f.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc357f.test.py
layout: document
title: F - Two Sequence Queries
---
