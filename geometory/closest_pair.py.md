---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_5_a_closest_pair.test.py
    title: "CGL5A \u6700\u8FD1\u70B9\u5BFE"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/geometory/closest_pair.test.py
    title: Closest Pair of Points
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Union, TypeVar\n\nT = TypeVar(\"T\")\n\n\nfrom geometory.basic.point\
    \ import Point\n\n\ndef closest_pair(ps_: list[Union[Point, tuple[T, T]]]) ->\
    \ tuple[float, Point, Point]:\n\n    assert len(ps_) >= 2\n\n    ps = sorted([Point(x,\
    \ y) for x, y in ps_])\n    if len(ps) == 2:\n        return (ps[0] - ps[1]).abs(),\
    \ ps[0], ps[1]\n\n    n = len(ps)\n    tmp = [None] * n\n    min_dist2 = float(\"\
    inf\")\n    up = vp = None\n    ps_origin = ps[:]\n\n    # \u975E\u518D\u5E30\
    dfs\n    st = [(0, n)]\n    while st:\n        l, r = st.pop()\n        if l >=\
    \ 0:\n            m = (l + r) >> 1\n            st.append((~l, r))\n         \
    \   if r - m > 1:\n                st.append((m, r))\n            if m - l > 1:\n\
    \                st.append((l, m))\n        else:\n            l = ~l\n      \
    \      m = (l + r) >> 1\n            mx = ps_origin[m].x\n            i, j = l,\
    \ m\n            idx = 0\n            while i < m and j < r:\n               \
    \ if Point.cmp(ps[i].y, ps[j].y, False) < 0:\n                    tmp[idx] = ps[i]\n\
    \                    i += 1\n                else:\n                    tmp[idx]\
    \ = ps[j]\n                    j += 1\n                idx += 1\n            for\
    \ k in range(i, m):\n                ps[l + idx + k - i] = ps[k]\n           \
    \ for k in range(l, l + idx):\n                ps[k] = tmp[k - l]\n\n        \
    \    bs = []\n            for cp in ps[l:r]:\n                if Point.cmp((cp.x\
    \ - mx) * (cp.x - mx), min_dist2, False) >= 0:\n                    continue\n\
    \                for bp in bs[::-1]:\n                    dp = cp - bp\n     \
    \               if Point.cmp(dp.y * dp.y, min_dist2, False) >= 0:\n          \
    \              break\n                    d = dp.norm()\n                    if\
    \ Point.cmp(d, min_dist2, False) < 0:\n                        min_dist2, up,\
    \ vp = d, cp, bp\n                bs.append(cp)\n\n    return min_dist2**0.5,\
    \ up, vp\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/closest_pair.py
  requiredBy: []
  timestamp: '2024-08-15 10:59:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/cgl/cgl_5_a_closest_pair.test.py
  - test/library_checker/geometory/closest_pair.test.py
documentation_of: geometory/closest_pair.py
layout: document
title: Closest Pair
---
