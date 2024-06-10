---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/fenwick_tree/cumulative_sum.py
    title: "\u7D2F\u7A4D\u548C"
  - icon: ':warning:'
    path: data_structure/fenwick_tree/fenwick_tree.py
    title: "\u62BD\u8C61\u5316Fenwick Tree"
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
  code: "from data_structure.fenwick_tree.fenwick_tree import FenwickTree\nfrom data_structure.fenwick_tree.cumulative_sum\
    \ import CumulativeSum\nfrom typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\n\
    class RangeAddRangeSum:\n    def __init__(self, arr: list[int], e: T = 0):\n \
    \       self.n = n = len(arr)\n        self.e = e\n        self.bit1 = FenwickTree(n,\
    \ e)\n        self.bit2 = FenwickTree(n, e)\n        self.cs = CumulativeSum(arr)\n\
    \n    def add(self, l: int, r: int, x: T) -> None:\n        assert 0 <= l <= r\
    \ <= self.n\n        self.bit1.add(l, x)\n        self.bit2.add(l, -x * self.cs.prod(0,\
    \ l))\n        if r != self.n:\n            self.bit1.add(r, -x)\n           \
    \ self.bit2.add(r, x * self.cs.prod(0, r))\n\n    def _prod(self, k: int) -> T:\n\
    \        return self.bit1.sum0(k) * self.cs.prod(0, k) + self.bit2.sum0(k)\n\n\
    \    def sum(self, l: int, r: int) -> T:\n        assert 0 <= l <= r <= self.n\n\
    \        return self._prod(r) - self._prod(l)\n\n    def set(self, k: int, x:\
    \ T) -> None:\n        self.add(k, k + 1, x - self.sum(k, k + 1))\n"
  dependsOn:
  - data_structure/fenwick_tree/fenwick_tree.py
  - data_structure/fenwick_tree/cumulative_sum.py
  isVerificationFile: false
  path: data_structure/fenwick_tree/range_add_range_sum.py
  requiredBy: []
  timestamp: '2024-06-10 12:42:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/fenwick_tree/range_add_range_sum.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
---

BIT２本による区間加算・区間和取得