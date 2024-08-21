---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/bipartite_matching.py
    title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u30DE\u30C3\u30C1\u30F3\u30B0"
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/bipartite_edge_coloring.test.py
    title: Edge Coloring of Bipartite Graph
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import *\n\nfrom graph.connectivity.unionfind import UnionFind\n\
    from graph.bipartite_matching import bipartite_matching\n\n\nclass RegularBipartiteGlaph:\n\
    \    def __init__(self, l: int, r: int, edges: list[tuple[int, int]]):\n     \
    \   self.l = l\n        self.r = r\n        self.el = []\n        self.er = []\n\
    \        for u, v in edges:\n            self.el.append(u)\n            self.er.append(v)\n\
    \        self._regularize()\n\n    def _contract(self, deg: list[int], k: int)\
    \ -> UnionFind:\n        pq = []\n        for i in range(len(deg)):\n        \
    \    heappush(pq, (deg[i], i))\n        uf = UnionFind(len(deg))\n        while\
    \ len(pq) > 1:\n            di, i = heappop(pq)\n            dj, j = heappop(pq)\n\
    \            if di + dj > k:\n                continue\n            uf.merge(i,\
    \ j)\n            heappush(pq, (di + dj, i))\n        return uf\n\n    def _regularize(self):\n\
    \        dl = [0] * self.l\n        dr = [0] * self.r\n        for i in self.el:\n\
    \            dl[i] += 1\n        for i in self.er:\n            dr[i] += 1\n \
    \       self.k = k = max(max(dl), max(dr))\n        ufl = self._contract(dl, k)\n\
    \        ufr = self._contract(dr, k)\n        cl = cr = 0\n        idl = [0] *\
    \ self.l\n        idr = [0] * self.r\n        for i in range(self.l):\n      \
    \      if ufl.leader(i) == i:\n                idl[i] = cl\n                cl\
    \ += 1\n        for i in range(self.r):\n            if ufr.leader(i) == i:\n\
    \                idr[i] = cr\n                cr += 1\n        self.n = n = max(cl,\
    \ cr)\n        self.lt = []\n        self.rt = []\n        dl = [0] * n\n    \
    \    dr = [0] * n\n        for i in range(len(self.el)):\n            l = idl[ufl.leader(self.el[i])]\n\
    \            r = idr[ufr.leader(self.er[i])]\n            self.lt.append(l)\n\
    \            self.rt.append(r)\n            dl[l] += 1\n            dr[r] += 1\n\
    \        j = 0\n        for i in range(n):\n            while dl[i] < k:\n   \
    \             while dr[j] == k:\n                    j += 1\n                self.lt.append(i)\n\
    \                self.rt.append(j)\n                dl[i] += 1\n             \
    \   dr[j] += 1\n\n\nclass BipartiteEdgeColoring:\n    def __init__(self, rg: RegularBipartiteGlaph):\n\
    \        self.n = rg.n\n        self.k = rg.k\n        self.lt = rg.lt\n     \
    \   self.rt = rg.rt\n        self.group = []\n        self.color = [-1] * self.n\
    \ * self.k\n\n    def euler_trail(self, edge: list[tuple[int, int]]) -> list[tuple[int,\
    \ int]]:\n        g = [[] for _ in range(self.n * 2)]\n        m = len(edge)\n\
    \        for i, e in enumerate(edge):\n            g[self.lt[e]].append((self.rt[e]\
    \ + self.n, i))\n            g[self.rt[e] + self.n].append((self.lt[e], i))\n\
    \        used_vtx = [False] * self.n * 2\n        used_edge = [False] * m\n  \
    \      res = []\n        for i in range(2 * self.n):\n            if used_vtx[i]:\n\
    \                continue\n            st = [(i, -1)]\n            ord = []\n\
    \            while st:\n                j = st[-1][0]\n                used_vtx[j]\
    \ = True\n                if g[j]:\n                    v, e = g[j].pop()\n  \
    \                  if used_edge[e]:\n                        continue\n      \
    \              used_edge[e] = True\n                    st.append((v, e))\n  \
    \              else:\n                    v, e = st.pop()\n                  \
    \  ord.append(e)\n            res.extend(ord[:-1][::-1])\n        for i, p in\
    \ enumerate(res):\n            res[i] = edge[p]\n        return res\n\n    def\
    \ solve(self):\n        ord = [i for i in range(len(self.lt))]\n        st = [(self.k,\
    \ ord)]\n        while st:\n            k, edge = st.pop()\n            if k ==\
    \ 0:\n                continue\n            if k == 1:\n                self.group.append(edge)\n\
    \            elif k % 2 == 0:\n                path = self.euler_trail(edge)\n\
    \                ord1 = []\n                ord2 = []\n                for i,\
    \ p in enumerate(path):\n                    if i % 2 == 0:\n                \
    \        ord1.append(p)\n                    else:\n                        ord2.append(p)\n\
    \                st += [(k // 2, ord1), (k // 2, ord2)]\n            else:\n \
    \               match_l, _ = bipartite_matching(\n                    self.n,\
    \ self.n, [(self.lt[i], self.rt[i]) for i in range(len(edge))]\n             \
    \   )\n                ord = []\n                matched = []\n              \
    \  for i in edge:\n                    if match_l[self.lt[i]] == self.rt[i]:\n\
    \                        match_l[self.lt[i]] = -1\n                        matched.append(i)\n\
    \                    else:\n                        ord.append(i)\n          \
    \      self.group.append(matched)\n                st.append((k - 1, ord))\n \
    \       for i in range(self.k):\n            for j in self.group[i]:\n       \
    \         self.color[j] = i\n"
  dependsOn:
  - graph/connectivity/unionfind.py
  - graph/bipartite_matching.py
  isVerificationFile: false
  path: graph/bipartite_edge_coloring.py
  requiredBy: []
  timestamp: '2024-08-21 11:11:33+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/bipartite_edge_coloring.test.py
documentation_of: graph/bipartite_edge_coloring.py
layout: document
title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u306E\u8FBA\u5F69\u8272"
---
