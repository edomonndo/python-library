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
  code: "from typing import TypeVar, Union\n\nT = TypeVar(\"T\")\n\n\nclass CSR:\n\
    \    def __init__(\n        self,\n        n: int,\n        edges: list[tuple[int,\
    \ int], tuple[int, int]],\n        directed: bool = False,\n    ) -> None:\n \
    \       self.start = [0] * (n + 1)\n        m = len(edges)\n        self.elist\
    \ = [0] * (m if directed else m * 2)\n        self.idx = dict()\n\n        for\
    \ e in edges:\n            self.start[e[0] + 1] += 1\n            if not directed:\n\
    \                self.start[e[1] + 1] += 1\n\n        for i in range(1, n + 1):\n\
    \            self.start[i] += self.start[i - 1]\n\n        counter = self.start[:]\n\
    \        for e in edges:\n            u, v = e[0], e[1]\n            self.elist[counter[u]]\
    \ = v\n            self.idx[u, v] = counter[u]\n            counter[u] += 1\n\
    \            if not directed:\n                self.elist[counter[v]] = u\n  \
    \              self.idx[v, u] = counter[v]\n                counter[v] += 1\n\n\
    \    def __getitem__(self, i: int) -> Union[list[int], list[tuple[int, T]]]:\n\
    \        l, r = self.start[i : i + 2]\n        return self.elist[l:r]\n\n\nclass\
    \ WeightedCSR:\n    def __init__(\n        self,\n        n: int,\n        edges:\
    \ list[tuple[int, int, T]],\n        directed: bool = False,\n        e: T = 0,\n\
    \    ) -> None:\n        self.start = [0] * (n + 1)\n        m = len(edges)\n\
    \        self.elist = [0] * (m if directed else m * 2)\n        self.w = [e] *\
    \ (m if directed else m * 2)\n        self.e = e\n        self.idx = dict()\n\n\
    \        for e in edges:\n            self.start[e[0] + 1] += 1\n            if\
    \ not directed:\n                self.start[e[1] + 1] += 1\n\n        for i in\
    \ range(1, n + 1):\n            self.start[i] += self.start[i - 1]\n\n       \
    \ counter = self.start[:]\n        for e in edges:\n            u, v = e[0], e[1]\n\
    \            self.elist[counter[u]] = v\n            self.idx[u, v] = counter[u]\n\
    \            self.w[counter[u]] = e[2]\n            counter[u] += 1\n        \
    \    if not directed:\n                self.elist[counter[v]] = u\n          \
    \      self.idx[v, u] = counter[v]\n                self.w[counter[v]] = e[2]\n\
    \                counter[v] += 1\n\n    def __getitem__(self, i: int) -> Union[list[int],\
    \ list[tuple[int, T]]]:\n        l, r = self.start[i : i + 2]\n        return\
    \ [(self.elist[j], self.w[j]) for j in range(l, r)]\n\n    def get(self, u: int,\
    \ v: int) -> T:\n        # assert self.weighted\n        # assert (u, v) in self.idx\n\
    \        return self.w[self.idx[u, v]]\n\n    def set(self, u: int, v: int, w:\
    \ T) -> None:\n        # assert self.weighted\n        # assert (u, v) in self.idx\n\
    \        self.w[self.idx[u, v]] = w\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/csr.py
  requiredBy: []
  timestamp: '2024-06-13 17:21:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/csr.py
layout: document
title: "CSR\u30B0\u30E9\u30D5(Compressed Spare Row)"
---

疎なグラフを省メモリで表現できる形式．

