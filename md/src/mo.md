---
title: Mo's Algorithm
documentation_of: //data_structure/mo.py
---

静的な配列で,クエリが先読みでき,区間$[l,r)$の結果から区間$[l+1,r)$,$[l−1,r)$,$[l,r−1)$,$[l,r+1)$の結果を容易に計算できるとき,適用できる.

区間の変更に対する処理は問題ごとに設定する必要がある. `MoState`クラスに記述する.

### mo = Mo(A)

初期化．

### mo.add_query(l, r)

半開区間$[l,r)$のクエリを追加する.

### mo.calc()

クエリの結果を取得する.