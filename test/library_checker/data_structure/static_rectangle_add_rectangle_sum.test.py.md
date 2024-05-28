---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
    links:
    - https://en.wikipedia.org/wiki/Fenwick_tree"""
    - https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum\n\
    from collections import deque\nimport typing\n\n\nclass FenwickTree:\n    \"\"\
    \"Reference: https://en.wikipedia.org/wiki/Fenwick_tree\"\"\"\n\n    def __init__(self,\
    \ n: int = 0) -> None:\n        self._n = n\n        self.data = [0] * n\n\n \
    \   def add(self, p: int, x: typing.Any) -> None:\n        assert 0 <= p < self._n\n\
    \n        p += 1\n        while p <= self._n:\n            self.data[p - 1] +=\
    \ x\n            p += p & -p\n\n    def sum(self, left: int, right: int) -> typing.Any:\n\
    \        assert 0 <= left <= right <= self._n\n\n        return self._sum(right)\
    \ - self._sum(left)\n\n    def _sum(self, r: int) -> typing.Any:\n        s =\
    \ 0\n        while r > 0:\n            s += self.data[r - 1]\n            r -=\
    \ r & -r\n\n        return s\n\n\nMOD = 998244353\n\n\nclass StaticRectangleAddRectangleSum:\n\
    \    def __init__(self, n: int, q: int):\n        self.X = [0] * (n << 1)\n  \
    \      self.rects = [0] * n\n        self.qs = [0] * q\n        self.pid = 0\n\
    \        self.qid = 0\n\n    def add_rect(self, x1: int, y1: int, x2: int, y2:\
    \ int, w: int) -> None:\n        i = self.pid\n        self.X[i << 1 | 0] = x1\n\
    \        self.X[i << 1 | 1] = x2\n        self.rects[i] = (x1, y1, x2, y2, w)\n\
    \        self.pid += 1\n\n    def add_query(self, x1: int, y1: int, x2: int, y2:\
    \ int) -> None:\n        self.qs[self.qid] = (x1, y1, x2, y2)\n        self.qid\
    \ += 1\n\n    def solve(self) -> list[int]:\n        dX = {x: i for i, x in enumerate(sorted(set(self.X)))}\n\
    \n        # \u30A4\u30D9\u30F3\u30C8\u30BD\u30FC\u30C8\n        event = [0] *\
    \ (self.pid << 1)\n        for i, (x1, y1, x2, y2, w) in enumerate(self.rects):\n\
    \            l, r = dX[x1], dX[x2]\n            event[i << 1 | 0] = (y1, l, r,\
    \ w)\n            event[i << 1 | 1] = (y2, l, r, -w)\n        event.sort(key=lambda\
    \ e: e[0])\n        event = deque(event)\n\n        bit = [[0, 0] for _ in range(self.pid\
    \ << 1)]\n        pq = [0] * (self.qid << 1)\n        for i, (x1, y1, x2, y2)\
    \ in enumerate(self.qs):\n            pq[i << 1 | 0] = (y1, i, 0)\n          \
    \  pq[i << 1 | 1] = (y2, i, 1)\n        pq.sort(key=lambda q: q[0])\n\n      \
    \  res = [0] * self.qid\n        for qy, qi, t in pq:\n            while event:\n\
    \                py, pl, pr, w = event.popleft()\n                if py < qy:\n\
    \                    event.appendleft((py, pl, pr, w))\n                    break\n\
    \                wy = w * py % MOD\n"
  dependsOn: []
  isVerificationFile: true
  path: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
  requiredBy: []
  timestamp: '2024-05-28 15:29:52+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
- /verify/test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py.html
title: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
---
