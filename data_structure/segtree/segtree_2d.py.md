---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/dsl/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py
    title: "DSL5B The Maximum Number of Overlaps (\u4E8C\u6B21\u5143\u30BB\u30B0\u6728\
      )"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass Segtree2d:\n\
    \    def __init__(\n        self,\n        h: int,\n        w: int,\n        op:\
    \ Callable[[T, T], T],\n        e: T,\n        ps: list[tuple[int, int, T]],\n\
    \    ):\n        self.h = self.w = 1\n        while self.h < h:\n            self.h\
    \ <<= 1\n        while self.w < w:\n            self.w <<= 1\n        self.op\
    \ = op\n        self.e = e\n        self.seg = [e for _ in range((self.h * self.w)\
    \ << 2)]\n        self._build(ps)\n\n    def _id(self, h: int, w: int) -> int:\n\
    \        return h * 2 * self.w + w\n\n    def _build(self, ps: list[tuple[int,\
    \ int, T]]):\n        seg, _id, op = self.seg, self._id, self.op\n\n        for\
    \ h, w, x in ps:\n            seg[_id(h + self.h, w + self.w)] = x\n\n       \
    \ for w in range(self.w, self.w << 1):\n            for h in range(self.h - 1,\
    \ 0, -1):\n                seg[_id(h, w)] = op(seg[_id(h << 1, w)], seg[_id(h\
    \ << 1 | 1, w)])\n        for h in range(self.h << 1):\n            for w in range(self.w\
    \ - 1, 0, -1):\n                seg[_id(h, w)] = op(seg[_id(h, w << 1)], seg[_id(h,\
    \ w << 1 | 1)])\n\n    def get(self, h: int, w: int) -> T:\n        return self.seg[self._id(h\
    \ + self.h, w + self.w)]\n\n    def set(self, h: int, w: int, x: T) -> None:\n\
    \        seg, _id, op = self.seg, self._id, self.op\n        h += self.h\n   \
    \     w += self.w\n        seg[_id(h, w)] = x\n        i = h >> 1\n        while\
    \ i:\n            seg[_id(i, w)] = op(seg[_id(i << 1, w)], seg[_id(i << 1 | 1,\
    \ w)])\n            i >>= 1\n        while h:\n            j = w >> 1\n      \
    \      while j:\n                seg[_id(h, j)] = op(seg[_id(h, j << 1)], seg[_id(h,\
    \ j << 1 | 1)])\n                j >>= 1\n            h >>= 1\n\n    def _inner_query(self,\
    \ h: int, w1: int, w2: int) -> T:\n        seg, _id, op = self.seg, self._id,\
    \ self.op\n        res = self.e\n        while w1 < w2:\n            if w1 & 1:\n\
    \                res = op(res, seg[_id(h, w1)])\n                w1 += 1\n   \
    \         if w2 & 1:\n                w2 -= 1\n                res = op(res, seg[_id(h,\
    \ w2)])\n            w1 >>= 1\n            w2 >>= 1\n        return res\n\n  \
    \  def prod(self, h1: int, w1: int, h2: int, w2: int) -> T:\n        if h1 >=\
    \ h2 or w1 >= w2:\n            return self.e\n        op, _inner_query = self.op,\
    \ self._inner_query\n        res = self.e\n        h1 += self.h\n        h2 +=\
    \ self.h\n        w1 += self.w\n        w2 += self.w\n        while h1 < h2:\n\
    \            if h1 & 1:\n                res = op(res, _inner_query(h1, w1, w2))\n\
    \                h1 += 1\n            if h2 & 1:\n                h2 -= 1\n  \
    \              res = op(res, _inner_query(h2, w1, w2))\n            h1 >>= 1\n\
    \            h2 >>= 1\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/segtree_2d.py
  requiredBy: []
  timestamp: '2024-06-09 10:02:15+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/dsl/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py
documentation_of: data_structure/segtree/segtree_2d.py
layout: document
redirect_from:
- /library/data_structure/segtree/segtree_2d.py
- /library/data_structure/segtree/segtree_2d.py.html
title: data_structure/segtree/segtree_2d.py
---
