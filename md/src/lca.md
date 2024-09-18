---
title: 最近共通祖先(Lowest Common Ancestor)
documentation_of: //graph/tree/lca.py
---

木上の頂点$u,v$の共通祖先の中でも最も$u,v$に近い頂点を求める.

### `lca=LcaDoubling(N: int, G: List[List[int]], root: int = 0)`

頂点数$N$の隣接リスト$G$で根を$root$にして初期化する.実装はダブリング.

### `lca.lca(u: int, v: int)`

頂点$u,v$の最近共通祖先を求める.

### `lca.dist(u: int, v: int)`

頂点$u,v$の最短距離を求める.

### `lca.up(v: int, k: int)`

頂点$v$から$k$個親の頂点を求める.

### `lca.jump(u: int, v: int, i: int)`

頂点$u,v$の最短経路上の$i$番目の頂点を求める.始点・終点は$u,v$で,$i$が最短距離より大きい場合は`-1`を返す.