---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/vertex_add_path_sum_hld.test.py
    title: Vertex Add Path Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/vertex_add_subtree_sum_hld.test.py
    title: Vertex Add Subtree Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/vertext_set_path_composite.test.py
    title: Vertex Set Path Composite
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable\n\n\nclass HeavyLightDecomposition:\n    def\
    \ __init__(self, n: int, edges: list[tuple[int, int]], root: int = 0):\n     \
    \   self.n = n\n        self.root = root\n        self.depth = [0] * n\n     \
    \   self.into = [-1] * n\n        self.out = [-1] * n\n        self.head = [root]\
    \ * n\n        self.par = [root] * n\n        self.adj = [[] for _ in range(n)]\n\
    \        for u, v in edges:\n            self.adj[u].append(v)\n            self.adj[v].append(u)\n\
    \        self._dfs_sz()\n        self._dfs_hld()\n\n    def _dfs_sz(self) -> None:\n\
    \        # calc subtree size\n        adj, par, depth = self.adj, self.par, self.depth\n\
    \        sz = [0] * self.n\n        st = [self.root]\n        while st:\n    \
    \        v = st.pop()\n            if v >= 0:\n                sz[v] = 1\n   \
    \             if len(adj[v]) >= 2 and adj[v][-1] == par[v]:\n                \
    \    adj[v][-1], adj[v][-2] = adj[v][-2], adj[v][-1]\n                for i, u\
    \ in enumerate(adj[v]):\n                    if u == par[v]:\n               \
    \         continue\n                    depth[u] = depth[v] + 1\n            \
    \        par[u] = v\n                    st += [i, ~u, u]\n                continue\n\
    \            v = ~v\n            p = par[v]\n            i = st.pop()\n      \
    \      sz[p] += sz[v]\n            if sz[v] > sz[adj[p][-1]]:\n              \
    \  adj[p][-1], adj[p][i] = adj[p][i], adj[p][-1]\n\n    def _dfs_hld(self):\n\
    \        # calc hld\n        adj, into, out, par, head = self.adj, self.into,\
    \ self.out, self.par, self.head\n        idx = 0\n        st = [~self.root, self.root]\n\
    \        while st:\n            v = st.pop()\n            if v >= 0:\n       \
    \         into[v] = idx\n                idx += 1\n                for u in adj[v]:\n\
    \                    if u == par[v]:\n                        continue\n     \
    \               head[u] = head[v] if u == adj[v][-1] else u\n                \
    \    st += [~u, u]\n                continue\n            out[~v] = idx\n\n  \
    \  def ascend(self, u: int, v: int) -> list[tuple[int, int]]:\n        into, par,\
    \ head = self.into, self.par, self.head\n        res = []\n        while head[u]\
    \ != head[v]:\n            res.append((into[u], into[head[u]]))\n            u\
    \ = par[head[u]]\n        if u != v:\n            res.append((into[u], into[v]\
    \ + 1))\n        return res\n\n    def descend(self, u: int, v: int) -> list[tuple[int,\
    \ int]]:\n        into, par, head = self.into, self.par, self.head\n        res\
    \ = []\n        while u != v:\n            if head[u] == head[v]:\n          \
    \      res.append((into[u] + 1, into[v]))\n                break\n           \
    \ res.append((into[head[v]], into[v]))\n            v = par[head[v]]\n       \
    \ return res[::-1]\n\n    def lca(self, u: int, v: int) -> int:\n        into,\
    \ par, head, depth = self.into, self.par, self.head, self.depth\n        while\
    \ head[u] != head[v]:\n            if into[u] < into[v]:\n                u, v\
    \ = v, u\n            u = par[head[u]]\n        return u if depth[u] < depth[v]\
    \ else v\n\n    def dist(self, u: int, v: int) -> int:\n        depth = self.depth\n\
    \        return depth[u] + depth[v] - 2 * depth[self.lca(u, v)]\n\n    def path_query(\n\
    \        self, u: int, v: int, f: Callable[[int, int], None], edge: bool = False\n\
    \    ) -> None:\n        l = self.lca(u, v)\n        for a, b in self.ascend(u,\
    \ l):\n            s, t = a + 1, b\n            f(s, t) if s < t else f(t, s)\n\
    \        if not edge:\n            f(self.into[l], self.into[l] + 1)\n       \
    \ for a, b in self.descend(l, v):\n            s, t = a, b + 1\n            f(s,\
    \ t) if s < t else f(t, s)\n\n    def path_noncommutative_query(\n        self,\
    \ u: int, v: int, f: Callable[[int, int], None], edge: bool = False\n    ) ->\
    \ None:\n        l = self.lca(u, v)\n        for a, b in self.ascend(u, l):\n\
    \            f(a + 1, b)\n        if not edge:\n            f(self.into[l], self.into[l]\
    \ + 1)\n        for a, b in self.descend(l, v):\n            f(a, b + 1)\n\n \
    \   def subtree_query(\n        self, u: int, f: Callable[[int, int], None], edge:\
    \ bool = False\n    ) -> None:\n        f(self.into[u] + edge, self.out[u])\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/heavy_light_decomposition.py
  requiredBy: []
  timestamp: '2024-06-09 10:02:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/vertext_set_path_composite.test.py
  - test/library_checker/data_structure/vertex_add_subtree_sum_hld.test.py
  - test/library_checker/data_structure/vertex_add_path_sum_hld.test.py
documentation_of: tree/heavy_light_decomposition.py
layout: document
title: "HL\u5206\u89E3"
---

木の高さを圧縮する.

https://qiita.com/Pro_ktmr/items/4e1e051ea0561772afa3


