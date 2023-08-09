---
title: 遅延セグメント木 (Lazy Segment Tree)
documentation_of: ./lazy_segment_tree.py
---

区間更新・区間クエリを高速で計算することが出来る.

### 初期化

```
G = LazySegtree([0 for i in range(N)], func, ide_ele, mapping, composition, identity)
```
ここで,最初のリストは初期値である.ここは全部 $0$ である必要はない.必要に応じて変えてもいい. 例えば, `A` だったり, `list(range(N))` だったりを入れる. また,`func`, `ide_ele` は演算と単位元である.この演算はモノイドであることが要求される. （注：モノイドとは,結合法則が成り立って,単位元が存在するような演算のことである.）`mapping`は，$F$
の元である$f$と$G$の元である$x$に対して，$mapping(f,x)=f(x)$を返す関数である（ここで，$x$は区間であることに注意）. `composition`は，$F$の元である$f$,$g$を取ってきたときに，$composiiton(f,g)=f○g$という関数である． `idneitty`は$F$における単位元である.

以下は遅延セグ木に載せることのできる演算の例である.これはあくまで具体例なので他にもたくさんある. 


| 分類 | mapping | composition | ID | 補足 |
| ---- | ---- | ---- | ---- | ---- | 
| 区間加算・区間最小値取得 | `lambda f,x: f + x` | `lambda f,g: f + g` | $0$ |  | 
| 区間加算・区間最大値取得 | `lambda f,x: f + x` | `lambda f,g: f + g` | $0$ |  | 
| 区間加算・区間和取得 | `lambda f,x: (x[0]+f*x[1], x[1])` | `lambda f, g: f+g` | $0$ | 区間幅が必要なので値をタプルで持つ．`(value,size)` | 
| 区間変更・区間最小値取得 | `lambda f,x: x if f==ID else f` | `lambda f,g: g if f==ID else f` | $INF$ |  | 
| 区間変更・区間最大値取得 | `lambda f,x: x if f==ID else f` | `lambda f, g: g if f==ID else f` | $INF$ |  | 
| 区間変更・区間和取得 | `lambda f,x: x if f==ID else (f*x[1], x[1])` | `lambda f, g: g if f==ID else f` | $INF$ | 区間幅が必要なので値をタプルで持つ．`(value,size)` |


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

### apply_point

```
G.apply_point(p, f)
```

1点更新. p番目の要素$A_p$を$f(A_p)$に変更する.

### apply

```
G.apply_point(l, r, f)
```

区間更新. 区間$[l,r)$の要素$A_l, ..., A_{r-1}$を$f(A_l), ..., f(A_{r-1})$に変更する.
