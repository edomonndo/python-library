---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/basic/circle.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u5186)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_B ERROR
      1e-6
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_B
    ERROR 1e-6


    from geometory.basic.circle import Circle


    x1, y1 = map(int, input().split())

    x2, y2 = map(int, input().split())

    x3, y3 = map(int, input().split())

    C = Circle.from_triangle(x1, y1, x2, y2, x3, y3)

    print(C.center.x, C.center.y, C.r)

    '
  dependsOn:
  - geometory/basic/circle.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_7_b_incircle_of_a_triangle.test.py
  requiredBy: []
  timestamp: '2024-08-16 12:43:32+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_7_b_incircle_of_a_triangle.test.py
layout: document
title: "CGL7B \u5185\u63A5\u5186"
---

