---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
  - icon: ':x:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
    title: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.segtree import SegTree\nfrom graph.tree.heavy_light_decomposition\
    \ import HeavyLightDecomposition\nfrom typing import Callable, TypeVar\n\nT =\
    \ TypeVar(\"T\")\n\n\nclass HldSegTree:\n    def __init__(\n        self,\n  \
    \      op: Callable[[T, T], T],\n        e: T,\n        v: list[int],\n      \
    \  n: int,\n        edges: list[int, int],\n        root: int = 0,\n    ):\n \
    \       # assert n == len(v)\n        self.hld = HeavyLightDecomposition(n, edges,\
    \ root)\n        nv = self.hld.build_list(v)\n        self.seg = SegTree(op, e,\
    \ nv)\n        self.op = op\n        self.e = e\n\n    def path_prod(self, u:\
    \ int, v: int) -> T:\n        head, into, depth = self.hld.head, self.hld.into,\
    \ self.hld.depth\n        seg, par, op = self.seg, self.hld.par, self.op\n\n \
    \       res = self.e\n        while head[u] != head[v]:\n            if depth[head[u]]\
    \ < depth[head[v]]:\n                u, v = v, u\n            res = op(res, seg.prod(into[head[u]],\
    \ into[u] + 1))\n            u = par[head[u]]\n        if depth[u] < depth[v]:\n\
    \            u, v = v, u\n        return op(res, seg.prod(into[v], into[u] + 1))\n\
    \n    def subtree_prod(self, v: int) -> T:\n        return self.seg.prod(self.hld.into[v],\
    \ self.hld.out[v])\n\n    def get(self, k: int) -> T:\n        return self.seg.get(self.hld.into[k])\n\
    \n    def set(self, k: int, v: T) -> None:\n        k = self.hld.into[k]\n   \
    \     self.seg.set(k, v)\n"
  dependsOn:
  - atcoder/segtree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: false
  path: graph/tree/hld_segtree.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
documentation_of: graph/tree/hld_segtree.py
layout: document
title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u30BB\u30B0\u6728\uFF08\u53EF\u63DB\u30AF\
  \u30A8\u30EA\uFF09"
---

