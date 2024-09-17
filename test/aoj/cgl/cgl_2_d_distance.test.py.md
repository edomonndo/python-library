---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/line.py
    title: geometory/basic/line.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_D
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_D\n\
    \nfrom geometory.basic.line import Line\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())\n    l1 = Line.from_int(x1,\
    \ y1, x2, y2)\n    l2 = Line.from_int(x3, y3, x4, y4)\n    ans = l1.get_distance_seg_to_seg(l2)\n\
    \    print(\"{:.10f}\".format(ans))\n"
  dependsOn:
  - geometory/basic/line.py
  isVerificationFile: true
  path: test/aoj/cgl/cgl_2_d_distance.test.py
  requiredBy: []
  timestamp: '2024-08-05 22:25:19+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl/cgl_2_d_distance.test.py
layout: document
title: "CGL2D \u8DDD\u96E2"
---

