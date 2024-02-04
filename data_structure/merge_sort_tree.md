---
title: Merge Sort Tree
documentation_of: ./merge_sort_tree.py
---

セグメント木にソート済みの配列をのせたもの.


### mst = MergeSortTree(arr)

初期化．$arr$はクエリの配列であり変更不可．

### mst.sum_le(l, r, x)

配列$arr$の半開区間$[l,r)$で、$x$以下の値の合計を計算する.

### mst.sum_lt(l, r, x)

配列$arr$の半開区間$[l,r)$で、$x$未満の値の合計を計算する.