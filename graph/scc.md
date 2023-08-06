---
title: 強連結成分分解
documentation_of: ./scc.py
---

強連結成分に分解する.

### `scc(N: int, M: int, edges: List[Tuple[int, int]]) `

- Args
    - $N$: グラフの頂点の数
    - $M$: 辺の数
    - $edges$: 辺のリスト.各要素は`(u,v)`のタプルで,頂点$u$から頂点$v$への有向辺を指す.
- Return  
sccの返り値は2次元のリスト. 全体のリストの要素数は強連結成分の数だけあって,各リストの要素は強連結成分に含まれる頂点すべてが入る.