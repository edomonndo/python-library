---
title: ValueRangeSum
documentation_of: ./value_range_sum.py
---

配列$A$に対して，$x$（未満/以下/以上/超過）の値の和を求める．
また，$x$との差の絶対値の和も求められる．

配列は一点更新が可能.

`ValueRangeSum`: $A[i]$の値を直接BITで管理する．

`CompressedValueRangeSum`: 座標圧縮することで$A[i]$が$10^9$オーダーでも対応可能．`possible_values`はクエリも含めて$A[i]$のとりうる値の集合. `possible_xs`はクエリで指定する$x$の集合.