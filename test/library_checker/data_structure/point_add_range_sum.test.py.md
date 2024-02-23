---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree.py
    title: Fenwick Tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    \nfrom data_structure.fenwick_tree import FenwickTree\n\nN, Q = map(int, input().split())\n\
    A = list(map(int, input().split()))\n\nINF = 1 << 60\nFT = FenwickTree(N)\nfor\
    \ i, a in enumerate(A):\n    FT.add(i, a)\n\nfor _ in range(Q):\n    t, x, y =\
    \ map(int, input().split())\n    if t == 0:\n        FT.add(x, y)\n    elif t\
    \ == 1:\n        print(FT.sum(x, y))\n"
  dependsOn:
  - data_structure/fenwick_tree.py
  isVerificationFile: true
  path: test/library_checker/data_structure/point_add_range_sum.test.py
  requiredBy: []
  timestamp: '2023-08-01 14:51:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/point_add_range_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/point_add_range_sum.test.py
- /verify/test/library_checker/data_structure/point_add_range_sum.test.py.html
title: test/library_checker/data_structure/point_add_range_sum.test.py
---