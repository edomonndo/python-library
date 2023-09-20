---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/sparse_table.py
    title: Sparse table
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D\n\
    \nfrom data_structure.sparse_table import SparseTable\n\nN, L = map(int, input().split())\n\
    A = [int(x) for x in input().split()]\nST = SparseTable(A, min)\nans = []\nfor\
    \ i in range(N + 1 - L):\n    ans.append(ST.query(i, i + L))\nprint(*ans)\n"
  dependsOn:
  - data_structure/sparse_table.py
  isVerificationFile: true
  path: test/aoj/dsl_3_d_sliding_minimum_element_st.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_3_d_sliding_minimum_element_st.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_3_d_sliding_minimum_element_st.test.py
- /verify/test/aoj/dsl_3_d_sliding_minimum_element_st.test.py.html
title: test/aoj/dsl_3_d_sliding_minimum_element_st.test.py
---
