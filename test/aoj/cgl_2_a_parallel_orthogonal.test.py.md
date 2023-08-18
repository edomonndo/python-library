---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/geometory.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_A\n\
    \nfrom geometory.geometory import Point, Line\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())\n    l1 = Line(Point(x1,\
    \ y1), Point(x2, y2))\n    l2 = Line(Point(x3, y3), Point(x4, y4))\n    if l1.is_parallel(l2):\n\
    \        print(2)\n    elif l1.is_orthogonal(l2):\n        print(1)\n    else:\n\
    \        print(0)\n"
  dependsOn:
  - geometory/geometory.py
  isVerificationFile: true
  path: test/aoj/cgl_2_a_parallel_orthogonal.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl_2_a_parallel_orthogonal.test.py
layout: document
redirect_from:
- /verify/test/aoj/cgl_2_a_parallel_orthogonal.test.py
- /verify/test/aoj/cgl_2_a_parallel_orthogonal.test.py.html
title: test/aoj/cgl_2_a_parallel_orthogonal.test.py
---
