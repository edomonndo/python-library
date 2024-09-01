---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
    title: GRL5E Range Query on a Tree II
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from data_structure.fenwick_tree.fenwick_tree import FenwickTree\nfrom typing\
    \ import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass RangeAddRangeSum:\n    def __init__(self,\
    \ arr: list[int], e: T = 0):\n        self.n = n = len(arr)\n        self.e =\
    \ e\n        self.bit1 = FenwickTree(n, e)\n        self.bit2 = FenwickTree(n,\
    \ e)\n\n    def add(self, l: int, r: int, x: T) -> None:\n        assert 0 <=\
    \ l <= r <= self.n\n        self.bit1.add(l, -x * l)\n        self.bit2.add(l,\
    \ x)\n        if r != self.n:\n            self.bit1.add(r, x * r)\n         \
    \   self.bit2.add(r, -x)\n\n    def sum(self, l: int, r: int) -> T:\n        assert\
    \ 0 <= l <= r <= self.n\n        rsum = self.bit2.sum0(r) * r + self.bit1.sum0(r)\n\
    \        lsum = self.bit2.sum0(l) * l + self.bit1.sum0(l)\n        return rsum\
    \ - lsum\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  isVerificationFile: false
  path: data_structure/fenwick_tree/range_add_range_sum.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/aoj/grl/grl_5_e_range_query_on_a_tree2_hld.test.py
documentation_of: data_structure/fenwick_tree/range_add_range_sum.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
---

BIT２本による区間加算・区間和取得