---
title: 抽象化Fenwick Tree
documentation_of: //data_structure/fenwick_tree/fenwick_tree.py
---

数列 $a_i (i=0,...,n-1)$ に対して以下のクエリを高速に行えます.

- $a_i$ を $x$ に更新する
- $k$ に対して, $a_0+...+a_{k-1}$ を求める

### 初期化

```
FT = fenwick_tree(N, e = 0)
```
$N$は配列のサイズです. モノイドをのせるときは,eにモノイドの単位元を指定します．

### 更新

```
FT.add(i, a)
```
$i$番目の値を$a$に更新します

### 和を求める1

```
print(FT.sum0(r))
```
$a_0+...+a_{r-1}$ の総和,つまり $sum(a[:r))$ を求めます.

### 和を求める2

```
print(FT.sum(l, r))
```
$a_l+...+a_{r-1}$ の総和,つまり $sum(a[l:r))$ を求めます.
