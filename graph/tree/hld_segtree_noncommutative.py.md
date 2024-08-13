---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  - icon: ':heavy_check_mark:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/tree/vertext_set_path_composite2.test.py
    title: Vertex Set Path Composite
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\nfrom data_structure.segtree.segment_tree\
    \ import Segtree\nfrom graph.tree.heavy_light_decomposition import HeavyLightDecomposition\n\
    \n\nclass HldSegTree:\n    def __init__(\n        self,\n        op: Callable[[T,\
    \ T], T],\n        e: T,\n        v: list[int],\n        n: int,\n        edges:\
    \ list[int, int],\n        root: int = 0,\n    ):\n        # assert n == len(v)\n\
    \        self.hld = HeavyLightDecomposition(n, edges, root)\n        v_hld = self.hld.build_list(v)\n\
    \        self.seg = Segtree(v_hld, op, e)\n        self.rseg = Segtree(v_hld[::-1],\
    \ op, e)\n        self.op = op\n        self.e = e\n\n    def prod(self, u: int,\
    \ v: int) -> T:\n        head, into, depth = self.hld.head, self.hld.into, self.hld.depth\n\
    \        seg, rseg, par, op, n = self.seg, self.rseg, self.hld.par, self.op, self.hld.n\n\
    \n        l, r = self.e, self.e\n        while head[u] != head[v]:\n         \
    \   if depth[head[u]] > depth[head[v]]:\n                l = op(l, rseg.prod(n\
    \ - into[u] - 1, n - into[head[u]]))\n                u = par[head[u]]\n     \
    \       else:\n                r = op(seg.prod(into[head[v]], into[v] + 1), r)\n\
    \                v = par[head[v]]\n        if depth[u] > depth[v]:\n         \
    \   l = op(l, rseg.prod(n - into[u] - 1, n - into[v]))\n        else:\n      \
    \      l = op(l, seg.prod(into[u], into[v] + 1))\n        return op(l, r)\n\n\
    \    def get(self, k: int) -> T:\n        return self.seg.get(self.hld.into[k])\n\
    \n    def set(self, k: int, v: T) -> None:\n        k = self.hld.into[k]\n   \
    \     self.seg.set(k, v)\n        self.rseg.set(self.hld.n - k - 1, v)\n"
  dependsOn:
  - data_structure/segtree/segment_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: false
  path: graph/tree/hld_segtree_noncommutative.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/tree/vertext_set_path_composite2.test.py
documentation_of: graph/tree/hld_segtree_noncommutative.py
layout: document
title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u30BB\u30B0\u6728\uFF08\u975E\u53EF\u63DB\
  \u30D1\u30B9\u30AF\u30A8\u30EA\uFF09"
---

