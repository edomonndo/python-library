---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_get_range_contour_add_on_tree.test.py
    title: Vertex Get Range Contour Add on Tree
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from data_structure.fenwick_tree.fenwick_tree import FenwickTree\nfrom typing\
    \ import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass RangeAddPointGet:\n    def __init__(self,\
    \ n: int, e: T = 0):\n        self.n = n\n        self.e = e\n        self.bit\
    \ = FenwickTree(n, e)\n\n    def add(self, l: int, r: int, x: T) -> None:\n  \
    \      assert 0 <= l <= r <= self.n\n        if l == r:\n            return self.e\n\
    \        self.bit.add(l, x)\n        if r != self.n:\n            self.bit.add(r,\
    \ -x)\n\n    def get(self, k: int) -> T:\n        assert 0 <= k < self.n\n   \
    \     return self.bit.sum0(k + 1)\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  isVerificationFile: false
  path: data_structure/fenwick_tree/range_add_point_get.py
  requiredBy: []
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/tree/vertex_get_range_contour_add_on_tree.test.py
documentation_of: data_structure/fenwick_tree/range_add_point_get.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB1\u70B9\u53D6\u5F97"
---

