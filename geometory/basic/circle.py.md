---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy:
  - icon: ':x:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
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
  code: "import math\nfrom typing import Union, TypeVar\n\nT = TypeVar(\"T\")\n\n\
    from geometory.basic.point import Point\n\n\nclass Circle:\n    def __init__(self,\
    \ center: Point, radius: int):\n        self.center = center\n        self.r =\
    \ radius\n\n    def __str__(self):\n        return f\"<Circle({self.center.x}\
    \ {self.center.y} {self.r})>\"\n\n    def _polar(self, a: T, r: T) -> Point:\n\
    \        return Point(math.cos(r) * a, math.sin(r) * a)\n\n    def get_diameter(self)\
    \ -> T:\n        return self.r * 2\n\n    def get_area(self) -> T:\n        return\
    \ math.pi * self.r * self.r\n\n    def intersect(self, other: \"Circle\") -> bool:\n\
    \        return self.center.dist_euclid(other.center) <= (self.r + other.r)\n\n\
    \    def get_cross_point(self, other: \"Circle\") -> tuple[T, T]:\n        if\
    \ not self.intersect(other):\n            return -1\n        d = (self.center\
    \ - other.center).abs()\n        a = math.acos((self.r**2 + d**2 - other.r**2)\
    \ / (2 * self.r * d))\n        t = (other.center - self.center).arg()\n      \
    \  p1, p2 = self.center + self._polar(self.r, t + a), self.center + self._polar(\n\
    \            self.r, t - a\n        )\n        if p1.x == p2.x and p1.y > p2.y:\n\
    \            p1, p2 = p2, p1\n        elif p1.x > p2.x:\n            p1, p2 =\
    \ p2, p1\n        return p1, p2\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/basic/circle.py
  requiredBy:
  - geometory/basic/line.py
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: geometory/basic/circle.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u5186)"
---
