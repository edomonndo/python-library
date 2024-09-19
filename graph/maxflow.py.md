---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_6_a_max_flow.test.py
    title: "GRL6A \u6700\u5927\u6D41"
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_7_a_bipartite_matching.test.py
    title: "GRL7A 2\u90E8\u30DE\u30C3\u30C1\u30F3\u30B0"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import NamedTuple, Optional\n\n\nclass MaxFlow:\n    class Edge(NamedTuple):\n\
    \        src: int\n        dst: int\n        cap: int\n        flow: int\n\n \
    \   class _Edge:\n        def __init__(self, dst: int, cap: int) -> None:\n  \
    \          self.dst = dst\n            self.cap = cap\n            self.rev: Optional[MaxFlow._Edge]\
    \ = None\n\n    def __init__(self, n: int) -> None:\n        self._n = n\n   \
    \     self._g: list[list[MaxFlow._Edge]] = [[] for _ in range(n)]\n        self._edges:\
    \ list[MaxFlow._Edge] = []\n\n    def add_edge(self, src: int, dst: int, cap:\
    \ int) -> int:\n        assert 0 <= src < self._n\n        assert 0 <= dst < self._n\n\
    \        assert 0 <= cap\n        m = len(self._edges)\n        e = MaxFlow._Edge(dst,\
    \ cap)\n        re = MaxFlow._Edge(src, 0)\n        e.rev = re\n        re.rev\
    \ = e\n        self._g[src].append(e)\n        self._g[dst].append(re)\n     \
    \   self._edges.append(e)\n        return m\n\n    def get_edge(self, i: int)\
    \ -> Edge:\n        assert 0 <= i < len(self._edges)\n        e = self._edges[i]\n\
    \        re = e.rev\n        return MaxFlow.Edge(re.dst, e.dst, e.cap + re.cap,\
    \ re.cap)\n\n    def edges(self) -> list[Edge]:\n        return [self.get_edge(i)\
    \ for i in range(len(self._edges))]\n\n    def change_edge(self, i: int, new_cap:\
    \ int, new_flow: int) -> None:\n        assert 0 <= i < len(self._edges)\n   \
    \     assert 0 <= new_flow <= new_cap\n        e = self._edges[i]\n        e.cap\
    \ = new_cap - new_flow\n        assert e.rev is not None\n        e.rev.cap =\
    \ new_flow\n\n    def flow(self, s: int, t: int, flow_limit: Optional[int] = None)\
    \ -> int:\n        assert 0 <= s < self._n\n        assert 0 <= t < self._n\n\
    \        assert s != t\n        if flow_limit is None:\n            flow_limit\
    \ = sum(e.cap for e in self._g[s])\n\n        current_edge = [0] * self._n\n \
    \       level = [0] * self._n\n\n        def bfs() -> bool:\n            for i\
    \ in range(self._n):\n                level[i] = self._n\n            queue =\
    \ []\n            q_front = 0\n            queue.append(s)\n            level[s]\
    \ = 0\n            while q_front < len(queue):\n                v = queue[q_front]\n\
    \                q_front += 1\n                next_level = level[v] + 1\n   \
    \             for e in self._g[v]:\n                    if e.cap == 0 or level[e.dst]\
    \ <= next_level:\n                        continue\n                    level[e.dst]\
    \ = next_level\n                    if e.dst == t:\n                        return\
    \ True\n                    queue.append(e.dst)\n            return False\n\n\
    \        def dfs(lim: int) -> int:\n            st = []\n            edge_st:\
    \ list[MaxFlow._Edge] = []\n            st.append(t)\n            while st:\n\
    \                v = st[-1]\n                if v == s:\n                    flow\
    \ = min(lim, min(e.cap for e in edge_st))\n                    for e in edge_st:\n\
    \                        e.cap -= flow\n                        assert e.rev is\
    \ not None\n                        e.rev.cap += flow\n                    return\
    \ flow\n                next_level = level[v] - 1\n                while current_edge[v]\
    \ < len(self._g[v]):\n                    e = self._g[v][current_edge[v]]\n  \
    \                  re = e.rev\n                    if level[e.dst] != next_level\
    \ or re.cap == 0:\n                        current_edge[v] += 1\n            \
    \            continue\n                    st.append(e.dst)\n                \
    \    edge_st.append(re)\n                    break\n                else:\n  \
    \                  st.pop()\n                    if edge_st:\n               \
    \         edge_st.pop()\n                    level[v] = self._n\n            return\
    \ 0\n\n        flow = 0\n        while flow < flow_limit:\n            if not\
    \ bfs():\n                break\n            for i in range(self._n):\n      \
    \          current_edge[i] = 0\n            while flow < flow_limit:\n       \
    \         f = dfs(flow_limit - flow)\n                flow += f\n            \
    \    if f == 0:\n                    break\n        return flow\n\n    def min_cut(self,\
    \ s: int) -> list[bool]:\n        visited = [False] * self._n\n        st = [s]\n\
    \        visited[s] = True\n        while st:\n            v = st.pop()\n    \
    \        for e in self._g[v]:\n                if e.cap > 0 and not visited[e.dst]:\n\
    \                    visited[e.dst] = True\n                    st.append(e.dst)\n\
    \        return visited\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/maxflow.py
  requiredBy: []
  timestamp: '2024-08-27 15:46:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_7_a_bipartite_matching.test.py
  - test/aoj/grl/grl_6_a_max_flow.test.py
documentation_of: graph/maxflow.py
layout: document
title: "\u6700\u5927\u30D5\u30ED\u30FC"
---

最大フロー問題を解く．

## 初期化　$O(N)$

```
G = mf_graph(N)
```

頂点数$N$のグラフを定義する．

## add_edge $O(1)$

```
G.add_edge(u, v, cap)
```

頂点$u$から頂点$v$へ，最大容量$cap$，流量$0$の辺を追加する．

## get_edge $O(1)$

```
G.get_edge(i)
```
$i$番目の辺の状態を返す．順番はadd_edgeで追加された順番．

## edges $O(M)$

```
G.edges()
```
`flow`を実行した後に，どの辺にどれだけの流量が流れているかを返す．
返り値は辞書のリストであり，キーは以下の4つのである．
- from: 出発する頂点
- to: 辺の向かう頂点
- cap: 最大流量
- flow: 流量

## change_edge　$O(1)$

```
G.change_edge(i, new_cap, new_flow)
```
$i$番目に追加された辺の容量，流量を更新する．


## flow $O(N^2M)$

```
G.flow(s, t, flow_limit)
```
頂点$s$から頂点$t$への最大フローを求める．flow_limitで流量の上限を指定可能．

## min_cut $O(N+M)$

```
G.min_cut(s)
```
長さ$N$の配列が返り，頂点$s$から残余グラフで到達可能なとき，その頂点の値はTrueである．
`flow(s, t)`をflow_limitなしでちょうど１回呼んだ後に実行すると，返り値は$s,t$間のmincutに対応する．