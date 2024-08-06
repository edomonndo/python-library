---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  - icon: ':heavy_check_mark:'
    path: geometory/basic/polygon.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u591A\u89D2\u5F62)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/CGL_3_A\n\
    \nfrom geometory.basic.point import Point\nfrom geometory.basic.polygon import\
    \ Polygon\n\nn = int(input())\nps = []\nfor i in range(n):\n    x, y = map(float,\
    \ input().split())\n    ps.append(Point(x, y))\npol = Polygon(ps)\nprint(pol.area())\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/basic/polygon.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_3_a_area.test.py
  requiredBy: []
  timestamp: '2024-08-06 22:59:49+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_3_a_area.test.py
layout: document
title: "CGL3A \u9762\u7A4D"
---

