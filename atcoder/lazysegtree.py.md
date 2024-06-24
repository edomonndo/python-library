---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: geometory/union_area_rectangle.py
    title: "\u9577\u65B9\u5F62\u306E\u548C\u96C6\u5408\u306E\u9762\u7A4D"
  - icon: ':warning:'
    path: tree/permutation_tree.py
    title: tree/permutation_tree.py
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/abc001-99/abc035c.test.py
    title: "C - \u30AA\u30BB\u30ED"
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc300-399/abc341e.test.py
    title: E - Alternating String
  - icon: ':x:'
    path: test/atcoder/abc300-399/abc357f.test.py
    title: F - Two Sequence Queries
  - icon: ':x:'
    path: test/atcoder/other/able.test.py
    title: E - Replace Digits
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar, Union, Optional\n\n\ndef _ceil_pow2(n:\
    \ int) -> int:\n    x = 0\n    while (1 << x) < n:\n        x += 1\n\n    return\
    \ x\n\n\nS = TypeVar(\"S\")\nF = TypeVar(\"F\")\n\n\nclass LazySegTree:\n    def\
    \ __init__(\n        self,\n        op: Callable[[S, S], S],\n        e: S,\n\
    \        mapping: Callable[[S, F], S],\n        composition: Callable[[F, F],\
    \ F],\n        id_: F,\n        v: Union[int, list[S]],\n    ) -> None:\n    \
    \    self._op = op\n        self._e = e\n        self._mapping = mapping\n   \
    \     self._composition = composition\n        self._id = id_\n\n        if isinstance(v,\
    \ int):\n            v = [e] * v\n\n        self._n = len(v)\n        self._log\
    \ = _ceil_pow2(self._n)\n        self._size = 1 << self._log\n        self._d\
    \ = [e] * (2 * self._size)\n        self._lz = [self._id] * self._size\n     \
    \   for i in range(self._n):\n            self._d[self._size + i] = v[i]\n   \
    \     for i in range(self._size - 1, 0, -1):\n            self._update(i)\n\n\
    \    def set(self, p: int, x: S) -> None:\n        assert 0 <= p < self._n\n\n\
    \        p += self._size\n        for i in range(self._log, 0, -1):\n        \
    \    self._push(p >> i)\n        self._d[p] = x\n        for i in range(1, self._log\
    \ + 1):\n            self._update(p >> i)\n\n    def get(self, p: int) -> S:\n\
    \        assert 0 <= p < self._n\n\n        p += self._size\n        for i in\
    \ range(self._log, 0, -1):\n            self._push(p >> i)\n        return self._d[p]\n\
    \n    def prod(self, left: int, right: int) -> S:\n        assert 0 <= left <=\
    \ right <= self._n\n\n        if left == right:\n            return self._e\n\n\
    \        left += self._size\n        right += self._size\n\n        for i in range(self._log,\
    \ 0, -1):\n            if ((left >> i) << i) != left:\n                self._push(left\
    \ >> i)\n            if ((right >> i) << i) != right:\n                self._push(right\
    \ >> i)\n\n        sml = self._e\n        smr = self._e\n        while left <\
    \ right:\n            if left & 1:\n                sml = self._op(sml, self._d[left])\n\
    \                left += 1\n            if right & 1:\n                right -=\
    \ 1\n                smr = self._op(self._d[right], smr)\n            left >>=\
    \ 1\n            right >>= 1\n\n        return self._op(sml, smr)\n\n    def all_prod(self)\
    \ -> S:\n        return self._d[1]\n\n    def apply(\n        self,\n        left:\
    \ int,\n        right: Optional[int] = None,\n        f: Optional[F] = None,\n\
    \    ) -> None:\n        assert f is not None\n\n        if right is None:\n \
    \           p = left\n            assert 0 <= left < self._n\n\n            p\
    \ += self._size\n            for i in range(self._log, 0, -1):\n             \
    \   self._push(p >> i)\n            self._d[p] = self._mapping(f, self._d[p])\n\
    \            for i in range(1, self._log + 1):\n                self._update(p\
    \ >> i)\n        else:\n            assert 0 <= left <= right <= self._n\n   \
    \         if left == right:\n                return\n\n            left += self._size\n\
    \            right += self._size\n\n            for i in range(self._log, 0, -1):\n\
    \                if ((left >> i) << i) != left:\n                    self._push(left\
    \ >> i)\n                if ((right >> i) << i) != right:\n                  \
    \  self._push((right - 1) >> i)\n\n            l2 = left\n            r2 = right\n\
    \            while left < right:\n                if left & 1:\n             \
    \       self._all_apply(left, f)\n                    left += 1\n            \
    \    if right & 1:\n                    right -= 1\n                    self._all_apply(right,\
    \ f)\n                left >>= 1\n                right >>= 1\n            left\
    \ = l2\n            right = r2\n\n            for i in range(1, self._log + 1):\n\
    \                if ((left >> i) << i) != left:\n                    self._update(left\
    \ >> i)\n                if ((right >> i) << i) != right:\n                  \
    \  self._update((right - 1) >> i)\n\n    def max_right(self, left: int, g: Callable[[S],\
    \ bool]) -> int:\n        assert 0 <= left <= self._n\n        assert g(self._e)\n\
    \n        if left == self._n:\n            return self._n\n\n        left += self._size\n\
    \        for i in range(self._log, 0, -1):\n            self._push(left >> i)\n\
    \n        sm = self._e\n        first = True\n        while first or (left & -left)\
    \ != left:\n            first = False\n            while left % 2 == 0:\n    \
    \            left >>= 1\n            if not g(self._op(sm, self._d[left])):\n\
    \                while left < self._size:\n                    self._push(left)\n\
    \                    left *= 2\n                    if g(self._op(sm, self._d[left])):\n\
    \                        sm = self._op(sm, self._d[left])\n                  \
    \      left += 1\n                return left - self._size\n            sm = self._op(sm,\
    \ self._d[left])\n            left += 1\n\n        return self._n\n\n    def min_left(self,\
    \ right: int, g: Callable[[S], bool]) -> int:\n        assert 0 <= right <= self._n\n\
    \        assert g(self._e)\n\n        if right == 0:\n            return 0\n\n\
    \        right += self._size\n        for i in range(self._log, 0, -1):\n    \
    \        self._push((right - 1) >> i)\n\n        sm = self._e\n        first =\
    \ True\n        while first or (right & -right) != right:\n            first =\
    \ False\n            right -= 1\n            while right > 1 and right % 2:\n\
    \                right >>= 1\n            if not g(self._op(self._d[right], sm)):\n\
    \                while right < self._size:\n                    self._push(right)\n\
    \                    right = 2 * right + 1\n                    if g(self._op(self._d[right],\
    \ sm)):\n                        sm = self._op(self._d[right], sm)\n         \
    \               right -= 1\n                return right + 1 - self._size\n  \
    \          sm = self._op(self._d[right], sm)\n\n        return 0\n\n    def _update(self,\
    \ k: int) -> None:\n        self._d[k] = self._op(self._d[2 * k], self._d[2 *\
    \ k + 1])\n\n    def _all_apply(self, k: int, f: F) -> None:\n        self._d[k]\
    \ = self._mapping(f, self._d[k])\n        if k < self._size:\n            self._lz[k]\
    \ = self._composition(f, self._lz[k])\n\n    def _push(self, k: int) -> None:\n\
    \        self._all_apply(2 * k, self._lz[k])\n        self._all_apply(2 * k +\
    \ 1, self._lz[k])\n        self._lz[k] = self._id\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/lazysegtree.py
  requiredBy:
  - geometory/union_area_rectangle.py
  - tree/permutation_tree.py
  timestamp: '2024-06-05 17:57:14+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/atcoder/other/able.test.py
  - test/atcoder/abc300-399/abc341e.test.py
  - test/atcoder/abc300-399/abc357f.test.py
  - test/atcoder/abc001-99/abc035c.test.py
documentation_of: atcoder/lazysegtree.py
layout: document
redirect_from:
- /library/atcoder/lazysegtree.py
- /library/atcoder/lazysegtree.py.html
title: atcoder/lazysegtree.py
---
