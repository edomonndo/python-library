---
title: 最適二分探索木(Hu-Tucker)
documentation_of: //data_structure/binary_search_tree/hu_tucker.py
---

$n$個の葉をもつ順序付き二分木の最小コストを求める.
コストは以下で定義する.

$$\displaystyle\sum^{n-1}_{i=0} {W_i} \times {depth_i}$$

$W_i$は葉の重み,$depth_i$は二分木における左から$i$個目の葉の深さを表す.

参考：https://atcoder.jp/contests/atc002/tasks/atc002_c