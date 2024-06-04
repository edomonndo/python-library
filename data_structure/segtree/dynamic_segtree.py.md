---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/arc008d_dyn_segtree.test.py
    title: test/atcoder/arc008d_dyn_segtree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
    title: test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import TypeVar, Callable\n\nT = TypeVar(\"T\")\n\n\nclass SegtreeNode:\n\
    \    def __init__(self, i, value: T):\n        self.idx = i\n        self.value\
    \ = value\n        self.product = value\n        self.p = None\n        self.l\
    \ = None\n        self.r = None\n\n\nclass DynamicSegtree:\n    def __init__(self,\
    \ n: int, op: Callable[[T, T], T], e: T):\n        self.root = SegtreeNode(0,\
    \ e)\n        self.n = n\n        self.op = op\n        self.e = e\n\n    def\
    \ _update(self, cur: SegtreeNode):\n        l, r, op = cur.l, cur.r, self.op\n\
    \        res = cur.value\n        if l is not None:\n            res = op(l.product,\
    \ res)\n        if r is not None:\n            res = op(res, r.product)\n    \
    \    cur.product = res\n\n    def set(self, i: int, value: T) -> None:\n     \
    \   assert 0 <= i < self.n\n        stack = [(self.root, ~0, self.n), (self.root,\
    \ 0, self.n)]\n        while stack:\n            cur, l, r = stack.pop()\n   \
    \         if l >= 0:\n                if cur is None:\n                    cur\
    \ = SegtreeNode(i, value)\n                    continue\n                if cur.idx\
    \ == i:\n                    cur.value = value\n                    continue\n\
    \                m = (l + r) >> 1\n                if i < m:\n               \
    \     if cur.idx < i:\n                        cur.idx, i = i, cur.idx\n     \
    \                   cur.value, value = value, cur.value\n                    if\
    \ cur.l is None:\n                        cur.l = SegtreeNode(i, value)\n    \
    \                stack += [(cur.l, ~l, m), (cur.l, l, m)]\n                else:\n\
    \                    if i < cur.idx:\n                        i, cur.idx = cur.idx,\
    \ i\n                        cur.value, value = value, cur.value\n           \
    \         if cur.r is None:\n                        cur.r = SegtreeNode(i, value)\n\
    \                    stack += [(cur.r, ~m, r), (cur.r, m, r)]\n            else:\n\
    \                self._update(cur)\n        return\n\n    __setitem__ = set\n\n\
    \    def get(self, i: int) -> T:\n        assert 0 <= i < self.n\n        stack\
    \ = [(self.root, 0, self.n)]\n        while stack:\n            cur, l, r = stack.pop()\n\
    \            if cur is None:\n                return self.e\n            if cur.idx\
    \ == i:\n                return cur.value\n            m = (l + r) >> 1\n    \
    \        if i < m:\n                stack.append((cur.l, l, m))\n            else:\n\
    \                stack.append((cur.r, m, r))\n\n    __getitem__ = get\n\n    def\
    \ prod(self, l: int, r: int) -> T:\n        assert 0 <= l < r and r <= self.n\n\
    \        stack = [(self.root, 0, self.n)]\n        res = self.e\n        while\
    \ stack:\n            cur, a, b = stack.pop()\n            if cur is None or b\
    \ <= l or r <= a:\n                continue\n            if l <= a and b <= r:\n\
    \                res = self.op(res, cur.product)\n                continue\n \
    \           if l <= cur.idx < r:\n                res = self.op(res, cur.value)\n\
    \            c = (a + b) >> 1\n            stack += [(cur.l, a, c), (cur.r, c,\
    \ b)]\n        return res\n\n    def all_prod(self):\n        return self.root.product\
    \ if self.root else self.e\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segtree/dynamic_segtree.py
  requiredBy: []
  timestamp: '2024-05-30 15:25:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/static_rmq_dyn_segtree.test.py
  - test/atcoder/arc008d_dyn_segtree.test.py
documentation_of: data_structure/segtree/dynamic_segtree.py
layout: document
title: "\u52D5\u7684\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dynamic Segment Tree)"
---
