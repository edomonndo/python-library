---
title: セグメント木 (Segment Tree)
documentation_of: ./segment_tree.py
---

一点更新・区間クエリを高速で計算することが出来る.

### 初期化

```
G = Segtree([0 for i in range(N)], func, ide_ele)
```
ここで,最初のリストは初期値である.ここは全部 $0$ である必要はない.必要に応じて変えてもいい. 例えば, `A` だったり, `list(range(N))` だったりを入れる. また,`func`, `ide_ele` は演算と単位元である.この演算はモノイドであることが要求される. （注：モノイドとは,結合法則が成り立って,単位元が存在するような演算のことである.）

以下はセグ木に載せることのできる演算の例である.これはあくまで具体例なので他にもたくさんある.


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

### 実装上の注意

前節で例に挙げた各演算について,セグ木に載せる際には例えば以下のように書く.

```
#add
G=Segtree(LIST,(lambda x,y:x+y),0)

#addの書き方その2
def add(x,y):
    return x+y
G=Segtree(LIST,add,0)


#times
G=Segtree(LIST,(lambda x,y:x*y),1)

#min
G=Segtree(LIST,min,INF)

#max
G=Segtree(LIST,max,-INF)

#gcd
from math import gcd
G=Segtree(LIST,gcd,0)

#lcm
from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)
G=Segtree(LIST,lcm,1)

# xor
G=Segtree(LIST,(lambda x,y:x^y),0)

# or
G=Segtree(LIST,(lambda x,y:x|y),0)

# and
N=30
G=Segtree(LIST,(lambda x,y:x&y),(1<<N)-1)
```
関数はラムダ式で定義しても,defで定義してもどちらでも問題ない.

### set

```
G.set(p,x)
```
$p$番目の値を$x$に変えることができる.

### get

```
G.get(p)
```
$p$番目の値が返ってくるという関数である.

### prod

```
G.prod(l,r)
```
$[l,r)$の範囲内での演算を求めた結果が返ってくる. 例えばセグ木関数が$max$だった場合 $max(A_l,...,A_{r-1})$ が返ってくる. セグ木関数が足し算だった場合 $A_l+...+A_{r-1}$ が返ってくる.

関数の返り値は,このようなコードを実行したときの答えと同じである.

```
def prod(l,r):
    ans=ide_ele
    for i in range(l,r):
        ans=segfunc(ans,A[i])
    return ans
```
セグ木で書いた場合この区間クエリを高速に計算することができる.

### all_prod

```
G.all_prod()
```
これは`G.prod(0, N)`と等価である.つまり,全区間での演算結果を求める.

### max_right

```
G.max_right(l, f)
```
二分探索をする.ここで,始点は$l$であり,単調性のある関数$f$の実行結果が変わる切れ目を求める.

### min_left

```
G.min_left(r, f)
```
二分探索をする.ここで,終点は$r$であり,単調性のある関数$f$の実行結果が変わる切れ目を求める.