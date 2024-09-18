---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_7_a_intersection.test.py
    title: "CGL7A \u5186\u306E\u4EA4\u5DEE\u5224\u5B9A"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_7_b_incircle_of_a_triangle.test.py
    title: "CGL7B \u5185\u63A5\u5186"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nfrom typing import TypeVar, Union\n\nT = TypeVar(\"T\")\n\n\
    from geometory.basic.point import Point\n\n\nclass Circle:\n    def __init__(self,\
    \ center: Point, radius: int):\n        self.center = center\n        self.r =\
    \ radius\n\n    @staticmethod\n    def from_int(x: T, y: T, radius: int) -> \"\
    Circle\":\n        return Circle(Point(x, y), radius)\n\n    def __str__(self):\n\
    \        return f\"<Circle({self.center.x} {self.center.y} {self.r})>\"\n\n  \
    \  def _polar(self, a: T, r: T) -> Point:\n        return Point(math.cos(r) *\
    \ a, math.sin(r) * a)\n\n    def get_diameter(self) -> T:\n        return self.r\
    \ * 2\n\n    def get_area(self) -> T:\n        return math.pi * self.r * self.r\n\
    \n    def is_intersect(self, other: \"Circle\") -> bool:\n        return self.center.dist_euclid(other.center)\
    \ <= (self.r + other.r)\n\n    def intersect(self, other: \"Circle\") -> int:\n\
    \        \"\"\"\u8FD4\u308A\u5024\u306F\u5171\u901A\u63A5\u7DDA\u306E\u6570\"\"\
    \"\n        d2 = (self.center - other.center).norm()\n        r2 = (self.r + other.r)\
    \ ** 2\n        if d2 > r2:\n            return 4  # \u63A5\u3057\u3066\u3044\u306A\
    \u3044\n        if d2 == r2:\n            return 3  # \u5916\u63A5\n        r2\
    \ = (self.r - other.r) ** 2\n        if d2 == r2:\n            return 1  # \u5185\
    \u63A5\n        if d2 < r2:\n            return 0  # \u5185\u5305\n        return\
    \ 2  # \u4EA4\u308F\u308B\n\n    def get_cross_point(self, other: \"Circle\")\
    \ -> Union[tuple[T, T], int]:\n        if not self.is_intersect(other):\n    \
    \        return -1\n        d = (self.center - other.center).abs()\n        a\
    \ = math.acos((self.r**2 + d**2 - other.r**2) / (2 * self.r * d))\n        t =\
    \ (other.center - self.center).arg()\n        p1, p2 = self.center + self._polar(self.r,\
    \ t + a), self.center + self._polar(\n            self.r, t - a\n        )\n \
    \       if p1.x == p2.x and p1.y > p2.y:\n            p1, p2 = p2, p1\n      \
    \  elif p1.x > p2.x:\n            p1, p2 = p2, p1\n        return p1, p2\n\n \
    \   @staticmethod\n    def from_triangle(x1: T, y1: T, x2: T, y2: T, x3: T, y3:\
    \ T) -> \"Circle\":\n        a, b, c = Point(x1, y1), Point(x2, y2), Point(x3,\
    \ y3)\n        ab, bc, ca = (a - b).abs(), (b - c).abs(), (c - a).abs()\n    \
    \    center = (a * bc + b * ca + c * ab) / (ab + bc + ca)\n        # Line.get_distance_segment_from_point\n\
    \        vec = b - a\n        if vec.dot(center - a) < 0:\n            r = (center\
    \ - a).abs()\n        elif vec.dot(b - center) < 0:\n            r = (center -\
    \ b).abs()\n        else:\n            r = abs(vec.cross(center - a) / vec.abs())\n\
    \        return Circle(center, r)\n"
  dependsOn:
  - geometory/basic/point.py
  isVerificationFile: false
  path: geometory/basic/circle.py
  requiredBy:
  - geometory/basic/line.py
  timestamp: '2024-08-15 10:59:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/cgl/cgl_7_b_incircle_of_a_triangle.test.py
  - test/aoj/cgl/cgl_7_a_intersection.test.py
documentation_of: geometory/basic/circle.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u5186)"
---
