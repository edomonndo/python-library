---
title: 遅延セグメント木 (Lazy Segment Tree)
documentation_of: //data_structure/segtree/lazy_segment_tree.py
---

#### 区間加算・区間最小値取得
```
inf=float("inf")
mapping = lambda f,x: f + x
composition = lambda f,g: f + g
ID = 0
seg = LazySegtree(A, min, inf, mapping, composition, ID)
```

#### 区間加算・区間最大値取得
```
inf=float("inf")
mapping = lambda f,x: f + x
composition = lambda f,g: f + g
ID = 0
seg = LazySegtree(A, max, -inf, mapping, composition, ID)
```
#### 区間加算・区間和取得

区間幅が必要なので値をタプルで持つ．`(value,size)`

```
op = lambda x,y: (x[0]+y[0], x[1]+y[1])
mapping = lambda f,x: (x[0]+f*x[1], x[1])
composition = lambda f,g: f + g
ID = 0
seg = LazySegtree(A, op, (0,1), mapping, composition, ID)
```

#### 区間変更・区間最小値取得
```
inf=float("inf")
mapping = lambda f,x: x if f==ID else f
composition = lambda f,g: g if f==ID else f
ID = inf
seg = LazySegtree(A, min, inf, mapping, composition, ID)
```

#### 区間変更・区間最大値取得

```
inf=float("inf")
mapping = lambda f,x: x if f==ID else f
composition = lambda f,g: g if f==ID else f
ID = inf
seg = LazySegtree(A, max, -inf, mapping, composition, ID)
```

#### 区間変更・区間和取得

区間幅が必要なので値をタプルで持つ．`(value,size)`

```
inf=float("inf")
op = lambda x,y: (x[0]+y[0], x[1]+y[1])
mapping = lambda f,x: x if f==ID else (f*x[1], x[1])
composition = lambda f,g: g if f==ID else f
ID = inf
G = LazySegtree(A, op, (0,1), mapping, composition, ID)
```