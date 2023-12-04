---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_1_a_union_find.test.py
    title: test/aoj/dsl_1_a_union_find.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
    title: test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/unionfind.test.py
    title: test/library_checker/data_structure/unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n):\n        self.n = n\n      \
    \  self.parent_or_size = [-1] * n\n        self.group = n\n\n    def merge(self,\
    \ a, b):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n\
    \        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n  \
    \      x = self.leader(a)\n        y = self.leader(b)\n        if x == y:\n  \
    \          return x\n        self.group -= 1\n        if -self.parent_or_size[x]\
    \ < -self.parent_or_size[y]:\n            x, y = y, x\n        self.parent_or_size[x]\
    \ += self.parent_or_size[y]\n        self.parent_or_size[y] = x\n        return\
    \ x\n\n    def same(self, a, b):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b,\
    \ self.n)\n        return self.leader(a) == self.leader(b)\n\n    def leader(self,\
    \ a):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n\
    \        if self.parent_or_size[a] < 0:\n            return a\n        self.parent_or_size[a]\
    \ = self.leader(self.parent_or_size[a])\n        return self.parent_or_size[a]\n\
    \n    def size(self, a):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        return -self.parent_or_size[self.leader(a)]\n\n  \
    \  def group_count(self):\n        return self.group\n\n    def groups(self):\n\
    \        leader_buf = [0 for i in range(self.n)]\n        group_size = [0 for\
    \ i in range(self.n)]\n        for i in range(self.n):\n            leader_buf[i]\
    \ = self.leader(i)\n            group_size[leader_buf[i]] += 1\n        result\
    \ = [[] for i in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n        result2 = []\n        for i in range(self.n):\n\
    \            if len(result[i]) > 0:\n                result2.append(result[i])\n\
    \        return result2\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/unionfind.py
  requiredBy: []
  timestamp: '2023-08-26 10:33:44+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/unionfind.test.py
  - test/aoj/dsl_1_a_union_find.test.py
  - test/aoj/grl_2_a_minimum_spanning_tree_kruskal.test.py
documentation_of: data_structure/unionfind.py
layout: document
title: Union Find
---

disjoint set union,つまりUnionFind木です.
主な使用例としては,最小全域木問題をクラスカル法で解くときなどに使います.Union by rankと経路圧縮により高速です.

### 初期化

```
G = UnionFind(N)
```
ここで$N$は頂点の数です.

### merge

```
G.merge(a, b)
```
頂点$a$がある連結成分と頂点$b$がある連結成分を合体します.

### same

```
G.same(a, b)
```
これは,「頂点$a$と頂点$b$が同じ連結成分」ならば`True`,そうでないならば`False`を返します.

### leader

```
G.leader(a)
```
$a$の連結成分の代表元を返します.

### size

```
G.size(a)
```
$a$の連結成分にある頂点数($a$を含む)を答えます.

### groups

```
G.groups()
```
グラフの連結成分の情報を答えます.