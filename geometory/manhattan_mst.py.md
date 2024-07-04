---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/SortedSet.py
    title: SortedSet
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/manhattanmst.test.py
    title: test/library_checker/graph/manhattanmst.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from data_structure.basic.SortedSet import SortedSet\n\n\nclass ManhattanMST:\n\
    \    def __init__(self) -> None:\n        self.n = 0\n        self.points = []\n\
    \        self.edges = []\n\n    def add_point(self, i, j):\n        self.n +=\
    \ 1\n        self.points.append(i)\n        self.points.append(j)\n\n    def _sweep(self):\n\
    \        m = SortedSet()\n        d = {}\n        for i in self.idx:\n       \
    \     x, y = self.points[i << 1], self.points[(i << 1) + 1]\n            while\
    \ m:\n                z = m.le(y)\n                if z is None:\n           \
    \         break\n                j = d[z]\n                dx = x - self.points[j\
    \ << 1]\n                dy = y - self.points[(j << 1) + 1]\n                if\
    \ dy > dx:\n                    break\n                self.edges.append((dx +\
    \ dy, i, j))\n                m.discard(z)\n                del d[z]\n       \
    \     m.add(y)\n            d[y] = i\n\n    def solve(self):\n        \"\"\"\n\
    \        2\u6B21\u5143\u306E\u70B9\u96C6\u5408[(xi,yi)]\u304B\u3089\u3001\u30DE\
    \u30F3\u30CF\u30C3\u30BF\u30F3\u6700\u5C0F\u5168\u57DF\u6728\u306E\u8FBA\u96C6\
    \u5408\u3092\u69CB\u7BC9\u3059\u308B.\n        [(distance, i, j)]\n        \"\"\
    \"\n        for i in range(2):\n            p_sum = [\n                self.points[x\
    \ << 1] + self.points[(x << 1) + 1] for x in range(self.n)\n            ]\n  \
    \          self.idx = sorted(range(self.n), key=lambda x: p_sum[x])\n        \
    \    for _ in range(2):\n                self._sweep()\n                for j\
    \ in range(self.n):\n                    self.points[j << 1], self.points[(j <<\
    \ 1) + 1] = (\n                        self.points[(j << 1) + 1],\n          \
    \              self.points[j << 1],\n                    )\n            if not\
    \ i:\n                for j in range(self.n):\n                    self.points[j\
    \ << 1] *= -1\n        self.edges.sort(key=lambda x: x[0])\n"
  dependsOn:
  - data_structure/basic/SortedSet.py
  isVerificationFile: false
  path: geometory/manhattan_mst.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/manhattanmst.test.py
documentation_of: geometory/manhattan_mst.py
layout: document
title: "\u30DE\u30F3\u30CF\u30C3\u30BF\u30F3\u8DDD\u96E2\u306E\u6700\u5C0F\u5168\u57DF\
  \u6728"
---