---
title: Union Find
documentation_of: ./unionfind.py
---

disjoint set union,つまりUnionFind木です. 主な使用例としては,最小全域木問題をクラスカル法で解くときなどに使います.

### 初期化

```
G=dsu(N)
```
ここで,Nは頂点の数です.

### merge

```
G.merge(a,b)
```
頂点aがある連結成分と頂点bがある連結成分を合体します.

### same

```
G.same(a,b)
```
これは,「頂点aと頂点bが同じ連結成分」ならばTrue,そうでないならばFalseを返します.

### leader

```
G.leader(a)
```
aの連結成分の代表元を返します.

### size

```
G.size(a)
```
aの連結成分にある頂点数(aを含む)を答えます.

### groups

```
G.groups()
```
グラフの連結成分の情報を答えます.