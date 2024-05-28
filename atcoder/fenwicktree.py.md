---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: geometory/offline_point_add_rectangle_sum.py
    title: geometory/offline_point_add_rectangle_sum.py
  - icon: ':heavy_check_mark:'
    path: geometory/offline_static_rectangle_sum.py
    title: geometory/offline_static_rectangle_sum.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://en.wikipedia.org/wiki/Fenwick_tree'''
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import typing\n\n\nclass FenwickTree:\n    '''Reference: https://en.wikipedia.org/wiki/Fenwick_tree'''\n\
    \n    def __init__(self, n: int = 0) -> None:\n        self._n = n\n        self.data\
    \ = [0] * n\n\n    def add(self, p: int, x: typing.Any) -> None:\n        assert\
    \ 0 <= p < self._n\n\n        p += 1\n        while p <= self._n:\n          \
    \  self.data[p - 1] += x\n            p += p & -p\n\n    def sum(self, left: int,\
    \ right: int) -> typing.Any:\n        assert 0 <= left <= right <= self._n\n\n\
    \        return self._sum(right) - self._sum(left)\n\n    def _sum(self, r: int)\
    \ -> typing.Any:\n        s = 0\n        while r > 0:\n            s += self.data[r\
    \ - 1]\n            r -= r & -r\n\n        return s\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/fenwicktree.py
  requiredBy:
  - geometory/offline_static_rectangle_sum.py
  - geometory/offline_point_add_rectangle_sum.py
  timestamp: '2024-02-05 08:23:41+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/fenwicktree.py
layout: document
redirect_from:
- /library/atcoder/fenwicktree.py
- /library/atcoder/fenwicktree.py.html
title: atcoder/fenwicktree.py
---
