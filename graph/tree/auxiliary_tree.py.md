---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc300-399/abc340g.test.py
    title: G - Leaf Color
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.segtree import SegTree\n\n\nclass AuxiliaryTree:\n    def __init__(self,\
    \ adj: list[list[int]], root=0):\n        self.n = len(adj)\n        self.ET,\
    \ self.into, self.out, self.depth = self._euler_tour(adj, root)\n\n        def\
    \ op(u, v):\n            return u if self.depth[u] <= self.depth[v] else v\n\n\
    \        self.depth_min = SegTree(op, self.n, self.ET)\n\n    @staticmethod\n\
    \    def _euler_tour(adj: list[list[int]], root: int = 0):\n        n = len(adj)\n\
    \        ET = []\n        into = [0] * n\n        out = [0] * n\n        depth\
    \ = [n] * (n + 1)\n\n        # Euler Tour\n        stack = [(root, -1)]\n    \
    \    while stack:\n            v, p = stack.pop()\n            if v >= 0:\n  \
    \              into[v] = len(ET)\n                ET.append(v)\n             \
    \   depth[v] = 0 if p == -1 else depth[p] + 1\n                out[v] = len(ET)\n\
    \                for u in adj[v]:\n                    if u == p:\n          \
    \              continue\n                    stack.append((~v, u))\n         \
    \           stack.append((u, v))\n            else:\n                v = ~v\n\
    \                ET.append(v)\n                out[v] = len(ET)\n        return\
    \ ET, into, out, depth\n\n    def _lca(self, u, v):\n        \"\"\"u\u3068v\u306E\
    \u6700\u8FD1\u5171\u901A\u7956\u5148\"\"\"\n        if self.into[u] > self.into[v]:\n\
    \            u, v = v, u\n        return self.depth_min.prod(self.into[u], self.out[v])\n\
    \n    def build(self, vs: list[int]) -> dict[list[int]]:\n        \"\"\"\u9802\
    \u70B9\u96C6\u5408vs\u3068\u305D\u308C\u3089\u306ELCA\u3092\u542B\u3080\u6728\u3092\
    \u69CB\u7BC9\u3059\u308B.\"\"\"\n        vs.sort(key=self.into.__getitem__)\n\
    \        k = len(vs)\n        for i in range(k - 1):\n            x = self._lca(vs[i],\
    \ vs[i + 1])\n            vs.append(x)\n        vs.sort(key=self.into.__getitem__)\n\
    \        root = vs[0]\n        stack = []\n        p = -1\n        res = dict()\n\
    \        for v in vs:\n            if v == p:\n                continue\n    \
    \        while stack and self.out[stack[-1]] < self.into[v]:\n               \
    \ stack.pop()\n            if stack:\n                res[stack[-1]].append(v)\n\
    \            res[v] = []\n            stack.append(v)\n            p = v\n   \
    \     return root, res\n"
  dependsOn:
  - atcoder/segtree.py
  isVerificationFile: false
  path: graph/tree/auxiliary_tree.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc300-399/abc340g.test.py
documentation_of: graph/tree/auxiliary_tree.py
layout: document
title: Auxiliary tree
---

木から、頂点集合$vs$とそれらのLCAからなる木を構築する
.
木の頂点数が圧縮され、$vs$の頂点数を$k$としたとき頂点数の上限は$2k-1$となる.

実装はEulerTour + Segment TreeでLCAを求めている.(前処理: $O(N)$, 構築: $O(k(logk + logN))$)
