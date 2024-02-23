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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import typing\n\nimport atcoder._bit\n\n\nclass SegTree:\n    def __init__(self,\n\
    \                 op: typing.Callable[[typing.Any, typing.Any], typing.Any],\n\
    \                 e: typing.Any,\n                 v: typing.Union[int, typing.List[typing.Any]])\
    \ -> None:\n        self._op = op\n        self._e = e\n\n        if isinstance(v,\
    \ int):\n            v = [e] * v\n\n        self._n = len(v)\n        self._log\
    \ = atcoder._bit._ceil_pow2(self._n)\n        self._size = 1 << self._log\n  \
    \      self._d = [e] * (2 * self._size)\n\n        for i in range(self._n):\n\
    \            self._d[self._size + i] = v[i]\n        for i in range(self._size\
    \ - 1, 0, -1):\n            self._update(i)\n\n    def set(self, p: int, x: typing.Any)\
    \ -> None:\n        assert 0 <= p < self._n\n\n        p += self._size\n     \
    \   self._d[p] = x\n        for i in range(1, self._log + 1):\n            self._update(p\
    \ >> i)\n\n    def get(self, p: int) -> typing.Any:\n        assert 0 <= p < self._n\n\
    \n        return self._d[p + self._size]\n\n    def prod(self, left: int, right:\
    \ int) -> typing.Any:\n        assert 0 <= left <= right <= self._n\n        sml\
    \ = self._e\n        smr = self._e\n        left += self._size\n        right\
    \ += self._size\n\n        while left < right:\n            if left & 1:\n   \
    \             sml = self._op(sml, self._d[left])\n                left += 1\n\
    \            if right & 1:\n                right -= 1\n                smr =\
    \ self._op(self._d[right], smr)\n            left >>= 1\n            right >>=\
    \ 1\n\n        return self._op(sml, smr)\n\n    def all_prod(self) -> typing.Any:\n\
    \        return self._d[1]\n\n    def max_right(self, left: int,\n           \
    \       f: typing.Callable[[typing.Any], bool]) -> int:\n        assert 0 <= left\
    \ <= self._n\n        assert f(self._e)\n\n        if left == self._n:\n     \
    \       return self._n\n\n        left += self._size\n        sm = self._e\n\n\
    \        first = True\n        while first or (left & -left) != left:\n      \
    \      first = False\n            while left % 2 == 0:\n                left >>=\
    \ 1\n            if not f(self._op(sm, self._d[left])):\n                while\
    \ left < self._size:\n                    left *= 2\n                    if f(self._op(sm,\
    \ self._d[left])):\n                        sm = self._op(sm, self._d[left])\n\
    \                        left += 1\n                return left - self._size\n\
    \            sm = self._op(sm, self._d[left])\n            left += 1\n\n     \
    \   return self._n\n\n    def min_left(self, right: int,\n                 f:\
    \ typing.Callable[[typing.Any], bool]) -> int:\n        assert 0 <= right <= self._n\n\
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
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/segtree.py
layout: document
redirect_from:
- /library/atcoder/segtree.py
- /library/atcoder/segtree.py.html
title: atcoder/segtree.py
---