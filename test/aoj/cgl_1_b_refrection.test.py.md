---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/geometory.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B\n\
    \nfrom geometory.geometory import Point, Line\n\nx1, y1, x2, y2 = map(int, input().split())\n\
    line = Line(Point(x1, y1), Point(x2, y2))\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    x, y = map(int, input().split())\n    p = Point(x, y)\n    ans = line.refrection(p)\n\
    \    print(\"{:.10f}\".format(ans.x), \"{:.10f}\".format(ans.y))\n"
  dependsOn:
  - geometory/geometory.py
  isVerificationFile: true
  path: test/aoj/cgl_1_b_refrection.test.py
  requiredBy: []
  timestamp: '2024-05-01 08:13:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl_1_b_refrection.test.py
layout: document
redirect_from:
- /verify/test/aoj/cgl_1_b_refrection.test.py
- /verify/test/aoj/cgl_1_b_refrection.test.py.html
title: test/aoj/cgl_1_b_refrection.test.py
---
