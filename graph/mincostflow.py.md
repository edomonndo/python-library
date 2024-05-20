---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_6_b_min_cost_flow.test.py
    title: test/aoj/grl_6_b_min_cost_flow.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\n\n\nclass mcf_graph:\n    n = 1\n    pos = []\n    g = [[]]\n\
    \n    def __init__(self, N):\n        self.n = N\n        self.pos = []\n    \
    \    self.g = [[] for i in range(N)]\n\n    def add_edge(self, From, To, cap,\
    \ cost):\n        assert 0 <= From and From < self.n\n        assert 0 <= To and\
    \ To < self.n\n        self.pos.append((From, len(self.g[From])))\n        self.g[From].append(\n\
    \            {\"to\": To, \"rev\": len(self.g[To]), \"cap\": cap, \"cost\": cost}\n\
    \        )\n        self.g[To].append(\n            {\"to\": From, \"rev\": len(self.g[From])\
    \ - 1, \"cap\": 0, \"cost\": -cost}\n        )\n\n    def get_edge(self, i):\n\
    \        m = len(self.pos)\n        assert 0 <= i and i < m\n        _e = self.g[self.pos[i][0]][self.pos[i][1]]\n\
    \        _re = self.g[_e[\"to\"]][_e[\"rev\"]]\n        return {\n           \
    \ \"from\": self.pos[i][0],\n            \"to\": _e[\"to\"],\n            \"cap\"\
    : _e[\"cap\"] + _re[\"cap\"],\n            \"flow\": _re[\"cap\"],\n         \
    \   \"cost\": _e[\"cost\"],\n        }\n\n    def edges(self):\n        m = len(self.pos)\n\
    \        result = [{} for i in range(m)]\n        for i in range(m):\n       \
    \     tmp = self.get_edge(i)\n            result[i][\"from\"] = tmp[\"from\"]\n\
    \            result[i][\"to\"] = tmp[\"to\"]\n            result[i][\"cap\"] =\
    \ tmp[\"cap\"]\n            result[i][\"flow\"] = tmp[\"flow\"]\n            result[i][\"\
    cost\"] = tmp[\"cost\"]\n        return result\n\n    def flow(self, s, t, flow_limit=-1\
    \ - (-1 << 63)):\n        return self.slope(s, t, flow_limit)[-1]\n\n    def slope(self,\
    \ s, t, flow_limit=-1 - (-1 << 63)):\n        assert 0 <= s and s < self.n\n \
    \       assert 0 <= t and t < self.n\n        assert s != t\n\n        dual =\
    \ [0 for i in range(self.n)]\n        dist = [0 for i in range(self.n)]\n    \
    \    pv = [0 for i in range(self.n)]\n        pe = [0 for i in range(self.n)]\n\
    \        vis = [False for i in range(self.n)]\n\n        def dual_ref():\n   \
    \         for i in range(self.n):\n                dist[i] = -1 - (-1 << 63)\n\
    \                pv[i] = -1\n                pe[i] = -1\n                vis[i]\
    \ = False\n            que = []\n            heapq.heappush(que, (0, s))\n   \
    \         dist[s] = 0\n            while que:\n                v = heapq.heappop(que)[1]\n\
    \                if vis[v]:\n                    continue\n                vis[v]\
    \ = True\n                if v == t:\n                    break\n\n          \
    \      for i in range(len(self.g[v])):\n                    e = self.g[v][i]\n\
    \                    if vis[e[\"to\"]] or not e[\"cap\"]:\n                  \
    \      continue\n\n                    cost = e[\"cost\"] - dual[e[\"to\"]] +\
    \ dual[v]\n                    if dist[e[\"to\"]] - dist[v] > cost:\n        \
    \                dist[e[\"to\"]] = dist[v] + cost\n                        pv[e[\"\
    to\"]] = v\n                        pe[e[\"to\"]] = i\n                      \
    \  heapq.heappush(que, (dist[e[\"to\"]], e[\"to\"]))\n            if not vis[t]:\n\
    \                return False\n            for v in range(self.n):\n         \
    \       if not vis[v]:\n                    continue\n                dual[v]\
    \ -= dist[t] - dist[v]\n            return True\n\n        flow = 0\n        cost\
    \ = 0\n        prev_cost = -1\n        result = [(flow, cost)]\n        while\
    \ flow < flow_limit:\n            if not dual_ref():\n                break\n\
    \            c = flow_limit - flow\n            v = t\n            while v !=\
    \ s:\n                c = min(c, self.g[pv[v]][pe[v]][\"cap\"])\n            \
    \    v = pv[v]\n            v = t\n            while v != s:\n               \
    \ self.g[pv[v]][pe[v]][\"cap\"] -= c\n                self.g[v][self.g[pv[v]][pe[v]][\"\
    rev\"]][\"cap\"] += c\n                v = pv[v]\n            d = -dual[s]\n \
    \           flow += c\n            cost += c * d\n            if prev_cost ==\
    \ d:\n                result.pop()\n            result.append((flow, cost))\n\
    \            prev_cost = cost\n        return result\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/mincostflow.py
  requiredBy: []
  timestamp: '2023-08-06 23:53:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl_6_b_min_cost_flow.test.py
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