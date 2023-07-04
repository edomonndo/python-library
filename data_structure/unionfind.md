---
title: Union Find
documentation_of: ./unionfind.py
---

disjoint set union、つまりUnionFind木です。
主な使用例としては、最小全域木問題をクラスカル法で解くときなどに使います。Union by rankと経路圧縮により高速です。

### 初期化

```
G = dsu(N)
```
ここで$N$は頂点の数です。

### merge

```
G.merge(a, b)
```
頂点$a$がある連結成分と頂点$b$がある連結成分を合体します。

### same

```
G.same(a, b)
```
これは、「頂点$a$と頂点$b$が同じ連結成分」ならば`True`、そうでないならば`False`を返します。

### leader

```
G.leader(a)
```
$a$の連結成分の代表元を返します。

### size

```
G.size(a)
```
$a$の連結成分にある頂点数($a$を含む)を答えます。

### groups

```
G.groups()
```
グラフの連結成分の情報を答えます。