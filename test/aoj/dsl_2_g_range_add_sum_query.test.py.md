---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G\n\
    \nfrom data_structure.lazy_segment_tree import LazySegtree\n\nN, Q = map(int,\
    \ input().split())\nA = [(0, 1)] * N\nINF = float(\"inf\")\nG = LazySegtree(\n\
    \    A,\n    lambda x, y: (x[0] + y[0], x[1] + y[1]),\n    (0, 1),\n    lambda\
    \ f, x: (x[0] + f * x[1], x[1]),\n    lambda f, g: f + g,\n    0,\n)\n\nfor _\
    \ in range(Q):\n    t, *q = map(int, input().split())\n    if t == 0:\n      \
    \  s, t, x = q\n        G.apply(s - 1, t, x)\n    else:\n        s, t = q\n  \
    \      print(G.prod(s - 1, t)[0])\n"
  dependsOn:
  - data_structure/lazy_segment_tree.py
  isVerificationFile: true
  path: test/aoj/dsl_2_g_range_add_sum_query.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_2_g_range_add_sum_query.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_2_g_range_add_sum_query.test.py
- /verify/test/aoj/dsl_2_g_range_add_sum_query.test.py.html
title: test/aoj/dsl_2_g_range_add_sum_query.test.py
---
