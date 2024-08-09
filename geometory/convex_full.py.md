---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/geometory/static_convex_hull.test.py
    title: Static Convex Hull
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from geometory.basic.point import Point\n\n\ndef convex_hull(ps: list[Point])\
    \ -> list[Point]:\n\n    if len(ps) <= 2:\n        return ps\n\n    ps.sort()\n\
    \    res = []\n\n    def cross3(a: Point, b: Point, c: Point) -> int:\n      \
    \  return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)\n\n    for p in\
    \ ps:\n        while len(res) > 1 and cross3(res[-1], res[-2], p) >= 0:\n    \
    \        res.pop()\n        res.append(p)\n\n    sz = len(res)\n    for p in ps[::-1][1:]:\n\
    \        while len(res) > sz and cross3(res[-1], res[-2], p) >= 0:\n         \
    \   res.pop()\n        res.append(p)\n    res.pop()\n    return res\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/convex_full.py
  requiredBy: []
  timestamp: '2024-08-09 19:58:16+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/geometory/static_convex_hull.test.py
documentation_of: geometory/convex_full.py
layout: document
title: Convex full
---

凸包．複数の点から全ての点を内包する多角形を考えた時，多角形を構成する点を求める．