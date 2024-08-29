---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_b_tree_height.test.py
    title: "GRL5B \u6728\u306E\u9AD8\u3055"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\nV = TypeVar(\"\
    V\")\n\nMOD = 998244353\n\n\nclass TreeDp:\n    def __init__(self, n: int, adj:\
    \ list[list[int]], r: int = 0):\n        par = [-1] * n\n        children = [[]\
    \ for _ in range(n)]\n        order = []\n        st = [r]\n        while st:\n\
    \            u = st.pop()\n            order.append(u)\n            for v in adj[u]:\n\
    \                if par[u] != v:\n                    par[v] = u\n           \
    \         children[u].append(v)\n                    st.append(v)\n        self.n\
    \ = n\n        self.par = par\n        self.children = children\n        self.order\
    \ = order\n\n    def calc(self, MAX: int = 200001) -> tuple[list[int], list[int],\
    \ list[int]]:\n        fa = [1] * (MAX + 1)\n        fainv = [1] * (MAX + 1)\n\
    \        inv = [1] * (MAX + 1)\n        for i in range(MAX):\n            fa[i\
    \ + 1] = fa[i] * (i + 1) % MOD\n        fainv[-1] = pow(fa[-1], MOD - 2, MOD)\n\
    \        for i in range(MAX)[::-1]:\n            fainv[i] = fainv[i + 1] * (i\
    \ + 1) % MOD\n        for i in range(1, MAX)[::-1]:\n            inv[i] = fainv[i]\
    \ * fa[i - 1]\n        return fa, fainv, inv\n\n    def size(self) -> list[int]:\n\
    \        order, par = self.order, self.par\n        res = [1] * self.n\n     \
    \   for v in order[1:][::-1]:\n            res[par[v]] += res[v]\n        return\
    \ res\n\n    def dp(self, e: T, merge: Callable[[T, T], T]) -> list[T]:\n    \
    \    order, par = self.order, self.par\n        res = [e] * self.n\n        for\
    \ v in order[1:][::-1]:\n            p = par[v]\n            res[p] = merge(res[p],\
    \ res[v])\n        return res\n\n    def rerooting(\n        self,\n        e:\
    \ T,\n        merge: Callable[[T, T], T],\n        op_bu: Callable[[T, V, V],\
    \ T],\n        op_td: Callable[[T, V, V], T],\n        op_fin: Callable[[T, V],\
    \ T],\n    ):\n        order, par, children = self.order, self.par, self.children\n\
    \n        cum_bu = [e] * self.n\n        cum_td = [e] * self.n\n        res =\
    \ [0] * self.n\n\n        for u in order[1:][::-1]:\n            p = par[u]\n\
    \            res[u] = op_bu(cum_bu[u], u, p)\n            cum_bu[p] = merge(cum_bu[p],\
    \ res[u])\n        r = order[0]\n        res[r] = op_fin(cum_bu[r], r)\n\n   \
    \     for u in order:\n            cum = cum_td[u]\n            for v in children[u]:\n\
    \                cum_td[v] = cum\n                cum = merge(cum, res[v])\n \
    \           cum = e\n            for v in children[u][::-1]:\n               \
    \ cum_td[v] = op_td(merge(cum_td[v], cum), v, u)\n                cum = merge(cum,\
    \ res[v])\n                res[v] = op_fin(merge(cum_bu[v], cum_td[v]), v)\n \
    \       return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/tree_dp.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_b_tree_height.test.py
documentation_of: graph/tree/tree_dp.py
layout: document
title: "(\u5168\u65B9\u4F4D)\u6728DP"
---

木上でのDP. 葉から根に向かって遷移させる．
全方位木DPは，ある頂点を根としたDPの結果から部分木をうまく計算して，各頂点を根としたときの値を求めることができる．$O(N)$

### `TDP=TreeDP(n, adj, r=0)`

頂点数$n$の隣接リストで初期化する．デフォルトでは，頂点$0$を根とする．

### `TDP.calc(MAX)`

組み合わせ計算の前処理.

### `TDP.size()`

部分木のサイズを求める．根は初期化時に指定する.

### `TDP.dp(e, op)`

木上でDPを計算する．引数の$e$は遷移の単位元，$op$は遷移の関数.

### `TDP.rerooting(e, merge, adj_bu, adj_td, adj_fin)`

全方位木DPを計算する．各引数の詳細は下記リンクを参照.  
https://qiita.com/Kiri8128/items/a011c90d25911bdb3ed3

### 木DP

- https://atcoder.jp/contests/abc036/tasks/abc036_d

### 全方位木DP

- https://atcoder.jp/contests/dp/tasks/dp_v
- https://atcoder.jp/contests/abc160/tasks/abc160_f
- https://atcoder.jp/contests/abc220/tasks/abc220_f
- https://atcoder.jp/contests/abc223/tasks/abc223_g