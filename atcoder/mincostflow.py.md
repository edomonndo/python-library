---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import NamedTuple, Optional, List, Tuple, cast\nfrom heapq import\
    \ heappush, heappop\n\n\nclass MCFGraph:\n    class Edge(NamedTuple):\n      \
    \  src: int\n        dst: int\n        cap: int\n        flow: int\n        cost:\
    \ int\n\n    class _Edge:\n        def __init__(self, dst: int, cap: int, cost:\
    \ int) -> None:\n            self.dst = dst\n            self.cap = cap\n    \
    \        self.cost = cost\n            self.rev: Optional[MCFGraph._Edge] = None\n\
    \n    def __init__(self, n: int) -> None:\n        self._n = n\n        self._g:\
    \ List[List[MCFGraph._Edge]] = [[] for _ in range(n)]\n        self._edges: List[MCFGraph._Edge]\
    \ = []\n\n    def add_edge(self, src: int, dst: int, cap: int, cost: int) -> int:\n\
    \        assert 0 <= src < self._n\n        assert 0 <= dst < self._n\n      \
    \  assert 0 <= cap\n        m = len(self._edges)\n        e = MCFGraph._Edge(dst,\
    \ cap, cost)\n        re = MCFGraph._Edge(src, 0, -cost)\n        e.rev = re\n\
    \        re.rev = e\n        self._g[src].append(e)\n        self._g[dst].append(re)\n\
    \        self._edges.append(e)\n        return m\n\n    def get_edge(self, i:\
    \ int) -> Edge:\n        assert 0 <= i < len(self._edges)\n        e = self._edges[i]\n\
    \        re = cast(MCFGraph._Edge, e.rev)\n        return MCFGraph.Edge(\n   \
    \         re.dst,\n            e.dst,\n            e.cap + re.cap,\n         \
    \   re.cap,\n            e.cost\n        )\n\n    def edges(self) -> List[Edge]:\n\
    \        return [self.get_edge(i) for i in range(len(self._edges))]\n\n    def\
    \ flow(self, s: int, t: int,\n             flow_limit: Optional[int] = None) ->\
    \ Tuple[int, int]:\n        return self.slope(s, t, flow_limit)[-1]\n\n    def\
    \ slope(self, s: int, t: int,\n              flow_limit: Optional[int] = None)\
    \ -> List[Tuple[int, int]]:\n        assert 0 <= s < self._n\n        assert 0\
    \ <= t < self._n\n        assert s != t\n        if flow_limit is None:\n    \
    \        flow_limit = cast(int, sum(e.cap for e in self._g[s]))\n\n        dual\
    \ = [0] * self._n\n        prev: List[Optional[Tuple[int, MCFGraph._Edge]]] =\
    \ [None] * self._n\n\n        def refine_dual() -> bool:\n            pq = [(0,\
    \ s)]\n            visited = [False] * self._n\n            dist: List[Optional[int]]\
    \ = [None] * self._n\n            dist[s] = 0\n            while pq:\n       \
    \         dist_v, v = heappop(pq)\n                if visited[v]:\n          \
    \          continue\n                visited[v] = True\n                if v ==\
    \ t:\n                    break\n                dual_v = dual[v]\n          \
    \      for e in self._g[v]:\n                    w = e.dst\n                 \
    \   if visited[w] or e.cap == 0:\n                        continue\n         \
    \           reduced_cost = e.cost - dual[w] + dual_v\n                    new_dist\
    \ = dist_v + reduced_cost\n                    dist_w = dist[w]\n            \
    \        if dist_w is None or new_dist < dist_w:\n                        dist[w]\
    \ = new_dist\n                        prev[w] = v, e\n                       \
    \ heappush(pq, (new_dist, w))\n            else:\n                return False\n\
    \            dist_t = dist[t]\n            for v in range(self._n):\n        \
    \        if visited[v]:\n                    dual[v] -= cast(int, dist_t) - cast(int,\
    \ dist[v])\n            return True\n\n        flow = 0\n        cost = 0\n  \
    \      prev_cost_per_flow: Optional[int] = None\n        result = [(flow, cost)]\n\
    \        while flow < flow_limit:\n            if not refine_dual():\n       \
    \         break\n            f = flow_limit - flow\n            v = t\n      \
    \      while prev[v] is not None:\n                u, e = cast(Tuple[int, MCFGraph._Edge],\
    \ prev[v])\n                f = min(f, e.cap)\n                v = u\n       \
    \     v = t\n            while prev[v] is not None:\n                u, e = cast(Tuple[int,\
    \ MCFGraph._Edge], prev[v])\n                e.cap -= f\n                assert\
    \ e.rev is not None\n                e.rev.cap += f\n                v = u\n \
    \           c = -dual[s]\n            flow += f\n            cost += f * c\n \
    \           if c == prev_cost_per_flow:\n                result.pop()\n      \
    \      result.append((flow, cost))\n            prev_cost_per_flow = c\n     \
    \   return result\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/mincostflow.py
  requiredBy: []
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/mincostflow.py
layout: document
redirect_from:
- /library/atcoder/mincostflow.py
- /library/atcoder/mincostflow.py.html
title: atcoder/mincostflow.py
---
