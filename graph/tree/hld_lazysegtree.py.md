---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  - icon: ':heavy_check_mark:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/past/past4m_hld2.test.py
    title: "M - \u7B46\u5857\u308A"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph2.test.py
    title: Global Minimum Cut of Dynamic Star Augmented Graph
  - icon: ':x:'
    path: "test/yukicoder/235_\u3081\u3050\u308B\u306F\u3081\u3050\u308B(5).test.py"
    title: "No.235 \u3081\u3050\u308B\u306F\u3081\u3050\u308B (5)"
  - icon: ':heavy_check_mark:'
    path: "test/yukicoder/399_\u52D5\u7684\u306A\u9818\u4E3B.test.py"
    title: "No.399 \u52D5\u7684\u306A\u9818\u4E3B"
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar, Union\n\nT = TypeVar(\"T\")\nF = TypeVar(\"\
    F\")\n\nfrom data_structure.segtree.lazy_segment_tree import LazySegtree\nfrom\
    \ graph.tree.heavy_light_decomposition import HeavyLightDecomposition\n\n\nclass\
    \ HldLazySegTree:\n    def __init__(\n        self,\n        op: Callable[[T,\
    \ T], T],\n        e: T,\n        mapping: Callable[[F, T], T],\n        composition:\
    \ Callable[[F, F], F],\n        id_: F,\n        v: list[int],\n        n: int,\n\
    \        edges: list[Union[tuple[int, int] | tuple[int, int, int]]],\n       \
    \ root: int = 0,\n        directed: bool = False,\n    ):\n        # assert n\
    \ == len(v)\n        self.hld = HeavyLightDecomposition(n, edges, root, directed)\n\
    \        nv = self.hld.build_list(v)\n        self.seg = LazySegtree(nv, op, e,\
    \ mapping, composition, id_)\n        self.op = op\n        self.e = e\n     \
    \   self.mapping = mapping\n        self.compositon = composition\n        self.id\
    \ = id_\n\n    def all_prod(self) -> T:\n        return self.seg.all_prod()\n\n\
    \    def path_prod(self, u: int, v: int, edge: bool = False) -> T:\n        hld,\
    \ seg = self.hld, self.seg\n        res = self.e\n\n        def _f(l: int, r:\
    \ int) -> None:\n            nonlocal res\n            res = self.op(res, seg.prod(l,\
    \ r))\n\n        hld.path_query(u, v, _f, edge)\n        return res\n\n    def\
    \ path_apply(self, u: int, v: int, f: F, edge: bool = False) -> None:\n      \
    \  hld, seg = self.hld, self.seg\n        hld.path_query(u, v, lambda l, r: seg.apply(l,\
    \ r, f), edge)\n\n    def subtree_prod(self, v: int) -> T:\n        return self.seg.prod(self.hld.into[v],\
    \ self.hld.out[v])\n\n    def subtree_apply(self, v: int, f: F) -> None:\n   \
    \     self.seg.apply(self.hld.into[v], self.hld.out[v], f)\n\n    def get(self,\
    \ k: int) -> T:\n        return self.seg.get(self.hld.into[k])\n\n    def set(self,\
    \ k: int, v: T) -> None:\n        k = self.hld.into[k]\n        self.seg.set(k,\
    \ v)\n"
  dependsOn:
  - data_structure/segtree/lazy_segment_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: false
  path: graph/tree/hld_lazysegtree.py
  requiredBy: []
  timestamp: '2024-09-01 09:56:46+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/atcoder/past/past4m_hld2.test.py
  - "test/yukicoder/235_\u3081\u3050\u308B\u306F\u3081\u3050\u308B(5).test.py"
  - "test/yukicoder/399_\u52D5\u7684\u306A\u9818\u4E3B.test.py"
  - test/library_checker/graph/global_minimum_cut_of_dynamic_star_augmented_graph2.test.py
documentation_of: graph/tree/hld_lazysegtree.py
layout: document
title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u9045\u5EF6\u30BB\u30B0\u6728"
---

