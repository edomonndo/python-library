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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_C\n\
    \nfrom geometory.geometory import Point\n\nx1, y1, x2, y2 = map(int, input().split())\n\
    p0 = Point(x1, y1)\np1 = Point(x2, y2)\n\nQ = int(input())\nfor _ in range(Q):\n\
    \    x, y = map(int, input().split())\n    p2 = Point(x, y)\n    res = p0.ccw(p1,\
    \ p2)\n    if res == 1:\n        print(\"COUNTER_CLOCKWISE\")\n    elif res ==\
    \ -1:\n        print(\"CLOCKWISE\")\n    elif res == 2:\n        print(\"ONLINE_BACK\"\
    )\n    elif res == -2:\n        print(\"ONLINE_FRONT\")\n    else:\n        print(\"\
    ON_SEGMENT\")\n"
  dependsOn:
  - geometory/geometory.py
  isVerificationFile: true
  path: test/aoj/cgl_1_c_counter_clockwise.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/cgl_1_c_counter_clockwise.test.py
layout: document
redirect_from:
- /verify/test/aoj/cgl_1_c_counter_clockwise.test.py
- /verify/test/aoj/cgl_1_c_counter_clockwise.test.py.html
title: test/aoj/cgl_1_c_counter_clockwise.test.py
---
