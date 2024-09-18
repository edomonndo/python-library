---
title: Deque（＋ランダムアクセス・合計）
documentation_of: //data_structure/basic/deque.py
---

デフォルトのdequeのランダムアクセスが計算量$O(N)$であるのに対し,$O(1)$で可能.

また,キューに入った要素の合計も$O(1)$で取得できる.

使い方は通常のdequeと同様.

バッファを拡張する/確認する作業が相対的に重いため,`max_size`が抑えられるならば,`is_full()`を外し多少の高速化が可能.

### `Deque.appendleft(x)`,`Deque.append(x)`

キューの先頭/末尾に$x$を追加する.

### `Deque.popleft()`,`Deque.pop()`

キューの先頭/末尾から$x$を削除する.削除した値が返り値となる.

### `Deque.sum`

キューに入った要素の合計を$O(1)$で取得する.