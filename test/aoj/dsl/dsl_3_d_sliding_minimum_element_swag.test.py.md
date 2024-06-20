---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/basic/FoldableQue.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D\n\
    \nfrom data_structure.basic.FoldableQue import FoldableQue\n\nN, L = map(int,\
    \ input().split())\nA = list(map(int, input().split()))\nINF = float(\"inf\")\n\
    que = FoldableQue(min, INF)\nans = []\nfor i in range(L):\n    que.push(A[i])\n\
    ans.append(que.fold())\nfor i in range(L, N):\n    que.pop()\n    que.push(A[i])\n\
    \    ans.append(que.fold())\nprint(*ans)\n"
  dependsOn:
  - data_structure/basic/FoldableQue.py
  isVerificationFile: true
  path: test/aoj/dsl/dsl_3_d_sliding_minimum_element_swag.test.py
  requiredBy: []
  timestamp: '2024-06-19 13:18:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl/dsl_3_d_sliding_minimum_element_swag.test.py
layout: document
title: DSL3D Sliding Minimum Element (SWAG)
---

