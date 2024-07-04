---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/lazysegtree.py
    title: atcoder/lazysegtree.py
  - icon: ':x:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
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
  code: "from atcoder.lazysegtree import LazySegTree\nfrom graph.tree.heavy_light_decomposition\
    \ import HeavyLightDecomposition\nfrom typing import Callable, TypeVar\n\nT =\
    \ TypeVar(\"T\")\nF = TypeVar(\"F\")\n\n\nclass HldLazySegTree:\n    def __init__(\n\
    \        self,\n        op: Callable[[T, T], T],\n        e: T,\n        mapping:\
    \ Callable[[F, T], T],\n        composition: Callable[[F, F], F],\n        id_:\
    \ F,\n        v: list[int],\n        n: int,\n        edges: list[int, int],\n\
    \        root: int = 0,\n    ):\n        # assert n == len(v)\n        self.hld\
    \ = HeavyLightDecomposition(n, edges, root)\n        nv = self.hld.build_list(v)\n\
    \        self.seg = LazySegTree(op, e, mapping, composition, id_, nv)\n      \
    \  self.rseg = LazySegTree(op, e, mapping, composition, id_, nv[::-1])\n     \
    \   self.op = op\n        self.e = e\n        self.mapping = mapping\n       \
    \ self.compositon = composition\n        self.id = id_\n\n    def path_prod(self,\
    \ u: int, v: int) -> T:\n        head, into, depth, n = self.hld.head, self.hld.into,\
    \ self.hld.depth, self.hld.n\n        seg, rseg, par, op = self.seg, self.rseg,\
    \ self.hld.par, self.op\n\n        l, r = self.e, self.e\n        while head[u]\
    \ != head[v]:\n            if depth[head[u]] > depth[head[v]]:\n             \
    \   l = op(l, rseg.prod(n - into[u] - 1, n - into[head[u]]))\n               \
    \ u = par[head[u]]\n            else:\n                r = op(seg.prod(into[head[v]],\
    \ into[v] + 1), r)\n                v = par[head[v]]\n        if depth[u] > depth[v]:\n\
    \            l = op(l, rseg.prod(n - into[u] - 1, n - into[v]))\n        else:\n\
    \            l = op(l, seg.prod(into[u], into[v] + 1))\n        return op(l, r)\n\
    \n    def path_apply(self, u: int, v: int, f: F) -> None:\n        head, into,\
    \ depth = self.hld.head, self.hld.into, self.hld.depth\n        seg, par = self.seg,\
    \ self.hld.par\n\n        while head[u] != head[v]:\n            if depth[head[u]]\
    \ < depth[head[v]]:\n                u, v = v, u\n            seg.apply(into[head[u]],\
    \ into[u] + 1, f)\n            u = par[head[u]]\n        if depth[u] < depth[v]:\n\
    \            u, v = v, u\n        seg.apply(into[v], into[u] + 1, f)\n\n    def\
    \ subtree_prod(self, v: int) -> T:\n        return self.seg.prod(self.hld.into[v],\
    \ self.hld.out[v])\n\n    def subtree_apply(self, v: int, f: F) -> None:\n   \
    \     self.seg.apply(self.hld.into[v], self.hld.out[v], f)\n\n    def get(self,\
    \ k: int) -> T:\n        return self.seg.get(self.hld.into[k])\n\n    def set(self,\
    \ k: int, v: T) -> None:\n        k = self.hld.into[k]\n        self.seg.set(k,\
    \ v)\n        self.rseg[self.hld.n - k - 1] = v\n"
  dependsOn:
  - atcoder/lazysegtree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: false
  path: graph/tree/hld_lazysegtree.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/tree/hld_lazysegtree.py
layout: document
title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u9045\u5EF6\u30BB\u30B0\u6728"
---

