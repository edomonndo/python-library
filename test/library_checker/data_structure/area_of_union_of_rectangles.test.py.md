---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: geometory/union_area_rectangle.py
    title: geometory/union_area_rectangle.py
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
    \nfrom geometory.union_area_rectangle import union_area\n\nn = int(input())\n\
    rects = []\nfor _ in range(n):\n    l, d, r, u = map(int, input().split())\n \
    \   rects.append((l, d, r, u))\nprint(union_area(rects))\n"
  dependsOn:
  - geometory/union_area_rectangle.py
  isVerificationFile: true
  path: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
  requiredBy: []
  timestamp: '2024-05-01 08:13:10+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/area_of_union_of_rectangles.test.py
- /verify/test/library_checker/data_structure/area_of_union_of_rectangles.test.py.html
title: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
---
