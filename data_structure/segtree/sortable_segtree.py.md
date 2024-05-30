---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
    title: test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import *\nfrom typing import TypeVar\n\nT = TypeVar(\"T\")\n\"\
    \"\"\nGlobal variables\nop: Callable[[T,T],T]\ne_: T\ntoggle: Callable[[T],T]\n\
    \"\"\"\n\n\ndef op(x: T, y: T) -> T:\n    pass\n\n\ne_ = None\n\n\ndef toggle(x:\
    \ T) -> T:\n    pass\n\n\ndef xor64():\n    x = 88172645463325252\n    while True:\n\
    \        x = x ^ ((x << 7) & 0xFFFFFFFF)\n        x = x ^ (x >> 9)\n        yield\
    \ x & 0xFFFFFFFF\n\n\nrand = xor64()\n\n\nclass SegNode:\n    def __init__(self,\
    \ key: int, value: T):\n        self.key = self.kmin = self.kmax = key\n     \
    \   self.val = self.sum = value\n        self.inner_l = self.inner_r = None\n\
    \        self.outer_l = self.outer_r = None\n        self.flip = 0\n        self.sz\
    \ = self.inner_sz = 1\n        self.pri = next(rand)\n\n    def __str__(self):\n\
    \        return f\"<SegNode(key={self.key}, val={self.val}, sum={self.sum}, inner=({type(self.inner_l).__name__},{type(self.inner_r).__name__}),\
    \ outer=({type(self.outer_l).__name__},{type(self.outer_r).__name__}), flip={self.flip})>\"\
    \n\n    def toggle(self) -> None:\n        self.inner_l, self.inner_r = self.inner_r,\
    \ self.inner_l\n        self.outer_l, self.outer_r = self.outer_r, self.outer_l\n\
    \        self.sum = toggle(self.sum)\n        self.flip ^= 1\n\n    def push_down(self)\
    \ -> None:\n        if not self.flip:\n            return\n        for SegNode\
    \ in [self.inner_l, self.inner_r, self.outer_l, self.outer_r]:\n            if\
    \ SegNode:\n                SegNode.toggle()\n        self.flip = 0\n\n    def\
    \ update(self) -> None:\n        self.sz, self.inner_sz = 0, 1\n        self.kmin\
    \ = self.kmax = self.key\n        self.sum = e_\n        if self.outer_l:\n  \
    \          self.sum = self.outer_l.sum\n            self.sz += self.outer_l.sz\n\
    \        if self.inner_l:\n            self.inner_sz += self.inner_l.inner_sz\n\
    \            self.sum = op(self.sum, self.inner_l.sum)\n            self.kmin\
    \ = min(self.kmin, self.inner_l.kmin)\n            self.kmax = max(self.kmax,\
    \ self.inner_l.kmax)\n        self.sum = op(self.sum, self.val)\n        if self.inner_r:\n\
    \            self.inner_sz += self.inner_r.inner_sz\n            self.sum = op(self.sum,\
    \ self.inner_r.sum)\n            self.kmin = min(self.kmin, self.inner_r.kmin)\n\
    \            self.kmax = max(self.kmax, self.inner_r.kmax)\n        if self.outer_r:\n\
    \            self.sum = op(self.sum, self.outer_r.sum)\n            self.sz +=\
    \ self.outer_r.sz\n        self.sz += self.inner_sz\n\n\nclass SortableSegtree:\n\
    \    def __init__(self, V: list[T]):\n        self.V = V\n        self.root =\
    \ self._build(0, len(V))\n\n    def _build(self, l: int, r: int) -> SegNode:\n\
    \        m = (l + r) >> 1\n        t = SegNode(self.V[m][0], self.V[m][1])\n \
    \       t.outer_l = self._build(l, m) if l < m else None\n        t.outer_r =\
    \ self._build(m + 1, r) if m + 1 < r else None\n        self._pri_satisfy(t)\n\
    \        t.update()\n        return t\n\n    def _pri_satisfy(self, t: SegNode)\
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
    \    def _size(t: SegNode) -> int:\n        return t.sz if t else 0\n\n    @classmethod\n\
    \    def _merge_outer(cls, l: SegNode, r: SegNode) -> SegNode:\n        if not\
    \ l:\n            return r\n        if not r:\n            return l\n        l.push_down()\n\
    \        r.push_down()\n        if l.pri > r.pri:\n            l.outer_r = cls._merge_outer(l.outer_r,\
    \ r)\n            l.update()\n            return l\n        else:\n          \
    \  r.outer_l = cls._merge_outer(l, r.outer_l)\n            r.update()\n      \
    \      return r\n\n    @classmethod\n    def _merge_compress(cls, l: SegNode,\
    \ r: SegNode) -> SegNode:\n        if not l:\n            return r\n        if\
    \ not r:\n            return l\n        l.push_down()\n        r.push_down()\n\
    \        if l.pri < r.pri:\n            l, r = r, l\n        if l.key < r.kmin:\n\
    \            l.inner_r = cls._merge_compress(l.inner_r, r)\n        elif r.kmax\
    \ < l.key:\n            l.inner_l = cls._merge_compress(l.inner_l, r)\n      \
    \  else:\n            rl, rr = cls._split_key(r, l.key)\n            l.inner_l\
    \ = cls._merge_compress(l.inner_l, rl)\n            l.inner_r = cls._merge_compress(l.inner_r,\
    \ rr)\n        l.update()\n        return l\n\n    @classmethod\n    def _split_key(cls,\
    \ t: SegNode, key: int) -> tuple[SegNode, SegNode]:\n        if not t:\n     \
    \       return None, None\n        if key < t.kmin:\n            return None,\
    \ t\n        if t.kmax <= key:\n            return t, None\n        t.push_down()\n\
    \        if key < t.key:\n            tl, tr = cls._split_key(t.inner_l, key)\n\
    \            t.inner_l = tr\n            t.update()\n            return tl, t\n\
    \        else:\n            tl, tr = cls._split_key(t.inner_r, key)\n        \
    \    t.inner_r = tl\n            t.update()\n            return t, tr\n\n    @classmethod\n\
    \    def _split_outer(cls, t: SegNode, i: int) -> tuple[SegNode, SegNode]:\n \
    \       if not t:\n            return None, None\n        t.push_down()\n    \
    \    szl = cls._size(t.outer_l)\n        szr = szl + t.inner_sz\n        if i\
    \ < szl:\n            tl, tr = cls._split_outer(t.outer_l, i)\n            t.outer_l\
    \ = tr\n            t.update()\n            return tl, t\n        elif szr <=\
    \ i:\n            tl, tr = cls._split_outer(t.outer_r, i - szr)\n            t.outer_r\
    \ = tl\n            t.update()\n            return t, tr\n        else:\n    \
    \        tmp_l, tmp_r = t.outer_l, t.outer_r\n            t.outer_l = t.outer_r\
    \ = None\n            t1, t2 = cls._split_inner(t, i - szl)\n            tl =\
    \ cls._merge_outer(tmp_l, t1)\n            tr = cls._merge_outer(t2, tmp_r)\n\
    \            return tl, tr\n\n    @classmethod\n    def _split_range_outer(\n\
    \        cls, t: SegNode, l: int, r: int\n    ) -> tuple[SegNode, SegNode, SegNode]:\n\
    \        tl, tr = cls._split_outer(t, l)\n        trl, trr = cls._split_outer(tr,\
    \ r - l)\n        return tl, trl, trr\n\n    @classmethod\n    def _split_inner(cls,\
    \ t: SegNode, i: int) -> tuple[SegNode, SegNode]:\n        if not t:\n       \
    \     return None, None\n        t.push_down()\n        szl = cls._size(t.inner_l)\n\
    \        if i <= szl:\n            tl, tr = cls._split_inner(t.inner_l, i)\n \
    \           t.inner_l = tr\n            t.update()\n            return tl, t\n\
    \        else:\n            tl, tr = cls._split_inner(t.inner_r, i - szl - 1)\n\
    \            t.inner_r = tl\n            t.update()\n            return t, tr\n\
    \n    @classmethod\n    def _cut_outer(cls, t: SegNode, i: int) -> tuple[SegNode,\
    \ SegNode, SegNode]:\n        if not t:\n            return None, None, None\n\
    \        t.push_down()\n        szl = cls._size(t.outer_l)\n        szr = szl\
    \ + t.inner_sz\n        if i < szl:\n            tl, tm, tr = cls._cut_outer(t.outer_l,\
    \ i)\n            t.outer_l = tr\n            t.update()\n            return tl,\
    \ tm, t\n        elif szr <= i:\n            tl, tm, tr = cls._cut_outer(t.outer_r,\
    \ i - szr)\n            t.outer_r = tl\n            t.update()\n            return\
    \ t, tm, tr\n        else:\n            tmp_l, tmp_r = t.outer_l, t.outer_r\n\
    \            t.outer_l = t.outer_r = None\n            tl, tm, tr = cls._cut_inner(t,\
    \ i - szl)\n            tl = cls._merge_outer(tmp_l, tl)\n            tr = cls._merge_outer(tr,\
    \ tmp_r)\n            return tl, tm, tr\n\n    @classmethod\n    def _cut_inner(cls,\
    \ t: SegNode, i: int) -> tuple[SegNode, SegNode, SegNode]:\n        if not t:\n\
    \            return None, None, None\n        t.push_down()\n        szl = cls._size(t.inner_l)\n\
    \        if i < szl:\n            tl, tm, tr = cls._cut_inner(t.inner_l, i)\n\
    \            t.inner_l = tr\n            t.update()\n            return tl, tm,\
    \ t\n        elif i == szl:\n            res = t.inner_l, t, t.inner_r\n     \
    \       t.inner_l = t.inner_r = None\n            t.update()\n            return\
    \ res\n        else:\n            tl, tm, tr = cls._cut_inner(t.inner_r, i - szl\
    \ - 1)\n            t.inner_r = tl\n            t.update()\n            return\
    \ t, tm, tr\n\n    @classmethod\n    def _query_range_outer(cls, t: SegNode, l:\
    \ int, r: int) -> T:\n        if not t:\n            return e_\n        if l ==\
    \ 0 and r == t.sz:\n            return t.sum\n        t.push_down()\n        szl\
    \ = cls._size(t.outer_l)\n        szr = szl + t.inner_sz\n        left_q = right_q\
    \ = e_\n        if l < szl:\n            if r <= szl:\n                return\
    \ cls._query_range_outer(t.outer_l, l, r)\n            left_q = cls._query_range_outer(t.outer_l,\
    \ l, szl)\n            l = szl\n        if szr < r:\n            if szr <= l:\n\
    \                return cls._query_range_outer(t.outer_r, l - szr, r - szr)\n\
    \            right_q = cls._query_range_outer(t.outer_r, 0, r - szr)\n       \
    \     r = szr\n        res = e_ if l == r else cls._query_range_inner(t, l - szl,\
    \ r - szl)\n        res = op(left_q, res)\n        res = op(res, right_q)\n  \
    \      return res\n\n    @classmethod\n    def _query_range_inner(cls, t: SegNode,\
    \ l: int, r: int) -> T:\n        if not t:\n            return e_\n        if\
    \ l == 0 and r == t.sz:\n            return t.sum\n        t.push_down()\n   \
    \     szl = cls._size(t.inner_l)\n        szr = szl + 1\n        left_q = right_q\
    \ = e_\n        if l < szl:\n            if r <= szl:\n                return\
    \ cls._query_range_inner(t.inner_l, l, r)\n            left_q = cls._query_range_inner(t.inner_l,\
    \ l, szl)\n            l = szl\n        if szr < r:\n            if szr <= l:\n\
    \                return cls._query_range_inner(t.inner_r, l - szr, r - szr)\n\
    \            right_q = cls._query_range_inner(t.inner_r, 0, r - szr)\n       \
    \     r = szr\n        res = e_ if l == r else t.val\n        res = op(left_q,\
    \ res)\n        res = op(res, right_q)\n        return res\n\n    @classmethod\n\
    \    def _enumerate_outer(cls, t: SegNode, res: list[tuple[int, T]]) -> None:\n\
    \        if not t:\n            return\n        t.push_down()\n        if t.outer_l:\n\
    \            cls._enumerate_outer(t.outer_l, res)\n        cls.enumerate_inner(t,\
    \ res)\n        if t.outer_r:\n            cls._enumerate_outer(t.outer_r, res)\n\
    \n    @classmethod\n    def _enumerate_inner(cls, t: SegNode, res: list[tuple[int,\
    \ T]]) -> None:\n        if not t:\n            return\n        t.push_down()\n\
    \        if t.inner_l:\n            cls._enumerate_inner(t.inner_l, res)\n   \
    \     res.append((t.key, t.val))\n        if t.inner_r:\n            cls._enumerate_inner(t.inner_r,\
    \ res)\n\n    @classmethod\n    def _sort_inner(cls, t: SegNode) -> SegNode:\n\
    \        if not t:\n            return None\n        tl, tr = t.outer_l, t.outer_r\n\
    \        t.outer_l = t.outer_r = None\n        t.push_down()\n        if (t.inner_l\
    \ and t.key < t.inner_l.kmax) or (\n            t.inner_r and t.inner_r.kmin <\
    \ t.key\n        ):\n            t.toggle()\n        res = cls._merge_compress(cls._sort_inner(tl),\
    \ t)\n        res = cls._merge_compress(res, cls._sort_inner(tr))\n        return\
    \ res\n\n    def set(self, i: int, key: int, value: T) -> None:\n        tl, tm,\
    \ tr = self._cut_outer(self.root, i)\n        tm.key = key\n        tm.val = value\n\
    \        tm.update()\n        self.root = self._merge_outer(tl, self._merge_outer(tm,\
    \ tr))\n\n    def prod(self, l: int, r: int) -> T:\n        if l == r:\n     \
    \       return e_\n        return self._query_range_outer(self.root, l, r)\n\n\
    \    def prod_all(self) -> T:\n        return self.root.sum\n\n    def sort(self,\
    \ l: int, r: int, descending: bool = False) -> None:\n        if l == r:\n   \
    \         return\n        tl, tm, tr = self._split_range_outer(self.root, l, r)\n\
    \        tm = self._sort_inner(tm)\n        if descending:\n            tm.toggle()\n\
    \        self.root = self._merge_outer(tl, self._merge_outer(tm, tr))\n\n    def\
    \ to_list(self):\n        res = []\n        self._enumerate_outer(self.root, res)\n\
    \        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/sortable_segtree.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/data_structure/point_set_range_sort_range_composite.test.py
documentation_of: data_structure/segtree/sortable_segtree.py
layout: document
redirect_from:
- /library/data_structure/segtree/sortable_segtree.py
- /library/data_structure/segtree/sortable_segtree.py.html
title: data_structure/segtree/sortable_segtree.py
---
