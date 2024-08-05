---
data:
  _extendedDependsOn: []
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
  code: "def convex_hull(xy: list[tuple[int, int]]):\n    bs = 31\n    msk = (1 <<\
    \ bs) - 1\n    offset = 1_000_000_000\n\n    ps = list(set(x + offset << bs |\
    \ y + offset for x, y in xy))\n    if len(ps) <= 2:\n        return [((p >> bs)\
    \ - offset, (p & msk) - offset) for p in ps]\n\n    ps.sort()\n    res = []\n\n\
    \    def cross3(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) ->\
    \ int:\n        ax, ay = a >> bs, a & msk\n        bx, by = b >> bs, b & msk\n\
    \        cx, cy = c >> bs, c & msk\n        return (bx - ax) * (cy - ay) - (by\
    \ - ay) * (cx - ax)\n\n    for p in ps:\n        while len(res) > 1 and cross3(res[-1],\
    \ res[-2], p) >= 0:\n            res.pop()\n        res.append(p)\n\n    sz =\
    \ len(res)\n    for p in ps[::-1][1:]:\n        while len(res) > sz and cross3(res[-1],\
    \ res[-2], p) >= 0:\n            res.pop()\n        res.append(p)\n    res.pop()\n\
    \    return [((p >> bs) - offset, (p & msk) - offset) for p in res]\n"
  dependsOn: []
  isVerificationFile: false
  path: geometory/convex_full.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/geometory/static_convex_hull.test.py
documentation_of: geometory/convex_full.py
layout: document
title: Convex full
---

凸包．複数の点から全ての点を内包する多角形を考えた時，多角形を構成する点を求める．