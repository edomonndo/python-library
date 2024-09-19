---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_3_a_area.test.py
    title: "CGL3A \u9762\u7A4D"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_3_b_is_convex.test.py
    title: "CGL3B \u51F8\u6027\u5224\u5B9A"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_3_c_polygon_point_containment.test.py
    title: "CGL3C \u591A\u89D2\u5F62 \u70B9\u306E\u5305\u542B"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from geometory.basic.point import Point\nfrom geometory.basic.line import\
    \ Line\n\nfrom typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass Polygon:\n\
    \    def __init__(self, arr: list[Point]):\n        \"\"\"\n        \u914D\u5217\
    arr\u306F\uFF0C\u591A\u89D2\u5F62\u306E\u96A3\u308A\u5408\u3063\u305F\u70B9\u3092\
    \u53CD\u6642\u8A08\u56DE\u308A\u306B\u8A2A\u554F\u3059\u308B\u9806\u756A\u3067\
    \u3042\u308B\u3053\u3068\uFF0E\n        \"\"\"\n        self.arr = arr\n     \
    \   self.n = len(arr)\n\n    def __len__(self) -> int:\n        return self.n\n\
    \n    def __getitem__(self, idx: int) -> Point:\n        return self.arr[idx]\n\
    \n    def contains(self, p: Point) -> int:\n        \"\"\"\n        \u70B9p\u304C\
    \u591A\u89D2\u5F62\u306B\u5185\u5305\u3055\u308C\u3066\u3044\u308B\u304B\u5224\
    \u5B9A\n        IN 2\n        ON 1\n        OUT 0\n        \"\"\"\n        x =\
    \ 0\n        for i in range(self.n):\n            a = self.arr[i] - p\n      \
    \      b = self.arr[(i + 1) % self.n] - p\n            if abs(a.cross(b)) < p.EPS\
    \ and a.dot(b) < p.EPS:\n                return 1\n            if a.y > b.y:\n\
    \                a, b = b, a\n            if a.y < p.EPS and p.EPS < b.y and a.cross(b)\
    \ > p.EPS:\n                x ^= 1\n        return 2 if x else 0\n\n    def is_convex(self)\
    \ -> bool:\n        for i in range(self.n):\n            pre = (i - 1) % self.n\n\
    \            nex = (i + 1) % self.n\n            if self.arr[pre].ccw(self.arr[i],\
    \ self.arr[nex]) == -1:\n                return False\n        return True\n\n\
    \    def area(self) -> T:\n        res = self.arr[-1].cross(self.arr[0])\n   \
    \     for i in range(self.n - 1):\n            res += self.arr[i].cross(self.arr[i\
    \ + 1])\n        return abs(res) / 2\n\n    def divide_by_segment(self, seg: Line)\
    \ -> int:\n        lines = [Line(self.arr[i], self.arr[(i + 1) % self.n]) for\
    \ i in range(self.n)]\n        cnt = sum(1 for line in lines if line.intersect(seg))\n\
    \        return (cnt >> 1) + 1\n\n    def convex_hull(ps: list[Point]) -> list[Point]:\n\
    \n        ps = list(set(ps))\n        if len(ps) <= 2:\n            return ps\n\
    \n        ps.sort()\n        res = []\n\n        def cross3(a: Point, b: Point,\
    \ c: Point) -> int:\n            return (b.x - a.x) * (c.y - a.y) - (b.y - a.y)\
    \ * (c.x - a.x)\n\n        for p in ps:\n            while len(res) > 1 and cross3(res[-1],\
    \ res[-2], p) >= 0:\n                res.pop()\n            res.append(p)\n\n\
    \        sz = len(res)\n        for p in ps[::-1][1:]:\n            while len(res)\
    \ > sz and cross3(res[-1], res[-2], p) >= 0:\n                res.pop()\n    \
    \        res.append(p)\n        res.pop()\n        return res\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/basic/line.py
  isVerificationFile: false
  path: geometory/basic/polygon.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/cgl/cgl_3_a_area.test.py
  - test/aoj/cgl/cgl_3_b_is_convex.test.py
  - test/aoj/cgl/cgl_3_c_polygon_point_containment.test.py
documentation_of: geometory/basic/polygon.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u591A\u89D2\u5F62)"
---
