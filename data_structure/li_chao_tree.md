---
title: Li Chao Tree
documentation_of: ./li_chao_tree.py
---

直線集合に直線追加($ax+b$), 直線集合に対して$x$での最小値を求める．

### LCT = LiChaoTree(arr)

初期化．$arr$はクエリの配列(オフライン不可)．

### LCT.add_edge(a, b)

直線$ax+b$を追加する．

### LCT.query(x)

点$x$での最小値を求める．