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
  code: "from typing import NamedTuple, Optional, List, cast\n\n\nclass MFGraph:\n\
    \    class Edge(NamedTuple):\n        src: int\n        dst: int\n        cap:\
    \ int\n        flow: int\n\n    class _Edge:\n        def __init__(self, dst:\
    \ int, cap: int) -> None:\n            self.dst = dst\n            self.cap =\
    \ cap\n            self.rev: Optional[MFGraph._Edge] = None\n\n    def __init__(self,\
    \ n: int) -> None:\n        self._n = n\n        self._g: List[List[MFGraph._Edge]]\
    \ = [[] for _ in range(n)]\n        self._edges: List[MFGraph._Edge] = []\n\n\
    \    def add_edge(self, src: int, dst: int, cap: int) -> int:\n        assert\
    \ 0 <= src < self._n\n        assert 0 <= dst < self._n\n        assert 0 <= cap\n\
    \        m = len(self._edges)\n        e = MFGraph._Edge(dst, cap)\n        re\
    \ = MFGraph._Edge(src, 0)\n        e.rev = re\n        re.rev = e\n        self._g[src].append(e)\n\
    \        self._g[dst].append(re)\n        self._edges.append(e)\n        return\
    \ m\n\n    def get_edge(self, i: int) -> Edge:\n        assert 0 <= i < len(self._edges)\n\
    \        e = self._edges[i]\n        re = cast(MFGraph._Edge, e.rev)\n       \
    \ return MFGraph.Edge(\n            re.dst,\n            e.dst,\n            e.cap\
    \ + re.cap,\n            re.cap\n        )\n\n    def edges(self) -> List[Edge]:\n\
    \        return [self.get_edge(i) for i in range(len(self._edges))]\n\n    def\
    \ change_edge(self, i: int, new_cap: int, new_flow: int) -> None:\n        assert\
    \ 0 <= i < len(self._edges)\n        assert 0 <= new_flow <= new_cap\n       \
    \ e = self._edges[i]\n        e.cap = new_cap - new_flow\n        assert e.rev\
    \ is not None\n        e.rev.cap = new_flow\n\n    def flow(self, s: int, t: int,\
    \ flow_limit: Optional[int] = None) -> int:\n        assert 0 <= s < self._n\n\
    \        assert 0 <= t < self._n\n        assert s != t\n        if flow_limit\
    \ is None:\n            flow_limit = cast(int, sum(e.cap for e in self._g[s]))\n\
    \n        current_edge = [0] * self._n\n        level = [0] * self._n\n\n    \
    \    def fill(arr: List[int], value: int) -> None:\n            for i in range(len(arr)):\n\
    \                arr[i] = value\n\n        def bfs() -> bool:\n            fill(level,\
    \ self._n)\n            queue = []\n            q_front = 0\n            queue.append(s)\n\
    \            level[s] = 0\n            while q_front < len(queue):\n         \
    \       v = queue[q_front]\n                q_front += 1\n                next_level\
    \ = level[v] + 1\n                for e in self._g[v]:\n                    if\
    \ e.cap == 0 or level[e.dst] <= next_level:\n                        continue\n\
    \                    level[e.dst] = next_level\n                    if e.dst ==\
    \ t:\n                        return True\n                    queue.append(e.dst)\n\
    \            return False\n\n        def dfs(lim: int) -> int:\n            stack\
    \ = []\n            edge_stack: List[MFGraph._Edge] = []\n            stack.append(t)\n\
    \            while stack:\n                v = stack[-1]\n                if v\
    \ == s:\n                    flow = min(lim, min(e.cap for e in edge_stack))\n\
    \                    for e in edge_stack:\n                        e.cap -= flow\n\
    \                        assert e.rev is not None\n                        e.rev.cap\
    \ += flow\n                    return flow\n                next_level = level[v]\
    \ - 1\n                while current_edge[v] < len(self._g[v]):\n            \
    \        e = self._g[v][current_edge[v]]\n                    re = cast(MFGraph._Edge,\
    \ e.rev)\n                    if level[e.dst] != next_level or re.cap == 0:\n\
    \                        current_edge[v] += 1\n                        continue\n\
    \                    stack.append(e.dst)\n                    edge_stack.append(re)\n\
    \                    break\n                else:\n                    stack.pop()\n\
    \                    if edge_stack:\n                        edge_stack.pop()\n\
    \                    level[v] = self._n\n            return 0\n\n        flow\
    \ = 0\n        while flow < flow_limit:\n            if not bfs():\n         \
    \       break\n            fill(current_edge, 0)\n            while flow < flow_limit:\n\
    \                f = dfs(flow_limit - flow)\n                flow += f\n     \
    \           if f == 0:\n                    break\n        return flow\n\n   \
    \ def min_cut(self, s: int) -> List[bool]:\n        visited = [False] * self._n\n\
    \        stack = [s]\n        visited[s] = True\n        while stack:\n      \
    \      v = stack.pop()\n            for e in self._g[v]:\n                if e.cap\
    \ > 0 and not visited[e.dst]:\n                    visited[e.dst] = True\n   \
    \                 stack.append(e.dst)\n        return visited\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/maxflow.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/maxflow.py
layout: document
redirect_from:
- /library/atcoder/maxflow.py
- /library/atcoder/maxflow.py.html
title: atcoder/maxflow.py
---
