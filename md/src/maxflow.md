---
title: 最大フロー
documentation_of: //graph/maxflow.py
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