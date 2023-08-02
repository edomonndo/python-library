---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple\n\n\ndef sortPointsByArgument(points: List[Tuple[int,\
    \ int]]) -> List[Tuple[int, int]]:\n    def msort(arr):\n        if not arr:\n\
    \            return\n        n = len(arr)\n        a = [arr, arr[:]]\n       \
    \ # \u975E\u518D\u5E30DFS\n        stack = [(0, n, 1, 0)]  # \u533A\u9593[l,r)\u3001\
    DFS\u306E\u30D5\u30E9\u30B0f\u3001\u5BFE\u8C61\u306E\u30EA\u30B9\u30C8\n     \
    \   while stack:\n            l, r, f, g = stack.pop()\n            m = (l + r)\
    \ // 2\n            if f:\n                stack.append((l, r, 0, g))\n      \
    \          if m - l > 1:\n                    stack.append((l, m, 1, g ^ 1))\n\
    \                if r - m > 1:\n                    stack.append((m, r, 1, g ^\
    \ 1))\n            else:\n                i, j, p, q = l, m, m - 1, r - 1\n  \
    \              a1 = a[g]\n                a2 = a[g ^ 1]\n                for k\
    \ in range((r - l) // 2):\n                    x, y = a2[i]\n                \
    \    s, t = a2[j]\n                    if s * y - t * x > 0:\n               \
    \         a1[l + k] = a2[j]\n                        j += 1\n                \
    \    else:\n                        a1[l + k] = a2[i]\n                      \
    \  i += 1\n                    x, y = a2[p]\n                    s, t = a2[q]\n\
    \                    if s * y - t * x > 0:\n                        a1[r - 1 -\
    \ k] = a2[p]\n                        p -= 1\n                    else:\n    \
    \                    a1[r - 1 - k] = a2[q]\n                        q -= 1\n \
    \               if (r - l) & 1:\n                    a1[m] = a2[i] if i == p else\
    \ a2[j]\n\n    # zi\u306F\u7B2Ci\u8C61\u9650\uFF08\u305F\u3060\u3057z5\u306F\u539F\
    \u70B9\uFF09\n    z1, z2, z3, z4, z5 = [], [], [], [], []\n    for x, y in points:\n\
    \        if x == y == 0:\n            z5.append((x, y))\n        elif y >= 0:\n\
    \            if x >= 0:\n                z1.append((x, y))\n            else:\n\
    \                z2.append((x, y))\n        else:\n            if x < 0:\n   \
    \             z3.append((x, y))\n            else:\n                z4.append((x,\
    \ y))\n\n    msort(z1)\n    msort(z2)\n    msort(z3)\n    msort(z4)\n\n    return\
    \ z3 + z4 + z5 + z1 + z2\n"
  dependsOn: []
  isVerificationFile: false
  path: geometory/sort_points_by_argument.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: geometory/sort_points_by_argument.py
layout: document
title: "\u504F\u89D2\u30BD\u30FC\u30C8"
---

座標群を第3象限から第2象限の順に偏角で並べ替える．