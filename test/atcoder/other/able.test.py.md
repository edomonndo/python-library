---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: atcoder/lazysegtree.py
    title: atcoder/lazysegtree.py
  - icon: ':x:'
    path: data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
    title: "\u533A\u9593\u6587\u5B57\u5217\u66F4\u65B0\u30FB\u533A\u9593\u548C"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
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
    \ *\nfrom atcoder.lazysegtree import LazySegTree\n\nn, q = map(int, input().split())\n\
    seg = LazySegTree(op, S(), mapping, composition, F(), [S(1, 1) for _ in range(n)])\n\
    \nfor _ in range(q):\n    l, r, d = map(int, input().split())\n    seg.apply(l\
    \ - 1, r, F(d))\n    print(seg.all_prod().value)\n"
  dependsOn:
  - data_structure/segtree/monoids_action/range_str_update_range_int_sum.py
  - atcoder/lazysegtree.py
  isVerificationFile: true
  path: test/atcoder/other/able.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:49:22+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/atcoder/other/able.test.py
layout: document
title: E - Replace Digits
---
