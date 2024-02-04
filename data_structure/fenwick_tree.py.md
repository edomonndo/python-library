---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_2_b_range_sum_query.test.py
    title: test/aoj/dsl_2_b_range_sum_query.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/point_add_range_sum.test.py
    title: test/library_checker/data_structure/point_add_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_range_sum.test.py
    title: test/library_checker/data_structure/static_range_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class FenwickTree:\n    n = 1\n    data = [0 for i in range(n)]\n\n    def\
    \ __init__(self, N):\n        self.n = N\n        self.data = [0 for i in range(N)]\n\
    \n    def add(self, p, x):\n        assert 0 <= p < self.n, \"0<=p<n,p={0},n={1}\"\
    .format(p, self.n)\n        p += 1\n        while p <= self.n:\n            self.data[p\
    \ - 1] += x\n            p += p & -p\n\n    def sum(self, l, r):\n        assert\
    \ 0 <= l and l <= r and r <= self.n, \"0<=l<=r<=n,l={0},r={1},n={2}\".format(\n\
    \            l, r, self.n\n        )\n        return self.sum0(r) - self.sum0(l)\n\
    \n    def sum0(self, r):\n        s = 0\n        while r > 0:\n            s +=\
    \ self.data[r - 1]\n            r -= r & -r\n        return s\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/fenwick_tree.py
  requiredBy: []
  timestamp: '2023-06-09 12:11:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/point_add_range_sum.test.py
  - test/library_checker/data_structure/static_range_sum.test.py
  - test/aoj/dsl_2_b_range_sum_query.test.py
documentation_of: data_structure/fenwick_tree.py
layout: document
title: Fenwick Tree
---

数列 $a_i (i=0,...,n-1)$ に対して以下のクエリを高速に行えます.

- $a_i$ を $x$ に更新する
- $k$ に対して, $a_0+...+a_{k-1}$ を求める

### 初期化

```
FT = fenwick_tree(N)
```
$N$は配列のサイズです. 初期化した時,最初の配列のサイズは全て$0$になっています. 【注意】もしバグったら,まずは初期値を間違えてないか確認しましょう.

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
