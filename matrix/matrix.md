---
title: 行列
documentation_of: ./matrix.py
---

Matrixクラスは$\bmod{998,244,353}$で計算される。

### `Mat = Matrix(N, M, [Mat])`

$N$行$M$列の行列を作成する。引数に$Mat$を指定した場合は、その行列をコピーする。

### `四則演算`

$+$、$-$、$\times$　がサポートされている。

### `Mat.is_square()`

正方行列(`self.n == self.m`)であれば`True`。

### `Mat.times(k)`

行列の各要素を`k`倍する。

### `Mat.determinant()`

行列式を計算する。

### `Mat.inverse()`

逆行列を計算する。

### `Mat.linear_equations(b)`

行列$A$とベクトル$b$から、$Ax=b$となるベクトル$x$を求める。

### `determinant_arbitrary_mod(N, A, m=998244353)`

$N$行$N$列の正方行列$A$と非負整数$m$から行列式を$\mod m$で求める。