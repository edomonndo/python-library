---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/range_parallel_unionfind.py
    title: Range Parallel Union Find
  - icon: ':warning:'
    path: graph/connectivity/static_range_parallel_unionfind.py
    title: Static Range Parallel Union Find
  - icon: ':x:'
    path: graph/tree_decomposition_width2.py
    title: "\u6728\u5206\u89E3\uFF08\u6728\u5E45\uFF12\u4EE5\u4E0B\uFF09"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/manhattanmst.test.py
    title: Manhattan MST
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/minimum_spanning_tree.test.py
    title: Minimum Spanning Tree
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/range_parallel_unionfind.test.py
    title: Range Parallel Unionfind
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n: int):\n        self.n = n\n \
    \       self.parent_or_size = [-1 for i in range(n)]\n\n    def merge(self, a:\
    \ int, b: int) -> int:\n        # assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        # assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b,\
    \ self.n)\n        x = self.leader(a)\n        y = self.leader(b)\n        if\
    \ x == y:\n            return x\n        if -self.parent_or_size[x] < -self.parent_or_size[y]:\n\
    \            x, y = y, x\n        self.parent_or_size[x] += self.parent_or_size[y]\n\
    \        self.parent_or_size[y] = x\n        return x\n\n    def same(self, a:\
    \ int, b: int) -> bool:\n        # assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        # assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b,\
    \ self.n)\n        return self.leader(a) == self.leader(b)\n\n    def leader(self,\
    \ a: int) -> int:\n        # assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a,\
    \ self.n)\n        if self.parent_or_size[a] < 0:\n            return a\n    \
    \    self.parent_or_size[a] = self.leader(self.parent_or_size[a])\n        return\
    \ self.parent_or_size[a]\n\n    def size(self, a: int) -> int:\n        # assert\
    \ 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n        return -self.parent_or_size[self.leader(a)]\n\
    \n    def groups(self) -> list[int]:\n        leader_buf = [0 for i in range(self.n)]\n\
    \        for i in range(self.n):\n            leader_buf[i] = self.leader(i)\n\
    \        result = [[] for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n        return [group for group\
    \ in result if len(group) > 0]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/connectivity/unionfind.py
  requiredBy:
  - graph/tree_decomposition_width2.py
  - graph/connectivity/range_parallel_unionfind.py
  - graph/connectivity/static_range_parallel_unionfind.py
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/manhattanmst.test.py
  - test/library_checker/graph/range_parallel_unionfind.test.py
  - test/library_checker/graph/minimum_spanning_tree.test.py
documentation_of: graph/connectivity/unionfind.py
layout: document
title: Union Find
---
