---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py
    title: Dynamic Sequence Range Affine Range Sum (Treap)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/range_reverse_range_sum_treap.test.py
    title: Range Reverse Range Sum (Treap)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nS = TypeVar(\"S\")\nF = TypeVar(\"\
    F\")\n\n\nclass ImplicitTreap:\n\n    def __init__(\n        self,\n        op:\
    \ Callable[[S, S], S],\n        e: S,\n        mapping: Callable[[F, S], S],\n\
    \        composition: Callable[[F, F], F],\n        id_: F,\n        arr: list[S],\n\
    \    ):\n        self.op = op\n        self.e = e\n        self.mapping = mapping\n\
    \        self.composition = composition\n        self.id = id_\n        self.rand\
    \ = self.__xor64()\n        self.__build(arr)\n\n    @staticmethod\n    def __xor64():\n\
    \        x = 88172645463325252\n        while True:\n            x = x ^ ((x <<\
    \ 7) & 0xFFFFFFFF)\n            x = x ^ (x >> 9)\n            yield x & 0xFFFFFFFF\n\
    \n    def __build(self, arr: list[S]) -> None:\n        n = len(arr)\n       \
    \ self.root = 0\n        self.val = val = [self.e] + arr\n        self.pri = pri\
    \ = [1 << 32] + [next(self.rand) for _ in range(n)]\n        self.ptr = ptr =\
    \ [0] * (n * 3 + 3)\n        self.cnt = cnt = [0] + [1] * n\n        self.cum\
    \ = cum = [self.e] * (n + 1)\n        self.lazy = [self.id] * (n + 1)\n      \
    \  op = self.op\n        par = [0] * (n + 1)\n        for i in range(2, n + 1):\n\
    \            p = i - 1\n            l = 0\n            while p and pri[i] > pri[p]:\n\
    \                pp = par[p]\n                if l:\n                    par[l]\
    \ = p\n                par[p] = i\n                l, p = p, pp\n            par[i]\
    \ = p\n        for i, p in enumerate(par):\n            if not p:\n          \
    \      self.root = i\n            elif i < p:\n                ptr[p * 3] = i\n\
    \            else:\n                ptr[p * 3 + 1] = i\n        stack = [self.root]\n\
    \        ord = []\n        while stack:\n            v = stack.pop()\n       \
    \     ord.append(v)\n            l, r = ptr[v * 3], ptr[v * 3 + 1]\n         \
    \   if l:\n                stack.append(l)\n            if r:\n              \
    \  stack.append(r)\n        for v in ord[::-1]:\n            l, r = ptr[v * 3],\
    \ ptr[v * 3 + 1]\n            cnt[v] = cnt[l] + cnt[r] + 1\n            cum[v]\
    \ = op(op(cum[l], val[v]), cum[r])\n\n    def __newnode(self, x: S) -> int:\n\
    \        idx = len(self.val)\n        self.val.append(x)\n        self.pri.append(next(self.rand))\n\
    \        self.ptr.extend([0, 0, 0])\n        self.cnt.append(1)\n        self.cum.append(self.e)\n\
    \        self.lazy.append(self.id)\n        return idx\n\n    def __push(self,\
    \ t: int) -> None:\n        ptr, lazy = self.ptr, self.lazy\n        if ptr[t\
    \ * 3 + 2]:\n            ptr[t * 3 + 2] = 0\n            l, r = ptr[t * 3], ptr[t\
    \ * 3 + 1] = ptr[t * 3 + 1], ptr[t * 3]\n            if l:\n                ptr[l\
    \ * 3 + 2] ^= 1\n            if r:\n                ptr[r * 3 + 2] ^= 1\n    \
    \    if lazy[t] != self.id:\n            l, r = ptr[t * 3], ptr[t * 3 + 1]\n \
    \           cum, val = self.cum, self.val\n            if l:\n               \
    \ lazy[l] = self.composition(lazy[t], lazy[l])\n                cum[l] = self.mapping(lazy[t],\
    \ cum[l])\n            if r:\n                lazy[r] = self.composition(lazy[t],\
    \ lazy[r])\n                cum[r] = self.mapping(lazy[t], cum[r])\n         \
    \   val[t] = self.mapping(lazy[t], val[t])\n            lazy[t] = self.id\n\n\
    \    def __update(self, t: int) -> None:\n        ptr, cnt, cum, val, op = self.ptr,\
    \ self.cnt, self.cum, self.val, self.op\n        l, r = ptr[t * 3], ptr[t * 3\
    \ + 1]\n        cnt[t] = cnt[l] + cnt[r] + 1\n        cum[t] = op(op(cum[l], val[t]),\
    \ cum[r])\n\n    def __split(self, t: int, k: int, update: bool = True) -> tuple[int,\
    \ int]:\n        ptr, cnt = self.ptr, self.cnt\n        l = r = 0\n        while\
    \ t:\n            self.__push(t)\n            p = cnt[ptr[t * 3]] + 1\n      \
    \      if k < p:\n                v, ptr[t * 3] = ptr[t * 3], r\n            \
    \    r, t = t, v\n            else:\n                v, ptr[t * 3 + 1] = ptr[t\
    \ * 3 + 1], l\n                l, t = t, v\n                k -= p\n        s\
    \ = 0\n        while l:\n            v, ptr[l * 3 + 1] = ptr[l * 3 + 1], s\n \
    \           if update:\n                self.__update(l)\n            s, l = l,\
    \ v\n        l, s = s, 0\n        while r:\n            v, ptr[r * 3] = ptr[r\
    \ * 3], s\n            if update:\n                self.__update(r)\n        \
    \    s, r = r, v\n        r = s\n        return l, r\n\n    def __merge(\n   \
    \     self, l: int, r: int, push_lt: bool = False, push_rt: bool = False\n   \
    \ ) -> int:\n        ptr, pri = self.ptr, self.pri\n        s = 0\n        while\
    \ l:\n            if push_lt:\n                self.__push(l)\n            v,\
    \ ptr[l * 3 + 1] = ptr[l * 3 + 1], s\n            s, l = l, v\n        l, s =\
    \ s, 0\n        while r:\n            if push_rt:\n                self.__push(r)\n\
    \            v, ptr[r * 3] = ptr[r * 3], s\n            s, r = r, v\n        r,\
    \ t = s, 0\n        while l or r:\n            if pri[l] < pri[r]:\n         \
    \       v, ptr[l * 3 + 1] = ptr[l * 3 + 1], t\n                self.__update(l)\n\
    \                t, l = l, v\n            else:\n                v, ptr[r * 3]\
    \ = ptr[r * 3], t\n                self.__update(r)\n                t, r = r,\
    \ v\n        return t\n\n    def size(self) -> int:\n        return self.cnt[self.root]\n\
    \n    def insert(self, p: int, x: S) -> None:\n        l, r = self.__split(self.root,\
    \ p, True)\n        self.root = self.__merge(self.__merge(l, self.__newnode(x)),\
    \ r)\n\n    def erase(self, p: int) -> None:\n        l, r = self.__split(self.root,\
    \ p + 1, True)\n        l, _ = self.__split(l, p, True)\n        self.root = self.__merge(l,\
    \ r)\n\n    def get(self, p: int) -> S:\n        t1, t2 = self.__split(self.root,\
    \ p + 1, True)\n        t1, t3 = self.__split(t1, p, True)\n        res = self.val[t3]\n\
    \        self.root = self.__merge(self.__merge(t1, t3), t2)\n        return res\n\
    \n    def reverse(self, l: int, r: int) -> None:\n        t2, t3 = self.__split(self.root,\
    \ r, True)\n        t1, t2 = self.__split(t2, l, True)\n        self.ptr[t2 *\
    \ 3 + 2] ^= 1\n        self.root = self.__merge(self.__merge(t1, t2, False, True),\
    \ t3, True, False)\n\n    def apply(self, l: int, r: int, f: F) -> None:\n   \
    \     t2, t3 = self.__split(self.root, r, True)\n        t1, t2 = self.__split(t2,\
    \ l, True)\n        self.lazy[t2] = self.composition(f, self.lazy[t2])\n     \
    \   self.root = self.__merge(self.__merge(t1, t2, False, True), t3, True, False)\n\
    \n    def prod(self, l: int, r: int) -> S:\n        t2, t3 = self.__split(self.root,\
    \ r, True)\n        t1, t2 = self.__split(t2, l, True)\n        res = self.cum[t2]\n\
    \        self.root = self.__merge(self.__merge(t1, t2), t3)\n        return res\n\
    \n    def iter(self):\n        stack = []\n        v = self.root\n        while\
    \ stack or v:\n            while v:\n                self.__push(v)\n        \
    \        stack.append(v)\n                v = self.ptr[v * 3]\n            v =\
    \ stack.pop()\n            yield self.val[v]\n            v = self.ptr[v * 3 +\
    \ 1]\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/binary_search_tree/implicit_treap.py
  requiredBy: []
  timestamp: '2024-06-07 10:09:10+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/range_reverse_range_sum_treap.test.py
  - test/library_checker/data_structure/dynamic_sequence_range_affine_range_sum_treap.test.py
documentation_of: data_structure/binary_search_tree/implicit_treap.py
layout: document
redirect_from:
- /library/data_structure/binary_search_tree/implicit_treap.py
- /library/data_structure/binary_search_tree/implicit_treap.py.html
title: data_structure/binary_search_tree/implicit_treap.py
---
