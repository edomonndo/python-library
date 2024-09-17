---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: geometory/basic/point.py
  - icon: ':heavy_check_mark:'
    path: geometory/basic/polygon.py
    title: geometory/basic/polygon.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_B\n\
    \nfrom geometory.basic.point import Point\nfrom geometory.basic.polygon import\
    \ Polygon\n\nn = int(input())\nps = []\nfor i in range(n):\n    x, y = map(float,\
    \ input().split())\n    ps.append(Point(x, y))\npol = Polygon(ps)\nprint(int(pol.is_convex()))\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/basic/polygon.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_3_b_is_convex.test.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_3_b_is_convex.test.py
layout: document
title: "CGL3B \u51F8\u6027\u5224\u5B9A"
---

