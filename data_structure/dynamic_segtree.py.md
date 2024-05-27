---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/arc008d_dyn_segtree.test.py
    title: test/atcoder/arc008d_dyn_segtree.test.py
  - icon: ':x:'
    path: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
    title: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\nsys.setrecursionlimit(10**6)\n\nimport pypyjit\n\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\nfrom typing import TypeVar, Callable\n\nT = TypeVar(\"\
    T\")\n\n\nclass SegtreeNode:\n    def __init__(self, i: int, value: T):\n    \
    \    self.idx = i\n        self.value = value\n        self.product = value\n\
    \        self.l = None\n        self.r = None\n\n\nclass DynamicSegtree:\n   \
    \ def __init__(self, n: int, op: Callable[[T, T], T], e: T):\n        self.root\
    \ = SegtreeNode(0, e)\n        self.n = n\n        self.op = op\n        self.e\
    \ = e\n\n    def _update(self, cur: SegtreeNode) -> None:\n        l, r, op =\
    \ cur.l, cur.r, self.op\n        res = cur.value\n        if l is not None:\n\
    \            res = op(l.product, res)\n        if r is not None:\n           \
    \ res = op(res, r.product)\n        cur.product = res\n\n    def _set(self, cur:\
    \ SegtreeNode, a: int, b: int, i: int, value: T) -> None:\n        if cur is None:\n\
    \            cur = SegtreeNode(i, value)\n            return\n        if cur.idx\
    \ == i:\n            cur.value = value\n            self._update(cur)\n      \
    \      return\n        c = (a + b) >> 1\n        if i < c:\n            if cur.idx\
    \ < i:\n                cur.idx, i = i, cur.idx\n                cur.value, value\
    \ = value, cur.value\n            if cur.l is None:\n                cur.l = SegtreeNode(i,\
    \ value)\n            self._set(cur.l, a, c, i, value)\n        else:\n      \
    \      if i < cur.idx:\n                i, cur.idx = cur.idx, i\n            \
    \    cur.value, value = value, cur.value\n            if cur.r is None:\n    \
    \            cur.r = SegtreeNode(i, value)\n            self._set(cur.r, c, b,\
    \ i, value)\n        self._update(cur)\n        return\n\n    def _get(self, cur:\
    \ SegtreeNode, a: int, b: int, i: int) -> T:\n        if cur is None:\n      \
    \      return self.e\n        if cur.idx == i:\n            return cur.value\n\
    \        c = (a + b) >> 1\n        if i < c:\n            return self._get(cur.l,\
    \ a, c, i)\n        else:\n            return self._get(cur.r, c, b, i)\n\n  \
    \  def _prod(self, cur: SegtreeNode, a: int, b: int, l: int, r: int) -> T:\n \
    \       if cur is None or b <= l or r <= a:\n            return self.e\n     \
    \   if l <= a and b <= r:\n            return cur.product\n        c = (a + b)\
    \ >> 1\n        res = self._prod(cur.l, a, c, l, r)\n        if l <= cur.idx and\
    \ cur.idx < r:\n            res = self.op(res, cur.value)\n        return self.op(res,\
    \ self._prod(cur.r, c, b, l, r))\n\n    def set(self, i: int, value: T) -> None:\n\
    \        self._set(self.root, 0, self.n, i, value)\n\n    __setitem__ = set\n\n\
    \    def get(self, i: int) -> T:\n        self._get(self.root, 0, self.n, i)\n\
    \n    __getitem__ = get\n\n    def prod(self, l: int, r: int) -> T:\n        assert\
    \ 0 <= l <= r and r <= self.n\n        return self._prod(self.root, 0, self.n,\
    \ l, r)\n\n    def all_prod(self) -> T:\n        return self.root.product if self.root\
    \ else self.e\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/dynamic_segtree.py
  requiredBy: []
  timestamp: '2024-05-27 17:45:23+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
  - test/atcoder/arc008d_dyn_segtree.test.py
documentation_of: data_structure/dynamic_segtree.py
layout: document
redirect_from:
- /library/data_structure/dynamic_segtree.py
- /library/data_structure/dynamic_segtree.py.html
title: data_structure/dynamic_segtree.py
---
