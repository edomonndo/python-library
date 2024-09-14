---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  - icon: ':warning:'
    path: graph/csr.py
    title: "CSR\u30B0\u30E9\u30D5(Compressed Spare Row)"
  - icon: ':question:'
    path: graph/scc.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/scc_incremental.test.py
    title: Strongly Connected Components (Incremental)
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from graph.csr import CSR\nfrom graph.scc import SCC\nfrom graph.connectivity.unionfind\
    \ import UnionFind\n\n\nclass IncrementalScc:\n\n    def __init__(self, n: int):\n\
    \        self.n = n\n        self.edges = []\n\n    def add_edge(self, src: int,\
    \ dst: int) -> None:\n        # assert 0 <= src < self.n\n        # assert 0 <=\
    \ dst < self.n\n        self.edges.append((src, dst))\n\n    def solve(self) ->\
    \ CSR:\n        n = self.n\n        edges = self.edges\n        scc = SCC(n)\n\
    \        scc.from_edge(edges)\n        _, cc = scc.scc_ids()\n        eis = [i\
    \ for i, (u, v) in enumerate(edges) if cc[u] == cc[v]]\n        sep = [0] * (len(edges)\
    \ + 1)\n        nc = []\n\n        def dfs(n: int, x: int, eis: list[int]):\n\
    \            m = len(eis)\n            if x == m:\n                return\n  \
    \          if x + 1 == m:\n                uf = UnionFind(n)\n               \
    \ for ei in eis:\n                    u, v = edges[ei]\n                    if\
    \ uf.same(u, v):\n                        continue\n                    uf.merge(u,\
    \ v)\n                    sep[eis[x] + 1] += 1\n                    nc.append(ei)\n\
    \                return\n            sz = 0\n            idx = [-1] * n\n    \
    \        for ei in eis:\n                u, v = edges[ei]\n                for\
    \ j in [u, v]:\n                    if idx[j] == -1:\n                       \
    \ idx[j] = sz\n                        sz += 1\n                edges[ei] = (idx[u],\
    \ idx[v])\n            y = (x + m) >> 1\n            scc = SCC(sz)\n         \
    \   for ei in eis[:y]:\n                u, v = edges[ei]\n                scc.add_edge(u,\
    \ v)\n            cc = scc.scc_ids()\n            eis_left, eis_right = [], []\n\
    \            for ei in eis[:x]:\n                u, v = edges[ei]\n          \
    \      if cc[u] == cc[v]:\n                    eis_left.append(ei)\n         \
    \       else:\n                    eis_right.append(ei)\n            xl = len(eis_left)\n\
    \            for ei in eis[x:y]:\n                u, v = edges[ei]\n         \
    \       if cc[u] == cc[v]:\n                    eis_left.append(ei)\n        \
    \        else:\n                    eis_right.append(ei)\n            xr = len(eis_right)\n\
    \            for ei in eis[y:]:\n                u, v = edges[ei]\n          \
    \      if cc[u] != cc[v]:\n                    eis_right.append(ei)\n        \
    \    dfs(sz, xl, eis_left)\n            for ei in eis_right:\n               \
    \ u, v = edges[ei]\n                edges[ei] = (cc[u], cc[v])\n            dfs(sz,\
    \ xr, eis_right)\n\n        dfs(n, 0, eis)\n        for i in range(len(sep) -\
    \ 1):\n            sep[i + 1] += sep[i]\n        return CSR(len(sep) - 1, sep,\
    \ nc)\n"
  dependsOn:
  - graph/csr.py
  - graph/scc.py
  - graph/connectivity/unionfind.py
  isVerificationFile: false
  path: graph/scc_incremental.py
  requiredBy: []
  timestamp: '2024-09-14 17:35:06+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/scc_incremental.test.py
documentation_of: graph/scc_incremental.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
---
