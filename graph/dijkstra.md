---
title: Dijkstra
documentation_of: ./dijkstra.py
---

N頂点、M辺の有向グラフで、頂点uから頂点vに距離cの辺をgraph[u] = [(c,v)]で持つ。

### dijkstra(N, graph, start)

頂点startから各頂点への最短距離を計算する。

注意：距離が負の辺には適用不可

#### Args
N: グラフの頂点数

G: 隣接リスト。頂点uから頂点vへの距離cをG[u] = [(c, v)]で表す。

start: 開始する頂点番号

#### Return
dist: 各頂点への距離を持つリスト

prev: 各頂点の親頂点を持つリスト  


### get_path(prev, start, goal)

頂点startから頂点goalまでのパスを返す

#### Args
prev: 各頂点の親頂点を持つリスト  

start, goal: 頂点番号

#### Return

path: 頂点番号のリスト。(path[0]=start, path[-1]=goal)


