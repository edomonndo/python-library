---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/point_set_range_frequency.py
    title: "1\u70B9\u66F4\u65B0\u30FB\u533A\u9593\u983B\u5EA6\uFF08\u30AA\u30D5\u30E9\
      \u30A4\u30F3\uFF09"
  - icon: ':heavy_check_mark:'
    path: geometory/offline_point_add_rectangle_sum.py
    title: "\uFF11\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C(\u30AA\u30D5\u30E9\u30A4\
      \u30F3)"
  - icon: ':heavy_check_mark:'
    path: geometory/offline_rectangle_add_point_get.py
    title: "\u77E9\u5F62\u52A0\u7B97\u30FB\uFF11\u70B9\u53D6\u5F97(\u30AA\u30D5\u30E9\
      \u30A4\u30F3)"
  - icon: ':heavy_check_mark:'
    path: geometory/offline_static_rectangle_sum.py
    title: "\u77E9\u5F62\u548C(\u30AA\u30D5\u30E9\u30A4\u30F3\u30FB\u9759\u7684)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_path_sum_hld.test.py
    title: Vertex Add Path Sum (HLD)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_range_contour_sum_on_tree.test.py
    title: Vertex Add Range Contour Sum on Tree
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
    title: Vertex Add Subtree Sum (HLD)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://en.wikipedia.org/wiki/Fenwick_tree"""
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class FenwickTree:\n    \"\"\"Reference: https://en.wikipedia.org/wiki/Fenwick_tree\"\
    \"\"\n\n    def __init__(self, n: int = 0) -> None:\n        self._n = n\n   \
    \     self.data = [0] * n\n\n    def add(self, p: int, x: int) -> None:\n    \
    \    assert 0 <= p < self._n\n\n        p += 1\n        while p <= self._n:\n\
    \            self.data[p - 1] += x\n            p += p & -p\n\n    def sum(self,\
    \ left: int, right: int) -> int:\n        assert 0 <= left <= right <= self._n\n\
    \n        return self._sum(right) - self._sum(left)\n\n    def _sum(self, r: int)\
    \ -> int:\n        s = 0\n        while r > 0:\n            s += self.data[r -\
    \ 1]\n            r -= r & -r\n\n        return s\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/fenwicktree.py
  requiredBy:
  - geometory/offline_point_add_rectangle_sum.py
  - geometory/offline_rectangle_add_point_get.py
  - geometory/offline_static_rectangle_sum.py
  - data_structure/fenwick_tree/point_set_range_frequency.py
  timestamp: '2024-05-29 14:24:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
  - test/library_checker/tree/vertex_add_range_contour_sum_on_tree.test.py
  - test/library_checker/tree/vertex_add_path_sum_hld.test.py
documentation_of: atcoder/fenwicktree.py
layout: document
redirect_from:
- /library/atcoder/fenwicktree.py
- /library/atcoder/fenwicktree.py.html
title: atcoder/fenwicktree.py
---
