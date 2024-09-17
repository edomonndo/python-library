---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: graph/connectivity/euler_tour_tree.py
    title: graph/connectivity/euler_tour_tree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/other/2235_graph_construction.test.py
    title: 2235 Graph Construction
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/dynamic_graph_vertex_add_component_sum_online.test.py
    title: Dynamic Graph Vertex Add Component Sum (Online)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\nfrom graph.connectivity.euler_tour_tree\
    \ import EulerTourTree\n\n\nclass DynamicConnectivity:\n    def __init__(self,\
    \ n: int, op: Callable[[T, T], T], e: T):\n        self.n = n\n        self.ett\
    \ = [EulerTourTree(n, op, e)]\n        self.edges = [[set() for _ in range(n)]]\n\
    \        self.depth = 1\n        self.op = op\n        self.e = e\n\n    def link(self,\
    \ u: int, v: int) -> bool:\n        ett, edges = self.ett, self.edges\n      \
    \  if u == v:\n            return False\n        if ett[0].link(u, v):\n     \
    \       return True\n        edges[0][u].add(v)\n        edges[0][v].add(u)\n\
    \        if len(edges[0][u]) == 1:\n            ett[0].edge_connected_update(u,\
    \ True)\n        if len(edges[0][v]) == 1:\n            ett[0].edge_connected_update(v,\
    \ True)\n        return False\n\n    def same(self, u: int, v: int) -> bool:\n\
    \        return self.ett[0].same(u, v)\n\n    def size(self, v: int) -> int:\n\
    \        return self.ett[0].size(v)\n\n    def cut(self, u: int, v: int) -> bool:\n\
    \        ett, edges = self.ett, self.edges\n        if u == v:\n            return\
    \ False\n        for i in range(self.depth):\n            edges[i][u].discard(v)\n\
    \            edges[i][v].discard(u)\n            if len(edges[i][u]) == 0:\n \
    \               ett[i].edge_connected_update(u, False)\n            if len(edges[i][v])\
    \ == 0:\n                ett[i].edge_connected_update(v, False)\n        for i\
    \ in range(self.depth - 1, -1, -1):\n            if ett[i].cut(u, v):\n      \
    \          if self.depth - 1 == i:\n                    self.depth += 1\n    \
    \                ett.append(EulerTourTree(self.n, self.op, self.e))\n        \
    \            edges.append([set() for _ in range(self.n)])\n                return\
    \ not self.try_reconnect(u, v, i)\n        return False\n\n    def try_reconnect(self,\
    \ u: int, v: int, k: int) -> bool:\n        ett, edges = self.ett, self.edges\n\
    \n        def op1(s: int, t: int) -> None:\n            ett[i + 1].link(s, t)\n\
    \n        def op2(x: int) -> bool:\n            arr = list(edges[i][x])\n    \
    \        for y in arr:\n                edges[i][x].discard(y)\n             \
    \   edges[i][y].discard(x)\n                if len(edges[i][x]) == 0:\n      \
    \              ett[i].edge_connected_update(x, False)\n                if len(edges[i][y])\
    \ == 0:\n                    ett[i].edge_connected_update(y, False)\n        \
    \        if ett[i].same(x, y):\n                    edges[i + 1][x].add(y)\n \
    \                   edges[i + 1][y].add(x)\n                    if len(edges[i\
    \ + 1][x]) == 1:\n                        ett[i + 1].edge_connected_update(x,\
    \ True)\n                    if len(edges[i + 1][y]) == 1:\n                 \
    \       ett[i + 1].edge_connected_update(y, True)\n                else:\n   \
    \                 for j in range(i + 1):\n                        ett[j].link(x,\
    \ y)\n                    return True\n            return False\n\n        for\
    \ i in range(k):\n            ett[i].cut(u, v)\n        for i in range(k, -1,\
    \ -1):\n            if ett[i].size(u) > ett[i].size(v):\n                u, v\
    \ = v, u\n            ett[i].edge_update(u, op1)\n            if ett[i].try_reconnect(u,\
    \ op2):\n                return True\n        return False\n\n    def update(self,\
    \ v: int, x: T) -> None:\n        self.ett[0].update(v, x)\n\n    def get_sum(self,\
    \ v: int) -> T:\n        return self.ett[0].get_sum(v)\n"
  dependsOn:
  - graph/connectivity/euler_tour_tree.py
  isVerificationFile: false
  path: graph/connectivity/dynamic_connectivity.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/dynamic_graph_vertex_add_component_sum_online.test.py
  - test/aoj/other/2235_graph_construction.test.py
documentation_of: graph/connectivity/dynamic_connectivity.py
layout: document
redirect_from:
- /library/graph/connectivity/dynamic_connectivity.py
- /library/graph/connectivity/dynamic_connectivity.py.html
title: graph/connectivity/dynamic_connectivity.py
---
