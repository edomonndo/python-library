---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: graph/csr.py
    title: "CSR\u30B0\u30E9\u30D5(Compressed Spare Row)"
  _extendedRequiredBy:
  - icon: ':x:'
    path: graph/scc_incremental.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
    title: "GRL3C \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  - icon: ':x:'
    path: test/library_checker/graph/scc.test.py
    title: Strongly Connected Components
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from graph.csr import CSR\n\n\nclass SCC:\n    def __init__(self, n: int):\n\
    \        self.n = n\n        self.edges = []\n        self.ids = None\n\n    def\
    \ from_edge(self, edges: list[tuple[int, int]]):\n        self.edges = edges\n\
    \n    def add_edge(self, src: int, dst: int) -> None:\n        # assert 0 <= src\
    \ < self.n\n        # assert 0 <= dst < self.n\n        self.edges.append((src,\
    \ dst))\n\n    def scc_ids(self) -> tuple[int, list[list[int]]]:\n        n, edges\
    \ = self.n, self.edges\n        adj = CSR.build(n, edges, True)\n        visited\
    \ = []\n        low = [0] * n\n        ord = [-1] * n\n        ids = [0] * n\n\
    \        idx = group_num = 0\n        for i in range(n):\n            if ord[i]\
    \ != -1:\n                continue\n            st = [(~i, -1), (i, -1)]\n   \
    \         while st:\n                v, p = st.pop()\n                if v >=\
    \ 0:\n                    if p != -1 and ord[v] != -1:\n                     \
    \   low[p] = min(low[p], ord[v])\n                        st.pop()\n         \
    \               continue\n                    low[v] = ord[v] = idx\n        \
    \            idx += 1\n                    visited.append(v)\n               \
    \     for u in adj[v]:\n                        if ord[u] == -1:\n           \
    \                 st += [(~u, v), (u, v)]\n                        else:\n   \
    \                         low[v] = min(low[v], ord[u])\n                    continue\n\
    \                v = ~v\n                if low[v] == ord[v]:\n              \
    \      while True:\n                        u = visited.pop()\n              \
    \          ord[u] = n\n                        ids[u] = group_num\n          \
    \              if u == v:\n                            break\n               \
    \     group_num += 1\n                low[p] = min(low[p], low[v])\n        for\
    \ i in range(n):\n            ids[i] = group_num - 1 - ids[i]\n        self.group_num\
    \ = group_num\n        self.ids = ids\n        return group_num, ids\n\n    def\
    \ get_mapping(self) -> list[list[int]]:\n        if self.ids is None:\n      \
    \      self.scc_ids()\n        group_num, ids = self.group_num, self.ids\n   \
    \     counts = [0] * group_num\n        for x in ids:\n            counts[x] +=\
    \ 1\n        groups = [[] for _ in range(group_num)]\n        for i in range(n):\n\
    \            groups[ids[i]].append(i)\n        return groups\n"
  dependsOn:
  - graph/csr.py
  isVerificationFile: false
  path: graph/scc.py
  requiredBy:
  - graph/scc_incremental.py
  timestamp: '2024-09-14 17:40:48+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/library_checker/graph/scc.test.py
  - test/aoj/grl/grl_3_c_strongly_connected_components.test.py
documentation_of: graph/scc.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
