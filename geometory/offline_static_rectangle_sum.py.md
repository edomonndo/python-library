---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: atcoder/fenwicktree.py
    title: atcoder/fenwicktree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/rectangle_sum.test.py
    title: Rectangle Sum
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\nfrom atcoder.fenwicktree import FenwickTree\n\
    \n\ndef solve(\n    points: list[tuple[int, int, int]], queries: list[tuple[int,\
    \ int]]\n) -> list[int]:\n    n, q = len(points), len(queries)\n\n    # y\u5EA7\
    \u6A19\u3067\u30BD\u30FC\u30C8&\u5EA7\u5727\n    points.sort(key=lambda p: p[1])\n\
    \    toY = []\n    for i in range(n):\n        x, y, w = points[i]\n        if\
    \ len(toY) == 0 or toY[-1] != y:\n            toY.append(y)\n        points[i]\
    \ = (x, len(toY) - 1, w)\n\n    # \u30A4\u30D9\u30F3\u30C8\u30BD\u30FC\u30C8\n\
    \    event = []\n    for qi, (x1, y1, x2, y2) in enumerate(queries):\n       \
    \ y1_ = bisect_left(toY, y1)\n        y2_ = bisect_left(toY, y2)\n        event\
    \ += [(x1, y1_, y2_, ~qi), (x2, y1_, y2_, qi)]\n\n    # x\u5EA7\u6A19\u3067\u30BD\
    \u30FC\u30C8\n    points.sort(key=lambda p: p[0])\n    event.sort(key=lambda e:\
    \ e[0])\n\n    # \u5E73\u9762\u8D70\u67FB\n    res = [0] * q\n    fw = FenwickTree(len(toY))\n\
    \    pi, qi = 0, 0\n    while qi < q * 2:\n        if pi == n or event[qi][0]\
    \ <= points[pi][0]:\n            x, y1, y2, i = event[qi]\n            s = fw.sum(y1,\
    \ y2)\n            if i < 0:\n                res[~i] -= s\n            else:\n\
    \                res[i] += s\n            qi += 1\n        else:\n           \
    \ fw.add(points[pi][1], points[pi][2])\n            pi += 1\n    return res\n"
  dependsOn:
  - atcoder/fenwicktree.py
  isVerificationFile: false
  path: geometory/offline_static_rectangle_sum.py
  requiredBy: []
  timestamp: '2024-05-29 14:24:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/rectangle_sum.test.py
documentation_of: geometory/offline_static_rectangle_sum.py
layout: document
title: "\u77E9\u5F62\u548C(\u30AA\u30D5\u30E9\u30A4\u30F3\u30FB\u9759\u7684)"
---
