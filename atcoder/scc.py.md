---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: atcoder/twosat.py
    title: atcoder/twosat.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\n\nclass CSR:\n    def __init__(self, n: int, edges: list[tuple[int,\
    \ int]]) -> None:\n        self.start = [0] * (n + 1)\n        self.elist = [0]\
    \ * len(edges)\n\n        for e in edges:\n            self.start[e[0] + 1] +=\
    \ 1\n\n        for i in range(1, n + 1):\n            self.start[i] += self.start[i\
    \ - 1]\n\n        counter = self.start.copy()\n        for e in edges:\n     \
    \       self.elist[counter[e[0]]] = e[1]\n            counter[e[0]] += 1\n\n\n\
    class _SCCGraph:\n    \"\"\"\n    Reference:\n    R. Tarjan,\n    Depth-First\
    \ Search and Linear Graph Algorithms\n    \"\"\"\n\n    def __init__(self, n:\
    \ int) -> None:\n        self._n = n\n        self._edges: list[tuple[int, int]]\
    \ = []\n\n    def num_vertices(self) -> int:\n        return self._n\n\n    def\
    \ add_edge(self, from_vertex: int, to_vertex: int) -> None:\n        self._edges.append((from_vertex,\
    \ to_vertex))\n\n    def scc_ids(self) -> tuple[int, list[int]]:\n        g =\
    \ CSR(self._n, self._edges)\n        now_ord = 0\n        group_num = 0\n    \
    \    visited = []\n        low = [0] * self._n\n        order = [-1] * self._n\n\
    \        ids = [0] * self._n\n\n        sys.setrecursionlimit(max(self._n + 1000,\
    \ sys.getrecursionlimit()))\n\n        def dfs(v: int) -> None:\n            nonlocal\
    \ now_ord\n            nonlocal group_num\n            nonlocal visited\n    \
    \        nonlocal low\n            nonlocal order\n            nonlocal ids\n\n\
    \            low[v] = now_ord\n            order[v] = now_ord\n            now_ord\
    \ += 1\n            visited.append(v)\n            for i in range(g.start[v],\
    \ g.start[v + 1]):\n                to = g.elist[i]\n                if order[to]\
    \ == -1:\n                    dfs(to)\n                    low[v] = min(low[v],\
    \ low[to])\n                else:\n                    low[v] = min(low[v], order[to])\n\
    \n            if low[v] == order[v]:\n                while True:\n          \
    \          u = visited[-1]\n                    visited.pop()\n              \
    \      order[u] = self._n\n                    ids[u] = group_num\n          \
    \          if u == v:\n                        break\n                group_num\
    \ += 1\n\n        for i in range(self._n):\n            if order[i] == -1:\n \
    \               dfs(i)\n\n        for i in range(self._n):\n            ids[i]\
    \ = group_num - 1 - ids[i]\n\n        return group_num, ids\n\n    def scc(self)\
    \ -> list[list[int]]:\n        ids = self.scc_ids()\n        group_num = ids[0]\n\
    \        counts = [0] * group_num\n        for x in ids[1]:\n            counts[x]\
    \ += 1\n        groups: list[list[int]] = [[] for _ in range(group_num)]\n   \
    \     for i in range(self._n):\n            groups[ids[1][i]].append(i)\n\n  \
    \      return groups\n\n\nclass SCCGraph:\n    def __init__(self, n: int = 0)\
    \ -> None:\n        self._internal = _SCCGraph(n)\n\n    def add_edge(self, from_vertex:\
    \ int, to_vertex: int) -> None:\n        n = self._internal.num_vertices()\n \
    \       assert 0 <= from_vertex < n\n        assert 0 <= to_vertex < n\n     \
    \   self._internal.add_edge(from_vertex, to_vertex)\n\n    def scc(self) -> list[list[int]]:\n\
    \        return self._internal.scc()\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/scc.py
  requiredBy:
  - atcoder/twosat.py
  timestamp: '2024-05-29 14:24:11+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/scc.py
layout: document
redirect_from:
- /library/atcoder/scc.py
- /library/atcoder/scc.py.html
title: atcoder/scc.py
---