---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: data_structure/fenwick_tree/range_add_range_sum.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
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
  code: "from typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass CumulativeSum:\n\
    \    def __init__(self, arr: list[int], e: T = 0):\n        self.n = n = len(arr)\n\
    \        self.e = e\n        self.dat = [e for _ in range(n + 1)]\n        for\
    \ i in range(n):\n            self.dat[i + 1] = self.dat[i] + arr[i]\n\n    def\
    \ prod(self, l: int, r: int) -> T:\n        assert 0 <= l <= r <= self.n\n   \
    \     return self.dat[r] - self.dat[l]\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/fenwick_tree/cumulative_sum.py
  requiredBy:
  - data_structure/fenwick_tree/range_add_range_sum.py
  timestamp: '2024-06-10 12:42:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/fenwick_tree/cumulative_sum.py
layout: document
title: "\u7D2F\u7A4D\u548C"
---
