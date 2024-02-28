---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_2_b_minimum_cost_arborescence.test.py
    title: test/aoj/grl_2_b_minimum_cost_arborescence.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\n\n\nclass MinCostArborescence:\n    # Edmonds' algorithm\n\
    \    def __init__(self, N, edges, root):\n        self.N = N\n        self.G =\
    \ [[] for _ in range(N)]\n        self.r = root\n        for u, v, w in edges:\n\
    \            if v != root:\n                heapq.heappush(self.G[v], [w, u, v])\n\
    \n    def calc_min_cost(self, weight=0):\n        min_incoming_edges = [None]\
    \ * self.N\n        for edges in self.G:\n            if edges:\n            \
    \    min_edge = edges[0]\n                min_incoming_edges[min_edge[2]] = min_edge\n\
    \                weight += min_edge[0]\n        vs_in_cycle = self._find_cycle(min_incoming_edges)\n\
    \        if not vs_in_cycle:\n            return weight\n        else:\n     \
    \       self._contract_cycle(vs_in_cycle)\n            return self.calc_min_cost(weight)\n\
    \n    def _find_cycle(self, incoming_edges):\n        in_tree = [0] * self.N\n\
    \        in_tree[self.r] = 1\n        for edge in incoming_edges:\n          \
    \  if edge:\n                S = [edge[2]]\n                while True:\n    \
    \                par = incoming_edges[S[-1]][1]\n                    if in_tree[par]:\n\
    \                        while S:\n                            in_tree[S.pop()]\
    \ = 1\n                        break\n                    elif par in S:\n   \
    \                     return S[S.index(par) :]\n                    else:\n  \
    \                      S.append(par)\n        return None\n\n    def _contract_cycle(self,\
    \ vs_in_cycle):\n        v_super = vs_in_cycle[0]\n        for edges in self.G:\n\
    \            if edges:\n                min_weight = edges[0][0]\n           \
    \     for edge in edges:\n                    edge[0] -= min_weight\n        \
    \            if edge[1] in vs_in_cycle:\n                        edge[1] = v_super\n\
    \                    if edge[2] in vs_in_cycle:\n                        edge[2]\
    \ = v_super\n        contracted_edges = []\n        for v in vs_in_cycle:\n  \
    \          for edge in self.G[v]:\n                if edge[1] != v_super:\n  \
    \                  contracted_edges.append(edge)\n            self.G[v] = []\n\
    \        self.G[v_super] = contracted_edges\n        heapq.heapify(self.G[v_super])\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/mincost_arborescence.py
  requiredBy: []
  timestamp: '2023-09-07 08:38:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl_2_b_minimum_cost_arborescence.test.py
documentation_of: graph/mincost_arborescence.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6709\u5411\u6728"
---
