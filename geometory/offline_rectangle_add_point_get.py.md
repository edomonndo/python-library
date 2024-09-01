---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/rectangle_add_point_get.test.py
    title: Range Add Point Get
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\nfrom bisect import bisect_left\n\nfrom data_structure.fenwick_tree.fenwick_tree\
    \ import FenwickTree\n\n\nclass StaticRectangleAddPointGet:\n    def __init__(self):\n\
    \        self.rects = []\n        self.qs = []\n\n    def add_rect(self, x1: int,\
    \ y1: int, x2: int, y2: int, w: int) -> None:\n        if x1 == x2 or y1 == y2:\n\
    \            return\n        assert x1 <= x2 and y1 <= y2\n        self.rects.append((x1,\
    \ y1, x2, y2, w))\n\n    def add_query(self, x: int, y: int) -> None:\n      \
    \  self.qs.append((x, y))\n\n    def solve(self) -> list[int]:\n        n, q =\
    \ len(self.rects), len(self.qs)\n        res = [0] * q\n        if n == 0 or q\
    \ == 0:\n            return res\n\n        toY = sorted(set(y for _, y in self.qs))\n\
    \n        event = []\n        for x1, y1, x2, y2, w in self.rects:\n         \
    \   y1_ = bisect_left(toY, y1)\n            y2_ = bisect_left(toY, y2)\n     \
    \       event += [(x1, y1_, y2_, 0, w), (x2, y1_, y2_, 1, w)]\n        event.sort()\n\
    \n        qs = list(range(q))\n        qs.sort(key=lambda i: self.qs[i][0])\n\n\
    \        j = 0\n        bit = FenwickTree(len(toY) + 1)\n        for i in qs:\n\
    \            x, y = self.qs[i]\n            while j < n + n and event[j][0] <=\
    \ x:\n                y1, y2, f, w = event[j][1:]\n                if f:\n   \
    \                 bit.add(y1, -w)\n                    bit.add(y2, w)\n      \
    \          else:\n                    bit.add(y1, w)\n                    bit.add(y2,\
    \ -w)\n                j += 1\n            y = bisect_left(toY, y)\n         \
    \   res[i] = bit.sum0(y + 1)\n\n        return res\n\n\nclass OfflineRectangleAddPointGet:\n\
    \    def __init__(self):\n        self.queries = []\n\n    def add_rect(self,\
    \ x1: int, y1: int, x2: int, y2: int, w: int) -> None:\n        if x1 == x2 or\
    \ y1 == y2:\n            return\n        assert x1 <= x2 and y1 <= y2\n      \
    \  self.queries.append((x1, y1, x2, y2, w))\n\n    def add_query(self, x: int,\
    \ y: int) -> None:\n        self.queries.append((x, y))\n\n    def solve(self)\
    \ -> list[int]:\n        q = len(self.queries)\n        rev = [-1] * q\n     \
    \   sz = 0\n        for i in range(q):\n            if len(self.queries[i]) ==\
    \ 2:\n                rev[i] = sz\n                sz += 1\n\n        res = [0]\
    \ * sz\n        st = deque([(0, q)])\n        while st:\n            l, r = st.popleft()\n\
    \            m = (l + r) >> 1\n            solver = StaticRectangleAddPointGet()\n\
    \            for k in range(l, m):\n                if len(self.queries[k]) >\
    \ 2:\n                    x1, y1, x2, y2, w = self.queries[k]\n              \
    \      solver.add_rect(x1, y1, x2, y2, w)\n            for k in range(m, r):\n\
    \                if len(self.queries[k]) == 2:\n                    x, y = self.queries[k]\n\
    \                    solver.add_query(x, y)\n            sub = solver.solve()\n\
    \            t = 0\n            for k in range(m, r):\n                if len(self.queries[k])\
    \ == 2:\n                    i = rev[k]\n                    res[i] += sub[t]\n\
    \                    t += 1\n            if l + 1 < m:\n                st.append((l,\
    \ m))\n            if m + 1 < r:\n                st.append((m, r))\n        return\
    \ res\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  isVerificationFile: false
  path: geometory/offline_rectangle_add_point_get.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/rectangle_add_point_get.test.py
documentation_of: geometory/offline_rectangle_add_point_get.py
layout: document
title: "\u77E9\u5F62\u52A0\u7B97\u30FB\uFF11\u70B9\u53D6\u5F97(\u30AA\u30D5\u30E9\u30A4\
  \u30F3)"
---
