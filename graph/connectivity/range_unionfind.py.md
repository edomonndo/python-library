---
data:
  _extendedDependsOn: []
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
  code: "class RangeUnionFind:\n    def __init__(self, n):\n        self.data = [-1]\
    \ * n\n        self.left = [0] * n\n        self.right = [1] * n\n\n    def leader(self,\
    \ k) -> int:\n        if self.data[k] < 0:\n            return k\n        self.data[k]\
    \ = self.leader(self.data[k])\n\n    def merge(self, x, y) -> bool:\n        x\
    \ = self.leader(x)\n        y = self.leader(y)\n        if x == y:\n         \
    \   return False\n        if self.data[x] > self.data[y]:\n            x, y =\
    \ y, x\n        self.data[x] += self.data[y]\n        self.data[y] = x\n     \
    \   self.left[x] = min(self.left[x], self.left[y])\n        self.right[x] = max(self.right[x],\
    \ self.right[y])\n        return True\n\n    def range_merge(self, l, r) -> None:\n\
    \        l = max(l, 0)\n        r = min(r, len(self.data))\n        if l < r:\n\
    \            m = self.right[self.leader(l)]\n            while m < r:\n      \
    \          assert self.left[self.leader(m)] == m\n                self.merge(l,\
    \ m)\n                m = self.right[self.leader(l)]\n\n    def size(self, k)\
    \ -> int:\n        return -self.data[self.leader(k)]\n\n    def same(self, x,\
    \ y) -> bool:\n        return self.leader(x) == self.leader(y)\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/connectivity/range_unionfind.py
  requiredBy: []
  timestamp: '2024-07-29 12:40:49+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/connectivity/range_unionfind.py
layout: document
title: Range Union Find
---
