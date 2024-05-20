---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/kd_tree.py
    title: KD tree
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C\n\
    \nfrom geometory.kd_tree import KDTree\n\nN = int(input())\nXY = [tuple(map(int,\
    \ input().split())) for _ in range(N)]\nkd = KDTree(N, XY)\n\nQ = int(input())\n\
    for _ in range(Q):\n    sx, tx, sy, ty = map(int, input().split())\n    ans =\
    \ kd.query(sx, sy, tx, ty)\n    for id in sorted(ans):\n        print(id)\n  \
    \  print()\n"
  dependsOn:
  - geometory/kd_tree.py
  isVerificationFile: true
  path: test/aoj/dsl_2_c_range_search.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_2_c_range_search.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_2_c_range_search.test.py
- /verify/test/aoj/dsl_2_c_range_search.test.py.html
title: test/aoj/dsl_2_c_range_search.test.py
---
