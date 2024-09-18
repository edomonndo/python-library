---
title: Foldable Queue(SWAG)
documentation_of: //data_structure/basic/FoldableQue.py
---

通常のQueueに加えて，列全体の総積を$O(1)$で求められる．

`.push(item)`, `.pop()`, `.front()`は通常のQueueと同様．
`.fold()`で総積を返す．総積に使用する関数と単位元は`op`,`e`で指定する．