---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/eulerian_trail_directed.test.py
    title: Eulerian Trail (Directed)
  - icon: ':x:'
    path: test/library_checker/graph/eulerian_trail_undirected.test.py
    title: Eulerian Trail (Undirected)
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
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
    \        break\n\n        ep = [0] * n\n        eids = [0] * m\n        alive\
    \ = [1] * m\n        pp, pq = 0, m\n        v = s\n        while pp < pq:\n  \
    \          if ep[v] >= len(adj[v]):\n                if pp == 0:\n           \
    \         return -1, []\n                pq -= 1\n                pp -= 1\n  \
    \              eids[pq] = eids[pp]\n                a, b = edges[eids[pq]]\n \
    \               v ^= a ^ b\n            else:\n                e = adj[v][ep[v]][1]\n\
    \                ep[v] += 1\n                if not alive[e]:\n              \
    \      continue\n                alive[e] = 0\n                eids[pp] = e\n\
    \                pp += 1\n                a, b = edges[e]\n                v ^=\
    \ a ^ b\n        return s, eids\n\n    def get_verticle_order(self, start: int,\
    \ eids: list[int]) -> list[int]:\n        path = [start]\n        cur = start\n\
    \        for i in eids:\n            u, v = self.edges[i]\n            cur ^=\
    \ u ^ v\n            path.append(cur)\n        return path\n\n\nT = int(input())\n\
    for _ in range(T):\n    n, m = map(int, input().split())\n    edges = [tuple(map(int,\
    \ input().split())) for _ in range(m)]\n    g = EulerianTrail(n, edges, True)\n\
    \    start, eids = g.get_edge_order()\n    if start == -1:\n        print(\"No\"\
    )\n    else:\n        print(\"Yes\")\n        path = g.get_verticle_order(start,\
    \ eids)\n        print(*path)\n        print(*eids)\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/eulerian_trail.py
  requiredBy: []
  timestamp: '2024-07-19 12:35:18+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/eulerian_trail_undirected.test.py
  - test/library_checker/graph/eulerian_trail_directed.test.py
documentation_of: graph/eulerian_trail.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u8DEF"
---
