---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/geometory.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/area_of_union_of_rectangles
    links:
    - https://judge.yosupo.jp/problem/area_of_union_of_rectangles
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/area_of_union_of_rectangles\n\
    \nfrom geometory.geometory import Rectangles, Rectangle, Point\n\nn = int(input())\n\
    rects = Rectangles()\nfor _ in range(n):\n    l, d, r, u = map(int, input().split())\n\
    \    rects.add(Rectangle(Point(l, d), Point(r, u)))\nprint(rects.union_area())\n"
  dependsOn:
  - geometory/geometory.py
  isVerificationFile: true
  path: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
  requiredBy: []
  timestamp: '2024-04-30 17:18:01+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/area_of_union_of_rectangles.test.py
- /verify/test/library_checker/data_structure/area_of_union_of_rectangles.test.py.html
title: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
---
