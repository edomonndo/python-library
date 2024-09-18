---
title: 双対セグメント木 (Dual Segment Tree)
documentation_of: //data_structure/segtree/dual_segment_tree.py
---

区間更新・1点取得を高速で計算することが出来る. 遅延セグ木から機能を落とし，定数倍を高速化している．

### 初期化

```
G = LazySegtree([0 for i in range(N)], func, ide_ele, mapping, composition, identity)
```
ここで,最初のリストは初期値である.ここは全部 $0$ である必要はない.必要に応じて変えてもいい. 例えば, `A` だったり, `list(range(N))` だったりを入れる. また,`func`, `ide_ele` は演算と単位元である.この演算はモノイドであることが要求される. （注：モノイドとは,結合法則が成り立って,単位元が存在するような演算のことである.）`mapping`は，$F$
の元である$f$と$G$の元である$x$に対して，$mapping(f,x)=f(x)$を返す関数である（ここで，$x$は区間であることに注意）. `composition`は，$F$の元である$f$,$g$を取ってきたときに，$composiiton(f,g)=f○g$という関数である． `idneitty`は$F$における単位元である.

双対セグ木に載せることのできる演算や使用例については，[遅延セグ木](./lazy_segment_tree.py)を参考にすること.

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
