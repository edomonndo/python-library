---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A\n\
    \nfrom data_structure.unionfind import UnionFind\n\nN, Q = map(int, input().split())\n\
    G = UnionFind(N)\nfor _ in range(Q):\n    t, x, y = map(int, input().split())\n\
    \    if t == 0:\n        G.merge(x, y)\n    else:\n        print(1 if G.same(x,\
    \ y) else 0)\n"
  dependsOn:
  - data_structure/unionfind.py
  isVerificationFile: true
  path: test/aoj/dsl_1_a_union_find.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_1_a_union_find.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_1_a_union_find.test.py
- /verify/test/aoj/dsl_1_a_union_find.test.py.html
title: test/aoj/dsl_1_a_union_find.test.py
---
