---
title: 最小コストフロー
documentation_of: ./mincostflow.py
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