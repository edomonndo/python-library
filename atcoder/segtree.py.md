---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: data_structure/segtree/compressed_segtree.py
    title: "\u5EA7\u6A19\u5727\u7E2E\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/range_set_range_composite.py
    title: "\u533A\u9593\u66F4\u65B0\u30FB\u533A\u9593\u30A2\u30D5\u30A3\u30F3"
  - icon: ':warning:'
    path: dynamic_programming/longest_increase_subsequence.py
    title: "\u6700\u9577\u5897\u52A0\u6587\u5B57\u5217(LIS)"
  - icon: ':heavy_check_mark:'
    path: tree/auxiliary_tree.py
    title: Auxiliary tree
  - icon: ':heavy_check_mark:'
    path: tree/euler_tour.py
    title: Euler tour
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/tree/vertext_set_path_composite.test.py
    title: Vertex Set Path Composite
  - icon: ':heavy_check_mark:'
    path: test/yukicoder/875_range_mindex_query.test.py
    title: No.875 Range Mindex Query
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\n\ndef _ceil_pow2(n: int) -> int:\n\
    \    x = 0\n    while (1 << x) < n:\n        x += 1\n\n    return x\n\n\nT = TypeVar(\"\
    T\")\n\n\nclass SegTree:\n    def __init__(self, op: Callable[[T, T], T], e: T,\
    \ v: list[T]) -> None:\n        self._op = op\n        self._e = e\n\n       \
    \ if isinstance(v, int):\n            v = [e] * v\n\n        self._n = len(v)\n\
    \        self._log = _ceil_pow2(self._n)\n        self._size = 1 << self._log\n\
    \        self._d = [e] * (2 * self._size)\n\n        for i in range(self._n):\n\
    \            self._d[self._size + i] = v[i]\n        for i in range(self._size\
    \ - 1, 0, -1):\n            self._update(i)\n\n    def set(self, p: int, x: T)\
    \ -> None:\n        assert 0 <= p < self._n\n\n        p += self._size\n     \
    \   self._d[p] = x\n        for i in range(1, self._log + 1):\n            self._update(p\
    \ >> i)\n\n    def get(self, p: int) -> T:\n        assert 0 <= p < self._n\n\n\
    \        return self._d[p + self._size]\n\n    def prod(self, left: int, right:\
    \ int) -> T:\n        assert 0 <= left <= right <= self._n\n        sml = self._e\n\
    \        smr = self._e\n        left += self._size\n        right += self._size\n\
    \n        while left < right:\n            if left & 1:\n                sml =\
    \ self._op(sml, self._d[left])\n                left += 1\n            if right\
    \ & 1:\n                right -= 1\n                smr = self._op(self._d[right],\
    \ smr)\n            left >>= 1\n            right >>= 1\n\n        return self._op(sml,\
    \ smr)\n\n    def all_prod(self) -> T:\n        return self._d[1]\n\n    def max_right(self,\
    \ left: int, f: Callable[[T], bool]) -> int:\n        assert 0 <= left <= self._n\n\
    \        assert f(self._e)\n\n        if left == self._n:\n            return\
    \ self._n\n\n        left += self._size\n        sm = self._e\n\n        first\
    \ = True\n        while first or (left & -left) != left:\n            first =\
    \ False\n            while left % 2 == 0:\n                left >>= 1\n      \
    \      if not f(self._op(sm, self._d[left])):\n                while left < self._size:\n\
    \                    left *= 2\n                    if f(self._op(sm, self._d[left])):\n\
    \                        sm = self._op(sm, self._d[left])\n                  \
    \      left += 1\n                return left - self._size\n            sm = self._op(sm,\
    \ self._d[left])\n            left += 1\n\n        return self._n\n\n    def min_left(self,\
    \ right: int, f: Callable[[T], bool]) -> int:\n        assert 0 <= right <= self._n\n\
    \        assert f(self._e)\n\n        if right == 0:\n            return 0\n\n\
    \        right += self._size\n        sm = self._e\n\n        first = True\n \
    \       while first or (right & -right) != right:\n            first = False\n\
    \            right -= 1\n            while right > 1 and right % 2:\n        \
    \        right >>= 1\n            if not f(self._op(self._d[right], sm)):\n  \
    \              while right < self._size:\n                    right = 2 * right\
    \ + 1\n                    if f(self._op(self._d[right], sm)):\n             \
    \           sm = self._op(self._d[right], sm)\n                        right -=\
    \ 1\n                return right + 1 - self._size\n            sm = self._op(self._d[right],\
    \ sm)\n\n        return 0\n\n    def _update(self, k: int) -> None:\n        self._d[k]\
    \ = self._op(self._d[2 * k], self._d[2 * k + 1])\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/segtree.py
  requiredBy:
  - dynamic_programming/longest_increase_subsequence.py
  - data_structure/segtree/compressed_segtree.py
  - data_structure/segtree/range_set_range_composite.py
  - tree/auxiliary_tree.py
  - tree/euler_tour.py
  timestamp: '2024-06-04 17:27:40+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/yukicoder/875_range_mindex_query.test.py
  - test/library_checker/tree/vertext_set_path_composite.test.py
documentation_of: atcoder/segtree.py
layout: document
redirect_from:
- /library/atcoder/segtree.py
- /library/atcoder/segtree.py.html
title: atcoder/segtree.py
---
