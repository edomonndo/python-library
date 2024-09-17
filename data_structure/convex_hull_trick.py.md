---
data:
  _extendedDependsOn: []
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
  code: "from collections import deque\n\n\nclass ConvexHullTrick:\n    def __init__(self):\n\
    \        self.deq = deque()\n\n    def _check(self, line1, line2, line3):\n  \
    \      return (line2[0] - line1[0]) * (line3[1] - line2[1]) >= (\n           \
    \ line2[1] - line1[1]\n        ) * (line3[0] - line2[0])\n\n    def _f(self, line_idx,\
    \ x):\n        a, b = self.deq[line_idx]\n        return a * x + b\n\n    def\
    \ add_line(self, a, b):\n        line = (a, b)\n        while len(self.deq) >=\
    \ 2 and self._check(self.deq[-2], self.deq[-1], line):\n            self.deq.pop()\n\
    \        self.deq.append(line)\n\n    def query(self, x):\n        while len(self.deq)\
    \ >= 2 and self._f(0, x) >= self._f(1, x):\n            self.deq.popleft()\n \
    \       return self._f(0, x)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/convex_hull_trick.py
  requiredBy: []
  timestamp: '2023-09-15 11:40:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/convex_hull_trick.py
layout: document
redirect_from:
- /library/data_structure/convex_hull_trick.py
- /library/data_structure/convex_hull_trick.py.html
title: data_structure/convex_hull_trick.py
---
