---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/circle.py
    title: geometory/basic/circle.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_A


    from geometory.basic.circle import Circle


    x, y, r = map(int, input().split())

    C1 = Circle.from_int(x, y, r)

    x, y, r = map(int, input().split())

    C2 = Circle.from_int(x, y, r)

    print(C1.intersect(C2))

    '
  dependsOn:
  - geometory/basic/circle.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_7_a_intersection.test.py
  requiredBy: []
  timestamp: '2024-08-15 10:59:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_7_a_intersection.test.py
layout: document
title: "CGL7A \u5186\u306E\u4EA4\u5DEE\u5224\u5B9A"
---

