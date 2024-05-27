---
title: (全方位)木DP
documentation_of: ./tree_dp.py
---

木上でのDP. 葉から根に向かって遷移させる．
全方位木DPは，ある頂点を根としたDPの結果から部分木をうまく計算して，各頂点を根としたときの値を求めることができる．$O(N)$

### `TDP=TreeDP(n, adj, r=0)`

頂点数$n$の隣接リストで初期化する．デフォルトでは，頂点$0$を根とする．

### `TDP.calc(MAX)`

組み合わせ計算の前処理.

### `TDP.size()`

部分木のサイズを求める．根は初期化時に指定する.

### `TDP.dp(e, op)`

木上でDPを計算する．引数の$e$は遷移の単位元，$op$は遷移の関数.

### `TDP.rerooting(e, merge, adj_bu, adj_td, adj_fin)`

全方位木DPを計算する．各引数の詳細は下記リンクを参照.  
https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3

### 木DP

- https://atcoder.jp/contests/abc036/tasks/abc036_d

### 全方位木DP

- https://atcoder.jp/contests/dp/tasks/dp_v
- https://atcoder.jp/contests/abc160/tasks/abc160_f
- https://atcoder.jp/contests/abc220/tasks/abc220_f
- https://atcoder.jp/contests/abc223/tasks/abc223_g
