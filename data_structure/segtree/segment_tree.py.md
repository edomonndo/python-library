---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: data_structure/segtree/compressed_segtree.py
    title: "\u5EA7\u6A19\u5727\u7E2E\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/range_set_range_composite.py
    title: "\u533A\u9593\u66F4\u65B0\u30FB\u533A\u9593\u30A2\u30D5\u30A3\u30F3"
  - icon: ':warning:'
    path: dynamic_programming/longest_increase_subsequence.py
    title: "\u6700\u9577\u5897\u52A0\u6587\u5B57\u5217(LIS)"
  - icon: ':heavy_check_mark:'
    path: graph/tree/auxiliary_tree.py
    title: Auxiliary tree
  - icon: ':heavy_check_mark:'
    path: graph/tree/euler_tour.py
    title: Euler tour
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_a_range_min_query.test.py
    title: DSL2A Range Minimum Query(RMQ)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/point_set_range_composite.test.py
    title: Point Set Range Composite
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_rmq_segtree.test.py
    title: Static RMQ (Segment Tree)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertext_set_path_composite.test.py
    title: Vertex Set Path Composite
  - icon: ':heavy_check_mark:'
    path: test/yukicoder/875_range_mindex_query.test.py
    title: No.875 Range Mindex Query
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Segtree:\n    def __init__(self, V, OP, E):\n        self.n = len(V)\n\
    \        self.op = OP\n        self.e = E\n        self.log = (self.n - 1).bit_length()\n\
    \        self.size = 1 << self.log\n        self.d = [E for i in range(2 * self.size)]\n\
    \        for i in range(self.n):\n            self.d[self.size + i] = V[i]\n \
    \       for i in range(self.size - 1, 0, -1):\n            self.update(i)\n\n\
    \    def set(self, p, x):\n        assert 0 <= p and p < self.n\n        p +=\
    \ self.size\n        self.d[p] = x\n        for i in range(1, self.log + 1):\n\
    \            self.update(p >> i)\n\n    def get(self, p):\n        assert 0 <=\
    \ p and p < self.n\n        return self.d[p + self.size]\n\n    def prod(self,\
    \ l, r):\n        assert 0 <= l and l <= r and r <= self.n\n        l += self.size\n\
    \        r += self.size\n        sml, smr = self.e, self.e\n        while l <\
    \ r:\n            if l & 1:\n                sml = self.op(sml, self.d[l])\n \
    \               l += 1\n            if r & 1:\n                smr = self.op(self.d[r\
    \ - 1], smr)\n                r -= 1\n            l >>= 1\n            r >>= 1\n\
    \        return self.op(sml, smr)\n\n    def all_prod(self):\n        return self.d[1]\n\
    \n    def max_right(self, l, f):\n        assert 0 <= l and l <= self.n\n    \
    \    assert f(self.e)\n        if l == self.n:\n            return self.n\n  \
    \      l += self.size\n        sm = self.e\n        while 1:\n            while\
    \ l % 2 == 0:\n                l >>= 1\n            if not f(self.op(sm, self.d[l])):\n\
    \                while l < self.size:\n                    l = 2 * l\n       \
    \             if f(self.op(sm, self.d[l])):\n                        sm = self.op(sm,\
    \ self.d[l])\n                        l += 1\n                return l - self.size\n\
    \            sm = self.op(sm, self.d[l])\n            l += 1\n            if (l\
    \ & -l) == l:\n                break\n        return self.n\n\n    def min_left(self,\
    \ r, f):\n        assert 0 <= r and r <= self.n\n        assert f(self.e)\n  \
    \      if r == 0:\n            return 0\n        r += self.size\n        sm =\
    \ self.e\n        while 1:\n            r -= 1\n            while r > 1 and (r\
    \ % 2):\n                r >>= 1\n            if not f(self.op(self.d[r], sm)):\n\
    \                while r < self.size:\n                    r = 2 * r + 1\n   \
    \                 if f(self.op(self.d[r], sm)):\n                        sm =\
    \ self.op(self.d[r], sm)\n                        r -= 1\n                return\
    \ r + 1 - self.size\n            sm = self.op(self.d[r], sm)\n            if (r\
    \ & -r) == r:\n                break\n        return 0\n\n    def update(self,\
    \ k):\n        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])\n\n    def\
    \ __str__(self):\n        return str([self.get(i) for i in range(self.n)])\n\n\
    \nclass RangeMinQuery:\n    def __init__(self, V):\n        self.n = len(V)\n\
    \        self.log = (self.n - 1).bit_length()\n        self.size = 1 << self.log\n\
    \        _INF = float(\"inf\")\n        self.e = _INF\n        self.d = [_INF\
    \ for i in range(2 * self.size)]\n        for i in range(self.n):\n          \
    \  self.d[self.size + i] = V[i]\n        for i in range(self.size - 1, 0, -1):\n\
    \            self._update(i)\n\n    def update(self, p, x):\n        assert 0\
    \ <= p and p < self.n\n        p += self.size\n        self.d[p] = x\n       \
    \ for i in range(1, self.log + 1):\n            self._update(p >> i)\n\n    def\
    \ get(self, p):\n        assert 0 <= p and p < self.n\n        return self.d[p\
    \ + self.size]\n\n    def query(self, l, r):\n        assert 0 <= l and l <= r\
    \ and r <= self.n\n        l += self.size\n        r += self.size\n        sml,\
    \ smr = self.e, self.e\n        while l < r:\n            if l & 1:\n        \
    \        sml = min(sml, self.d[l])\n                l += 1\n            if r &\
    \ 1:\n                smr = min(self.d[r - 1], smr)\n                r -= 1\n\
    \            l >>= 1\n            r >>= 1\n        return min(sml, smr)\n\n  \
    \  def fold(self):\n        return self.d[1]\n\n    def _update(self, k):\n  \
    \      self.d[k] = min(self.d[2 * k], self.d[2 * k + 1])\n\n    def __str__(self):\n\
    \        return str([self.get(i) for i in range(self.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/segment_tree.py
  requiredBy:
  - graph/tree/euler_tour.py
  - graph/tree/auxiliary_tree.py
  - dynamic_programming/longest_increase_subsequence.py
  - data_structure/segtree/compressed_segtree.py
  - data_structure/segtree/range_set_range_composite.py
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/yukicoder/875_range_mindex_query.test.py
  - test/aoj/dsl/dsl_2_a_range_min_query.test.py
  - test/library_checker/tree/vertext_set_path_composite.test.py
  - test/library_checker/data_structure/point_set_range_composite.test.py
  - test/library_checker/data_structure/static_rmq_segtree.test.py
documentation_of: data_structure/segtree/segment_tree.py
layout: document
title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
---

一点更新・区間クエリを高速で計算することが出来る.

### 初期化

```
G = Segtree([0 for i in range(N)], func, ide_ele)
```
ここで,最初のリストは初期値である.ここは全部 $0$ である必要はない.必要に応じて変えてもいい. 例えば, `A` だったり, `list(range(N))` だったりを入れる. また,`func`, `ide_ele` は演算と単位元である.この演算はモノイドであることが要求される. （注：モノイドとは,結合法則が成り立って,単位元が存在するような演算のことである.）

以下はセグ木に載せることのできる演算の例である.これはあくまで具体例なので他にもたくさんある.


| セグ木関数 | 単位元 | 補足 |
| ---- | ---- | ---- | 
| add | $0$ | 足し算 | 
| times | $1$ | 掛け算 | 
| min | $INF$ | 最小値 | 
| max | $-INF$ | 最大値 | 
| gcd | $0$ | 最大公約数 | 
| lcm | $1$ | 最小公倍数 | 
| xor | $0$ | 排他的論理和 | 
| or | $0$ | bitwise or | 
| and | $2^N-1$ | bitwise and（Nは制約に応じて十分大きな値を取る） | 
| convolution | $[1]$ | 多項式の積（畳み込みを参照） | 
(a,b)*(c,d)->(ac,bc+d) | $(1,0)$ | 1次関数の合成,(a,b)はx->ax+bに対応 | 
| matrix | 単位行列 | 行列の積 | 

### 実装上の注意

前節で例に挙げた各演算について,セグ木に載せる際には例えば以下のように書く.

```
#add
G=Segtree(LIST,(lambda x,y:x+y),0)

#addの書き方その2
def add(x,y):
    return x+y
G=Segtree(LIST,add,0)


#times
G=Segtree(LIST,(lambda x,y:x*y),1)

#min
G=Segtree(LIST,min,INF)

#max
G=Segtree(LIST,max,-INF)

#gcd
from math import gcd
G=Segtree(LIST,gcd,0)

#lcm
from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)
G=Segtree(LIST,lcm,1)

# xor
G=Segtree(LIST,(lambda x,y:x^y),0)

# or
G=Segtree(LIST,(lambda x,y:x|y),0)

# and
N=30
G=Segtree(LIST,(lambda x,y:x&y),(1<<N)-1)
```
関数はラムダ式で定義しても,defで定義してもどちらでも問題ない.

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