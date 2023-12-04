---
title: トポロジカルソート
documentation_of: ./topological_sort.py
---

有向グラフの順序を守るようにソートする
閉路があるか判定も出来る
計算量: O(E+V)

G (list): edge[i] = [a, b,...] iからa,b,...に辺が伸びている
deg (list): deg[i] = iの入力辺の本数

返り値が$-1$のとき閉路が存在する．それ以外のとき，ソートされた頂点リストが返る．