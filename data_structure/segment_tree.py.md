---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: library_checker/data_structure/static_rmq.test.py
    title: library_checker/data_structure/static_rmq.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Segtree:\n    n = 1\n    size = 1\n    log = 2\n    d = [0]\n    op\
    \ = None\n    e = 10**15\n\n    def __init__(self, V, OP, E):\n        self.n\
    \ = len(V)\n        self.op = OP\n        self.e = E\n        self.log = (self.n\
    \ - 1).bit_length()\n        self.size = 1 << self.log\n        self.d = [E for\
    \ i in range(2 * self.size)]\n        for i in range(self.n):\n            self.d[self.size\
    \ + i] = V[i]\n        for i in range(self.size - 1, 0, -1):\n            self.update(i)\n\
    \n    def set(self, p, x):\n        assert 0 <= p and p < self.n\n        p +=\
    \ self.size\n        self.d[p] = x\n        for i in range(1, self.log + 1):\n\
    \            self.update(p >> i)\n\n    def get(self, p):\n        assert 0 <=\
    \ p and p < self.n\n        return self.d[p + self.size]\n\n    def prod(self,\
    \ l, r):\n        assert 0 <= l and l <= r and r <= self.n\n        sml = self.e\n\
    \        smr = self.e\n        l += self.size\n        r += self.size\n      \
    \  while l < r:\n            if l & 1:\n                sml = self.op(sml, self.d[l])\n\
    \                l += 1\n            if r & 1:\n                smr = self.op(self.d[r\
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
    \ __str__(self):\n        return str([self.get(i) for i in range(self.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segment_tree.py
  requiredBy: []
  timestamp: '2023-07-05 10:35:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - library_checker/data_structure/static_rmq.test.py
documentation_of: data_structure/segment_tree.py
layout: document
title: Segment Tree
---

一点更新・区間クエリを高速で計算することが出来る。

### 初期化

```
G = Segtree([0 for i in range(N)], func, ide_ele)
```
ここで、最初のリストは初期値である。ここは全部 $0$ である必要はない。必要に応じて変えてもいい。 例えば、 `A` だったり、 `list(range(N))` だったりを入れる。 また、`func`, `ide_ele` は演算と単位元である。この演算はモノイドであることが要求される。 （注：モノイドとは、結合法則が成り立って、単位元が存在するような演算のことである。）

以下はセグ木に載せることのできる演算の例である。これはあくまで具体例なので他にもたくさんある。

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
(a,b)*(c,d)->(ac,ad+b) | $(1,0)$ | 1次関数の合成,(a,b)はx->ax+bに対応 | 
| matrix | 単位行列 | 行列の積 | 

注：INFは、実装する際には適当な大きな数（ex:10の15乗）などを定める。ここで、INFの値の大きさが足りないと誤答の原因になるかもしれない。pythonだとmathにinfというものが実装されているが、バージョンが古いpythonでは使うことができない。

注2：足し算や掛け算は、掛け算＆modという組み合わせでも出てくるかもしれない。 modの世界で足し算や掛け算をしてもモノイドの性質は失われない。

注3：gcdを使う際に`from math import gcd`を使っているが、これもpythonのバージョンが古い場合エラーの原因となる。もしエラーが出た場合は
`from fractions import gcd`で試してみるともしかしたらうまくいくかもしれない。

注4：1次関数の合成や、行列の積については、$\bmod 998244353$ (or $\bmod 10^9+7$)上での演算として定める場合が多いと思われる。行列は$k\times k$の積を計算するときに$O(k^3)$の計算量がかかるため、もし出るとしても$k=2,3$あたりだろう。

### 実装上の注意

前節で例に挙げた各演算について、セグ木に載せる際には例えば以下のように書く。

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
関数はラムダ式で定義しても、defで定義してもどちらでも問題ない。

### set

```
G.set(p,x)
```
$p$番目の値を$x$に変えることができる。

### get

```
G.get(p)
```
$p$番目の値が返ってくるという関数である。

### prod

```
G.prod(l,r)
```
$[l,r)$の範囲内での演算を求めた結果が返ってくる。 例えばセグ木関数が$max$だった場合 $max(A_l,...,A_{r-1})$ が返ってくる。 セグ木関数が足し算だった場合 $A_l+...+A_{r-1}$ が返ってくる。

関数の返り値は、このようなコードを実行したときの答えと同じである。

```
def prod(l,r):
    ans=ide_ele
    for i in range(l,r):
        ans=segfunc(ans,A[i])
    return ans
```
セグ木で書いた場合この区間クエリを高速に計算することができる。

### all_prod

```
G.all_prod()
```
これは`G.prod(0, N)`と等価である。つまり、全区間での演算結果を求める。

### max_right

```
G.max_right(l, f)
```
二分探索をする。ここで、始点は$l$であり、単調性のある関数$f$の実行結果が変わる切れ目を求める。

### min_left

```
G.min_left(r, f)
```
二分探索をする。ここで、終点は$r$であり、単調性のある関数$f$の実行結果が変わる切れ目を求める。