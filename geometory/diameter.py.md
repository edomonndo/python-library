---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  - icon: ':heavy_check_mark:'
    path: geometory/convex_full.py
    title: Convex full
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_4_b_diameter_of_a_convex_polygon.test.py
    title: "CGL4B \u51F8\u591A\u89D2\u5F62\u306E\u76F4\u5F84"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/geometory/furthest_pair.test.py
    title: Furthest Pair of Points
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Union, Optional, TypeVar\n\nT = TypeVar(\"T\")\n\nfrom\
    \ geometory.basic.point import Point\nfrom geometory.convex_full import convex_hull\n\
    \n\ndef diameter(\n    ps: list[Union[Point, tuple[T, T]]]\n) -> Optional[tuple[float,\
    \ Point, Point]]:\n\n    ch = convex_hull(ps)\n    n = len(ch)\n    if n == 0:\n\
    \        return None\n    if n == 1:\n        return 0, ch[0], ch[0]\n    if n\
    \ == 2:\n        return (ch[0] - ch[1]).abs(), ch[0], ch[1]\n\n    u = v = 0\n\
    \    up = vp = ch[0]\n    for i in range(n):\n        if ch[u] > ch[i]:\n    \
    \        u = i\n            up = ch[i]\n        if ch[v] < ch[i]:\n          \
    \  v = i\n            vp = ch[i]\n\n    dist2, su, sv = 0, u, v\n    loop = False\n\
    \    while u != su or v != sv or not loop:\n        loop = True\n        d2 =\
    \ (ch[u] - ch[v]).norm()\n        if dist2 < d2:\n            dist2 = d2\n   \
    \         up, vp = ch[u], ch[v]\n        a = ch[(u + 1) % n] - ch[u]\n       \
    \ b = ch[(v + 1) % n] - ch[v]\n        if a.cross(b) < 0:\n            u = (u\
    \ + 1) % n\n        else:\n            v = (v + 1) % n\n    return dist2**0.5,\
    \ up, vp\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/convex_full.py
  isVerificationFile: false
  path: geometory/diameter.py
  requiredBy: []
  timestamp: '2024-08-14 14:54:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/geometory/furthest_pair.test.py
  - test/aoj/cgl/cgl_4_b_diameter_of_a_convex_polygon.test.py
documentation_of: geometory/diameter.py
layout: document
title: "\u591A\u89D2\u5F62\u306E\u76F4\u5F84"
---