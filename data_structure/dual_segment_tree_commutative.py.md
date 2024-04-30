---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/abc342g.test.py
    title: test/atcoder/abc342g.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DualSegtreeCommutative:\n    def __init__(self, V, OP, ID, GET, E):\n\
    \        self.n = n = len(V)\n        log = (n - 1).bit_length()\n        self.size\
    \ = 1 << log\n        # \u533A\u9593[0,self.size)\u3092\u9045\u5EF6\u4F1D\u64AD\
    \u7528\uFF0C\u533A\u9593[self.size, self.size + n)\u304C\u5B9F\u30C7\u30FC\u30BF\
    \n        self.d = [ID for _ in range(2 * self.size)]\n        for i in range(n):\n\
    \            self.d[self.size + i] = V[i]\n        self.op = OP\n        self.identity\
    \ = ID\n        self._get = GET\n        self.e = E\n\n    def get(self, p: int):\n\
    \        assert 0 <= p and p < self.n\n        res = self.e\n        p += self.size\n\
    \        while p:\n            res = self._get(res, self.d[p])\n            p\
    \ >>= 1\n        return res\n\n    def apply(self, l: int, r: int, f):\n     \
    \   assert 0 <= l and l <= r and r <= self.n\n        if l == r:\n           \
    \ return\n        l += self.size\n        r += self.size\n        while l < r:\n\
    \            if l & 1:\n                self.op(f, self.d[l])\n              \
    \  l += 1\n            if r & 1:\n                r -= 1\n                self.op(f,\
    \ self.d[r])\n            l >>= 1\n            r >>= 1\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/dual_segment_tree_commutative.py
  requiredBy: []
  timestamp: '2024-03-01 13:03:21+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith:
  - test/atcoder/abc342g.test.py
documentation_of: data_structure/dual_segment_tree_commutative.py
layout: document
title: "\u64CD\u4F5C\u53EF\u63DB\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dual\
  \ Segment Tree)"
---

区間操作が可換な場合に遅延伝搬処理を省略し,定数倍高速化を図った双対セグ木.