---
title: Foldable Deque(DSWAG)
documentation_of: //data_structure/basic/FoldableDeque.py
---

通常のDeeueに加えて，列全体の総積を$O(1)$で求められる．

`.push(item)`, `.pushleft(item)`, `.pop()`, `.popleft()`は通常のDequeと同様．
`.fold()`で総積を返す．総積に使用する関数と単位元は`op`,`e`で指定する．