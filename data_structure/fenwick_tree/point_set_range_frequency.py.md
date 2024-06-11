---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/fenwicktree.py
    title: atcoder/fenwicktree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/point_set_range_frequency.test.py
    title: Point Set Range Frequency
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.fenwicktree import FenwickTree\nfrom bisect import bisect_left\n\
    \n\nclass PointSetRangeFrequency:\n\n    def __init__(self, arr: list[int]):\n\
    \        self.n = len(arr)\n        self.dat = arr\n        self.qs = qs = []\n\
    \        for i, a in enumerate(arr):\n            qs.append((0, 1, a * self.n\
    \ + i))\n\n    def add_set_query(self, p: int, x: int):\n        assert 0 <= p\
    \ < self.n\n        self.qs.append((0, -1, self.dat[p] * self.n + p))\n      \
    \  self.dat[p] = x\n        self.qs.append((0, 1, x * self.n + p))\n\n    def\
    \ add_freq_query(self, l: int, r: int, x: int):\n        assert 0 <= l <= r <=\
    \ self.n\n        self.qs.append((1, x * self.n + l, x * self.n + r))\n\n    def\
    \ solve(self) -> list[int]:\n        qs = self.qs\n        vs = sorted(set([b\
    \ for t, _, b in qs if t == 0]))\n        bit = FenwickTree(len(vs) + 1)\n   \
    \     res = []\n        for t, a, b in qs:\n            if t == 0:\n         \
    \       z = bisect_left(vs, b)\n                bit.add(z, a)\n            else:\n\
    \                l = bisect_left(vs, a)\n                r = bisect_left(vs, b)\n\
    \                res.append(bit.sum(l, r))\n        return res\n"
  dependsOn:
  - atcoder/fenwicktree.py
  isVerificationFile: false
  path: data_structure/fenwick_tree/point_set_range_frequency.py
  requiredBy: []
  timestamp: '2024-06-11 11:00:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/point_set_range_frequency.test.py
documentation_of: data_structure/fenwick_tree/point_set_range_frequency.py
layout: document
redirect_from:
- /library/data_structure/fenwick_tree/point_set_range_frequency.py
- /library/data_structure/fenwick_tree/point_set_range_frequency.py.html
title: data_structure/fenwick_tree/point_set_range_frequency.py
---
