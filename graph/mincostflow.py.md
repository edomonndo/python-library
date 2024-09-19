---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_6_b_min_cost_flow.test.py
    title: "GRL6B \u6700\u5C0F\u8CBB\u7528\u6D41"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import NamedTuple, Optional\nfrom heapq import *\n\n\nclass MinCostFlow:\n\
    \    class Edge(NamedTuple):\n        src: int\n        dst: int\n        cap:\
    \ int\n        flow: int\n        cost: int\n\n    class _Edge:\n        def __init__(self,\
    \ dst: int, cap: int, cost: int) -> None:\n            self.dst = dst\n      \
    \      self.cap = cap\n            self.cost = cost\n            self.rev: Optional[MinCostFlow._Edge]\
    \ = None\n\n    def __init__(self, n: int) -> None:\n        self._n = n\n   \
    \     self._g: list[list[MinCostFlow._Edge]] = [[] for _ in range(n)]\n      \
    \  self._edges: list[MinCostFlow._Edge] = []\n\n    def add_edge(self, src: int,\
    \ dst: int, cap: int, cost: int) -> int:\n        assert 0 <= src < self._n\n\
    \        assert 0 <= dst < self._n\n        assert 0 <= cap\n        m = len(self._edges)\n\
    \        e = MinCostFlow._Edge(dst, cap, cost)\n        re = MinCostFlow._Edge(src,\
    \ 0, -cost)\n        e.rev = re\n        re.rev = e\n        self._g[src].append(e)\n\
    \        self._g[dst].append(re)\n        self._edges.append(e)\n        return\
    \ m\n\n    def get_edge(self, i: int) -> Edge:\n        assert 0 <= i < len(self._edges)\n\
    \        e = self._edges[i]\n        re = e.rev\n        return MinCostFlow.Edge(re.dst,\
    \ e.dst, e.cap + re.cap, re.cap, e.cost)\n\n    def edges(self) -> list[Edge]:\n\
    \        return [self.get_edge(i) for i in range(len(self._edges))]\n\n    def\
    \ flow(self, s: int, t: int, flow_limit: Optional[int] = None) -> tuple[int, int]:\n\
    \        return self.slope(s, t, flow_limit)[-1]\n\n    def slope(\n        self,\
    \ s: int, t: int, flow_limit: Optional[int] = None\n    ) -> list[tuple[int, int]]:\n\
    \        assert 0 <= s < self._n\n        assert 0 <= t < self._n\n        assert\
    \ s != t\n        if flow_limit is None:\n            flow_limit = sum(e.cap for\
    \ e in self._g[s])\n\n        dual = [0] * self._n\n        prev: list[Optional[tuple[int,\
    \ MinCostFlow._Edge]]] = [None] * self._n\n\n        def refine_dual() -> bool:\n\
    \            pq = [(0, s)]\n            visited = [False] * self._n\n        \
    \    dist: list[Optional[int]] = [None] * self._n\n            dist[s] = 0\n \
    \           while pq:\n                dist_v, v = heappop(pq)\n             \
    \   if visited[v]:\n                    continue\n                visited[v] =\
    \ True\n                if v == t:\n                    break\n              \
    \  dual_v = dual[v]\n                for e in self._g[v]:\n                  \
    \  w = e.dst\n                    if visited[w] or e.cap == 0:\n             \
    \           continue\n                    reduced_cost = e.cost - dual[w] + dual_v\n\
    \                    new_dist = dist_v + reduced_cost\n                    dist_w\
    \ = dist[w]\n                    if dist_w is None or new_dist < dist_w:\n   \
    \                     dist[w] = new_dist\n                        prev[w] = v,\
    \ e\n                        heappush(pq, (new_dist, w))\n            else:\n\
    \                return False\n            dist_t = dist[t]\n            for v\
    \ in range(self._n):\n                if visited[v]:\n                    dual[v]\
    \ -= dist_t - dist[v]\n            return True\n\n        flow = 0\n        cost\
    \ = 0\n        prev_cost_per_flow: Optional[int] = None\n        result = [(flow,\
    \ cost)]\n        while flow < flow_limit:\n            if not refine_dual():\n\
    \                break\n            f = flow_limit - flow\n            v = t\n\
    \            while prev[v] is not None:\n                u, e = prev[v]\n    \
    \            f = min(f, e.cap)\n                v = u\n            v = t\n   \
    \         while prev[v] is not None:\n                u, e = prev[v]\n       \
    \         e.cap -= f\n                assert e.rev is not None\n             \
    \   e.rev.cap += f\n                v = u\n            c = -dual[s]\n        \
    \    flow += f\n            cost += f * c\n            if c == prev_cost_per_flow:\n\
    \                result.pop()\n            result.append((flow, cost))\n     \
    \       prev_cost_per_flow = c\n        return result\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/mincostflow.py
  requiredBy: []
  timestamp: '2024-08-27 15:46:23+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_6_b_min_cost_flow.test.py
documentation_of: graph/mincostflow.py
layout: document
title: "\u6700\u5C0F\u30B3\u30B9\u30C8\u30D5\u30ED\u30FC"
---

最小コストフロー問題を解く．

## 初期化　$O(N)$

```
G = mcf_graph(N)
```

頂点数$N$のグラフを定義する．

## add_edge $O(1)$

```
G.add_edge(From, To, cap, cost)
```

頂点$u$から頂点$v$へ，最大容量$cap$，コスト$cost$の辺を追加する．

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


## flow $O(F(N+M) \log(N+M)$

```
G.flow(s, t, flow_limit)
```
頂点$s$から頂点$t$へ流せるだけ流し，その流量とコストを返す．flow_limitで流量の上限を指定可能．

## min_cut_slope $O(F(N+M) \log(N+M)$

```
G.min_cost_slope(s, t, flow_limit)
```
返り値に流量とコストの関係の折線が入る．全ての$x$について，流量$x$の時の最小コストを$g(x)$とすると，$(x, g(x))$は返り値を折線として見たものに含まれる．

- 返り値の最初の要素は$(0,0)$
- 返り値のタプルは共に狭義単調増加
- 3点が同一線上にあることはない
- (1) 返り値の最後の要素は最大流量$x$として$(x,g(x))$
- (2) 返り値の最後の要素は$y=min(x, flow_limit)$として(y,g(y))