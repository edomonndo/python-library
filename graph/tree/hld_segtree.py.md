---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  - icon: ':question:'
    path: graph/tree/heavy_light_decomposition.py
    title: "HL\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
    title: GRL5D Range Query on a Tree
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_path_sum_hld2.test.py
    title: Vertex Add Path Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_subtree_sum_hld2.test.py
    title: Vertex Add Subtree Sum (HLD)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
    \        self.hld = HeavyLightDecomposition(n, edges, root)\n        nv = self.hld.build_list(v)\n\
    \        self.seg = Segtree(nv, op, e)\n        self.op = op\n        self.e =\
    \ e\n\n    def path_prod(self, u: int, v: int) -> T:\n        head, into, depth\
    \ = self.hld.head, self.hld.into, self.hld.depth\n        seg, par, op = self.seg,\
    \ self.hld.par, self.op\n\n        res = self.e\n        while head[u] != head[v]:\n\
    \            if depth[head[u]] < depth[head[v]]:\n                u, v = v, u\n\
    \            res = op(res, seg.prod(into[head[u]], into[u] + 1))\n           \
    \ u = par[head[u]]\n        if depth[u] < depth[v]:\n            u, v = v, u\n\
    \        return op(res, seg.prod(into[v], into[u] + 1))\n\n    def subtree_prod(self,\
    \ v: int) -> T:\n        return self.seg.prod(self.hld.into[v], self.hld.out[v])\n\
    \n    def get(self, k: int) -> T:\n        return self.seg.get(self.hld.into[k])\n\
    \n    def set(self, k: int, v: T) -> None:\n        k = self.hld.into[k]\n   \
    \     self.seg.set(k, v)\n"
  dependsOn:
  - data_structure/segtree/segment_tree.py
  - graph/tree/heavy_light_decomposition.py
  isVerificationFile: false
  path: graph/tree/hld_segtree.py
  requiredBy: []
  timestamp: '2024-09-01 16:55:25+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_d_range_query_on_a_tree_hld2.test.py
  - test/library_checker/tree/vertex_add_subtree_sum_hld2.test.py
  - test/library_checker/tree/vertex_add_path_sum_hld2.test.py
documentation_of: graph/tree/hld_segtree.py
layout: document
title: "HL\u5206\u89E3\u6728\u4E0A\u306E\u30BB\u30B0\u6728\uFF08\u53EF\u63DB\u30AF\
  \u30A8\u30EA\uFF09"
---

