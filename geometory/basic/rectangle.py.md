---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_4_a_union_of_rectangles_basic.test.py
    title: "DSL4A Union of Rectangles (\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8\
      )"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar\n\nT = TypeVar(\"T\")\n\nfrom geometory.basic.point\
    \ import Point\n\n\nclass Rectangle:\n    def __init__(self, top_left: Point,\
    \ bottom_right: Point):\n        self.top_left = top_left\n        self.bottom_right\
    \ = bottom_right\n\n    @classmethod\n    def from_int(cls, x1: T, y1: T, x2:\
    \ T, y2: T) -> \"Rectangle\":\n        return Rectangle(Point(x1, y1), Point(x2,\
    \ y2))\n\n    def __str__(self):\n        return f\"<Rect({self.top_left}, {self.bottom_right})>\"\
    \n\n    def sub(self, other: \"Rectangle\"):\n        xs1, ys1 = self.top_left.get()\n\
    \        xs2, ys2 = self.bottom_right.get()\n        xo1, yo1 = other.top_left.get()\n\
    \        xo2, yo2 = other.bottom_right.get()\n\n        if xs1 < xo1:\n      \
    \      yield Rectangle(Point(xs1, ys1), Point(xo1, ys2))\n        if xs2 > xo2:\n\
    \            yield Rectangle(Point(xo2, ys1), Point(xs2, ys2))\n        if ys1\
    \ < yo1:\n            yield Rectangle(Point(max(xs1, xo1), ys1), Point(min(xs2,\
    \ xo2), yo1))\n        if ys2 > yo2:\n            yield Rectangle(Point(max(xs1,\
    \ xo1), yo2), Point(min(xs2, xo2), ys2))\n\n    def intersect(self, other: \"\
    Rectangle\") -> bool:\n        xs1, ys1 = self.top_left.get()\n        xs2, ys2\
    \ = self.bottom_right.get()\n        xo1, yo1 = other.top_left.get()\n       \
    \ xo2, yo2 = other.bottom_right.get()\n\n        if xs1 >= xo2:\n            return\
    \ False\n        elif xs2 <= xo1:\n            return False\n\n        if ys1\
    \ >= yo2:\n            return False\n        elif ys2 <= yo1:\n            return\
    \ False\n        return True\n\n    def get_area(self) -> T:\n        return (self.bottom_right.x\
    \ - self.top_left.x) * (\n            self.bottom_right.y - self.top_left.y\n\
    \        )\n\n\nclass Rectangles:\n    def __init__(self):\n        self.rects\
    \ = []\n\n    def __str__(self):\n        return \"<Rects(\" + \"\\n \".join(str(r)\
    \ for r in self.rects) + \")>\"\n\n    def add(self, rect: Rectangle) -> None:\n\
    \        rects = []\n        for r in self.rects:\n            if rect.intersect(r):\n\
    \                rects.extend(r.sub(rect))\n            else:\n              \
    \  rects.append(r)\n        rects.append(rect)\n        self.rects = rects\n\n\
    \    def area(self) -> T:\n        \"\"\"O(n^2)\"\"\"\n        return sum(r.get_area()\
    \ for r in self.rects)\n\n    def not_intersect(self) -> bool:\n        n = len(self.rects)\n\
    \        for i in range(n - 1):\n            for j in range(i + 1, n):\n     \
    \           if self.rects[i].intersect(self.rects[j]):\n                    return\
    \ False\n        return True\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/basic/rectangle.py
  requiredBy: []
  timestamp: '2024-08-09 19:58:16+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl/dsl_4_a_union_of_rectangles_basic.test.py
documentation_of: geometory/basic/rectangle.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u56DB\u89D2\u5F62)"
---
