---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/monoids/RangeMinIndex.py
    title: data_structure/segtree/monoids/RangeMinIndex.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://yukicoder.me/problems/no/875
    links:
    - https://yukicoder.me/problems/no/875
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://yukicoder.me/problems/no/875\n\n\n\
    from data_structure.segtree.monoids.RangeMinIndex import *\nfrom atcoder.segtree\
    \ import SegTree\n\nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\
    seg = SegTree(op, S(), [S(A[i], i + 1) for i in range(n)])\nfor _ in range(q):\n\
    \    t, l, r = map(int, input().split())\n    if t == 1:\n        l -= 1\n   \
    \     r -= 1\n        tmp = seg.get(l)\n        lv, li = tmp.value, tmp.index\n\
    \        tmp = seg.get(r)\n        rv, ri = tmp.value, tmp.index\n        seg.set(l,\
    \ S(rv, li))\n        seg.set(r, S(lv, ri))\n    else:\n        l -= 1\n     \
    \   print(seg.prod(l, r).index)\n"
  dependsOn:
  - data_structure/segtree/monoids/RangeMinIndex.py
  - atcoder/segtree.py
  isVerificationFile: true
  path: test/yukicoder/875_range_mindex_query.test.py
  requiredBy: []
  timestamp: '2024-06-13 11:50:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/yukicoder/875_range_mindex_query.test.py
layout: document
title: No.875 Range Mindex Query
---
