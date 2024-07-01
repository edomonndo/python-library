---
title: 二項係数(mod)
documentation_of: ./combination_mod.py
---

### `combination_mod(n: int, r: int, m=10**9 + 7)`

$nCr\pmod m$を求める.

繰り返し計算が必要な場合は，Combクラスで前処理することでクエリに$O(1)$で答えられる．