---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/FoldableQue.py
    title: Foldable Queue(SWAG)
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D\n\
    \nfrom data_structure.FoldableQue import FoldableQue\n\nN, L = map(int, input().split())\n\
    A = list(map(int, input().split()))\nINF = float(\"inf\")\nque = FoldableQue(min,\
    \ INF)\nans = []\nfor i in range(L):\n    que.push(A[i])\nans.append(que.fold())\n\
    for i in range(L, N):\n    que.pop()\n    que.push(A[i])\n    ans.append(que.fold())\n\
    print(*ans)\n"
  dependsOn:
  - data_structure/FoldableQue.py
  isVerificationFile: true
  path: test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
- /verify/test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py.html
title: test/aoj/dsl_3_d_sliding_minimum_element_swag.test.py
---
