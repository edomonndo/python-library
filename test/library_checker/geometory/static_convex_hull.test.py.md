---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  - icon: ':x:'
    path: geometory/convex_full.py
    title: Convex full
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_convex_hull
    links:
    - https://judge.yosupo.jp/problem/static_convex_hull
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_convex_hull\n\
    \nfrom geometory.basic.point import Point\nfrom geometory.convex_full import convex_hull\n\
    \nT = int(input())\nfor _ in range(T):\n    n = int(input())\n    xy = list(set(tuple(map(int,\
    \ input().split())) for _ in range(n)))\n    res = convex_hull([Point(x, y) for\
    \ x, y in xy])\n    print(len(res))\n    for x, y in res:\n        print(x, y)\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/convex_full.py
  isVerificationFile: true
  path: test/library_checker/geometory/static_convex_hull.test.py
  requiredBy: []
  timestamp: '2024-08-09 17:42:45+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/geometory/static_convex_hull.test.py
layout: document
title: Static Convex Hull
---
