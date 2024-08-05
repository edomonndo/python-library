---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/convex_full.py
    title: Convex full
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_convex_hull
    links:
    - https://judge.yosupo.jp/problem/static_convex_hull
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_convex_hull\n\
    \nfrom geometory.convex_full import convex_hull\n\nT = int(input())\nfor _ in\
    \ range(T):\n    n = int(input())\n    xy = [tuple(map(int, input().split()))\
    \ for _ in range(n)]\n    res = convex_hull(xy)\n    print(len(res))\n    for\
    \ x, y in res:\n        print(x, y)\n"
  dependsOn:
  - geometory/convex_full.py
  isVerificationFile: true
  path: test/library_checker/geometory/static_convex_hull.test.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/geometory/static_convex_hull.test.py
layout: document
title: Static Convex Hull
---
