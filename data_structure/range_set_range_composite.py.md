---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
  - icon: ':warning:'
    path: data_structure/basic/SortedMultiset.py
    title: SortedMultiset
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/data_structure/range_set_range_composite.test.py
    title: test/library_checker/data_structure/range_set_range_composite.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Callable\nfrom atcoder.segtree import SegTree\n\
    from data_structure.basic.SortedMultiset import SortedMultiset\n\nT = TypeVar(\"\
    T\")\n\n\nclass RangeSetRangeComposite:\n    def __init__(\n        self,\n  \
    \      op: Callable[[T, T], T],\n        e: T,\n        pow_: Callable[[T, int],\
    \ T],\n        id_: T,\n        A: list[T],\n    ):\n        self.op = op\n  \
    \      self.e = e\n        self.pow = pow_\n        self.id = id_\n        self.seg\
    \ = SegTree(op, e, A + [e])\n        self.n = len(A) + 1\n        self.idx = SortedMultiset(range(self.n\
    \ + 1))\n        self.val = A + [e]\n        self.beki = [1] * self.n\n\n    def\
    \ prod(self, l: int, r: int) -> int:\n        assert 0 <= l < r <= self.n\n  \
    \      l1 = self.idx.ge(l)\n        r1 = self.idx.le(r)\n        res = self.e\n\
    \        if l1 != l:\n            l0 = self.idx.le(l)\n            beki = self.beki[l0]\
    \ - (l - l0) if l0 + self.beki[l0] <= r else r - l\n            res = self.pow(self.val[l0],\
    \ beki)\n        if l1 < r1:\n            res = self.op(res, self.seg.prod(l1,\
    \ r1))\n        if r1 != r and l <= r1:\n            res = self.op(res, self.pow(self.val[r1],\
    \ r - r1))\n        return res\n\n    def apply(self, l: int, r: int, f: T) ->\
    \ None:\n        idx, val, beki, seg = self.idx, self.val, self.beki, self.seg\n\
    \n        l0, r0 = idx.le(l), idx.le(r)\n        if l != l0:\n            seg.set(l0,\
    \ self.pow(val[l0], l - l0))\n        if r != r0:\n            beki[r] = beki[r0]\
    \ - (r - r0)\n            idx.add(r)\n            val[r] = val[r0]\n         \
    \   seg.set(r, self.pow(val[r], beki[r]))\n        if l != l0:\n            beki[l0]\
    \ = l - l0\n\n        i = idx.gt(l)\n        while i < r:\n            seg.set(i,\
    \ self.e)\n            idx.discard(i)\n            i = idx.gt(i)\n        val[l]\
    \ = f\n        idx.add(l)\n        beki[l] = r - l\n        seg.set(l, self.pow(f,\
    \ beki[l]))\n"
  dependsOn:
  - atcoder/segtree.py
  - data_structure/basic/SortedMultiset.py
  isVerificationFile: false
  path: data_structure/range_set_range_composite.py
  requiredBy: []
  timestamp: '2024-05-28 15:29:52+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/data_structure/range_set_range_composite.test.py
documentation_of: data_structure/range_set_range_composite.py
layout: document
redirect_from:
- /library/data_structure/range_set_range_composite.py
- /library/data_structure/range_set_range_composite.py.html
title: data_structure/range_set_range_composite.py
---
