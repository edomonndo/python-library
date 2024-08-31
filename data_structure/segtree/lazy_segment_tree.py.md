---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: geometory/union_area_rectangle.py
    title: "\u9577\u65B9\u5F62\u306E\u548C\u96C6\u5408\u306E\u9762\u7A4D"
  - icon: ':question:'
    path: graph/tree/hld_lazysegtree.py
    title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u9045\u5EF6\u30BB\u30B0\u6728"
  - icon: ':warning:'
    path: graph/tree/permutation_tree.py
    title: "\u9806\u5217\u6728"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_f_range_update_min_query.test.py
    title: DSL2F RMQ and RUQ
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_g_range_add_sum_query.test.py
    title: DSL2G RSQ and RAQ
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_h_range_add_min_query.test.py
    title: DSL2H RMQ and RAQ
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_i_range_update_sum_query.test.py
    title: DSL2I RSQ and RUQ
  - icon: ':grey_question:'
    path: test/atcoder/abc001-99/abc035c.test.py
    title: "C - \u30AA\u30BB\u30ED"
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc300-399/abc341e.test.py
    title: E - Alternating String
  - icon: ':grey_question:'
    path: test/atcoder/abc300-399/abc357f.test.py
    title: F - Two Sequence Queries
  - icon: ':grey_question:'
    path: test/atcoder/other/able.test.py
    title: E - Replace Digits
  - icon: ':x:'
    path: test/atcoder/past/past4m_hld.test.py
    title: "M - \u7B46\u5857\u308A"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/range_affine_range_sum.test.py
    title: Range Affine Range Sum
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
    title: Global Minimum Cut of Dynamic Star Augmented Graph
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LazySegtree:\n    def __init__(self, V, OP, E, MAPPING, COMPOSITION,\
    \ ID):\n        self.n = len(V)\n        self.op = OP\n        self.e = E\n  \
    \      self.log = (self.n - 1).bit_length()\n        self.size = 1 << self.log\n\
    \        self.d = [E for i in range(2 * self.size)]\n        for i in range(self.n):\n\
    \            self.d[self.size + i] = V[i]\n        for i in range(self.size -\
    \ 1, 0, -1):\n            self._update(i)\n        # \u9045\u5EF6\u4F1D\u64AD\u7528\
    \n        self.lz = [ID for i in range(self.size)]\n        self.mapping = MAPPING\n\
    \        self.composition = COMPOSITION\n        self.identity = ID\n\n    def\
    \ set(self, p, x):\n        assert 0 <= p and p < self.n\n        p += self.size\n\
    \        # \u9045\u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n\
    \            self._push(p >> i)\n        self.d[p] = x\n        for i in range(1,\
    \ self.log + 1):\n            self._update(p >> i)\n\n    def get(self, p):\n\
    \        assert 0 <= p and p < self.n\n        p += self.size\n        # \u9045\
    \u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n            self._push(p\
    \ >> i)\n        return self.d[p]\n\n    def prod(self, l, r):\n        assert\
    \ 0 <= l and l <= r and r <= self.n\n        if l == r:\n            return self.e\n\
    \        l += self.size\n        r += self.size\n        # \u9045\u5EF6\u4F1D\u64AD\
    \n        for i in range(self.log, 0, -1):\n            if ((l >> i) << i) !=\
    \ l:\n                self._push(l >> i)\n            if ((r >> i) << i) != r:\n\
    \                self._push(r >> i)\n        sml, smr = self.e, self.e\n     \
    \   while l < r:\n            if l & 1:\n                sml = self.op(sml, self.d[l])\n\
    \                l += 1\n            if r & 1:\n                r -= 1\n     \
    \           smr = self.op(self.d[r], smr)\n            l >>= 1\n            r\
    \ >>= 1\n        return self.op(sml, smr)\n\n    def all_prod(self):\n       \
    \ return self.d[1]\n\n    def max_right(self, l, f):\n        assert 0 <= l and\
    \ l <= self.n\n        assert f(self.e)\n        if l == self.n:\n           \
    \ return self.n\n        l += self.size\n        # \u9045\u5EF6\u4F1D\u64AD\n\
    \        for i in range(self.log, 0, -1):\n            self._push(l >> i)\n  \
    \      sm = self.e\n        while 1:\n            while l % 2 == 0:\n        \
    \        l >>= 1\n            if not f(self.op(sm, self.d[l])):\n            \
    \    while l < self.size:\n                    # \u9045\u5EF6\u4F1D\u64AD\n  \
    \                  self._push(l)\n                    l = 2 * l\n            \
    \        if f(self.op(sm, self.d[l])):\n                        sm = self.op(sm,\
    \ self.d[l])\n                        l += 1\n                return l - self.size\n\
    \            sm = self.op(sm, self.d[l])\n            l += 1\n            if (l\
    \ & -l) == l:\n                break\n        return self.n\n\n    def min_left(self,\
    \ r, f):\n        assert 0 <= r and r <= self.n\n        assert f(self.e)\n  \
    \      if r == 0:\n            return 0\n        r += self.size\n        # \u9045\
    \u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n            self._push((r\
    \ - 1) >> i)\n        sm = self.e\n        while 1:\n            r -= 1\n    \
    \        while r > 1 and (r % 2):\n                r >>= 1\n            if not\
    \ f(self.op(self.d[r], sm)):\n                while r < self.size:\n         \
    \           # \u9045\u5EF6\u4F1D\u64AD\n                    self._push(r)\n  \
    \                  r = 2 * r + 1\n                    if f(self.op(self.d[r],\
    \ sm)):\n                        sm = self.op(self.d[r], sm)\n               \
    \         r -= 1\n                return r + 1 - self.size\n            sm = self.op(self.d[r],\
    \ sm)\n            if (r & -r) == r:\n                break\n        return 0\n\
    \n    def apply_point(self, p, f):\n        assert 0 <= p and p < self.n\n   \
    \     p += self.size\n        for i in range(self.log, 0, -1):\n            self._push(p\
    \ >> i)\n        self.d[p] = self.mapping(f, self.d[p])\n        for i in range(1,\
    \ self.log + 1):\n            self._update(p >> i)\n\n    def apply(self, l, r,\
    \ f):\n        assert 0 <= l and l <= r and r <= self.n\n        if l == r:\n\
    \            return\n        l += self.size\n        r += self.size\n        for\
    \ i in range(self.log, 0, -1):\n            if ((l >> i) << i) != l:\n       \
    \         self._push(l >> i)\n            if ((r >> i) << i) != r:\n         \
    \       self._push((r - 1) >> i)\n        l2, r2 = l, r\n        while l < r:\n\
    \            if l & 1:\n                self._all_apply(l, f)\n              \
    \  l += 1\n            if r & 1:\n                r -= 1\n                self._all_apply(r,\
    \ f)\n            l >>= 1\n            r >>= 1\n        l, r = l2, r2\n      \
    \  for i in range(1, self.log + 1):\n            if ((l >> i) << i) != l:\n  \
    \              self._update(l >> i)\n            if ((r >> i) << i) != r:\n  \
    \              self._update((r - 1) >> i)\n\n    def _update(self, k):\n     \
    \   self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])\n\n    def _all_apply(self,\
    \ k, f):\n        self.d[k] = self.mapping(f, self.d[k])\n        if k < self.size:\n\
    \            self.lz[k] = self.composition(f, self.lz[k])\n\n    def _push(self,\
    \ k):\n        self._all_apply(2 * k, self.lz[k])\n        self._all_apply(2 *\
    \ k + 1, self.lz[k])\n        self.lz[k] = self.identity\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/lazy_segment_tree.py
  requiredBy:
  - graph/tree/hld_lazysegtree.py
  - graph/tree/permutation_tree.py
  - geometory/union_area_rectangle.py
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/atcoder/other/able.test.py
  - test/atcoder/abc001-99/abc035c.test.py
  - test/atcoder/abc300-399/abc341e.test.py
  - test/atcoder/abc300-399/abc357f.test.py
  - test/atcoder/past/past4m_hld.test.py
  - test/aoj/dsl/dsl_2_g_range_add_sum_query.test.py
  - test/aoj/dsl/dsl_2_i_range_update_sum_query.test.py
  - test/aoj/dsl/dsl_2_h_range_add_min_query.test.py
  - test/aoj/dsl/dsl_2_f_range_update_min_query.test.py
  - test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph.test.py
  - test/library_checker/data_structure/range_affine_range_sum.test.py
documentation_of: data_structure/segtree/lazy_segment_tree.py
layout: document
title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
---

区間更新・区間クエリを高速で計算することが出来る.

### 初期化

#### 区間加算・区間最小値取得
```
inf=float("inf")
mapping = lambda f,x: f + x
composition = lambda f,g: f + g
ID = 0
G = LazySegtree(A, min, inf, mapping, composition, ID)
```

#### 区間加算・区間最大値取得
```
inf=float("inf")
mapping = lambda f,x: f + x
composition = lambda f,g: f + g
ID = 0
G = LazySegtree(A, max, -inf, mapping, composition, ID)
```
#### 区間加算・区間和取得

区間幅が必要なので値をタプルで持つ．`(value,size)`

```
mapping = lambda f,x: (x[0]+f*x[1], x[1])
composition = lambda f,g: f + g
ID = 0
G = LazySegtree(A, lambda x,y:x+y, 0, mapping, composition, ID)
```

#### 区間変更・区間最小値取得
```
inf=float("inf")
mapping = lambda f,x: x if f==ID else f
composition = lambda f,g: g if f==ID else f
ID = inf
G = LazySegtree(A, min, inf, mapping, composition, ID)
```

#### 区間変更・区間最大値取得

```
inf=float("inf")
mapping = lambda f,x: x if f==ID else f
composition = lambda f,g: g if f==ID else f
ID = inf
G = LazySegtree(A, max, -inf, mapping, composition, ID)
```

#### 区間変更・区間和取得

区間幅が必要なので値をタプルで持つ．`(value,size)`

```
inf=float("inf")
mapping = lambda f,x: x if f==ID else (f*x[1], x[1])
composition = lambda f,g: g if f==ID else f
ID = inf
G = LazySegtree(A, lambda x,y:x+y, 0, mapping, composition, ID)
```

ここで,最初のリストは初期値である.ここは全部 $0$ である必要はない.必要に応じて変えてもいい. 例えば, `A` だったり, `list(range(N))` だったりを入れる. また,`func`, `ide_ele` は演算と単位元である.この演算はモノイドであることが要求される. （注：モノイドとは,結合法則が成り立って,単位元が存在するような演算のことである.）`mapping`は，$F$
の元である$f$と$G$の元である$x$に対して，$mapping(f,x)=f(x)$を返す関数である（ここで，$x$は区間であることに注意）. `composition`は，$F$の元である$f$,$g$を取ってきたときに，$composiiton(f,g)=f○g$という関数である． `ID`は$F$における単位元である.




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
G.apply(l, r, f)
```

区間更新. 区間$[l,r)$の要素$A_l, ..., A_{r-1}$を$f(A_l), ..., f(A_{r-1})$に変更する.
