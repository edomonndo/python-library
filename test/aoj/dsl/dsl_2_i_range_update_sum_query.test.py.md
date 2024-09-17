---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: data_structure/segtree/lazy_segment_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_I
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_I
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_I\n\
    \nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\n\nN, Q = map(int,\
    \ input().split())\nA = [(0, 1)] * N\nINF = float(\"inf\")\nG = LazySegtree(\n\
    \    A,\n    lambda x, y: (x[0] + y[0], x[1] + y[1]),\n    (0, 1),\n    lambda\
    \ f, x: x if f == INF else (f * x[1], x[1]),\n    lambda f, g: g if f == INF else\
    \ f,\n    INF,\n)\n\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        s, t, x = q\n        G.apply(s, t + 1, x)\n    else:\n\
    \        s, t = q\n        print(G.prod(s, t + 1)[0])\n"
  dependsOn:
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: true
  path: test/aoj/dsl/dsl_2_i_range_update_sum_query.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl/dsl_2_i_range_update_sum_query.test.py
layout: document
title: DSL2I RSQ and RUQ
---

