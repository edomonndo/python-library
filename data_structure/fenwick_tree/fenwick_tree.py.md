---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/point_set_range_frequency.py
    title: data_structure/fenwick_tree/point_set_range_frequency.py
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/range_add_point_get.py
    title: data_structure/fenwick_tree/range_add_point_get.py
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/range_add_range_sum.py
    title: data_structure/fenwick_tree/range_add_range_sum.py
  - icon: ':warning:'
    path: data_structure/fenwick_tree/value_range_sum.py
    title: data_structure/fenwick_tree/value_range_sum.py
  - icon: ':heavy_check_mark:'
    path: geometory/offline_point_add_rectangle_sum.py
    title: geometory/offline_point_add_rectangle_sum.py
  - icon: ':heavy_check_mark:'
    path: geometory/offline_rectangle_add_point_get.py
    title: geometory/offline_rectangle_add_point_get.py
  - icon: ':heavy_check_mark:'
    path: geometory/offline_rectangle_add_rectangle_sum.py
    title: geometory/offline_rectangle_add_rectangle_sum.py
  - icon: ':heavy_check_mark:'
    path: geometory/offline_static_rectangle_sum.py
    title: geometory/offline_static_rectangle_sum.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_b_range_sum_query.test.py
    title: DSL2B Range Sum Query
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_d_range_query_on_a_tree_hld.test.py
    title: GRL5D Range Query on a Tree
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
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass FenwickTree:\n\
    \    def __init__(self, N: int, e: T = 0):\n        self.n = N\n        self.data\
    \ = [e for i in range(N)]\n        self.e = e\n\n    def add(self, p: int, x:\
    \ T) -> None:\n        assert 0 <= p < self.n, \"0<=p<n,p={0},n={1}\".format(p,\
    \ self.n)\n        p += 1\n        while p <= self.n:\n            self.data[p\
    \ - 1] += x\n            p += p & -p\n\n    def sum(self, l: int, r: int) -> T:\n\
    \        assert 0 <= l and l <= r and r <= self.n, \"0<=l<=r<=n,l={0},r={1},n={2}\"\
    .format(\n            l, r, self.n\n        )\n        return self.sum0(r) - self.sum0(l)\n\
    \n    def sum0(self, r: int) -> T:\n        s = self.e\n        while r > 0:\n\
    \            s += self.data[r - 1]\n            r -= r & -r\n        return s\n\
    \n    def bisect_left(self, x: T) -> int:\n        \"\"\"minimize i s.t. sum[0,\
    \ i) >= x. Note x should be integer.\"\"\"\n\n        if x <= self.e:\n      \
    \      return 0\n        p = 0\n        k = 1 << (self.n.bit_length() - 1)\n \
    \       while k:\n            if p + k <= self.n and self.data[p + k - 1] < x:\n\
    \                x -= self.data[p + k - 1]\n                p += k\n         \
    \   k >>= 1\n        return p + 1\n\n    def bisect_right(self, x: T) -> int:\n\
    \        \"\"\"minimize i s.t. sum[0,i) > x. Note x should be integer.\"\"\"\n\
    \        if x <= self.e:\n            return 0\n        p = 0\n        k = 1 <<\
    \ (self.n.bit_length() - 1)\n        while k:\n            if p + k <= self.n\
    \ and self.data[p + k - 1] <= x:\n                x -= self.data[p + k - 1]\n\
    \                p += k\n            k >>= 1\n        return p + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/fenwick_tree/fenwick_tree.py
  requiredBy:
  - data_structure/fenwick_tree/range_add_point_get.py
  - data_structure/fenwick_tree/value_range_sum.py
  - data_structure/fenwick_tree/range_add_range_sum.py
  - data_structure/fenwick_tree/point_set_range_frequency.py
  - geometory/offline_rectangle_add_point_get.py
  - geometory/offline_point_add_rectangle_sum.py
  - geometory/offline_rectangle_add_rectangle_sum.py
  - geometory/offline_static_rectangle_sum.py
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/tree/vertex_add_subtree_sum_hld.test.py
  - test/library_checker/tree/vertex_add_path_sum_hld.test.py
  - test/library_checker/tree/vertex_add_range_contour_sum_on_tree.test.py
  - test/aoj/dsl/dsl_2_b_range_sum_query.test.py
  - test/aoj/grl/grl_5_d_range_query_on_a_tree_hld.test.py
documentation_of: data_structure/fenwick_tree/fenwick_tree.py
layout: document
redirect_from:
- /library/data_structure/fenwick_tree/fenwick_tree.py
- /library/data_structure/fenwick_tree/fenwick_tree.py.html
title: data_structure/fenwick_tree/fenwick_tree.py
---
