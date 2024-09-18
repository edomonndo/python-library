---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_d_range_update_query.test.py
    title: DSL2D Range Update Query(RUQ)
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_e_range_add_query.test.py
    title: DSL2E Range Add Query(RAQ)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/range_affine_point_get.test.py
    title: Range Affine Point Get
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DualSegtree:\n    def __init__(self, V, MAPPING, COMPOSITION, ID):\n\
    \        self.n = len(V)\n        self.log = (self.n - 1).bit_length()\n     \
    \   self.size = 1 << self.log\n        # \u533A\u9593[0,self.size)\u3092\u9045\
    \u5EF6\u4F1D\u64AD\u7528\uFF0C\u533A\u9593[self.size, self.size + n)\u304C\u5B9F\
    \u30C7\u30FC\u30BF\n        self.d = [ID for i in range(2 * self.size)]\n    \
    \    for i in range(self.n):\n            self.d[self.size + i] = V[i]\n     \
    \   # \u9045\u5EF6\u4F1D\u64AD\u7528\n        self.mapping = MAPPING\n       \
    \ self.composition = COMPOSITION\n        self.identity = ID\n\n    def set(self,\
    \ p, x):\n        assert 0 <= p and p < self.n\n        p += self.size\n     \
    \   # \u9045\u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n   \
    \         self._push(p >> i)\n        self.d[p] = x\n\n    def get(self, p):\n\
    \        assert 0 <= p and p < self.n\n        p += self.size\n        # \u9045\
    \u5EF6\u4F1D\u64AD\n        for i in range(self.log, 0, -1):\n            self._push(p\
    \ >> i)\n        return self.d[p]\n\n    def apply_point(self, p, f):\n      \
    \  assert 0 <= p and p < self.n\n        p += self.size\n        for i in range(self.log,\
    \ 0, -1):\n            self._push(p >> i)\n        self.d[p] = self.mapping(f,\
    \ self.d[p])\n\n    def apply(self, l, r, f):\n        assert 0 <= l and l <=\
    \ r and r <= self.n\n        if l == r:\n            return\n        l += self.size\n\
    \        r += self.size\n        for i in range(self.log, 0, -1):\n          \
    \  if ((l >> i) << i) != l:\n                self._push(l >> i)\n            if\
    \ ((r >> i) << i) != r:\n                self._push((r - 1) >> i)\n        while\
    \ l < r:\n            if l & 1:\n                self._all_apply(l, f)\n     \
    \           l += 1\n            if r & 1:\n                r -= 1\n          \
    \      self._all_apply(r, f)\n            l >>= 1\n            r >>= 1\n\n   \
    \ def _all_apply(self, k, f):\n        if k < self.size:\n            self.d[k]\
    \ = self.composition(f, self.d[k])\n        else:\n            self.d[k] = self.mapping(f,\
    \ self.d[k])\n\n    def _push(self, k):\n        self._all_apply(2 * k, self.d[k])\n\
    \        self._all_apply(2 * k + 1, self.d[k])\n        self.d[k] = self.identity\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/dual_segment_tree.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/range_affine_point_get.test.py
  - test/aoj/dsl/dsl_2_e_range_add_query.test.py
  - test/aoj/dsl/dsl_2_d_range_update_query.test.py
documentation_of: data_structure/segtree/dual_segment_tree.py
layout: document
redirect_from:
- /library/data_structure/segtree/dual_segment_tree.py
- /library/data_structure/segtree/dual_segment_tree.py.html
title: data_structure/segtree/dual_segment_tree.py
---
