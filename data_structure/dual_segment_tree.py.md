---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_2_d_range_update_query.test.py
    title: test/aoj/dsl_2_d_range_update_query.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl_2_e_range_add_query.test.py
    title: test/aoj/dsl_2_e_range_add_query.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/range_affine_point_get.test.py
    title: test/library_checker/data_structure/range_affine_point_get.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DualSegtree:\n    def __init__(self, V, OP, E, MAPPING, COMPOSITION,\
    \ ID):\n        self.n = len(V)\n        self.op = OP\n        self.e = E\n  \
    \      self.log = (self.n - 1).bit_length()\n        self.size = 1 << self.log\n\
    \        # \u533A\u9593[0,self.size)\u3092\u9045\u5EF6\u4F1D\u64AD\u7528\uFF0C\
    \u533A\u9593[self.size, self.size + n)\u304C\u5B9F\u30C7\u30FC\u30BF\n       \
    \ self.d = [ID for i in range(self.size)] + [E for i in range(self.size)]\n  \
    \      for i in range(self.n):\n            self.d[self.size + i] = V[i]\n   \
    \     # \u9045\u5EF6\u4F1D\u64AD\u7528\n        self.mapping = MAPPING\n     \
    \   self.composition = COMPOSITION\n        self.identity = ID\n\n    def set(self,\
    \ p, x):\n        assert 0 <= p and p < self.n\n        p += self.size\n     \
    \   # \u9045\u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n   \
    \         self._push(p >> i)\n        self.d[p] = x\n\n    def get(self, p):\n\
    \        assert 0 <= p and p < self.n\n        p += self.size\n        # \u9045\
    \u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n            self._push(p\
    \ >> i)\n        return self.d[p]\n\n    def apply_point(self, p, f):\n      \
    \  assert 0 <= p and p < self.n\n        p += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self._push(p >> i)\n        self.d[p] = self.mapping(f,\
    \ self.d[p])\n\n    def apply(self, l, r, f):\n        assert 0 <= l and l <=\
    \ r and r <= self.n\n        if l == r:\n            return\n        l += self.size\n\
    \        r += self.size\n        for i in range(self.log, 0, -1):\n          \
    \  if ((l >> i) << i) != l:\n                self._push(l >> i)\n            if\
    \ ((r >> i) << i) != r:\n                self._push((r - 1) >> i)\n        l2,\
    \ r2 = l, r\n        while l < r:\n            if l & 1:\n                self._all_apply(l,\
    \ f)\n                l += 1\n            if r & 1:\n                r -= 1\n\
    \                self._all_apply(r, f)\n            l >>= 1\n            r >>=\
    \ 1\n        l, r = l2, r2\n\n    def _update(self, k):\n        self.d[k] = self.op(self.d[2\
    \ * k], self.d[2 * k + 1])\n\n    def _all_apply(self, k, f):\n        if k <\
    \ self.size:\n            self.d[k] = self.composition(f, self.d[k])\n       \
    \ else:\n            self.d[k] = self.mapping(f, self.d[k])\n\n    def _push(self,\
    \ k):\n        self._all_apply(2 * k, self.d[k])\n        self._all_apply(2 *\
    \ k + 1, self.d[k])\n        self.d[k] = self.identity\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/dual_segment_tree.py
  requiredBy: []
  timestamp: '2023-08-10 00:04:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/range_affine_point_get.test.py
  - test/aoj/dsl_2_d_range_update_query.test.py
  - test/aoj/dsl_2_e_range_add_query.test.py
documentation_of: data_structure/dual_segment_tree.py
layout: document
title: "\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dual Segment Tree)"
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
