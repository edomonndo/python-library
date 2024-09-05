---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_1_b_weighted_union_find.test.py
    title: "DSL1B \u91CD\u307F\u4ED8\u304DUnion Find\u6728"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/unionfind_with_potential.test.py
    title: Unionfind with Potential
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/unionfind_with_potential_non_commutative_group.test.py
    title: Unionfind with Potential (Non-Commutative Group)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Optional, TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass WeightedUnionFind:\n\
    \    def __init__(self, n, e: T = 0):\n        self.n = n\n        self.parent_or_size\
    \ = [-1] * n\n        self.ng = [False] * n\n        self.group = n\n        self.e\
    \ = e\n        self.weight = [e for _ in range(n)]  # W_i - W_{P_i}\n        self.base\
    \ = [e for _ in range(n)]\n\n    # weight[a] - weight[b] = w\n    def merge(self,\
    \ a: int, b: int, w: T) -> int:\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b,\
    \ self.n)\n        x = self.leader(a)\n        y = self.leader(b)\n        if\
    \ x == y:\n            if w != self.e:\n                self.ng[x] = True\n  \
    \          return x\n        self.group -= 1\n        if self.parent_or_size[x]\
    \ < self.parent_or_size[y]:\n            a, b = b, a\n            x, y = y, x\n\
    \            w = self.e - w\n        self.parent_or_size[y] += self.parent_or_size[x]\n\
    \        self.parent_or_size[x] = y\n        self.weight[x] = self.e - self.weight[a]\
    \ + w + self.weight[b]\n        self.ng[y] |= self.ng[x]\n        return y\n\n\
    \    def same(self, a: int, b: int) -> bool:\n        assert 0 <= a < self.n,\
    \ \"0<=a<n,a={0},n={1}\".format(a, self.n)\n        assert 0 <= b < self.n, \"\
    0<=b<n,b={0},n={1}\".format(b, self.n)\n        return self.leader(a) == self.leader(b)\n\
    \n    def leader(self, a: int) -> int:\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        p = self.parent_or_size[a]\n        if p < 0:\n  \
    \          return a\n        r = self.leader(p)\n        self.parent_or_size[a]\
    \ = r\n        self.weight[a] = self.weight[a] + self.weight[p]\n        return\
    \ r\n\n    def size(self, a: int) -> int:\n        assert 0 <= a < self.n, \"\
    0<=a<n,a={0},n={1}\".format(a, self.n)\n        return -self.parent_or_size[self.leader(a)]\n\
    \n    def group_count(self) -> int:\n        return self.group\n\n    def groups(self)\
    \ -> list[list[int]]:\n        leader_buf = [0 for _ in range(self.n)]\n     \
    \   group_size = [0 for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            leader_buf[i] = self.leader(i)\n            group_size[leader_buf[i]]\
    \ += 1\n        result = [[] for i in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n        result2 = []\n        for\
    \ i in range(self.n):\n            if len(result[i]) > 0:\n                result2.append(result[i])\n\
    \        return result2\n\n    def diff(self, a: int, b: int) -> Optional[T]:\n\
    \        if not self.same(a, b):\n            return None\n        else:\n   \
    \         self.leader(a)\n            self.leader(b)\n            return self.weight[a]\
    \ - self.weight[b]\n\n    def add(self, a: int, w: T) -> None:\n        a = self.leader(a)\n\
    \        self.base[a] = self.base[a] + w\n\n    def get(self, a: int) -> T:\n\
    \        p = self.leader(a)\n        return self.base[p] + self.diff(a, p)\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/connectivity/weighted_unionfind.py
  requiredBy: []
  timestamp: '2024-07-29 12:40:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/unionfind_with_potential.test.py
  - test/library_checker/graph/unionfind_with_potential_non_commutative_group.test.py
  - test/aoj/dsl/dsl_1_b_weighted_union_find.test.py
documentation_of: graph/connectivity/weighted_unionfind.py
layout: document
title: "\u91CD\u307F\u4ED8\u304D Union Find"
---
