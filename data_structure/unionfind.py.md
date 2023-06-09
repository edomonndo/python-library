---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: library_checker/data_structure/unionfind.test.py
    title: library_checker/data_structure/unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, N):\n        self.n = N\n      \
    \  self.parent_or_size = [-1 for i in range(N)]\n\n    def merge(self, a, b):\n\
    \        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n  \
    \      assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n    \
    \    x = self.leader(a)\n        y = self.leader(b)\n        if x == y:\n    \
    \        return x\n        if -self.parent_or_size[x] < -self.parent_or_size[y]:\n\
    \            x, y = y, x\n        self.parent_or_size[x] += self.parent_or_size[y]\n\
    \        self.parent_or_size[y] = x\n        return x\n\n    def same(self, a,\
    \ b):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n\
    \        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n  \
    \      return self.leader(a) == self.leader(b)\n\n    def leader(self, a):\n \
    \       assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n   \
    \     if self.parent_or_size[a] < 0:\n            return a\n        self.parent_or_size[a]\
    \ = self.leader(self.parent_or_size[a])\n        return self.parent_or_size[a]\n\
    \n    def size(self, a):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        return -self.parent_or_size[self.leader(a)]\n\n  \
    \  def groups(self):\n        leader_buf = [0 for i in range(self.n)]\n      \
    \  group_size = [0 for i in range(self.n)]\n        for i in range(self.n):\n\
    \            leader_buf[i] = self.leader(i)\n            group_size[leader_buf[i]]\
    \ += 1\n        result = [[] for i in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n        result2 = []\n        for\
    \ i in range(self.n):\n            if len(result[i]) > 0:\n                result2.append(result[i])\n\
    \        return result2\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/unionfind.py
  requiredBy: []
  timestamp: '2023-06-09 12:42:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - library_checker/data_structure/unionfind.test.py
documentation_of: data_structure/unionfind.py
layout: document
title: Union Find
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