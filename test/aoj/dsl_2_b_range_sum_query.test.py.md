---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B\n\
    \nfrom data_structure.fenwick_tree import FenwickTree\n\nN, Q = map(int, input().split())\n\
    FT = FenwickTree(N)\n\nans = []\nfor _ in range(Q):\n    t, x, y = map(int, input().split())\n\
    \    if t == 0:\n        FT.add(x - 1, y)\n    else:\n        ans.append(FT.sum(x\
    \ - 1, y))\nprint(*ans, sep=\"\\n\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/dsl_2_b_range_sum_query.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_2_b_range_sum_query.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_2_b_range_sum_query.test.py
- /verify/test/aoj/dsl_2_b_range_sum_query.test.py.html
title: test/aoj/dsl_2_b_range_sum_query.test.py
---
