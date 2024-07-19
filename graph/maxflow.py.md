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
  code: "from collections import deque\n\n\nclass mf_graph:\n    n = 1\n    g = [[]\
    \ for i in range(1)]\n    pos = []\n\n    def __init__(self, N):\n        self.n\
    \ = N\n        self.g = [[] for i in range(N)]\n        self.pos = []\n\n    def\
    \ add_edge(self, From, To, cap):\n        assert 0 <= From and From < self.n\n\
    \        assert 0 <= To and To < self.n\n        assert 0 <= cap\n        m =\
    \ len(self.pos)\n        from_id = len(self.g[From])\n        self.pos.append([From,\
    \ from_id])\n        to_id = len(self.g[To])\n        if From == To:\n       \
    \     to_id += 1\n        self.g[From].append([To, to_id, cap])\n        self.g[To].append([From,\
    \ from_id, 0])\n        return m\n\n    def get_edge(self, i):\n        m = len(self.pos)\n\
    \        assert 0 <= i and i < m\n        _e = self.g[self.pos[i][0]][self.pos[i][1]]\n\
    \        _re = self.g[_e[0]][_e[1]]\n        return [self.pos[i][0], _e[0], _e[2]\
    \ + _re[2], _re[2]]\n\n    def edges(self):\n        m = len(self.pos)\n     \
    \   result = []\n        for i in range(m):\n            a, b, c, d = self.get_edge(i)\n\
    \            result.append({\"from\": a, \"to\": b, \"cap\": c, \"flow\": d})\n\
    \        return result\n\n    def change_edge(self, i, new_cap, new_flow):\n \
    \       m = len(self.pos)\n        assert 0 <= i and i < m\n        assert 0 <=\
    \ new_flow and new_flow <= new_cap\n        _e = self.g[self.pos[i][0]][self.pos[i][1]]\n\
    \        _re = self.g[_e[0]][_e[1]]\n        _e[2] = new_cap - new_flow\n    \
    \    _re[2] = new_flow\n\n    def flow(self, s, t, flow_limit=(1 << 63) - 1):\n\
    \        assert 0 <= s and s < self.n\n        assert 0 <= t and t < self.n\n\
    \        assert s != t\n\n        def bfs():\n            level = [-1 for i in\
    \ range(self.n)]\n            level[s] = 0\n            que = deque([])\n    \
    \        que.append(s)\n            while que:\n                v = que.popleft()\n\
    \                for to, _, cap in self.g[v]:\n                    if cap == 0\
    \ or level[to] >= 0:\n                        continue\n                    level[to]\
    \ = level[v] + 1\n                    if to == t:\n                        return\
    \ level\n                    que.append(to)\n            return level\n\n    \
    \    def dfs(v, up):\n            if v == s:\n                return up\n    \
    \        res = 0\n            level_v = level[v]\n            for i in range(Iter[v],\
    \ len(self.g[v])):\n                Iter[v] = i\n                to, rev, _ =\
    \ self.g[v][i]\n                if level_v <= level[to] or self.g[to][rev][2]\
    \ == 0:\n                    continue\n                d = dfs(to, min(up - res,\
    \ self.g[to][rev][2]))\n                if d <= 0:\n                    continue\n\
    \                self.g[v][i][2] += d\n                self.g[to][rev][2] -= d\n\
    \                res += d\n                if res == up:\n                   \
    \ return res\n            level[v] = self.n\n            return res\n\n      \
    \  flow = 0\n        while flow < flow_limit:\n            level = bfs()\n   \
    \         if level[t] == -1:\n                break\n            Iter = [0 for\
    \ i in range(self.n)]\n            f = dfs(t, flow_limit - flow)\n           \
    \ if not f:\n                break\n            flow += f\n        return flow\n\
    \n    def min_cut(self, s):\n        visited = [False for i in range(self.n)]\n\
    \        que = deque([])\n        que.append(s)\n        while len(que) > 0:\n\
    \            p = que.popleft()\n            visited[p] = True\n            for\
    \ to, _, cap in self.g[p]:\n                if cap and not visited[to]:\n    \
    \                visited[to] = True\n                    que.append(to)\n    \
    \    return visited\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/maxflow.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
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