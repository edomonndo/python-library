---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/union_area_rectangle.py
    title: geometory/union_area_rectangle.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A


    from geometory.union_area_rectangle import union_area


    n = int(input())

    rects = [tuple(map(int, input().split())) for _ in range(n)]

    print(union_area(rects))

    '
  dependsOn:
  - geometory/union_area_rectangle.py
  isVerificationFile: true
  path: test/aoj/dsl/dsl_4_a_union_of_rectangles_lst.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl/dsl_4_a_union_of_rectangles_lst.test.py
layout: document
title: "DSL4A Union of Rectangles (\u9045\u5EF6\u30BB\u30B0\u6728)"
---

