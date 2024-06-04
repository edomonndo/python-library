---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/union_area_rectangle.py
    title: "\u9577\u65B9\u5F62\u306E\u548C\u96C6\u5408\u306E\u9762\u7A4D"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/area_of_union_of_rectangles
    links:
    - https://judge.yosupo.jp/problem/area_of_union_of_rectangles
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
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
  timestamp: '2024-05-01 09:39:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/area_of_union_of_rectangles.test.py
- /verify/test/library_checker/data_structure/area_of_union_of_rectangles.test.py.html
title: test/library_checker/data_structure/area_of_union_of_rectangles.test.py
---
