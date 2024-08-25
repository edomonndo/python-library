---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/chordal_graph_recognition.test.py
    title: Chordal Graph Recognition
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class ChordalGraph:\n    def __init__(self, n: int, edges: list[tuple[int,\
    \ int]]):\n        self.n = n\n        self.m = len(edges)\n        self.edges\
    \ = edges\n        self.adj = [[] for _ in range(n)]\n        for u, v in edges:\n\
    \            self.adj[u].append(v)\n            self.adj[v].append(u)\n      \
    \  self.m_phase = 0\n        self.x = self.y = self.z = -1\n        self.adj2\
    \ = None\n        self.mcsordered = None\n        self._is_chordal_graph = None\n\
    \        self.induced_cycle = None\n\n    def _contract(self, mapping: list[int])\
    \ -> list[list[int]]:\n        new_adj = [[] for _ in range(self.n)]\n       \
    \ for u, v in self.edges:\n            nu, nv = mapping[u], mapping[v]\n     \
    \       new_adj[nu].append(nv)\n            new_adj[nv].append(nu)\n        return\
    \ new_adj\n\n    def _adj_query(self, adj: list[list[int]], qs: list[tuple[int,\
    \ int]]) -> list[bool]:\n        n = len(adj)\n        q = len(qs)\n        res\
    \ = [False] * q\n        qadj = [[] for _ in range(self.n)]\n        for qi, (u,\
    \ _) in enumerate(qs):\n            if qi >= self.n:\n                break\n\
    \            if u < self.n:\n                qadj[u].append(qi)\n        buf =\
    \ [-1] * n\n        for i in range(n):\n            for j in adj[i]:\n       \
    \         buf[j] = i\n            for qj in qadj[i]:\n                if buf[qs[qj][1]]\
    \ == i:\n                    res[qj] = True\n        return res\n\n    def get_max_cardinality_search_order(self)\
    \ -> list[int]:\n        if self.m_phase >= 1:\n            return self.mcsordered\n\
    \        res = [0] * self.n\n        idx = [0] * self.n\n        lp = list(range(self.n\
    \ * 2 + 1))\n        rp = list(range(self.n * 2 + 1))\n\n        def insert(i:\
    \ int, j: int) -> None:\n            rp[lp[j]] = i\n            lp[i] = lp[j]\n\
    \            lp[j], rp[i] = i, j\n\n        def erase(i: int) -> None:\n     \
    \       rp[lp[i]] = rp[i]\n            lp[rp[i]] = lp[i]\n\n        for i in range(self.n):\n\
    \            insert(i, self.n)\n        li = self.n\n        for i in range(self.n):\n\
    \            li += 1\n            while lp[li] == li:\n                li -= 1\n\
    \            v = lp[li]\n            idx[v] = -1\n            erase(v)\n     \
    \       for u in self.adj[v]:\n                if idx[u] >= 0:\n             \
    \       erase(u)\n                    idx[u] += 1\n                    insert(u,\
    \ self.n + idx[u])\n            res[i] = v\n        self.m_phase = 1\n       \
    \ self.mcsordered = res\n        return res\n\n    def is_chordal_graph(self)\
    \ -> bool:\n        if self.m_phase < 1:\n            self.get_max_cardinality_search_order()\n\
    \        if self.m_phase >= 2:\n            return self._is_chordal_graph\n\n\
    \        inv_mcs = [0] * self.n\n        for i in range(self.n):\n           \
    \ inv_mcs[self.mcsordered[i]] = i\n\n        self.adj2 = adj2 = self._contract(inv_mcs)\n\
    \        pre = [-1] * self.n\n        for i in range(self.n):\n            for\
    \ j in adj2[i]:\n                if j < i and pre[i] < j:\n                  \
    \  pre[i] = j\n\n        es = []\n        z = []\n        for i in range(self.n):\n\
    \            if pre[i] == -1:\n                continue\n            for j in\
    \ adj2[i]:\n                if j < pre[i]:\n                    es.append((pre[i],\
    \ j))\n                    z.append(i)\n        qres = self._adj_query(adj2, es)\n\
    \        for i, (u, v) in enumerate(es):\n            if not qres[i]:\n      \
    \          self.x, self.y, self.z = v, u, z[i]\n                break\n      \
    \  self.m_phase = 2\n        self._is_chordal_graph = self.z == -1\n        return\
    \ self._is_chordal_graph\n\n    def find_induced_cycle(self) -> list[int]:\n \
    \       if self.m_phase >= 3:\n            return self.induced_cycle\n       \
    \ if self.is_chordal_graph():\n            self.m_phase = 3\n            self.induced_cycle\
    \ = []\n            return self.induced_cycle\n        dist = [0] * self.n\n \
    \       par = [-1] * self.n\n        bfs = [self.x, self.y]\n        for inc in\
    \ self.adj2[self.z]:\n            par[inc] = -2\n        dist[self.x] = -1\n \
    \       dist[self.y] = 1\n        par[self.x] = par[self.y] = self.z\n       \
    \ d = self.n + 1\n        x = y = -1\n        i = 0\n        while i < len(bfs):\n\
    \            p = bfs[i]\n            for q in self.adj2[p]:\n                if\
    \ q < p and par[q] != -2:\n                    if dist[p] < 0 and dist[q] > 0\
    \ and dist[q] - dist[p] < d:\n                        d = dist[q] - dist[p]\n\
    \                        x, y = p, q\n                    elif dist[p] > 0 and\
    \ dist[q] and dist[p] - dist[q] < d:\n                        d = dist[p] - dist[q]\n\
    \                        x, y = q, p\n                    elif dist[q] == 0:\n\
    \                        dist[q] = dist[p] + (-1 if dist[p] < 0 else 1)\n    \
    \                    par[q] = p\n                        bfs.append(q)\n     \
    \       i += 1\n\n        res = [0] * (d + 1)\n        off = -dist[x]\n      \
    \  res[off] = self.mcsordered[self.z]\n        for k in [x, y]:\n            while\
    \ True:\n                res[dist[k] + off] = self.mcsordered[k]\n           \
    \     k = par[k]\n                if k == self.z:\n                    break\n\
    \        self.m_phase = 3\n        self.induced_cycle = res\n        return self.induced_cycle\n\
    \n    def get_perfect_elimination_order(self) -> list[int]:\n        if not self.is_chordal_graph():\n\
    \            return []\n        res = self.get_max_cardinality_search_order()\n\
    \        return res[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/chordal_graph.py
  requiredBy: []
  timestamp: '2024-08-25 16:30:57+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/chordal_graph_recognition.test.py
documentation_of: graph/chordal_graph.py
layout: document
redirect_from:
- /library/graph/chordal_graph.py
- /library/graph/chordal_graph.py.html
title: graph/chordal_graph.py
---
