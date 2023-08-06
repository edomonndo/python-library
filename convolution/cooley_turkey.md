---
title: 畳み込み カラツバ法
documentation_of: ./cooley_turkey.py
--- 

内容は理解できていない.

多項式 $a_0 + a_1x + a_2x^2 + a_{n-1}x^{n-1}$ を配列 $[a_0, a_1, ..., a_{n-1}]$　で表す.

このとき,$A = [a_0, a_1, ..., a_{n-1}]$ と $B = [b_0, b_1, ..., b_{m-1}]$ から $C = [c_0, c_1, ..., c_{(n-1)+(m-1)}]$ を求める.
ただし,

$$C_k = \displaystyle\sum^{}_{i+j=k} a_i b_j\mod 1,000,000,007$$

###　使い方

```
C = CooleyTukey().karatsuba(A, B, 10**9 + 7)
```