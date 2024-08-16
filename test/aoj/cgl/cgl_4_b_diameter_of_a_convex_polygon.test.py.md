---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/diameter.py
    title: "\u591A\u89D2\u5F62\u306E\u76F4\u5F84"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    ERROR: 1e-6
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_B

    # verification-helper: ERROR 1e-6


    from geometory.diameter import diameter


    n = int(input())

    ps = [tuple(map(float, input().split())) for _ in range(n)]

    d, _, _ = diameter(ps)

    print(d)

    '
  dependsOn:
  - geometory/diameter.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_4_b_diameter_of_a_convex_polygon.test.py
  requiredBy: []
  timestamp: '2024-08-16 14:15:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_4_b_diameter_of_a_convex_polygon.test.py
layout: document
title: "CGL4B \u51F8\u591A\u89D2\u5F62\u306E\u76F4\u5F84"
---

