---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: data_structure/connectivity/weighted_union_find.py
    title: "\u91CD\u307F\u4ED8\u304D Union Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B\n\
    \nfrom data_structure.connectivity.weighted_union_find import WeightedUnionFind\n\
    \nN, Q = map(int, input().split())\nG = WeightedUnionFind(N)\nfor _ in range(Q):\n\
    \    t, *q = map(int, input().split())\n    if t == 0:\n        x, y, z = q\n\
    \        G.merge(y, x, z)\n    else:\n        x, y = q\n        ans = G.diff(y,\
    \ x)\n        print(ans if ans is not None else \"?\")\n"
  dependsOn:
  - data_structure/connectivity/weighted_union_find.py
  isVerificationFile: true
  path: test/aoj/dsl/dsl_1_b_weighted_union_find.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/dsl/dsl_1_b_weighted_union_find.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl/dsl_1_b_weighted_union_find.test.py
- /verify/test/aoj/dsl/dsl_1_b_weighted_union_find.test.py.html
title: test/aoj/dsl/dsl_1_b_weighted_union_find.test.py
---
