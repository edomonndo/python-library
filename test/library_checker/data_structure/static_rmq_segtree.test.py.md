---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/segment_tree.py
    title: data_structure/segtree/segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \nfrom data_structure.segtree.segment_tree import Segtree\n\nN, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\n\nINF = 1 << 60\nSeg = Segtree(A, min, INF)\n\
    \nfor _ in range(Q):\n    l, r = map(int, input().split())\n    print(Seg.prod(l,\
    \ r))\n"
  dependsOn:
  - data_structure/segtree/segment_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_rmq_segtree.test.py
  requiredBy: []
  timestamp: '2024-06-07 11:47:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_rmq_segtree.test.py
layout: document
title: Static RMQ (Segment Tree)
---
