---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/eulerian_trail_directed.test.py
    title: Eulerian Trail (Directed)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/eulerian_trail_undirected.test.py
    title: Eulerian Trail (Undirected)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class EulerianTrail:\n    def __init__(\n        self, n: int, edges: list[tuple[int,\
    \ int]], is_undirected: bool = True\n    ):\n        self.n = n\n        self.m\
    \ = len(edges)\n        self.edges = edges\n        self.is_undirected = is_undirected\n\
    \        self.adj = [[] for _ in range(n)]\n        for eid, (u, v) in enumerate(edges):\n\
    \            self.adj[u].append((v, eid))\n            if is_undirected:\n   \
    \             self.adj[v].append((u, eid))\n\n    def get_edge_order(self) ->\
    \ tuple[int, list[int]]:\n        if self.m == 0:\n            return 0, []\n\n\
    \        n, m, adj, edges = self.n, self.m, self.adj, self.edges\n\n        s\
    \ = -1\n        if self.is_undirected:\n            codd = sum(len(adj[v]) & 1\
    \ for v in range(n))\n            if codd > 2:\n                return -1, []\n\
    \            if codd == 2:\n                for v in range(n):\n             \
    \       if len(adj[v]) & 1 == 1:\n                        s = v\n            \
    \            break\n        else:\n            di = [0] * n\n            for _,\
    \ v in edges:\n                di[v] += 1\n            codd = sum(abs(len(adj[v])\
    \ - di[v]) for v in range(n))\n            if codd > 2:\n                return\
    \ -1, []\n            if codd == 2:\n                for v in range(n):\n    \
    \                if len(adj[v]) > di[v]:\n                        s = v\n    \
    \                    break\n        if s < 0:\n            for v in range(n):\n\
    \                if len(adj[v]) > 0:\n                    s = v\n            \
    \        break\n\n        ep = [0] * n\n        eids = [0] * m\n        used =\
    \ [0] * m\n        pp, pq = 0, m\n        v = s\n        while pp < pq:\n    \
    \        if ep[v] >= len(adj[v]):\n                if pp == 0:\n             \
    \       return -1, []\n                pq -= 1\n                pp -= 1\n    \
    \            eids[pq] = eids[pp]\n                a, b = edges[eids[pq]]\n   \
    \             v ^= a ^ b\n            else:\n                e = adj[v][ep[v]][1]\n\
    \                ep[v] += 1\n                if used[e]:\n                   \
    \ continue\n                used[e] = 1\n                eids[pp] = e\n      \
    \          pp += 1\n                a, b = edges[e]\n                v ^= a ^\
    \ b\n        return s, eids\n\n    def get_verticle_order(self, start: int, eids:\
    \ list[int]) -> list[int]:\n        path = [start]\n        cur = start\n    \
    \    for i in eids:\n            u, v = self.edges[i]\n            cur ^= u ^\
    \ v\n            path.append(cur)\n        return path\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/eulerian_trail.py
  requiredBy: []
  timestamp: '2024-07-19 13:46:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/eulerian_trail_directed.test.py
  - test/library_checker/graph/eulerian_trail_undirected.test.py
documentation_of: graph/eulerian_trail.py
layout: document
redirect_from:
- /library/graph/eulerian_trail.py
- /library/graph/eulerian_trail.py.html
title: graph/eulerian_trail.py
---
