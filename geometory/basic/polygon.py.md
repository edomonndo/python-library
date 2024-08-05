---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from geometory.basic.point import Point\nfrom geometory.basic.line import\
    \ Line\n\n\nclass Polygon:\n    def __init__(self, arr: list[Point]):\n      \
    \  \"\"\"\n        \u914D\u5217arr\u306F\uFF0C\u591A\u89D2\u5F62\u306E\u96A3\u308A\
    \u5408\u3063\u305F\u70B9\u3092\u53CD\u6642\u8A08\u56DE\u308A\u306B\u8A2A\u554F\
    \u3059\u308B\u9806\u756A\u3067\u3042\u308B\u3053\u3068\uFF0E\n        \"\"\"\n\
    \        self.arr = arr\n        self.n = len(arr)\n\n    def __len__(self) ->\
    \ int:\n        return self.n\n\n    def __getitem__(self, idx: int) -> Point:\n\
    \        return self.arr[idx]\n\n    def contains(self, p: Point) -> int:\n  \
    \      \"\"\"\n        \u70B9p\u304C\u591A\u89D2\u5F62\u306B\u5185\u5305\u3055\
    \u308C\u3066\u3044\u308B\u304B\u5224\u5B9A\n        IN 2\n        ON 1\n     \
    \   OUT 0\n        \"\"\"\n        x = False\n        for i in range(self.n):\n\
    \            a = self.arr[i] - p\n            b = self.arr[(i + 1) % self.n] -\
    \ p\n            if abs(a.cross(b)) < p.EPS and a.dot(b) < p.EPS:\n          \
    \      return 1\n            if a.y > b.y:\n                a, b = b, a\n    \
    \        if a.y < p.EPS and p.EPS < b.y and a.cross(b) > p.EPS:\n            \
    \    x = True\n        return 2 if x else 0\n\n    def divide_by_segment(self,\
    \ seg: Line) -> int:\n        lines = [Line(self.arr[i], self.arr[(i + 1) % self.n])\
    \ for i in range(self.n)]\n        cnt = sum(1 for line in lines if line.intersect(seg))\n\
    \        return (cnt >> 1) + 1\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/basic/line.py
  isVerificationFile: false
  path: geometory/basic/polygon.py
  requiredBy: []
  timestamp: '2024-08-05 21:31:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: geometory/basic/polygon.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u591A\u89D2\u5F62)"
---
