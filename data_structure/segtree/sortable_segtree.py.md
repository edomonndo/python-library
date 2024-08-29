---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
    title: Point Set Range Sort Composite
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import *\nfrom typing import Callable, TypeVar\n\nT = TypeVar(\"\
    T\")\nS = TypeVar(\"S\", bound=\"SegNode\")\n\n\ndef xor64():\n    x = 88172645463325252\n\
    \    while True:\n        x = x ^ ((x << 7) & 0xFFFFFFFF)\n        x = x ^ (x\
    \ >> 9)\n        yield x & 0xFFFFFFFF\n\n\nrand = xor64()\n\n\nclass SegNode:\n\
    \    def __init__(self, key: int, value: T):\n        self.key = self.kmin = self.kmax\
    \ = key\n        self.val = self.sum = value\n        self.inner_l = self.inner_r\
    \ = None\n        self.outer_l = self.outer_r = None\n        self.flip = 0\n\
    \        self.sz = self.inner_sz = 1\n        self.pri = next(rand)\n\n    def\
    \ __str__(self):\n        return f\"<SegNode(key={self.key}, val={self.val}, sum={self.sum},\
    \ inner=({type(self.inner_l).__name__},{type(self.inner_r).__name__}), outer=({type(self.outer_l).__name__},{type(self.outer_r).__name__}),\
    \ flip={self.flip})>\"\n\n\nclass SortableSegtree:\n    def __init__(\n      \
    \  self, op: Callable[[T, T], T], e_: T, toggle: Callable[[T], T], V: list[T]\n\
    \    ):\n        self.op = op\n        self.e = e_\n        self.toggle = toggle\n\
    \        self.V = V\n        self.root = self._build(0, len(V))\n\n    def _build(self,\
    \ l: int, r: int) -> S:\n        m = (l + r) >> 1\n        t = SegNode(self.V[m][0],\
    \ self.V[m][1])\n        t.outer_l = self._build(l, m) if l < m else None\n  \
    \      t.outer_r = self._build(m + 1, r) if m + 1 < r else None\n        self._pri_satisfy(t)\n\
    \        self._update(t)\n        return t\n\n    def _pri_satisfy(self, t: S)\
    \ -> None:\n        if not t.outer_l:\n            if not t.outer_r or t.pri >\
    \ t.outer_r.pri:\n                return\n            t.pri, t.outer_r.pri = t.outer_r.pri,\
    \ t.pri\n            self._pri_satisfy(t.outer_r)\n        elif not t.outer_r:\n\
    \            if t.pri > t.outer_l.pri:\n                return\n            t.pri,\
    \ t.outer_l.pri = t.outer_l.pri, t.pri\n            self._pri_satisfy(t.outer_l)\n\
    \        elif t.outer_l.pri > t.outer_r.pri:\n            if t.pri > t.outer_l.pri:\n\
    \                return\n            t.pri, t.outer_l.pri = t.outer_l.pri, t.pri\n\
    \            self._pri_satisfy(t.outer_l)\n        else:\n            if t.pri\
    \ > t.outer_r.pri:\n                return\n            t.pri, t.outer_r.pri =\
    \ t.outer_r.pri, t.pri\n            self._pri_satisfy(t.outer_r)\n\n    @staticmethod\n\
    \    def _size(t: S) -> int:\n        return t.sz if t else 0\n\n    def _toggle(self,\
    \ t: S) -> None:\n        t.inner_l, t.inner_r = t.inner_r, t.inner_l\n      \
    \  t.outer_l, t.outer_r = t.outer_r, t.outer_l\n        t.sum = self.toggle(t.sum)\n\
    \        t.flip ^= 1\n\n    def _push_down(self, t: S) -> None:\n        if not\
    \ t.flip:\n            return\n        for node in [t.inner_l, t.inner_r, t.outer_l,\
    \ t.outer_r]:\n            if node:\n                self._toggle(node)\n    \
    \    t.flip = 0\n\n    def _update(self, t: S) -> None:\n        t.sz, t.inner_sz\
    \ = 0, 1\n        t.kmin = t.kmax = t.key\n        t.sum = self.e\n        if\
    \ t.outer_l:\n            t.sum = t.outer_l.sum\n            t.sz += t.outer_l.sz\n\
    \        if t.inner_l:\n            t.inner_sz += t.inner_l.inner_sz\n       \
    \     t.sum = self.op(t.sum, t.inner_l.sum)\n            t.kmin = min(t.kmin,\
    \ t.inner_l.kmin)\n            t.kmax = max(t.kmax, t.inner_l.kmax)\n        t.sum\
    \ = self.op(t.sum, t.val)\n        if t.inner_r:\n            t.inner_sz += t.inner_r.inner_sz\n\
    \            t.sum = self.op(t.sum, t.inner_r.sum)\n            t.kmin = min(t.kmin,\
    \ t.inner_r.kmin)\n            t.kmax = max(t.kmax, t.inner_r.kmax)\n        if\
    \ t.outer_r:\n            t.sum = self.op(t.sum, t.outer_r.sum)\n            t.sz\
    \ += t.outer_r.sz\n        t.sz += t.inner_sz\n\n    def _merge_outer(self, l:\
    \ S, r: S) -> S:\n        if not l:\n            return r\n        if not r:\n\
    \            return l\n        self._push_down(l)\n        self._push_down(r)\n\
    \        if l.pri > r.pri:\n            l.outer_r = self._merge_outer(l.outer_r,\
    \ r)\n            self._update(l)\n            return l\n        else:\n     \
    \       r.outer_l = self._merge_outer(l, r.outer_l)\n            self._update(r)\n\
    \            return r\n\n    def _merge_compress(self, l: S, r: S) -> S:\n   \
    \     if not l:\n            return r\n        if not r:\n            return l\n\
    \        self._push_down(l)\n        self._push_down(r)\n        if l.pri < r.pri:\n\
    \            l, r = r, l\n        if l.key < r.kmin:\n            l.inner_r =\
    \ self._merge_compress(l.inner_r, r)\n        elif r.kmax < l.key:\n         \
    \   l.inner_l = self._merge_compress(l.inner_l, r)\n        else:\n          \
    \  rl, rr = self._split_key(r, l.key)\n            l.inner_l = self._merge_compress(l.inner_l,\
    \ rl)\n            l.inner_r = self._merge_compress(l.inner_r, rr)\n        self._update(l)\n\
    \        return l\n\n    def _split_key(self, t: S, key: int) -> tuple[S, S]:\n\
    \        if not t:\n            return None, None\n        if key < t.kmin:\n\
    \            return None, t\n        if t.kmax <= key:\n            return t,\
    \ None\n        self._push_down(t)\n        if key < t.key:\n            tl, tr\
    \ = self._split_key(t.inner_l, key)\n            t.inner_l = tr\n            self._update(t)\n\
    \            return tl, t\n        else:\n            tl, tr = self._split_key(t.inner_r,\
    \ key)\n            t.inner_r = tl\n            self._update(t)\n            return\
    \ t, tr\n\n    def _split_outer(self, t: S, i: int) -> tuple[S, S]:\n        if\
    \ not t:\n            return None, None\n        self._push_down(t)\n        szl\
    \ = self._size(t.outer_l)\n        szr = szl + t.inner_sz\n        if i < szl:\n\
    \            tl, tr = self._split_outer(t.outer_l, i)\n            t.outer_l =\
    \ tr\n            self._update(t)\n            return tl, t\n        elif szr\
    \ <= i:\n            tl, tr = self._split_outer(t.outer_r, i - szr)\n        \
    \    t.outer_r = tl\n            self._update(t)\n            return t, tr\n \
    \       else:\n            tmp_l, tmp_r = t.outer_l, t.outer_r\n            t.outer_l\
    \ = t.outer_r = None\n            t1, t2 = self._split_inner(t, i - szl)\n   \
    \         tl = self._merge_outer(tmp_l, t1)\n            tr = self._merge_outer(t2,\
    \ tmp_r)\n            return tl, tr\n\n    def _split_range_outer(self, t: S,\
    \ l: int, r: int) -> tuple[S, S, S]:\n        tl, tr = self._split_outer(t, l)\n\
    \        trl, trr = self._split_outer(tr, r - l)\n        return tl, trl, trr\n\
    \n    def _split_inner(self, t: S, i: int) -> tuple[S, S]:\n        if not t:\n\
    \            return None, None\n        self._push_down(t)\n        szl = self._size(t.inner_l)\n\
    \        if i <= szl:\n            tl, tr = self._split_inner(t.inner_l, i)\n\
    \            t.inner_l = tr\n            self._update(t)\n            return tl,\
    \ t\n        else:\n            tl, tr = self._split_inner(t.inner_r, i - szl\
    \ - 1)\n            t.inner_r = tl\n            self._update(t)\n            return\
    \ t, tr\n\n    def _cut_outer(self, t: S, i: int) -> tuple[S, S, S]:\n       \
    \ if not t:\n            return None, None, None\n        self._push_down(t)\n\
    \        szl = self._size(t.outer_l)\n        szr = szl + t.inner_sz\n       \
    \ if i < szl:\n            tl, tm, tr = self._cut_outer(t.outer_l, i)\n      \
    \      t.outer_l = tr\n            self._update(t)\n            return tl, tm,\
    \ t\n        elif szr <= i:\n            tl, tm, tr = self._cut_outer(t.outer_r,\
    \ i - szr)\n            t.outer_r = tl\n            self._update(t)\n        \
    \    return t, tm, tr\n        else:\n            tmp_l, tmp_r = t.outer_l, t.outer_r\n\
    \            t.outer_l = t.outer_r = None\n            tl, tm, tr = self._cut_inner(t,\
    \ i - szl)\n            tl = self._merge_outer(tmp_l, tl)\n            tr = self._merge_outer(tr,\
    \ tmp_r)\n            return tl, tm, tr\n\n    def _cut_inner(self, t: S, i: int)\
    \ -> tuple[S, S, S]:\n        if not t:\n            return None, None, None\n\
    \        self._push_down(t)\n        szl = self._size(t.inner_l)\n        if i\
    \ < szl:\n            tl, tm, tr = self._cut_inner(t.inner_l, i)\n           \
    \ t.inner_l = tr\n            self._update(t)\n            return tl, tm, t\n\
    \        elif i == szl:\n            res = t.inner_l, t, t.inner_r\n         \
    \   t.inner_l = t.inner_r = None\n            self._update(t)\n            return\
    \ res\n        else:\n            tl, tm, tr = self._cut_inner(t.inner_r, i -\
    \ szl - 1)\n            t.inner_r = tl\n            self._update(t)\n        \
    \    return t, tm, tr\n\n    def _query_range_outer(self, t: S, l: int, r: int)\
    \ -> T:\n        if not t:\n            return self.e\n        if l == 0 and r\
    \ == t.sz:\n            return t.sum\n        self._push_down(t)\n        szl\
    \ = self._size(t.outer_l)\n        szr = szl + t.inner_sz\n        left_q = right_q\
    \ = self.e\n        if l < szl:\n            if r <= szl:\n                return\
    \ self._query_range_outer(t.outer_l, l, r)\n            left_q = self._query_range_outer(t.outer_l,\
    \ l, szl)\n            l = szl\n        if szr < r:\n            if szr <= l:\n\
    \                return self._query_range_outer(t.outer_r, l - szr, r - szr)\n\
    \            right_q = self._query_range_outer(t.outer_r, 0, r - szr)\n      \
    \      r = szr\n        res = self.e if l == r else self._query_range_inner(t,\
    \ l - szl, r - szl)\n        res = self.op(left_q, res)\n        res = self.op(res,\
    \ right_q)\n        return res\n\n    def _query_range_inner(self, t: S, l: int,\
    \ r: int) -> T:\n        if not t:\n            return self.e\n        if l ==\
    \ 0 and r == t.sz:\n            return t.sum\n        self._push_down(t)\n   \
    \     szl = self._size(t.inner_l)\n        szr = szl + 1\n        left_q = right_q\
    \ = self.e\n        if l < szl:\n            if r <= szl:\n                return\
    \ self._query_range_inner(t.inner_l, l, r)\n            left_q = self._query_range_inner(t.inner_l,\
    \ l, szl)\n            l = szl\n        if szr < r:\n            if szr <= l:\n\
    \                return self._query_range_inner(t.inner_r, l - szr, r - szr)\n\
    \            right_q = self._query_range_inner(t.inner_r, 0, r - szr)\n      \
    \      r = szr\n        res = self.e if l == r else t.val\n        res = self.op(left_q,\
    \ res)\n        res = self.op(res, right_q)\n        return res\n\n    def _enumerate_outer(self,\
    \ t: S, res: list[tuple[int, T]]) -> None:\n        if not t:\n            return\n\
    \        self._push_down(t)\n        if t.outer_l:\n            self._enumerate_outer(t.outer_l,\
    \ res)\n        self._enumerate_inner(t, res)\n        if t.outer_r:\n       \
    \     self._enumerate_outer(t.outer_r, res)\n\n    def _enumerate_inner(self,\
    \ t: S, res: list[tuple[int, T]]) -> None:\n        if not t:\n            return\n\
    \        self._push_down(t)\n        if t.inner_l:\n            self._enumerate_inner(t.inner_l,\
    \ res)\n        res.append((t.key, t.val))\n        if t.inner_r:\n          \
    \  self._enumerate_inner(t.inner_r, res)\n\n    def _sort_inner(self, t: S) ->\
    \ S:\n        if not t:\n            return None\n        tl, tr = t.outer_l,\
    \ t.outer_r\n        t.outer_l = t.outer_r = None\n        self._push_down(t)\n\
    \        if (t.inner_l and t.key < t.inner_l.kmax) or (\n            t.inner_r\
    \ and t.inner_r.kmin < t.key\n        ):\n            self._toggle(t)\n      \
    \  res = self._merge_compress(self._sort_inner(tl), t)\n        res = self._merge_compress(res,\
    \ self._sort_inner(tr))\n        return res\n\n    def set(self, i: int, key:\
    \ int, value: T) -> None:\n        tl, tm, tr = self._cut_outer(self.root, i)\n\
    \        tm.key = key\n        tm.val = value\n        self._update(tm)\n    \
    \    self.root = self._merge_outer(tl, self._merge_outer(tm, tr))\n\n    def prod(self,\
    \ l: int, r: int) -> T:\n        if l == r:\n            return self.e\n     \
    \   return self._query_range_outer(self.root, l, r)\n\n    def prod_all(self)\
    \ -> T:\n        return self.root.sum\n\n    def sort(self, l: int, r: int, descending:\
    \ bool = False) -> None:\n        if l == r:\n            return\n        tl,\
    \ tm, tr = self._split_range_outer(self.root, l, r)\n        tm = self._sort_inner(tm)\n\
    \        if descending:\n            self._toggle(tm)\n        self.root = self._merge_outer(tl,\
    \ self._merge_outer(tm, tr))\n\n    def tolist(self):\n        res = []\n    \
    \    self._enumerate_outer(self.root, res)\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/sortable_segtree.py
  requiredBy: []
  timestamp: '2024-08-29 22:20:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
documentation_of: data_structure/segtree/sortable_segtree.py
layout: document
title: "\uFF11\u70B9\u66F4\u65B0\u30FB\u533A\u9593\u30BD\u30FC\u30C8\u30BB\u30B0\u30E1\
  \u30F3\u30C8\u6728"
---
