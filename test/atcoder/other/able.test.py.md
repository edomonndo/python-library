---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  - icon: ':warning:'
    path: data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
    title: data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':grey_question:'
  attributes:
    IGNORE: https://atcoder.jp/contests/abl/tasks/abl_e
    links:
    - https://atcoder.jp/contests/abl/tasks/abl_e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: IGNORE https://atcoder.jp/contests/abl/tasks/abl_e\n\
    \nfrom data_structure.segtree.monoids_action.range_str_update_range_int_sum import\
    \ *\nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\n\n\nn,\
    \ q = map(int, input().split())\nseg = LazySegtree([S(1, 1) for _ in range(n)],\
    \ op, S(), mapping, composition, F())\n\nfor _ in range(q):\n    l, r, d = map(int,\
    \ input().split())\n    seg.apply(l - 1, r, F(d))\n    print(seg.all_prod().value)\n"
  dependsOn:
  - data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/atcoder/other/able.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_IGNORED
  verifiedWith: []
documentation_of: test/atcoder/other/able.test.py
layout: document
title: E - Replace Digits
---
