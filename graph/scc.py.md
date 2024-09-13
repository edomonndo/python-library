---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: graph/csr.py
    title: "CSR\u30B0\u30E9\u30D5(Compressed Spare Row)"
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/scc_incremental.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
    title: "GRL3C \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/scc.test.py
    title: Strongly Connected Components
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from graph.csr import CSR\n\n\nclass SCC:\n    def __init__(self, n: int):\n\
    \        self.n = n\n        self.edges = []\n        self.redges = []\n\n   \
    \ def add_edge(self, src: int, dst: int) -> None:\n        # assert 0 <= src <\
    \ self.n\n        # assert 0 <= dst < self.n\n        self.edges.append((src,\
    \ dst))\n        self.redges.append((dst, src))\n\n    def build(self) -> None:\n\
    \        n = self.n\n        ord = [0] * n\n        adj = CSR.build(n, self.edges,\
    \ True)\n        idx = n\n        par = [-1] * n\n        eis = [0] * n\n    \
    \    for s in range(n):\n            if par[s] == -1:\n                par[s],\
    \ p = -2, s\n                while p >= 0:\n                    arr = adj[p]\n\
    \                    if eis[p] == len(arr):\n                        idx -= 1\n\
    \                        ord[idx], p = p, par[p]\n                        continue\n\
    \                    q = arr[eis[p]]\n                    eis[p] += 1\n      \
    \              if par[q] == -1:\n                        par[q], p = p, q\n  \
    \      rev = CSR.build(n, self.redges, True)\n        sep = [0]\n        csr =\
    \ [0] * n\n        vis = [0] * n\n        p1, p2 = 0, 0\n        for s in ord:\n\
    \            if not vis[s]:\n                csr[p2], vis[s] = s, 1\n        \
    \        p2 += 1\n                while p1 < p2:\n                    v = csr[p1]\n\
    \                    for u in rev[v]:\n                        if not vis[u]:\n\
    \                            vis[u] = 1\n                            csr[p2] =\
    \ u\n                            p2 += 1\n                    p1 += 1\n      \
    \          sep.append(p2)\n        self.induce = CSR.from_raw(sep, csr)\n    \
    \    self._componet_count = len(self.induce)\n\n    def count_components(self):\n\
    \        return self._componet_count\n\n    def get_mapping(self):\n        res\
    \ = [0] * self.n\n        for i in range(self._componet_count):\n            for\
    \ v in self.induce[i]:\n                res[v] = i\n        return res\n"
  dependsOn:
  - graph/csr.py
  isVerificationFile: false
  path: graph/scc.py
  requiredBy:
  - graph/scc_incremental.py
  timestamp: '2024-09-14 02:22:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/scc.test.py
  - test/aoj/grl/grl_3_c_strongly_connected_components.test.py
documentation_of: graph/scc.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
