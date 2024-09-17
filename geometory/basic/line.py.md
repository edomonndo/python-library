---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/circle.py
    title: geometory/basic/circle.py
  - icon: ':heavy_check_mark:'
    path: geometory/basic/point.py
    title: geometory/basic/point.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: geometory/basic/polygon.py
    title: geometory/basic/polygon.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_1_a_projection.test.py
    title: "CGL1A \u5C04\u5F71"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_1_b_refrection.test.py
    title: "CGL1B \u53CD\u5C04"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_2_a_parallel_orthogonal.test.py
    title: "CGL2A \u5E73\u884C\u30FB\u5782\u76F4"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_2_b_intersection.test.py
    title: "CGL2B \u4EA4\u5DEE\u5224\u5B9A"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_2_c_cross_point.test.py
    title: "CGL2C \u4EA4\u70B9"
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_2_d_distance.test.py
    title: "CGL2D \u8DDD\u96E2"
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
    \ import Point\nfrom geometory.basic.circle import Circle\n\n\nclass Line:\n \
    \   def __init__(self, p1: Point, p2: Point):\n        self.EPS = 1e-10\n    \
    \    self.s = p1\n        self.t = p2\n        self.vector = p2 - p1\n\n    def\
    \ __str__(self):\n        return f\"<Line({self.s.x} {self.s.y} {self.t.x} {self.t.y})>\"\
    \n\n    @classmethod\n    def from_int(cls, x1: T, y1: T, x2: T, y2: T) -> \"\
    Line\":\n        return Line(Point(x1, y1), Point(x2, y2))\n\n    def is_orthogonal(self,\
    \ other: \"Line\") -> bool:\n        return abs(self.vector.dot(other.vector))\
    \ < self.EPS\n\n    def is_parallel(self, other: \"Line\") -> bool:\n        return\
    \ abs(self.vector.cross(other.vector)) < self.EPS\n\n    def project_from_point(self,\
    \ point: Point) -> Point:\n        \"\"\"\u76F4\u7DDA\u306B\u70B9point\u304B\u3089\
    \u5782\u7DDA\u3092\u5F15\u3044\u305F\u3068\u304D\u306E\u4EA4\u70B9\"\"\"\n   \
    \     r = self.vector.dot(point - self.s) / self.vector.norm()\n        return\
    \ self.s + self.vector * r\n\n    def project(self, x: T, y: T) -> Point:\n  \
    \      return self.project_from_point(Point(x, y))\n\n    def refrection_from_point(self,\
    \ point: Point) -> Point:\n        \"\"\"\u76F4\u7DDA\u3092\u5BFE\u79F0\u8EF8\u3068\
    \u3057\u3066\uFF0C\u70B9point\u3068\u7DDA\u5BFE\u79F0\u306A\u70B9\u306E\u5EA7\u6A19\
    \"\"\"\n        return point + (self.project_from_point(point) - point) * 2\n\n\
    \    def refrection(self, x: T, y: T) -> Point:\n        return self.refrection_from_point(Point(x,\
    \ y))\n\n    def get_distance_from_point(self, point: Point) -> T:\n        \"\
    \"\"\u76F4\u7DDA\u3068\u70B9\u306E\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u8DDD\u96E2\
    \"\"\"\n        return abs(self.vector.cross(point - self.s) / self.vector.abs())\n\
    \n    def get_distance(self, x: T, y: T) -> T:\n        return self.get_distance_from_point(Point(x,\
    \ y))\n\n    def get_distance_segment_from_point(self, point: Point) -> T:\n \
    \       \"\"\"\u7DDA\u5206\u3068\u70B9\u306E\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\
    \u8DDD\u96E2\"\"\"\n        if self.vector.dot(point - self.s) < 0:\n        \
    \    p = point - self.s\n            return p.abs()\n        if self.vector.dot(self.t\
    \ - point) < 0:\n            p = point - self.t\n            return p.abs()\n\
    \        return self.get_distance_from_point(point)\n\n    def get_distance_segment(self,\
    \ x: T, y: T) -> T:\n        return self.get_distance_segment_from_point(Point(x,\
    \ y))\n\n    def get_distance_seg_to_seg(self, other: \"Line\") -> int:\n    \
    \    \"\"\"\u7DDA\u5206\u3068\u7DDA\u5206\u306E\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\
    \u8DDD\u96E2\"\"\"\n        if self.intersect(other):\n            return 0\n\
    \        return min(\n            self.get_distance_segment_from_point(other.s),\n\
    \            self.get_distance_segment_from_point(other.t),\n            other.get_distance_segment_from_point(self.s),\n\
    \            other.get_distance_segment_from_point(self.t),\n        )\n\n   \
    \ def intersect(self, other: Union[\"Line\", Circle]) -> bool:\n        if isinstance(other,\
    \ Line):\n            return (\n                self.s.ccw(self.t, other.s) *\
    \ self.s.ccw(self.t, other.t) <= 0\n                and other.s.ccw(other.t, self.s)\
    \ * other.s.ccw(other.t, self.t) <= 0\n            )\n        if isinstance(other,\
    \ Circle):\n            return self.get_distance_from_point(other.center) <= other.r\n\
    \        raise TypeError\n\n    def get_cross_point(self, other: Union[\"Line\"\
    , Circle]) -> Union[Point, int]:\n        if isinstance(other, Line):\n      \
    \      if not self.intersect(other):\n                return -1\n            d1\
    \ = abs(other.vector.cross(self.s - other.t))\n            d2 = abs(other.vector.cross(self.t\
    \ - other.t))\n            t = d1 / (d1 + d2)\n            return self.s + (self.vector)\
    \ * t\n        if isinstance(other, Circle):\n            if not self.intersect(other):\n\
    \                return -1\n            pr = self.project(other.center)\n    \
    \        e = self.vector / self.vector.abs()\n            base = (other.r**2 -\
    \ (pr - other.center).norm()) ** 0.5\n            p1, p2 = pr + e * base, pr -\
    \ e * base\n            if p1.x == p2.x:\n                return (p1, p2) if p1.y\
    \ < p2.y else (p2, p1)\n            if p1.x < p2.x:\n                return (p1,\
    \ p2)\n            return (p2, p1)\n        raise TypeError\n"
  dependsOn:
  - geometory/basic/point.py
  - geometory/basic/circle.py
  isVerificationFile: false
  path: geometory/basic/line.py
  requiredBy:
  - geometory/basic/polygon.py
  timestamp: '2024-08-15 10:59:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/cgl/cgl_2_d_distance.test.py
  - test/aoj/cgl/cgl_1_a_projection.test.py
  - test/aoj/cgl/cgl_2_b_intersection.test.py
  - test/aoj/cgl/cgl_1_b_refrection.test.py
  - test/aoj/cgl/cgl_2_a_parallel_orthogonal.test.py
  - test/aoj/cgl/cgl_2_c_cross_point.test.py
documentation_of: geometory/basic/line.py
layout: document
redirect_from:
- /library/geometory/basic/line.py
- /library/geometory/basic/line.py.html
title: geometory/basic/line.py
---
