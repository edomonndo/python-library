---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: data_structure/segtree/compressed_segtree.py
    title: data_structure/segtree/compressed_segtree.py
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/range_set_range_composite.py
    title: data_structure/segtree/range_set_range_composite.py
  - icon: ':warning:'
    path: dynamic_programming/longest_increase_subsequence.py
    title: dynamic_programming/longest_increase_subsequence.py
  - icon: ':heavy_check_mark:'
    path: graph/tree/auxiliary_tree.py
    title: graph/tree/auxiliary_tree.py
  - icon: ':heavy_check_mark:'
    path: graph/tree/euler_tour.py
    title: graph/tree/euler_tour.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_2_a_range_min_query.test.py
    title: DSL2A Range Minimum Query(RMQ)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/point_set_range_composite.test.py
    title: Point Set Range Composite
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_rmq_segtree.test.py
    title: Static RMQ (Segment Tree)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertext_set_path_composite.test.py
    title: Vertex Set Path Composite
  - icon: ':heavy_check_mark:'
    path: "test/yukicoder/650_\u884C\u5217\u6728\u30AF\u30A8\u30EA.test.py"
    title: "No.650 \u884C\u5217\u6728\u30AF\u30A8\u30EA"
  - icon: ':heavy_check_mark:'
    path: test/yukicoder/875_range_mindex_query.test.py
    title: No.875 Range Mindex Query
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Segtree:\n    def __init__(self, V, OP, E):\n        self.n = len(V)\n\
    \        self.op = OP\n        self.e = E\n        self.log = (self.n - 1).bit_length()\n\
    \        self.size = 1 << self.log\n        self.d = [E for i in range(2 * self.size)]\n\
    \        for i in range(self.n):\n            self.d[self.size + i] = V[i]\n \
    \       for i in range(self.size - 1, 0, -1):\n            self.update(i)\n\n\
    \    def set(self, p, x):\n        assert 0 <= p and p < self.n\n        p +=\
    \ self.size\n        self.d[p] = x\n        for i in range(1, self.log + 1):\n\
    \            self.update(p >> i)\n\n    def get(self, p):\n        assert 0 <=\
    \ p and p < self.n\n        return self.d[p + self.size]\n\n    def prod(self,\
    \ l, r):\n        assert 0 <= l and l <= r and r <= self.n\n        l += self.size\n\
    \        r += self.size\n        sml, smr = self.e, self.e\n        while l <\
    \ r:\n            if l & 1:\n                sml = self.op(sml, self.d[l])\n \
    \               l += 1\n            if r & 1:\n                smr = self.op(self.d[r\
    \ - 1], smr)\n                r -= 1\n            l >>= 1\n            r >>= 1\n\
    \        return self.op(sml, smr)\n\n    def all_prod(self):\n        return self.d[1]\n\
    \n    def max_right(self, l, f):\n        assert 0 <= l and l <= self.n\n    \
    \    assert f(self.e)\n        if l == self.n:\n            return self.n\n  \
    \      l += self.size\n        sm = self.e\n        while 1:\n            while\
    \ l % 2 == 0:\n                l >>= 1\n            if not f(self.op(sm, self.d[l])):\n\
    \                while l < self.size:\n                    l = 2 * l\n       \
    \             if f(self.op(sm, self.d[l])):\n                        sm = self.op(sm,\
    \ self.d[l])\n                        l += 1\n                return l - self.size\n\
    \            sm = self.op(sm, self.d[l])\n            l += 1\n            if (l\
    \ & -l) == l:\n                break\n        return self.n\n\n    def min_left(self,\
    \ r, f):\n        assert 0 <= r and r <= self.n\n        assert f(self.e)\n  \
    \      if r == 0:\n            return 0\n        r += self.size\n        sm =\
    \ self.e\n        while 1:\n            r -= 1\n            while r > 1 and (r\
    \ % 2):\n                r >>= 1\n            if not f(self.op(self.d[r], sm)):\n\
    \                while r < self.size:\n                    r = 2 * r + 1\n   \
    \                 if f(self.op(self.d[r], sm)):\n                        sm =\
    \ self.op(self.d[r], sm)\n                        r -= 1\n                return\
    \ r + 1 - self.size\n            sm = self.op(self.d[r], sm)\n            if (r\
    \ & -r) == r:\n                break\n        return 0\n\n    def update(self,\
    \ k):\n        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])\n\n    def\
    \ __str__(self):\n        return str([self.get(i) for i in range(self.n)])\n\n\
    \nclass RangeMinQuery:\n    def __init__(self, V):\n        self.n = len(V)\n\
    \        self.log = (self.n - 1).bit_length()\n        self.size = 1 << self.log\n\
    \        _INF = float(\"inf\")\n        self.e = _INF\n        self.d = [_INF\
    \ for i in range(2 * self.size)]\n        for i in range(self.n):\n          \
    \  self.d[self.size + i] = V[i]\n        for i in range(self.size - 1, 0, -1):\n\
    \            self._update(i)\n\n    def update(self, p, x):\n        assert 0\
    \ <= p and p < self.n\n        p += self.size\n        self.d[p] = x\n       \
    \ for i in range(1, self.log + 1):\n            self._update(p >> i)\n\n    def\
    \ get(self, p):\n        assert 0 <= p and p < self.n\n        return self.d[p\
    \ + self.size]\n\n    def query(self, l, r):\n        assert 0 <= l and l <= r\
    \ and r <= self.n\n        l += self.size\n        r += self.size\n        sml,\
    \ smr = self.e, self.e\n        while l < r:\n            if l & 1:\n        \
    \        sml = min(sml, self.d[l])\n                l += 1\n            if r &\
    \ 1:\n                smr = min(self.d[r - 1], smr)\n                r -= 1\n\
    \            l >>= 1\n            r >>= 1\n        return min(sml, smr)\n\n  \
    \  def fold(self):\n        return self.d[1]\n\n    def _update(self, k):\n  \
    \      self.d[k] = min(self.d[2 * k], self.d[2 * k + 1])\n\n    def __str__(self):\n\
    \        return str([self.get(i) for i in range(self.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/segment_tree.py
  requiredBy:
  - dynamic_programming/longest_increase_subsequence.py
  - graph/tree/euler_tour.py
  - graph/tree/auxiliary_tree.py
  - data_structure/segtree/compressed_segtree.py
  - data_structure/segtree/range_set_range_composite.py
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - "test/yukicoder/650_\u884C\u5217\u6728\u30AF\u30A8\u30EA.test.py"
  - test/yukicoder/875_range_mindex_query.test.py
  - test/library_checker/tree/vertext_set_path_composite.test.py
  - test/library_checker/data_structure/point_set_range_composite.test.py
  - test/library_checker/data_structure/static_rmq_segtree.test.py
  - test/aoj/dsl/dsl_2_a_range_min_query.test.py
documentation_of: data_structure/segtree/segment_tree.py
layout: document
redirect_from:
- /library/data_structure/segtree/segment_tree.py
- /library/data_structure/segtree/segment_tree.py.html
title: data_structure/segtree/segment_tree.py
---
