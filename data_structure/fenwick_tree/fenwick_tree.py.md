---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass FenwickTree:\n\
    \    def __init__(self, N: int, e: T = 0):\n        self.n = N\n        self.data\
    \ = [e for i in range(N)]\n\n    def add(self, p: int, x: T) -> None:\n      \
    \  assert 0 <= p < self.n, \"0<=p<n,p={0},n={1}\".format(p, self.n)\n        p\
    \ += 1\n        while p <= self.n:\n            self.data[p - 1] += x\n      \
    \      p += p & -p\n\n    def sum(self, l: int, r: int) -> T:\n        assert\
    \ 0 <= l and l <= r and r <= self.n, \"0<=l<=r<=n,l={0},r={1},n={2}\".format(\n\
    \            l, r, self.n\n        )\n        return self.sum0(r) - self.sum0(l)\n\
    \n    def sum0(self, r: int) -> T:\n        s = 0\n        while r > 0:\n    \
    \        s += self.data[r - 1]\n            r -= r & -r\n        return s\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/fenwick_tree/fenwick_tree.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/fenwick_tree/fenwick_tree.py
layout: document
title: "\u62BD\u8C61\u5316Fenwick Tree"
---

数列 $a_i (i=0,...,n-1)$ に対して以下のクエリを高速に行えます.

- $a_i$ を $x$ に更新する
- $k$ に対して, $a_0+...+a_{k-1}$ を求める

### 初期化

```
FT = fenwick_tree(N, e = 0)
```
$N$は配列のサイズです. モノイドをのせるときは,eにモノイドの単位元を指定します．

### 更新

```
FT.add(i, a)
```
$i$番目の値を$a$に更新します

### 和を求める1

```
print(FT.sum0(r))
```
$a_0+...+a_{r-1}$ の総和,つまり $sum(a[:r))$ を求めます.

### 和を求める2

```
print(FT.sum(l, r))
```
$a_l+...+a_{r-1}$ の総和,つまり $sum(a[l:r))$ を求めます.
