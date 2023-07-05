---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segment_tree.py
    title: Segment Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \nfrom data_structure.segment_tree import Segtree\n\nN, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\n\nINF = 1 << 60\nSeg = Segtree(A, min, INF)\n\
    \nfor _ in range(Q):\n    l, r = map(int, input().split())\n    print(Seg.prod(l,\
    \ r))\n"
  dependsOn:
  - data_structure/segment_tree.py
  isVerificationFile: true
  path: library_checker/data_structure/static_rmq.test.py
  requiredBy: []
  timestamp: '2023-07-05 10:35:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/data_structure/static_rmq.test.py
layout: document
redirect_from:
- /verify/library_checker/data_structure/static_rmq.test.py
- /verify/library_checker/data_structure/static_rmq.test.py.html
title: library_checker/data_structure/static_rmq.test.py
---
