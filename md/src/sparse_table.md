---
title: Sparse table
documentation_of: //data_structure/sparse_table.py
---

静的な数列の区間に対するクエリを前処理$O(NlogN)$, クエリ$O(1)$で求めます．
Sparse tableに乗せられる演算は半群が条件です．（min, max, xor, gcd, lcmなど） 

### ST = SparseTable(arr, op)

数列$arr$からSparse tableを構築します．$op$は演算です．

### ST.query(l, r)

区間$[l, r)$の演算結果を返します．