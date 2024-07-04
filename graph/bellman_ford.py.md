---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_b_bellman_ford.test.py
    title: "GRL1B \u5358\u4E00\u59CB\u70B9\u6700\u77ED\u7D4C\u8DEF\uFF08\u8CA0\u306E\
      \u91CD\u307F\u3092\u3082\u3064\u8FBA\u3092\u542B\u3080\uFF09"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BellmanFord:\n    def __init__(self, n):\n        self.n = n\n    \
    \    self.adj = [[] for _ in range(n)]\n        self.adj_rev = [[] for _ in range(n)]\n\
    \        self.edges = []\n\n    def add_edge(self, u: int, v: int, w: int):\n\
    \        self.adj[u].append(v)\n        self.adj_rev[v].append(u)\n        self.edges.append((u,\
    \ v, w))\n\n    @staticmethod\n    def _can_reach(adj: list[list[int]], v: int)\
    \ -> list[bool]:\n        res = [False] * len(adj)\n        res[v] = True\n  \
    \      stack = [v]\n        while stack:\n            v = stack.pop()\n      \
    \      for u in adj[v]:\n                if not res[u]:\n                    res[u]\
    \ = True\n                    stack.append(u)\n        return res\n\n    def solve_spsp(self,\
    \ s: int, t: int) -> tuple[bool, int]:\n        \"\"\"Single-Pair Shortest Path\"\
    \"\"\n        n = self.n\n        assert 0 <= s < n\n        rs = self._can_reach(self.adj,\
    \ s)\n        rt = self._can_reach(self.adj_rev, t)\n        edges = [\n     \
    \       (u, v, w) for u, v, w in self.edges if rs[u] and rt[u] and rs[v] and rt[v]\n\
    \        ]\n\n        inf = float(\"inf\")\n        dist = [inf] * n\n       \
    \ dist[s] = 0\n        for i in range(n):\n            for u, v, w in edges:\n\
    \                if i == n - 1 and dist[v] > dist[u] + w:\n                  \
    \  return False, -1\n                dist[v] = min(dist[v], dist[u] + w)\n   \
    \     return True, dist[t]\n\n    def solve_sssp(self, s: int) -> list[int] |\
    \ int:\n        \"\"\"Single-Source Shortest Path\"\"\"\n        n = self.n\n\
    \        assert 0 <= s < n\n        rs = self._can_reach(self.adj, s)\n      \
    \  edges = [(u, v, w) for u, v, w in self.edges if rs[u] and rs[v]]\n\n      \
    \  inf = float(\"inf\")\n        dist = [inf] * n\n        dist[s] = 0\n     \
    \   for i in range(n):\n            for u, v, w in edges:\n                if\
    \ i == n - 1 and dist[v] > dist[u] + w:\n                    return -1\n     \
    \           dist[v] = min(dist[v], dist[u] + w)\n        return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/bellman_ford.py
  requiredBy: []
  timestamp: '2024-04-19 07:43:56+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_1_b_bellman_ford.test.py
documentation_of: graph/bellman_ford.py
layout: document
title: "\u30D9\u30EB\u30DE\u30F3\u30D5\u30A9\u30FC\u30C9"
---

負の辺があるときに最短経路を求められる．
有向閉路があるときは，$(-1,-1)$を返す．