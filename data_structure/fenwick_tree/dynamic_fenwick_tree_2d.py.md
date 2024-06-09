---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
    title: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
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
  code: "from collections import defaultdict\nfrom typing import TypeVar\n\nT = TypeVar(\"\
    T\")\n\n\nclass DynamicFenwickTree2d:\n    def __init__(self, h: int, w: int,\
    \ e: T):\n        self.h = h\n        self.w = w\n        self.dat = defaultdict(lambda:\
    \ defaultdict(lambda: e))\n        self.e = e\n\n    def add_point(self, x: int,\
    \ y: int, w: T) -> T:\n        dat = self.dat\n        x += 1\n        y += 1\n\
    \        while x <= self.h:\n            node = dat[x]\n            y1 = y\n \
    \           while y1 <= self.w:\n                node[y1] += w\n             \
    \   y1 += y1 & -y1\n            x += x & -x\n\n    def add_rect(self, x1: int,\
    \ y1: int, x2: int, y2: int, w: T) -> None:\n        self.add_point(x1, y1, w)\n\
    \        self.add_point(x1, y2 + 1, -w)\n        self.add_point(x2 + 1, y1, -w)\n\
    \        self.add_point(x2 + 1, y2 + 1, w)\n\n    def sum0(self, x: int, y: int)\
    \ -> T:\n        dat = self.dat\n        x = min(x + 1, self.h)\n        y = min(y\
    \ + 1, self.w)\n        res = self.e\n        while x > 0:\n            if x in\
    \ dat:\n                node = dat[x]\n                y1 = y\n              \
    \  while y1 > 0:\n                    if y1 in node:\n                       \
    \ res += node[y1]\n                    y1 -= y1 & -y1\n            x -= x & -x\n\
    \        return res\n\n    def sum(self, x1: int, y1: int, x2: int, y2: int) ->\
    \ T:\n        sum0 = self.sum0\n        return sum0(x2, y2) - sum0(x1 - 1, y2)\
    \ - sum0(x2, y1 - 1) + sum0(x1 - 1, y1 - 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/fenwick_tree/dynamic_fenwick_tree_2d.py
  requiredBy:
  - test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/fenwick_tree/dynamic_fenwick_tree_2d.py
layout: document
title: "\u4E8C\u6B21\u5143\u52D5\u7684Fenwick Tree"
---
