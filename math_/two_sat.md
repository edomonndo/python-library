---
title: 2 Sat
documentation_of: ./two_sat.py
---

2-SATを解きます。 変数 $x_0, x_1, ..., x_{N-1}$に関して、
$$(x_i = f)∨(x_j = g)$$
というクローズを足し、これをすべて満たす変数の割当があるかを解きます。

### `two_sat(n: int, clause: List[Tuple[int, bool, int, bool]])`

- Args
    - $n$: 変数の数
    - $clause$: M個の節。各節を$(x_i, f, x_j, g)$で表す。なお$f$、$g$は`bool`。

- Return
    - 充足可能な場合: 割り当て可能な各変数の真偽値
    - 充足不可の場合: `None`
