---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/tree_decomposition_width2.test.py
    title: Tree Decomposition (Width 2)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\nfrom typing import Optional\nimport sys\n\n\
    sys.setrecursionlimit(2_000_000)\n\nfrom graph.connectivity.unionfind import UnionFind\n\
    \n\nclass TreeDecompositionWidth2:\n    def __init__(self, n: int, edges: list[tuple[int,\
    \ int]]):\n        self.n = n\n        self.adj = adj = [[] for _ in range(n)]\n\
    \        for u, v in edges:\n            if u == v:\n                continue\n\
    \            if u > v:\n                u, v = v, u\n            du, dv = len(adj[u]),\
    \ len(adj[v])\n            adj[u].append((v, dv))\n            adj[v].append((u,\
    \ du))\n\n    def _remove_edge(self, u: int, idx_uv: int) -> int:\n        adj\
    \ = self.adj\n        v, idx_vu = adj[u][idx_uv]\n        if idx_vu != len(adj[v])\
    \ - 1:\n            w, idx_wv = adj[v][-1]\n            adj[v][idx_vu], adj[v][-1]\
    \ = adj[v][-1], adj[v][idx_vu]\n            c, _ = adj[w][idx_wv]\n          \
    \  adj[w][idx_wv] = (c, idx_vu)\n        adj[v].pop()\n        if idx_uv != len(adj[u])\
    \ - 1:\n            z, idx_zu = adj[u][-1]\n            adj[u][idx_uv], adj[u][-1]\
    \ = adj[u][-1], adj[u][idx_uv]\n            c, _ = adj[z][idx_zu]\n          \
    \  adj[z][idx_zu] = (c, idx_uv)\n        adj[u].pop()\n        self._remove_multiedges(v,\
    \ idx_vu)\n        self._remove_multiedges(u, idx_uv)\n        return v\n\n  \
    \  def _remove_multiedges(self, u: int, idx_uv: int) -> None:\n        def is_unnecessary(idx_uv:\
    \ int) -> bool:\n            us = self.adj[u]\n            du = len(us)\n    \
    \        if idx_uv >= du:\n                return False\n            c = us[idx_uv][0]\n\
    \            for di in [-2, -1, 1, 2]:\n                nidx = idx_uv + di\n \
    \               if 0 <= nidx < du and c == us[nidx][0]:\n                    return\
    \ True\n            return False\n\n        while is_unnecessary(idx_uv):\n  \
    \          self._remove_edge(u, idx_uv)\n\n    def build(self) -> Optional[tuple[list[list[int]],\
    \ list[tuple[int, int]]]]:\n        n, adj = self.n, self.adj\n        seen =\
    \ [0] * n\n        dq = deque()\n        for i in range(n):\n            if len(adj[i])\
    \ <= 2:\n                dq.append(i)\n                seen[i] = 1\n\n       \
    \ roots = []\n        edges = []\n        bag = [[] for _ in range(n)]\n     \
    \   link = [[] for _ in range(n)]\n        uf = UnionFind(n)\n        for i in\
    \ range(n):\n            if not dq:\n                return None\n           \
    \ u = dq.popleft()\n            if len(adj[u]) == 0:\n                bag[i] =\
    \ [u]\n                roots.append(i)\n            elif len(adj[u]) == 1:\n \
    \               v = self._remove_edge(u, 0)\n                if len(adj[v]) <=\
    \ 2:\n                    if not seen[v]:\n                        seen[v] = 1\n\
    \                        dq.append(v)\n                bag[i] = [u, v]\n     \
    \           link[v].append(i)\n            else:\n                v = self._remove_edge(u,\
    \ 0)\n                w = self._remove_edge(u, 0)\n                if v > w:\n\
    \                    v, w = w, v\n                bag[i] = [u, v, w]\n       \
    \         dv, dw = len(adj[v]), len(adj[w])\n                adj[v].append((w,\
    \ dw))\n                adj[w].append((v, dv))\n                self._remove_multiedges(v,\
    \ dv)\n                self._remove_multiedges(w, dw)\n                if len(adj[v])\
    \ <= 2:\n                    if not seen[v]:\n                        seen[v]\
    \ = 1\n                        dq.append(v)\n                if len(adj[w]) <=\
    \ 2:\n                    if not seen[w]:\n                        seen[w] = 1\n\
    \                        dq.append(w)\n                link[v].append(i)\n   \
    \             link[w].append(i)\n\n            link[u].reverse()\n           \
    \ for j in link[u]:\n                if not uf.same(i, j):\n                 \
    \   edges.append((i, j))\n                    uf.merge(i, j)\n            adj[u].clear()\n\
    \            link[u].clear()\n\n        for i in range(len(roots) - 1):\n    \
    \        edges.append((roots[i], roots[i + 1]))\n        return bag, edges\n"
  dependsOn:
  - graph/connectivity/unionfind.py
  isVerificationFile: false
  path: graph/tree_decomposition_width2.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/tree_decomposition_width2.test.py
documentation_of: graph/tree_decomposition_width2.py
layout: document
redirect_from:
- /library/graph/tree_decomposition_width2.py
- /library/graph/tree_decomposition_width2.py.html
title: graph/tree_decomposition_width2.py
---
