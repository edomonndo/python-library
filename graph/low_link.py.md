---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/aoj/grl/grl_3_a_articulation_points.test.py
    title: "GRL3A \u95A2\u7BC0\u70B9"
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_b_bridges.test.py
    title: "GRL3B \u6A4B"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/biconnected_components.test.py
    title: Biconnected Components
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/two_edge_connected_components.test.py
    title: Two-Edge-Connected Components
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LowLink:\n    def __init__(self, adj: list[list[int]]):\n        self.n\
    \ = n = len(adj)\n        self.order = order = [-1] * n\n        self.low = low\
    \ = [n] * n\n        self.child = child = [[] for _ in range(n)]\n        self.is_root\
    \ = is_root = [0] * n\n        self.roots = roots = []\n\n        par = [-1] *\
    \ n\n        idx = 0\n        for u in range(n):\n            if order[u] != -1:\n\
    \                continue\n            is_root[u] = 1\n            roots.append(u)\n\
    \            st = [u]\n            par[u] = -2\n            while st:\n      \
    \          v = st.pop()\n                if v >= 0:\n                    if order[v]\
    \ != -1:\n                        continue\n                    order[v] = idx\n\
    \                    low[v] = idx\n                    idx += 1\n            \
    \        if v != u:\n                        child[par[v]].append(v)\n       \
    \                 st.append(~v)\n                    check_p = 0\n           \
    \         for nv in adj[v]:\n                        if nv == par[v] and check_p\
    \ == 0:\n                            check_p += 1\n                          \
    \  continue\n                        elif order[nv] != -1:\n                 \
    \           low[v] = min(low[v], order[nv])\n                        else:\n \
    \                           par[nv] = v\n                            st.append(nv)\n\
    \                    continue\n                v = ~v\n                p = par[v]\n\
    \                low[p] = min(low[p], low[v])\n\n    def get_articulation(self)\
    \ -> list[int]:\n        order, low, is_root, child = self.order, self.low, self.is_root,\
    \ self.child\n        res = [0] * self.n\n        for v in range(self.n):\n  \
    \          if is_root[v]:\n                if len(child[v]) >= 2:\n          \
    \          res[v] = 1\n                continue\n            for u in child[v]:\n\
    \                if order[v] <= low[u]:\n                    res[v] = 1\n    \
    \                break\n        return res\n\n    def get_bridge(self) -> list[tuple[int,\
    \ int]]:\n        order, low, roots, child = self.order, self.low, self.roots,\
    \ self.child\n        res = []\n        for v in roots:\n            st = [v]\n\
    \            while st:\n                v = st.pop()\n                for u in\
    \ child[v]:\n                    if order[v] < low[u]:\n                     \
    \   if u < v:\n                            res.append((u, v))\n              \
    \          else:\n                            res.append((v, u))\n           \
    \         st.append(u)\n        return res\n\n    def two_edge_connected_components(self)\
    \ -> tuple[list[int], list[tuple[int, int]]]:\n        order, low, roots, child\
    \ = self.order, self.low, self.roots, self.child\n\n        components = [-1]\
    \ * self.n\n        new_edges = []\n        idx = 0\n        for v in roots:\n\
    \            components[v] = idx\n            st = [v]\n            while st:\n\
    \                v = st.pop()\n                for u in child[v]:\n          \
    \          if order[v] < low[u]:\n                        idx += 1\n         \
    \               components[u] = idx\n                        if components[v]\
    \ < idx:\n                            new_edges.append((components[v], idx))\n\
    \                        else:\n                            new_edges.append((idx,\
    \ components[v]))\n                    else:\n                        components[u]\
    \ = components[v]\n                    st.append(u)\n            idx += 1\n  \
    \      return components, new_edges\n\n    @staticmethod\n    def _build_dfs_tree(adj:\
    \ list[list[int]]):\n        n = len(adj)\n        dfs_order = []\n        par\
    \ = [-2] * n\n        eid = [0] * n\n        for r in range(n):\n            if\
    \ par[r] != -2:\n                continue\n            v = r\n            par[v]\
    \ = -1\n            while v >= 0:\n                if eid[v] == 0:\n         \
    \           dfs_order.append(v)\n                if eid[v] == len(adj[v]):\n \
    \                   v = par[v]\n                    continue\n               \
    \ u = adj[v][eid[v]]\n                eid[v] += 1\n                if par[u] !=\
    \ -2:\n                    continue\n                v, par[u] = u, v\n      \
    \  return dfs_order, par\n\n    @classmethod\n    def _biconnected_components(\n\
    \        cls, adj: list[list[int]]\n    ) -> tuple[int, list[tuple[int, int]]]:\n\
    \        n = len(adj)\n        order, par = cls._build_dfs_tree(adj)\n\n     \
    \   vtx_to_dfs = [0] * n\n        for i in range(n):\n            vtx_to_dfs[order[i]]\
    \ = i\n        low = vtx_to_dfs[:]\n        for u in range(n):\n            for\
    \ v in adj[u]:\n                low[u] = min(low[u], vtx_to_dfs[v])\n        for\
    \ v in order[::-1]:\n            p = par[v]\n            if p >= 0:\n        \
    \        low[p] = min(low[p], low[v])\n        num_bcc = 0\n        bc_vtx_pair\
    \ = []\n        for v in order:\n            if par[v] >= 0:\n               \
    \ p = par[v]\n                if low[v] < vtx_to_dfs[p]:\n                   \
    \ low[v] = low[p]\n                    bc_vtx_pair.append((low[v], v))\n     \
    \           else:\n                    low[v] = num_bcc\n                    num_bcc\
    \ += 1\n                    bc_vtx_pair += [(low[v], p), (low[v], v)]\n      \
    \  for v in range(n):\n            if len(adj[v]) == 0:\n                bc_vtx_pair.append((num_bcc,\
    \ v))\n                num_bcc += 1\n        return num_bcc, bc_vtx_pair\n\n \
    \   @classmethod\n    def block_cut_tree(cls, adj: list[list[int]]) -> list[list[int]]:\n\
    \        num_bcc, bc_vtx_pair = cls._biconnected_components(adj)\n        n =\
    \ len(adj)\n        edges = []\n        for u, v in bc_vtx_pair:\n           \
    \ edges.append((u + n, v))\n        bc_tree = [[] for _ in range(n + num_bcc)]\n\
    \        for u, v in edges:\n            bc_tree[u].append(v)\n            bc_tree[v].append(u)\n\
    \        return bc_tree\n\n    @classmethod\n    def biconnected_components_verticle(cls,\
    \ adj: list[list[int]]) -> list[list[int]]:\n        num_bcc, bc_vtx_pair = cls._biconnected_components(adj)\n\
    \        res = [[] for _ in range(num_bcc)]\n        for u, v in bc_vtx_pair:\n\
    \            res[u].append(v)\n        return res\n\n    @classmethod\n    def\
    \ biconnected_components_edge(\n        cls, n: int, edges: list[tuple[int, int]]\n\
    \    ) -> list[tuple[int, int]]:\n        adj = [[] for _ in range(n)]\n     \
    \   for u, v in edges:\n            adj[u].append(v)\n            adj[v].append(u)\n\
    \        bc_tree = cls.block_cut_tree(adj)\n        n = len(bc_tree)\n       \
    \ par = [-1] * n\n        dep = [0] * n\n        bfs = [None] * n\n        l,\
    \ r = 0, 0\n        for root in range(n):\n            if par[root] >= 0:\n  \
    \              continue\n            bfs[r] = root\n            r += 1\n     \
    \       while l < r and r < n:\n                v = bfs[l]\n                for\
    \ u in bc_tree[v]:\n                    if par[v] != u:\n                    \
    \    par[u] = v\n                        dep[u] = dep[v] + 1\n               \
    \         bfs[r] = u\n                        r += 1\n                l += 1\n\
    \n        res = [[] for _ in range(n - len(adj))]\n        for eid, (u, v) in\
    \ enumerate(edges):\n            s = par[v if dep[u] <= dep[v] else u] - len(adj)\n\
    \            res[s].append(eid)\n        return res\n\n    @classmethod\n    def\
    \ three_edge_connected_components(cls, adj: list[list[int]]) -> list[int]:\n \
    \       raise NotImplementedError\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/low_link.py
  requiredBy: []
  timestamp: '2024-07-19 12:35:18+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/library_checker/graph/biconnected_components.test.py
  - test/library_checker/graph/two_edge_connected_components.test.py
  - test/aoj/grl/grl_3_a_articulation_points.test.py
  - test/aoj/grl/grl_3_b_bridges.test.py
documentation_of: graph/low_link.py
layout: document
title: Low Link
---

以下を求める.

- 関節点:　グラフから取り除くと連結でなくなる頂点
- 橋: グラフから取り除くと連結でなくなる頂点
- 二辺連結成分分解: 辺を１つ取り除いても連結である連結成分に分解
- 二頂点連結成分分解: 頂点を１つ取り除いても連結である連結成分に分解