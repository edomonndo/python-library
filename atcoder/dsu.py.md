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
  code: "import typing\n\n\nclass DSU:\n    '''\n    Implement (union by size) + (path\
    \ halving)\n\n    Reference:\n    Zvi Galil and Giuseppe F. Italiano,\n    Data\
    \ structures and algorithms for disjoint set union problems\n    '''\n\n    def\
    \ __init__(self, n: int = 0) -> None:\n        self._n = n\n        self.parent_or_size\
    \ = [-1] * n\n\n    def merge(self, a: int, b: int) -> int:\n        assert 0\
    \ <= a < self._n\n        assert 0 <= b < self._n\n\n        x = self.leader(a)\n\
    \        y = self.leader(b)\n\n        if x == y:\n            return x\n\n  \
    \      if -self.parent_or_size[x] < -self.parent_or_size[y]:\n            x, y\
    \ = y, x\n\n        self.parent_or_size[x] += self.parent_or_size[y]\n       \
    \ self.parent_or_size[y] = x\n\n        return x\n\n    def same(self, a: int,\
    \ b: int) -> bool:\n        assert 0 <= a < self._n\n        assert 0 <= b < self._n\n\
    \n        return self.leader(a) == self.leader(b)\n\n    def leader(self, a: int)\
    \ -> int:\n        assert 0 <= a < self._n\n\n        parent = self.parent_or_size[a]\n\
    \        while parent >= 0:\n            if self.parent_or_size[parent] < 0:\n\
    \                return parent\n            self.parent_or_size[a], a, parent\
    \ = (\n                self.parent_or_size[parent],\n                self.parent_or_size[parent],\n\
    \                self.parent_or_size[self.parent_or_size[parent]]\n          \
    \  )\n\n        return a\n\n    def size(self, a: int) -> int:\n        assert\
    \ 0 <= a < self._n\n\n        return -self.parent_or_size[self.leader(a)]\n\n\
    \    def groups(self) -> typing.List[typing.List[int]]:\n        leader_buf =\
    \ [self.leader(i) for i in range(self._n)]\n\n        result: typing.List[typing.List[int]]\
    \ = [[] for _ in range(self._n)]\n        for i in range(self._n):\n         \
    \   result[leader_buf[i]].append(i)\n\n        return list(filter(lambda r: r,\
    \ result))\n"
  dependsOn: []
  isVerificationFile: false
  path: atcoder/dsu.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: atcoder/dsu.py
layout: document
redirect_from:
- /library/atcoder/dsu.py
- /library/atcoder/dsu.py.html
title: atcoder/dsu.py
---
