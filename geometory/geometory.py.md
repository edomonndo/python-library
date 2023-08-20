---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/aoj/cgl_1_a_projection.test.py
    title: test/aoj/cgl_1_a_projection.test.py
  - icon: ':x:'
    path: test/aoj/cgl_1_b_refrection.test.py
    title: test/aoj/cgl_1_b_refrection.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl_1_c_counter_clockwise.test.py
    title: test/aoj/cgl_1_c_counter_clockwise.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl_2_a_parallel_orthogonal.test.py
    title: test/aoj/cgl_2_a_parallel_orthogonal.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/cgl_2_b_intersection.test.py
    title: test/aoj/cgl_2_b_intersection.test.py
  - icon: ':x:'
    path: test/aoj/cgl_2_c_cross_point.test.py
    title: test/aoj/cgl_2_c_cross_point.test.py
  - icon: ':x:'
    path: test/aoj/cgl_2_d_distance.test.py
    title: test/aoj/cgl_2_d_distance.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_4_a_union_of_rectangles.test.py
    title: test/aoj/dsl_4_a_union_of_rectangles.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\n\nclass Point:\n    def __init__(self, x, y):\n        self.EPS\
    \ = 1e-10\n        self.x = x\n        self.y = y\n\n    def __add__(self, other):\n\
    \        return Point(self.x + other.x, self.y + other.y)\n\n    def __sub__(self,\
    \ other):\n        return Point(self.x - other.x, self.y - other.y)\n\n    def\
    \ __mul__(self, k):\n        return Point(self.x * k, self.y * k)\n\n    def __truediv__(self,\
    \ k):\n        return Point(self.x / k, self.y / k)\n\n    def __floordiv__(self,\
    \ k):\n        return Point(self.x // k, self.y // k)\n\n    def __eq__(self,\
    \ other):\n        return abs(self.x - other.x) < self.EPS and abs(self.y - other.y)\
    \ < self.EPS\n\n    def __ne__(self, other):\n        return not self.__eq__(other)\n\
    \n    def __lt__(self, other):\n        if self.x != other.x:\n            return\
    \ self.x < other.x\n        return self.y < other.y\n\n    def __gt__(self, other):\n\
    \        if self.x != other.x:\n            return self.x > other.x\n        return\
    \ self.y > other.y\n\n    def __str__(self):\n        return f\"<Point({self.x}\
    \ {self.y})>\"\n\n    def norm(self):\n        return self.x**2 + self.y**2\n\n\
    \    def abs(self):\n        return self.norm() ** 0.5\n\n    def dot(self, other):\n\
    \        \"\"\"\u5185\u7A4D\"\"\"\n        return self.x * other.x + self.y *\
    \ other.y\n\n    def cross(self, other):\n        \"\"\"\u5916\u7A4D\"\"\"\n \
    \       return self.x * other.y - self.y * other.x\n\n    def dist_euclid(self,\
    \ other):\n        \"\"\"\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u8DDD\u96E2\"\"\"\
    \n        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5\n\n\
    \    def dist_manhattan(self, other):\n        \"\"\"\u30DE\u30F3\u30CF\u30C3\u30BF\
    \u30F3\u8DDD\u96E2\"\"\"\n        return abs(self.x - other.x) + abs(self.y -\
    \ other.y)\n\n    def dist_chebyshev(self, other):\n        \"\"\"\u30C1\u30A7\
    \u30D3\u30B7\u30A7\u30D5\u8DDD\u96E2\"\"\"\n        return max(abs(self.x - other.x),\
    \ abs(self.y - other.y))\n\n    def is_orthogonal(self, other):\n        \"\"\"\
    \u76F4\u4EA4\u5224\u5B9A\"\"\"\n        return abs(self.dot(other)) < self.EPS\n\
    \n    def is_parallel(self, other):\n        \"\"\"\u5E73\u884C\u5224\u5B9A\"\"\
    \"\n        return abs(self.cross(other)) < self.EPS\n\n    def ccw(self, other1,\
    \ other2):\n        \"\"\"\u81EA\u8EAB\u304B\u3089\u70B9other1\u306B\u5411\u304B\
    \u3046\u30D9\u30AF\u30C8\u30EB\u306B\u5BFE\u3057\u3066\uFF0C\u70B9other2\u306E\
    \u4F4D\u7F6E\u3092\u8FD4\u3059.\n        COUNTER_CLOCKWISE = 1\n        CLOCKWISE\
    \ = -1\n        ONLINE_BACK = 2\n        ONLINE_FRONT = -2\n        ON_SEGMENT\
    \ = 0\n        \"\"\"\n        a = other1 - self\n        b = other2 - self\n\
    \        if a.cross(b) > self.EPS:\n            return 1\n        if a.cross(b)\
    \ < -self.EPS:\n            return -1\n        if a.dot(b) < -self.EPS:\n    \
    \        return 2\n        if a.norm() < b.norm():\n            return -2\n  \
    \      return 0\n\n    def arg(self):\n        return math.atan2(self.y, self.x)\n\
    \n    def get(self):\n        return self.x, self.y\n\n\nclass Line:\n    def\
    \ __init__(self, p1: Point, p2: Point):\n        self.EPS = 1e-10\n        self.s\
    \ = p1\n        self.t = p2\n        self.vector = p2 - p1\n\n    def __str__(self):\n\
    \        return f\"<Line({self.s.x} {self.s.y} {self.t.x} {self.t.y})>\"\n\n \
    \   def is_orthogonal(self, other):\n        return abs(self.vector.dot(other.vector))\
    \ < self.EPS\n\n    def is_parallel(self, other):\n        return abs(self.vector.cross(other.vector))\
    \ < self.EPS\n\n    def project(self, point):\n        \"\"\"\u76F4\u7DDA\u306B\
    \u70B9point\u304B\u3089\u5782\u7DDA\u3092\u5F15\u3044\u305F\u3068\u304D\u306E\u4EA4\
    \u70B9\"\"\"\n        r = self.vector.dot(point - self.s) / self.vector.norm()\n\
    \        return self.s + self.vector * r\n\n    def refrection(self, point):\n\
    \        \"\"\"\u76F4\u7DDA\u3092\u5BFE\u79F0\u8EF8\u3068\u3057\u3066\uFF0C\u70B9\
    point\u3068\u7DDA\u5BFE\u79F0\u306A\u70B9\u306E\u5EA7\u6A19\"\"\"\n        return\
    \ point + (self.project(point) - point) * 2\n\n    def get_distance(self, point):\n\
    \        \"\"\"\u76F4\u7DDA\u3068\u70B9\u306E\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\
    \u8DDD\u96E2\"\"\"\n        return abs(self.vector.cross(point - self.s) / self.vector.abs())\n\
    \n    def get_distance_segment(self, point):\n        \"\"\"\u7DDA\u5206\u3068\
    \u70B9\u306E\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u8DDD\u96E2\"\"\"\n        if\
    \ self.vector.dot(point - self.s) < 0:\n            p = point - self.s\n     \
    \       return p.abs()\n        if self.vector.dot(self.t - point) < 0:\n    \
    \        p = point - self.t\n            return p.abs()\n        return self.get_distance(point)\n\
    \n    def get_distance_seg_to_seg(self, other):\n        \"\"\"\u7DDA\u5206\u3068\
    \u7DDA\u5206\u306E\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u8DDD\u96E2\"\"\"\n   \
    \     if self.intersect(other):\n            return 0\n        return min(\n \
    \           self.get_distance_segment(other.s),\n            self.get_distance_segment(other.t),\n\
    \            other.get_distance_segment(self.s),\n            other.get_distance_segment(self.t),\n\
    \        )\n\n    def intersect(self, other):\n        if isinstance(other, Line):\n\
    \            return (\n                self.s.ccw(self.t, other.s) * self.s.ccw(self.t,\
    \ other.t) <= 0\n                and other.s.ccw(other.t, self.s) * other.s.ccw(other.t,\
    \ self.t) <= 0\n            )\n        if isinstance(other, Circle):\n       \
    \     return self.get_distance(other.center) <= other.r\n        raise TypeError\n\
    \n    def get_cross_point(self, other):\n        if isinstance(other, Line):\n\
    \            if not self.intersect(other):\n                return -1\n      \
    \      d1 = abs(other.vector.cross(self.s - other.t))\n            d2 = abs(other.vector.cross(self.t\
    \ - other.t))\n            t = d1 / (d1 + d2)\n            return self.s + (self.vector)\
    \ * t\n        if isinstance(other, Circle):\n            if not self.intersect(other):\n\
    \                return -1\n            pr = self.project(other.center)\n    \
    \        e = self.vector / self.vector.abs()\n            base = (other.r**2 -\
    \ (pr - other.center).norm()) ** 0.5\n            p1, p2 = pr + e * base, pr -\
    \ e * base\n            if p1.x == p2.x:\n                return (p1, p2) if p1.y\
    \ < p2.y else (p2, p1)\n            if p1.x < p2.x:\n                return (p1,\
    \ p2)\n            return (p2, p1)\n        raise TypeError\n\n\nclass Circle:\n\
    \    def __init__(self, center: Point, radius):\n        self.center = center\n\
    \        self.r = radius\n\n    def __str__(self):\n        return f\"<Circle({self.center.x}\
    \ {self.center.y} {self.r})>\"\n\n    def get_diameter(self):\n        return\
    \ self.r * 2\n\n    def get_area(self):\n        return math.pi * self.r * self.r\n\
    \n    def intersect(self, other):\n        if isinstance(other, Line):\n     \
    \       return other.get_distance(self.center) <= self.r\n        elif isinstance(other,\
    \ Circle):\n            return self.center.dist_euclid(other.center) <= (self.r\
    \ + other.r)\n        else:\n            raise TypeError\n\n    def get_cross_point(self,\
    \ other):\n        if isinstance(other, Line):\n            if not other.intersect(self):\n\
    \                return -1\n            pr = other.project(self.center)\n    \
    \        e = other.vector / other.vector.abs()\n            base = (self.r**2\
    \ - (pr - self.center).norm()) ** 0.5\n            p1, p2 = pr + e * base, pr\
    \ - e * base\n            if p1.x == p2.x and p1.y > p2.y:\n                p1,\
    \ p2 = p2, p1\n            elif p1.x > p2.x:\n                p1, p2 = p2, p1\n\
    \            return p1, p2\n        elif isinstance(other, Circle):\n        \
    \    if not self.intersect(other):\n                return -1\n            d =\
    \ (self.center - other.center).abs()\n            a = math.acos((self.r**2 + d**2\
    \ - other.r**2) / (2 * self.r * d))\n            t = (other.center - self.center).arg()\n\
    \            p1, p2 = self.center + self._polar(\n                self.r, t +\
    \ a\n            ), self.center + self._polar(self.r, t - a)\n            if p1.x\
    \ == p2.x and p1.y > p2.y:\n                p1, p2 = p2, p1\n            elif\
    \ p1.x > p2.x:\n                p1, p2 = p2, p1\n            return p1, p2\n \
    \       else:\n            raise TypeError\n\n    def _polar(self, a, r):\n  \
    \      return Point(math.cos(r) * a, math.sin(r) * a)\n\n\nclass Rectangle:\n\
    \    def __init__(self, top_left, bottom_right):\n        self.top_left = top_left\n\
    \        self.bottom_right = bottom_right\n\n    def __str__(self):\n        return\
    \ f\"<Rect({self.top_left}, {self.bottom_right})>\"\n\n    def sub(self, other):\n\
    \        xs1, ys1 = self.top_left.get()\n        xs2, ys2 = self.bottom_right.get()\n\
    \        xo1, yo1 = other.top_left.get()\n        xo2, yo2 = other.bottom_right.get()\n\
    \n        if xs1 < xo1:\n            yield Rectangle(Point(xs1, ys1), Point(xo1,\
    \ ys2))\n        if xs2 > xo2:\n            yield Rectangle(Point(xo2, ys1), Point(xs2,\
    \ ys2))\n        if ys1 < yo1:\n            yield Rectangle(Point(max(xs1, xo1),\
    \ ys1), Point(min(xs2, xo2), yo1))\n        if ys2 > yo2:\n            yield Rectangle(Point(max(xs1,\
    \ xo1), yo2), Point(min(xs2, xo2), ys2))\n\n    def intersect(self, other):\n\
    \        xs1, ys1 = self.top_left.get()\n        xs2, ys2 = self.bottom_right.get()\n\
    \        xo1, yo1 = other.top_left.get()\n        xo2, yo2 = other.bottom_right.get()\n\
    \n        if xs1 >= xo2:\n            return False\n        elif xs2 <= xo1:\n\
    \            return False\n\n        if ys1 >= yo2:\n            return False\n\
    \        elif ys2 <= yo1:\n            return False\n        return True\n\n \
    \   def get_area(self):\n        return (self.bottom_right.x - self.top_left.x)\
    \ * (\n            self.bottom_right.y - self.top_left.y\n        )\n\n\nclass\
    \ Rectangles:\n    def __init__(self):\n        self.rects = []\n\n    def __str__(self):\n\
    \        return \"<Rects(\" + \"\\n \".join(str(r) for r in self.rects) + \")>\"\
    \n\n    def add(self, rect):\n        rects = []\n        for r in self.rects:\n\
    \            if rect.intersect(r):\n                rects.extend(r.sub(rect))\n\
    \            else:\n                rects.append(r)\n        rects.append(rect)\n\
    \        self.rects = rects\n\n    def area(self):\n        return sum(r.get_area()\
    \ for r in self.rects)\n\n    def not_intersect(self):\n        N = len(self.rects)\n\
    \        for i in range(N - 1):\n            for j in range(i + 1, N):\n     \
    \           if self.rects[i].intersect(self.rects[j]):\n                    return\
    \ False\n        return True\n\n\nclass Polygon:\n    def __init__(self, arr):\n\
    \        \"\"\"\n        \u914D\u5217arr\u306F\uFF0C\u591A\u89D2\u5F62\u306E\u96A3\
    \u308A\u5408\u3063\u305F\u70B9\u3092\u53CD\u6642\u8A08\u56DE\u308A\u306B\u8A2A\
    \u554F\u3059\u308B\u9806\u756A\u3067\u3042\u308B\u3053\u3068\uFF0E\n        \"\
    \"\"\n        self.arr = arr\n        self.n = len(arr)\n\n    def __len__(self):\n\
    \        return self.n\n\n    def __getitem__(self, idx):\n        return self.arr[idx]\n\
    \n    def contains(self, p):\n        \"\"\"\n        \u70B9p\u304C\u591A\u89D2\
    \u5F62\u306B\u5185\u5305\u3055\u308C\u3066\u3044\u308B\u304B\u5224\u5B9A\n   \
    \     IN 2\n        ON 1\n        OUT 0\n        \"\"\"\n        x = False\n \
    \       for i in range(self.n):\n            a = self.arr[i] - p\n           \
    \ b = self.arr[(i + 1) % self.n] - p\n            if abs(a.cross(b)) < p.EPS and\
    \ a.dot(b) < p.EPS:\n                return 1\n            if a.y > b.y:\n   \
    \             a, b = b, a\n            if a.y < p.EPS and p.EPS < b.y and a.cross(b)\
    \ > p.EPS:\n                x = True\n        return 2 if x else 0\n\n    def\
    \ convex_hull(self):\n        \"\"\"\n        \u30A2\u30F3\u30C9\u30EA\u30E5\u30FC\
    \u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0\uFF0E\n        \"\"\"\n        if self.n\
    \ < 3:\n            return -1\n        arr = sorted(self.arr)\n        upper =\
    \ [arr[0], arr[1]]  # x\u304C\u5C0F\u3055\u3044\u3082\u306E\u304B\u30892\u3064\
    \u8FFD\u52A0\n        # \u51F8\u5305\u306E\u4E0A\u90E8\u3092\u5F62\u6210\n   \
    \     for p in arr[2:]:\n            n = len(upper)\n            while n >= 2\
    \ and upper[-2].ccw(upper[-1], p) == 1:\n                upper.pop()\n       \
    \         n -= 1\n            upper.append(p)\n\n        lower = [arr[-1], arr[-2]]\
    \  # x\u304C\u5927\u304D\u3044\u3082\u306E\u304B\u3089\uFF12\u3064\u8FFD\u52A0\
    \n        # \u51F8\u5305\u306E\u4E0B\u90E8\u3092\u5F62\u6210\n        for p in\
    \ arr[::-1][2::]:\n            n = len(lower)\n            while n >= 2 and lower[-2].ccw(lower[-1],\
    \ p) == 1:\n                lower.pop()\n                n -= 1\n            lower.append(p)\n\
    \        # \u6642\u8A08\u56DE\u308A\u306B\u306A\u308B\u3088\u3046\u306B\u51F8\u5305\
    \u306E\u70B9\u306E\u5217\u3092\u5F62\u6210\n        res = upper[1:-1] + lower\n\
    \        return res[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: geometory/geometory.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/aoj/cgl_1_b_refrection.test.py
  - test/aoj/cgl_1_c_counter_clockwise.test.py
  - test/aoj/cgl_2_d_distance.test.py
  - test/aoj/cgl_2_c_cross_point.test.py
  - test/aoj/cgl_2_a_parallel_orthogonal.test.py
  - test/aoj/cgl_2_b_intersection.test.py
  - test/aoj/dsl_4_a_union_of_rectangles.test.py
  - test/aoj/cgl_1_a_projection.test.py
documentation_of: geometory/geometory.py
layout: document
title: "\u5E7E\u4F55\u30C6\u30F3\u30D7\u30EC\u30FC\u30C8"
---
