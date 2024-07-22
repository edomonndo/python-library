---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/biconnected_components.test.py
    title: Biconnected Components
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BiconnectedComponents:\n    def __init__(self, n: int, edges: list[list[int]]):\n\
    \        self.n = n\n        self.edges = edges\n        self.adj = adj = [[]\
    \ for _ in range(n)]\n        for u, v in edges:\n            adj[u].append(v)\n\
    \            adj[v].append(u)\n        self.num_bcc, self.bc_vtx_pair = self._biconnected_components()\n\
    \n    @staticmethod\n    def _build_dfs_tree(adj: list[list[int]]):\n        n\
    \ = len(adj)\n        dfs_order = []\n        par = [-2] * n\n        eid = [0]\
    \ * n\n        for r in range(n):\n            if par[r] != -2:\n            \
    \    continue\n            v = r\n            par[v] = -1\n            while v\
    \ >= 0:\n                if eid[v] == 0:\n                    dfs_order.append(v)\n\
    \                if eid[v] == len(adj[v]):\n                    v = par[v]\n \
    \                   continue\n                u = adj[v][eid[v]]\n           \
    \     eid[v] += 1\n                if par[u] != -2:\n                    continue\n\
    \                v, par[u] = u, v\n        return dfs_order, par\n\n    def _biconnected_components(self)\
    \ -> tuple[int, list[tuple[int, int]]]:\n        order, par = self._build_dfs_tree(self.adj)\n\
    \n        vtx_to_dfs = [0] * self.n\n        for i in range(self.n):\n       \
    \     vtx_to_dfs[order[i]] = i\n        low = vtx_to_dfs[:]\n        for u in\
    \ range(self.n):\n            for v in self.adj[u]:\n                low[u] =\
    \ min(low[u], vtx_to_dfs[v])\n        for v in order[::-1]:\n            p = par[v]\n\
    \            if p >= 0:\n                low[p] = min(low[p], low[v])\n      \
    \  num_bcc = 0\n        bc_vtx_pair = []\n        for v in order:\n          \
    \  if par[v] >= 0:\n                p = par[v]\n                if low[v] < vtx_to_dfs[p]:\n\
    \                    low[v] = low[p]\n                    bc_vtx_pair.append((low[v],\
    \ v))\n                else:\n                    low[v] = num_bcc\n         \
    \           num_bcc += 1\n                    bc_vtx_pair += [(low[v], p), (low[v],\
    \ v)]\n        for v in range(self.n):\n            if len(self.adj[v]) == 0:\n\
    \                bc_vtx_pair.append((num_bcc, v))\n                num_bcc +=\
    \ 1\n        return num_bcc, bc_vtx_pair\n\n    def block_cut_tree(self) -> list[list[int]]:\n\
    \        edges = []\n        for u, v in self.bc_vtx_pair:\n            edges.append((u\
    \ + self.n, v))\n        bc_tree = [[] for _ in range(self.n + self.num_bcc)]\n\
    \        for u, v in edges:\n            bc_tree[u].append(v)\n            bc_tree[v].append(u)\n\
    \        return bc_tree\n\n    def biconnected_components_verticle(self) -> list[list[int]]:\n\
    \        res = [[] for _ in range(self.num_bcc)]\n        for u, v in self.bc_vtx_pair:\n\
    \            res[u].append(v)\n        return res\n\n    def biconnected_components_edge(self)\
    \ -> list[tuple[int, int]]:\n        bc_tree = self.block_cut_tree()\n       \
    \ n = len(bc_tree)\n        par = [-1] * n\n        dep = [0] * n\n        bfs\
    \ = [None] * n\n        l, r = 0, 0\n        for root in range(n):\n         \
    \   if par[root] >= 0:\n                continue\n            bfs[r] = root\n\
    \            r += 1\n            while l < r and r < n:\n                v = bfs[l]\n\
    \                for u in bc_tree[v]:\n                    if par[v] != u:\n \
    \                       par[u] = v\n                        dep[u] = dep[v] +\
    \ 1\n                        bfs[r] = u\n                        r += 1\n    \
    \            l += 1\n\n        res = [[] for _ in range(n - self.n)]\n       \
    \ for eid, (u, v) in enumerate(self.edges):\n            s = par[v if dep[u] <=\
    \ dep[v] else u] - self.n\n            res[s].append(eid)\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/biconnected_components.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/biconnected_components.test.py
documentation_of: graph/biconnected_components.py
layout: document
title: "\u4E8C\u9802\u70B9\u9023\u7D50\u6210\u5206\u5206\u89E3/Block Cut Tree"
---
