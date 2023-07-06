---
title: Splay tree
documentation_of: ./splay_tree.py
---

追加、削除、検索が$O(logN)$でできる二分木。
独特なSplay操作により、選択された頂点が上にくるため、繰り返し同じ内容を検索するときに有利。
Splay操作は木を平衡二分木に近い状態に保ち、最悪計算量を悪化させない。


### `ST=SplayTree()`

初期化。

### `ST.insert(x)`

$x$を追加する。

### `ST.search(self, ST.root, x)`

スプレー木から$x$のノードを検索する。第１引数は検索を開始するノードを指定する。$x$により近い先祖ノードが分かっていればルートノード以外を指定してもよい。

### `ST.delete(x)`

$x$を削除する

### `ST.inorder(ST.root)`

ルートノードの子孫ノードを左から順に出力する。