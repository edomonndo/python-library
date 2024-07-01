---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/dsu.py
    title: atcoder/dsu.py
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
  code: "from atcoder.dsu import DSU\n\n\nclass StaticRangeParallelUnionFind:\n  \
    \  def __init__(self, n):\n        self.n = n\n        self.qs = [[] for _ in\
    \ range(n + 1)]\n\n    def merge(self, x, y, d):\n        \"\"\"merge(x+i, y+i)\
    \ for i in range(d)\"\"\"\n        if d == 0:\n            return\n        self.qs[min(d,\
    \ self.n)].append((x, y))\n\n    def build(self) -> DSU:\n        n = self.n\n\
    \        uf = DSU(n)\n        q = []\n        for d in reversed(range(1, n + 1)):\n\
    \            q += self.qs[d]\n            nq = []\n            for x, y in q:\n\
    \                if uf.same(x, y):\n                    continue\n           \
    \     uf.merge(x, y)\n                nq.append((x + 1, y + 1))\n            q\
    \ = nq\n        return uf\n"
  dependsOn:
  - atcoder/dsu.py
  isVerificationFile: false
  path: graph/connectivity/static_range_parallel_union_find.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/connectivity/static_range_parallel_union_find.py
layout: document
title: Static Range Parallel Union Find
---
