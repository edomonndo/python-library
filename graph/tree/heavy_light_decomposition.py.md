---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld.test.py
    title: GRL5D Range Query on a Tree
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
    title: GRL5E Range Query on a Tree II
  - icon: ':heavy_check_mark:'
    path: test/atcoder/past/past4m_hld.test.py
    title: "M - \u7B46\u5857\u308A"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
    title: Global Minimum Cut of Dynamic Star Augmented Graph
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/jump_on_tree_hld.test.py
    title: Jump on Tree (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_path_sum_hld.test.py
    title: Vertex Add Path Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
    title: Vertex Add Subtree Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertext_set_path_composite.test.py
    title: Vertex Set Path Composite
  - icon: ':heavy_check_mark:'
    path: "test/yukicoder/235_\u3081\u3050\u308B\u306F\u3081\u3050\u308B(5).test.py"
    title: "No.235 \u3081\u3050\u308B\u306F\u3081\u3050\u308B (5)"
  - icon: ':heavy_check_mark:'
    path: "test/yukicoder/399_\u52D5\u7684\u306A\u9818\u4E3B.test.py"
    title: "No.399 \u52D5\u7684\u306A\u9818\u4E3B"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Union\n\n\nclass HeavyLightDecomposition:\n    def __init__(\n\
    \        self,\n        n: int,\n        adj: list[list[Union[int, tuple[int,\
    \ int]]]],\n        root: int = 0,\n        has_weight: bool = False,\n      \
    \  is_undirect: bool = True,\n    ):\n        # assert len(edges) == n-1\n   \
    \     self.n = n\n        self.root = root\n        self.adj = adj\n        self.has_weight\
    \ = has_weight\n        self.is_undirect = is_undirect\n        self.par = [-1]\
    \ * n\n        self.depth = [0] * n\n        order = self._root_tree()\n\n   \
    \     self.sz = [1] * self.n\n        self._dfs_sz(order)\n\n        self.into\
    \ = [-1] * n\n        self.head = [root] * n\n        self.hld = []\n        self._dfs_hld()\n\
    \        # assert len(self.hld) == n\n\n    def _root_tree(self) -> None:\n  \
    \      adj, par, depth = self.adj, self.par, self.depth\n        res = []\n  \
    \      st = [self.root]\n        while st:\n            v = st.pop()\n       \
    \     res.append(v)\n            if self.is_undirect and par[v] != -1:\n     \
    \           adj[v].remove(par[v])\n            if self.has_weight:\n         \
    \       for e in adj[v]:\n                    # assert len(e) == 2\n         \
    \           u, w = e[0], e[1]\n                    par[u] = (v, w)\n         \
    \           depth[u] = depth[v] + 1\n                    st.append(u)\n      \
    \      else:\n                for u in adj[v]:\n                    par[u] = v\n\
    \                    depth[u] = depth[v] + 1\n                    st.append(u)\n\
    \        if self.has_weight:\n            par[self.root] = (-1, 0)\n         \
    \   self.par = [p for p, _ in par]\n        return res\n\n    def _dfs_sz(self,\
    \ order: list[int]) -> None:\n        # calc subtree size\n        adj, sz = self.adj,\
    \ self.sz\n        for p in order[::-1]:\n            vs = adj[p]\n          \
    \  for i in range(len(vs)):\n                x = sz[vs[i][0] if self.has_weight\
    \ else vs[i]]\n                if x > sz[vs[0][0] if self.has_weight else vs[0]]:\n\
    \                    vs[0], vs[i] = vs[i], vs[0]\n                sz[p] += x\n\
    \n    def _dfs_hld(self) -> None:\n        # calc hld\n        adj, into, head,\
    \ hld = self.adj, self.into, self.head, self.hld\n\n        st = [self.root]\n\
    \        while st:\n            v = st.pop()\n            into[v] = len(hld)\n\
    \            hld.append(v)\n            if self.has_weight:\n                for\
    \ e in adj[v][1:]:\n                    u = e[0]\n                    head[u]\
    \ = u\n                    st.append(u)\n                if adj[v]:\n        \
    \            u = adj[v][0][0]\n                    head[u] = head[v]\n       \
    \             st.append(u)\n            else:\n                for u in adj[v][1:]:\n\
    \                    head[u] = u\n                    st.append(u)\n         \
    \       if adj[v]:\n                    u = adj[v][0]\n                    head[u]\
    \ = head[v]\n                    st.append(u)\n\n    def build_list(self, a: list[int])\
    \ -> list[int]:\n        return [a[x] for x in self.hld]\n\n    def lca(self,\
    \ u: int, v: int) -> int:\n        into, par, head, depth = self.into, self.par,\
    \ self.head, self.depth\n        while head[u] != head[v]:\n            if into[u]\
    \ < into[v]:\n                u, v = v, u\n            u = par[head[u]]\n    \
    \    return u if depth[u] < depth[v] else v\n\n    def dist(self, u: int, v: int)\
    \ -> int:\n        depth = self.depth\n        return depth[u] + depth[v] - 2\
    \ * depth[self.lca(u, v)]\n\n    def jump(self, u: int, v: int, k: int) -> int:\n\
    \        head, depth, par = self.head, self.depth, self.par\n\n        d = self.dist(u,\
    \ v)\n        if d < k:\n            return -1\n        lca = self.lca(u, v)\n\
    \        if depth[u] - depth[lca] < k:\n            u = v\n            k = d -\
    \ k\n        h = head[u]\n        while depth[u] - depth[h] < k:\n           \
    \ k -= depth[u] - depth[h] + 1\n            u = par[h]\n            h = head[u]\n\
    \        return self.hld[self.into[u] - k]\n\n    def is_on_path(self, u: int,\
    \ v: int, x: int) -> bool:\n        return self.dist(u, x) + self.dist(x, v) ==\
    \ self.dist(u, v)\n\n    def index(self, idx: int, edge: bool = False) -> int:\n\
    \        return self.into[idx] + edge\n\n    def _ascend(self, u: int, v: int)\
    \ -> list[tuple[int, int]]:\n        into, head, par, depth = self.into, self.head,\
    \ self.par, self.depth\n        res = []\n        while head[u] != head[v]:\n\
    \            res.append((into[u], into[head[u]]))\n            u = par[head[u]]\n\
    \        if u != v:\n            res.append((into[u], into[v] + 1))\n        return\
    \ res\n\n    def _descend(self, u: int, v: int) -> list[tuple[int, int]]:\n  \
    \      return [(r, l) for l, r in self._ascend(v, u)[::-1]]\n\n    def path_query(self,\
    \ u: int, v: int, edge: bool = False) -> list[tuple[int, int]]:\n        l = self.lca(u,\
    \ v)\n        tmp = self._ascend(u, l)\n        if not edge:\n            tmp.append((self.into[l],\
    \ self.into[l]))\n        tmp += self._descend(l, v)\n        res = []\n     \
    \   for l, r in tmp:\n            if l > r:\n                l, r = r, l\n   \
    \         res.append((l, r + 1))\n        return res\n\n    def path_query_noncommutative(\n\
    \        self, u: int, v: int, edge: bool = False\n    ) -> list[tuple[int, int,\
    \ bool]]:\n        l = self.lca(u, v)\n        tmp = self._ascend(u, l)\n    \
    \    if not edge:\n            tmp.append((self.into[l], self.into[l]))\n    \
    \    tmp += self._descend(l, v)\n        res = []\n        for l, r in tmp:\n\
    \            if l > r:\n                res.append((r, l + 1, True))\n       \
    \     else:\n                res.append((l, r + 1, False))\n        return res\n\
    \n    def subtree_query(self, u: int, edge: bool = False) -> tuple[int, int]:\n\
    \        return self.into[u] + edge, self.into[u] + self.sz[u]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/heavy_light_decomposition.py
  requiredBy: []
  timestamp: '2024-09-02 11:34:25+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/past/past4m_hld.test.py
  - "test/yukicoder/235_\u3081\u3050\u308B\u306F\u3081\u3050\u308B(5).test.py"
  - "test/yukicoder/399_\u52D5\u7684\u306A\u9818\u4E3B.test.py"
  - test/aoj/grl/grl_5_d_range_query_on_a_tree_hld.test.py
  - test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
  - test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
  - test/library_checker/tree/jump_on_tree_hld.test.py
  - test/library_checker/tree/vertext_set_path_composite.test.py
  - test/library_checker/tree/vertex_add_path_sum_hld.test.py
  - test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
documentation_of: graph/tree/heavy_light_decomposition.py
layout: document
title: "HL\u5206\u89E3"
---

木の高さを圧縮する.

https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3


