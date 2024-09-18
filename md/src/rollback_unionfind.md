---
title: Rollback Union Find
documentation_of: //graph/connectivity/rollback_unionfind.py
---

UnionFindにundoやrollbackの操作を加えた構造．
代わりに経路圧縮をしていないため，通常のUnionFindの操作は$O(logN)$となる．

通常のUnionFindeに加えて以下の操作が可能である．

### undo()

直前の`merge`操作を取り消す． $O(1)$

### snapshot()

現在の状態を保存する. $O(1)$

### get_state()

現在の`merge`操作が行われた回数を返す. $O(1)$

### rollback(state: int=-1)

`state=-1`のとき，snapshot()で保存した状態に戻す.
`state!=-1`のとき，`merge`が`state`回操作されたときの状態に戻す．

