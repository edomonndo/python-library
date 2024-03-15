---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/jump_on_tree.test.py
    title: test/library_checker/tree/jump_on_tree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/lowest_common_ancestor.test.py
    title: test/library_checker/tree/lowest_common_ancestor.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\nclass LcaDoubling:\n    def __init__(self,\
    \ N: int, G: list[list[int]], root: int = 0):\n        self.parent = [-1] * N\n\
    \        self.depth = [0] * N\n        que = deque([root])\n        while que:\n\
    \            v = que.popleft()\n            for u in G[v]:\n                if\
    \ self.parent[v] != u:\n                    self.parent[u] = v\n             \
    \       que.append(u)\n                    self.depth[u] = self.depth[v] + 1\n\
    \n        self.ancestor = [self.parent]  # self.ancestor[k][u]\u306Fu\u306E2**k\u5148\
    \u306E\u7956\u5148.\n\n        # \u30C0\u30D6\u30EA\u30F3\u30B0\n        k = 1\n\
    \        while (1 << k) < N:\n            anc_k = [0] * N\n            for u in\
    \ range(N):\n                if self.ancestor[-1][u] == -1:\n                \
    \    anc_k[u] = -1\n                else:\n                    anc_k[u] = self.ancestor[-1][self.ancestor[-1][u]]\n\
    \            self.ancestor.append(anc_k)\n            k += 1\n\n    def lca(self,\
    \ u: int, v: int) -> int:\n        # u\u3088\u308Av\u306E\u65B9\u304C\u6DF1\u3044\
    \u9802\u70B9\u3068\u3059\u308B\n        if self.depth[u] < self.depth[v]:\n  \
    \          u, v = v, u\n        for k, bit in enumerate(reversed(format(self.depth[u]\
    \ - self.depth[v], \"b\"))):\n            if bit == \"1\":\n                u\
    \ = self.ancestor[k][u]\n        if u == v:\n            return u\n        for\
    \ anc in reversed(self.ancestor):\n            if anc[u] != anc[v]:\n        \
    \        u = anc[u]\n                v = anc[v]\n        return self.ancestor[0][u]\n\
    \n    def dist(self, u: int, v: int) -> int:\n        c = self.lca(u, v)\n   \
    \     return self.depth[u] + self.depth[v] - 2 * self.depth[c]\n\n    def up(self,\
    \ v: int, k: int) -> int:\n        i = 0\n        while k:\n            if k &\
    \ 1:\n                v = self.ancestor[i][v]\n            k >>= 1\n         \
    \   i += 1\n        return v\n\n    def jump(self, u: int, v: int, i: int) ->\
    \ int:\n        c = self.lca(u, v)\n        dist = self.depth[u] + self.depth[v]\
    \ - 2 * self.depth[c]\n        if i > dist:\n            return -1\n\n       \
    \ if i <= self.depth[u] - self.depth[c]:\n            return self.up(u, i)\n\n\
    \        return self.up(v, dist - i)\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/lca.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/tree/lowest_common_ancestor.test.py
  - test/library_checker/tree/jump_on_tree.test.py
documentation_of: tree/lca.py
layout: document
title: "\u6700\u8FD1\u5171\u901A\u7956\u5148(Lowest Common Ancestor)"
---

木上の頂点$u,v$の共通祖先の中でも最も$u,v$に近い頂点を求める.

### `lca=LcaDoubling(N: int, G: List[List[int]], root: int = 0)`

頂点数$N$の隣接リスト$G$で根を$root$にして初期化する.実装はダブリング.

### `lca.lca(u: int, v: int)`

頂点$u,v$の最近共通祖先を求める.

### `lca.dist(u: int, v: int)`

頂点$u,v$の最短距離を求める.

### `lca.up(v: int, k: int)`

頂点$v$から$k$個親の頂点を求める.

### `lca.jump(u: int, v: int, i: int)`

頂点$u,v$の最短経路上の$i$番目の頂点を求める.始点・終点は$u,v$で,$i$が最短距離より大きい場合は`-1`を返す.