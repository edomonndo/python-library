---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: geometory/basic/circle.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u5186)"
  - icon: ':x:'
    path: geometory/basic/line.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u76F4\u7DDA\u30FB\u7DDA\
      \u5206)"
  - icon: ':warning:'
    path: geometory/basic/polygon.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u591A\u89D2\u5F62)"
  - icon: ':x:'
    path: geometory/basic/rectangle.py
    title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u56DB\u89D2\u5F62)"
  - icon: ':warning:'
    path: geometory/convex_layer.py
    title: geometory/convex_layer.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl/cgl_1_c_counter_clockwise.test.py
    title: "CGL1C \u53CD\u6642\u8A08\u56DE\u308A"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\nfrom typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass\
    \ Point:\n    def __init__(self, x: T, y: T):\n        self.EPS = 1e-10\n    \
    \    self.x = x\n        self.y = y\n\n    def __add__(self, other: \"Point\"\
    ) -> \"Point\":\n        return Point(self.x + other.x, self.y + other.y)\n\n\
    \    def __sub__(self, other: \"Point\") -> \"Point\":\n        return Point(self.x\
    \ - other.x, self.y - other.y)\n\n    def __mul__(self, k: \"Point\") -> \"Point\"\
    :\n        return Point(self.x * k, self.y * k)\n\n    def __truediv__(self, k:\
    \ \"Point\") -> \"Point\":\n        return Point(self.x / k, self.y / k)\n\n \
    \   def __floordiv__(self, k: \"Point\") -> \"Point\":\n        return Point(self.x\
    \ // k, self.y // k)\n\n    def __eq__(self, other: \"Point\") -> bool:\n    \
    \    return abs(self.x - other.x) < self.EPS and abs(self.y - other.y) < self.EPS\n\
    \n    def __ne__(self, other: \"Point\") -> bool:\n        return not self.__eq__(other)\n\
    \n    def __lt__(self, other: \"Point\") -> bool:\n        if self.x != other.x:\n\
    \            return self.x < other.x\n        return self.y < other.y\n\n    def\
    \ __gt__(self, other: \"Point\") -> bool:\n        if self.x != other.x:\n   \
    \         return self.x > other.x\n        return self.y > other.y\n\n    def\
    \ __str__(self) -> str:\n        return f\"<Point({self.x} {self.y})>\"\n\n  \
    \  __repr__ = __str__\n\n    def norm(self) -> T:\n        return self.x**2 +\
    \ self.y**2\n\n    def abs(self) -> T:\n        return self.norm() ** 0.5\n\n\
    \    def dot(self, other: \"Point\") -> T:\n        \"\"\"\u5185\u7A4D\"\"\"\n\
    \        return self.x * other.x + self.y * other.y\n\n    def cross(self, other:\
    \ \"Point\") -> T:\n        \"\"\"\u5916\u7A4D\"\"\"\n        return self.x *\
    \ other.y - self.y * other.x\n\n    def dist_euclid(self, other: \"Point\") ->\
    \ T:\n        \"\"\"\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u8DDD\u96E2\"\"\"\n \
    \       return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5\n\n\
    \    def dist_manhattan(self, other: \"Point\") -> T:\n        \"\"\"\u30DE\u30F3\
    \u30CF\u30C3\u30BF\u30F3\u8DDD\u96E2\"\"\"\n        return abs(self.x - other.x)\
    \ + abs(self.y - other.y)\n\n    def dist_chebyshev(self, other: \"Point\") ->\
    \ T:\n        \"\"\"\u30C1\u30A7\u30D3\u30B7\u30A7\u30D5\u8DDD\u96E2\"\"\"\n \
    \       return max(abs(self.x - other.x), abs(self.y - other.y))\n\n    def is_orthogonal(self,\
    \ other: \"Point\") -> bool:\n        \"\"\"\u76F4\u4EA4\u5224\u5B9A\"\"\"\n \
    \       return abs(self.dot(other)) < self.EPS\n\n    def is_parallel(self, other:\
    \ \"Point\") -> bool:\n        \"\"\"\u5E73\u884C\u5224\u5B9A\"\"\"\n        return\
    \ abs(self.cross(other)) < self.EPS\n\n    def ccw(self, other1: \"Point\", other2:\
    \ \"Point\") -> int:\n        \"\"\"\u81EA\u8EAB\u304B\u3089\u70B9other1\u306B\
    \u5411\u304B\u3046\u30D9\u30AF\u30C8\u30EB\u306B\u5BFE\u3057\u3066\uFF0C\u70B9\
    other2\u306E\u4F4D\u7F6E\u3092\u8FD4\u3059.\n        COUNTER_CLOCKWISE = 1\n \
    \       CLOCKWISE = -1\n        ONLINE_BACK = 2\n        ONLINE_FRONT = -2\n \
    \       ON_SEGMENT = 0\n        \"\"\"\n        a = other1 - self\n        b =\
    \ other2 - self\n        if a.cross(b) > self.EPS:\n            return 1\n   \
    \     if a.cross(b) < -self.EPS:\n            return -1\n        if a.dot(b) <\
    \ -self.EPS:\n            return 2\n        if a.norm() < b.norm():\n        \
    \    return -2\n        return 0\n\n    def arg(self) -> T:\n        return math.atan2(self.y,\
    \ self.x)\n\n    def get(self) -> T:\n        return self.x, self.y\n"
  dependsOn: []
  isVerificationFile: false
  path: geometory/basic/point.py
  requiredBy:
  - geometory/convex_layer.py
  - geometory/basic/polygon.py
  - geometory/basic/line.py
  - geometory/basic/circle.py
  - geometory/basic/rectangle.py
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/cgl/cgl_1_c_counter_clockwise.test.py
documentation_of: geometory/basic/point.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8(\u70B9)"
---
