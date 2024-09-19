---
title: Convex Hull Trick
documentation_of: //data_structure/convex_hull_trick.py
---

直線集合に直線追加($ax+b$), 直線集合に対して$x$での最小値を求める．
追加する直線の傾きが単調増加（減少）であること， クエリの$x$が単調増加（減少）であることに制限することで，直線追加を$O(N)$,クエリを$O(Q)$の計算量にできる．
いずれかの制限がない場合，各々計算量に$O(logN)$がつく．しかし，これは実装されていない．

両方の制限がない場合，[LiChaoTree](./li_chao_tree.py)が利用できる．

### CHT = ConvexHullTrick()

初期化．

### CHT.add_edge(a, b)

直線$ax+b$を追加する．

### CHT.query(x)

点$x$での最小値を求める．