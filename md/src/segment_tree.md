---
title: セグメント木 (Segment Tree)
documentation_of: //data_structure/segtree/segment_tree.py
---

一点更新・区間クエリを高速で計算することが出来る.

| セグ木関数 | 単位元 | 補足 |
| ---- | ---- | ---- | 
| add | $0$ | 足し算 | 
| times | $1$ | 掛け算 | 
| min | $INF$ | 最小値 | 
| max | $-INF$ | 最大値 | 
| gcd | $0$ | 最大公約数 | 
| lcm | $1$ | 最小公倍数 | 
| xor | $0$ | 排他的論理和 | 
| or | $0$ | bitwise or | 
| and | $2^N-1$ | bitwise and（Nは制約に応じて十分大きな値を取る） | 
| convolution | $[1]$ | 多項式の積（畳み込みを参照） | 
(a,b)*(c,d)->(ac,bc+d) | $(1,0)$ | 1次関数の合成,(a,b)はx->ax+bに対応 | 
| matrix | 単位行列 | 行列の積 | 
