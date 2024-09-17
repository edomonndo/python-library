---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/basic/SortedMultiset.py
    title: data_structure/basic/SortedMultiset.py
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/dual_segment_tree_commutative.py
    title: data_structure/segtree/dual_segment_tree_commutative.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc342/tasks/abc342_g
    links:
    - https://atcoder.jp/contests/abc342/tasks/abc342_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc342/tasks/abc342_g\n\
    \nfrom data_structure.segtree.dual_segment_tree_commutative import DualSegtreeCommutative\n\
    from data_structure.basic.SortedMultiset import SortedMultiset\n\n\ndef op(f:\
    \ int, S: SortedMultiset):\n    if f > 0:\n        S.add(f)\n    elif f < 0:\n\
    \        S.discard(-f)\n\n\ndef get(x: int, y: SortedMultiset):\n    if len(y)\
    \ == 0:\n        return x\n    else:\n        return max(x, y[-1])\n\n\nN = int(input())\n\
    A = [SortedMultiset([int(x)]) for x in input().split()]\nseg = DualSegtreeCommutative(A,\
    \ op, None, get, 0)\n# \u521D\u671F\u5316\u6642\u306E\u30B7\u30E3\u30ED\u30FC\u30B3\
    \u30D4\u30FC\u56DE\u907F\nfor i in range(seg.size):\n    seg.d[i] = SortedMultiset()\n\
    \nQ = int(input())\nhistory = []\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n\
    \    history.append(q)\n    if t == 1:\n        l, r, x = q\n        seg.apply(l\
    \ - 1, r, x)\n    elif t == 2:\n        l, r, x = history[q[0] - 1]\n        seg.apply(l\
    \ - 1, r, -x)\n    else:\n        print(seg.get(q[0] - 1))\n"
  dependsOn:
  - data_structure/segtree/dual_segment_tree_commutative.py
  - data_structure/basic/SortedMultiset.py
  isVerificationFile: true
  path: test/atcoder/abc300-399/abc342g.test.py
  requiredBy: []
  timestamp: '2024-06-24 17:00:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc300-399/abc342g.test.py
layout: document
title: G - Retroactive Range Chmax
---
