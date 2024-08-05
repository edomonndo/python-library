---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B\n\
    \nfrom geometory.basic.line import Line\n\nx1, y1, x2, y2 = map(int, input().split())\n\
    line = Line.from_int(x1, y1, x2, y2)\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    x, y = map(int, input().split())\n    ans = line.refrection(x, y)\n    print(\"\
    {:.10f}\".format(ans.x), \"{:.10f}\".format(ans.y))\n"
  dependsOn:
  - geometory/basic/line.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_1_b_refrection.test.py
  requiredBy: []
  timestamp: '2024-08-05 22:04:36+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_1_b_refrection.test.py
layout: document
title: "CGL1B \u53CD\u5C04"
---

