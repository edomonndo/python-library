---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_C\n\
    \nfrom geometory.basic.line import Line\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())\n    l1 = Line.from_int(x1,\
    \ y1, x2, y2)\n    l2 = Line.from_int(x3, y3, x4, y4)\n    ans = l1.get_cross_point(l2)\n\
    \    print(\"{:.10f}\".format(ans.x), \"{:.10f}\".format(ans.y))\n"
  dependsOn:
  - geometory/basic/line.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_2_c_cross_point.test.py
  requiredBy: []
  timestamp: '2024-08-05 22:25:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_2_c_cross_point.test.py
layout: document
title: "CGL2C \u4EA4\u70B9"
---
