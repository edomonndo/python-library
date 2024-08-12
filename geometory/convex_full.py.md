---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/arg_sort.py
    title: "\u504F\u89D2\u30BD\u30FC\u30C8"
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy:
  - icon: ':warning:'
    path: geometory/diameter.py
    title: "\u591A\u89D2\u5F62\u306E\u76F4\u5F84"
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/geometory/static_convex_hull.test.py
    title: Static Convex Hull
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Union\n\nfrom geometory.basic.point import Point\nfrom\
    \ geometory.arg_sort import arg_sort\n\n\ndef convex_hull(\n    ps_: list[Union[Point,\
    \ tuple[int, int]]], multi: bool = False\n) -> list[Point]:\n    ps = arg_sort(ps_)\n\
    \    if not ps:\n        return []\n\n    if not multi:\n        tmp = [ps[0]]\n\
    \        for p in ps[1:]:\n            if p != tmp[-1]:\n                tmp.append(p)\n\
    \        ps = tmp\n\n    n = len(ps)\n    if n <= 2:\n        return ps\n\n  \
    \  def cross3(a: Point, b: Point, c: Point) -> int:\n        ax, ay = a\n    \
    \    bx, by = b\n        cx, cy = c\n        return (bx - ax) * (cy - ay) - (by\
    \ - ay) * (cx - ax)\n\n    res = []\n    for p in ps:\n        while len(res)\
    \ > 1 and cross3(res[-1], res[-2], p) >= 0:\n            res.pop()\n        res.append(p)\n\
    \n    sz = len(res)\n    for p in ps[::-1][1:]:\n        while len(res) > sz and\
    \ cross3(res[-1], res[-2], p) >= 0:\n            res.pop()\n        res.append(p)\n\
    \    res.pop()\n\n    return res\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/arg_sort.py
  isVerificationFile: false
  path: geometory/convex_full.py
  requiredBy:
  - geometory/diameter.py
  timestamp: '2024-08-13 00:35:22+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/geometory/static_convex_hull.test.py
documentation_of: geometory/convex_full.py
layout: document
title: Convex full
---

凸包．複数の点から全ての点を内包する多角形を考えた時，多角形を構成する点を求める．