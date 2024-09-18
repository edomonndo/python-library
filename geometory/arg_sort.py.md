---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/geometory/sort_points_by_argument.test.py
    title: Sort Points by Argument
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Union, TypeVar\n\nT = TypeVar(\"T\")\n\nfrom geometory.basic.point\
    \ import Point\n\n\ndef arg_sort(ps: list[Union[Point, tuple[T, T]]]) -> list[Point]:\n\
    \    def merge_sort(arr):\n        if not arr:\n            return\n        n\
    \ = len(arr)\n        a = [arr, arr[:]]\n        # \u975E\u518D\u5E30DFS\n   \
    \     st = [(0, n, 1, 0)]  # \u533A\u9593[l,r),DFS\u306E\u30D5\u30E9\u30B0f,\u5BFE\
    \u8C61\u306E\u30EA\u30B9\u30C8\n        while st:\n            l, r, f, g = st.pop()\n\
    \            m = (l + r) >> 1\n            if f:\n                st.append((l,\
    \ r, 0, g))\n                if m - l > 1:\n                    st.append((l,\
    \ m, 1, g ^ 1))\n                if r - m > 1:\n                    st.append((m,\
    \ r, 1, g ^ 1))\n            else:\n                i, j, p, q = l, m, m - 1,\
    \ r - 1\n                a1 = a[g]\n                a2 = a[g ^ 1]\n          \
    \      for k in range((r - l) >> 1):\n                    xi, yi = a2[i]\n   \
    \                 xj, yj = a2[j]\n                    if xj * yi - yj * xi > 0:\n\
    \                        a1[l + k] = a2[j]\n                        j += 1\n \
    \                   else:\n                        a1[l + k] = a2[i]\n       \
    \                 i += 1\n                    xp, yp = a2[p]\n               \
    \     xq, yq = a2[q]\n                    if xq * yp - yq * xp > 0:\n        \
    \                a1[r - 1 - k] = a2[p]\n                        p -= 1\n     \
    \               else:\n                        a1[r - 1 - k] = a2[q]\n       \
    \                 q -= 1\n                if (r - l) & 1:\n                  \
    \  a1[m] = a2[i] if i == p else a2[j]\n\n    # zi\u306F\u7B2Ci\u8C61\u9650\uFF08\
    \u305F\u3060\u3057z5\u306F\u539F\u70B9\uFF09\n    z1, z2, z3, z4, z5 = [], [],\
    \ [], [], []\n    for x, y in ps:\n        if x == y == 0:\n            z = z5\n\
    \        elif y >= 0:\n            z = z1 if x >= 0 else z2\n        else:\n \
    \           z = z3 if x < 0 else z4\n        z.append(Point(x, y))\n\n    for\
    \ z in [z1, z2, z3, z4]:\n        merge_sort(z)\n\n    return z3 + z4 + z5 + z1\
    \ + z2\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/arg_sort.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/geometory/sort_points_by_argument.test.py
documentation_of: geometory/arg_sort.py
layout: document
redirect_from:
- /library/geometory/arg_sort.py
- /library/geometory/arg_sort.py.html
title: geometory/arg_sort.py
---
