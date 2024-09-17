---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: data_structure/fenwick_tree/fenwick_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
    title: Static Rectangle Add Rectangle Sum
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\nfrom data_structure.fenwick_tree.fenwick_tree\
    \ import FenwickTree\n\nMOD = 998244353\n\n\nclass Node:\n    def __init__(self,\
    \ a: int, b: int, c: int, d: int):\n        self.a = a % MOD\n        self.b =\
    \ b % MOD\n        self.c = c % MOD\n        self.d = d % MOD\n\n    def __iadd__(self,\
    \ other) -> \"Node\":\n        a = self.a + other.a\n        if a >= MOD:\n  \
    \          a -= MOD\n        b = self.b + other.b\n        if b >= MOD:\n    \
    \        b -= MOD\n        c = self.c + other.c\n        if c >= MOD:\n      \
    \      c -= MOD\n        d = self.d + other.d\n        if d >= MOD:\n        \
    \    d -= MOD\n        return Node(a, b, c, d)\n\n\nclass OfflineRectangleAddRectangleSum:\n\
    \    def __init__(self):\n        self.rects = []\n        self.qs = []\n\n  \
    \  def add_rect(self, x1: int, y1: int, x2: int, y2: int, w: int) -> None:\n \
    \       if x1 == x2 or y1 == y2:\n            return\n        assert x1 <= x2\
    \ and y1 <= y2\n        self.rects.append((x1, y1, x2, y2, w))\n\n    def add_query(self,\
    \ x1: int, y1: int, x2: int, y2: int) -> None:\n        self.qs.append((x1, y1,\
    \ x2, y2))\n\n    def solve(self) -> list[int]:\n        n, q = len(self.rects),\
    \ len(self.qs)\n        res = [0] * q\n        if n == 0 or q == 0:\n        \
    \    return res\n\n        toY = []\n        for _, y1, _, y2 in self.qs:\n  \
    \          toY += [y1, y2]\n        toY = sorted(set(toY))\n\n        event_rect\
    \ = []\n        for i, (x1, y1, x2, y2, w) in enumerate(self.rects):\n       \
    \     y1_ = bisect_left(toY, y1)\n            y2_ = bisect_left(toY, y2)\n   \
    \         event_rect += [(x1, y1_, y2_, 0, i), (x2, y1_, y2_, 1, i)]\n       \
    \ event_rect.sort()\n\n        event_qs = []\n        for i, (x1, y1, x2, y2)\
    \ in enumerate(self.qs):\n            y1_ = bisect_left(toY, y1)\n           \
    \ y2_ = bisect_left(toY, y2)\n            event_qs += [(x1, y1_, y2_, 0, i), (x2,\
    \ y1_, y2_, 1, i)]\n        event_qs.sort()\n\n        j = 0\n        bit = FenwickTree(len(toY)\
    \ + 1, Node(0, 0, 0, 0))\n        for qx, qy1, qy2, qf, qi in event_qs:\n    \
    \        while j < n + n and event_rect[j][0] < qx:\n                p1, p2, f,\
    \ i = event_rect[j][1:]\n                rx1, ry1, rx2, ry2, w = self.rects[i]\n\
    \                if f:\n                    bit.add(p1, Node(-w * rx2 * ry1, -w,\
    \ w * ry1, w * rx2))\n                    bit.add(p2, Node(w * rx2 * ry2, w, -w\
    \ * ry2, -w * rx2))\n                else:\n                    bit.add(p1, Node(w\
    \ * rx1 * ry1, w, -w * ry1, -w * rx1))\n                    bit.add(p2, Node(-w\
    \ * rx1 * ry2, -w, w * ry2, w * rx1))\n                j += 1\n\n            qu\
    \ = self.qs[qi]\n\n            sub1 = bit.sum0(qy2 + 1)\n            res[qi] +=\
    \ sub1.a\n            res[qi] += (sub1.b * qx * qu[3]) % MOD\n            res[qi]\
    \ += (sub1.c * qx) % MOD\n            res[qi] += (sub1.d * qu[3]) % MOD\n    \
    \        res[qi] %= MOD\n\n            sub2 = bit.sum0(qy1 + 1)\n            res[qi]\
    \ -= sub2.a\n            res[qi] -= (sub2.b * qx * qu[1]) % MOD\n            res[qi]\
    \ -= (sub2.c * qx) % MOD\n            res[qi] -= (sub2.d * qu[1]) % MOD\n\n  \
    \          if not qf:\n                res[qi] *= -1\n\n            res[qi] %=\
    \ MOD\n\n        return res\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  isVerificationFile: false
  path: geometory/offline_rectangle_add_rectangle_sum.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
documentation_of: geometory/offline_rectangle_add_rectangle_sum.py
layout: document
redirect_from:
- /library/geometory/offline_rectangle_add_rectangle_sum.py
- /library/geometory/offline_rectangle_add_rectangle_sum.py.html
title: geometory/offline_rectangle_add_rectangle_sum.py
---
