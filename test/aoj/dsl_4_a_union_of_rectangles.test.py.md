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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/4/DSL_4_A\n\
    \nfrom geometory.geometory import Point, Rectangle, Rectangles\n\nN = int(input())\n\
    rects = Rectangles()\nfor _ in range(N):\n    x1, y1, x2, y2 = map(int, input().split())\n\
    \    rects.add(Rectangle(Point(x1, y1), Point(x2, y2)))\nprint(rects.area())\n"
  dependsOn:
  - geometory/geometory.py
  isVerificationFile: true
  path: test/aoj/dsl_4_a_union_of_rectangles.test.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_4_a_union_of_rectangles.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_4_a_union_of_rectangles.test.py
- /verify/test/aoj/dsl_4_a_union_of_rectangles.test.py.html
title: test/aoj/dsl_4_a_union_of_rectangles.test.py
---
