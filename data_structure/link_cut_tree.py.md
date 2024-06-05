---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
    title: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
    title: test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\n\nclass LinkCutTree:\n\
    \    def __init__(self, op: Callable[[T, T], T], e: T, arr: list[T]):\n      \
    \  self.op = op\n        self.e = e\n        self.n = n = len(arr)\n        self.ptr\
    \ = [-1] * (n << 2)  # l, r, p, rev\n        for i in range(n):\n            self.ptr[i\
    \ << 2 | 3] = 0\n        self.val = arr[:]\n        self.sum = [e] * (n + 1)\n\
    \        self.rev = [e] * (n + 1)\n\n    def __toggle(self, v: int) -> None:\n\
    \        if v == -1:\n            return\n        sum_, rev, ptr = self.sum, self.rev,\
    \ self.ptr\n        sum_[v], rev[v] = rev[v], sum_[v]\n        l = v << 2\n  \
    \      r, rv = l + 1, l + 3\n        ptr[l], ptr[r] = ptr[r], ptr[l]\n       \
    \ ptr[rv] ^= 1\n\n    def __push(self, v: int) -> None:\n        ptr = self.ptr\n\
    \        l = v << 2\n        rv = l + 3\n        if v == -1 or not ptr[rv]:\n\
    \            return\n        r = l + 1\n        self.__toggle(ptr[l])\n      \
    \  self.__toggle(ptr[r])\n        ptr[rv] = 0\n\n    def __update(self, v: int)\
    \ -> None:\n        sum_, op, ptr, val, rev = self.sum, self.op, self.ptr, self.val,\
    \ self.rev\n        l = v << 2\n        r = l + 1\n        lp, rp = ptr[l], ptr[r]\n\
    \        sum_[v] = op(op(sum_[lp], val[v]), sum_[rp])\n        rev[v] = op(op(rev[rp],\
    \ val[v]), rev[lp])\n\n    def __state(self, v: int) -> int:\n        ptr = self.ptr\n\
    \        p = ptr[v << 2 | 2]\n        pl = p << 2\n        if ptr[pl] == v:\n\
    \            return 1\n        elif ptr[pl | 1] == v:\n            return -1\n\
    \        else:\n            return 0\n\n    def __rotate(self, v: int) -> None:\n\
    \        s = self.__state(v)\n        if s == 0:\n            return\n       \
    \ ptr = self.ptr\n        p = ptr[v << 2 | 2]\n        pp = ptr[p << 2 | 2]\n\
    \        t = self.__state(p)\n        if s == 1:\n            r = ptr[v << 2 |\
    \ 1]\n            ptr[v << 2 | 1] = p\n            ptr[p << 2 | 0] = r\n     \
    \       if r != -1:\n                ptr[r << 2 | 2] = p\n        else:\n    \
    \        l = ptr[v << 2 | 0]\n            ptr[v << 2 | 0] = p\n            ptr[p\
    \ << 2 | 1] = l\n            if l != -1:\n                ptr[l << 2 | 2] = p\n\
    \        ptr[p << 2 | 2] = v\n        ptr[v << 2 | 2] = pp\n        self.__update(p)\n\
    \        self.__update(v)\n        if t == 0:\n            return\n        elif\
    \ t == 1:\n            ptr[pp << 2 | 0] = v\n        else:\n            ptr[pp\
    \ << 2 | 1] = v\n\n    def __splay(self, v: int) -> None:\n        ptr, push,\
    \ state, rotate = self.ptr, self.__push, self.__state, self.__rotate\n       \
    \ push(v)\n        while True:\n            s = state(v)\n            if not s:\n\
    \                break\n            p = ptr[v << 2 | 2]\n            t = state(p)\n\
    \            if t == 0:\n                push(p)\n                push(v)\n  \
    \              rotate(v)\n            elif s == t:\n                push(ptr[p\
    \ << 2 | 2])\n                push(p)\n                push(v)\n             \
    \   rotate(p)\n                rotate(v)\n            else:\n                push(ptr[p\
    \ << 2 | 2])\n                push(p)\n                push(v)\n             \
    \   rotate(v)\n                rotate(v)\n\n    def __access(self, v: int) ->\
    \ int:\n        ptr, splay, update = self.ptr, self.__splay, self.__update\n \
    \       c = v\n        r = -1\n        while v != -1:\n            splay(v)\n\
    \            ptr[v << 2 | 1] = r\n            update(v)\n            r = v\n \
    \           v = ptr[v << 2 | 2]\n        splay(c)\n        return r\n\n    def\
    \ link(self, v: int, p: int) -> None:\n        \"\"\"\u9802\u70B9v,p\u3092,p\u3092\
    v\u306E\u89AA\u306B\u3057\u3066\u9023\u7D50\u3059\u308B. \u3053\u306E\u3068\u304D\
    v\u304C\u6839\u3067\u3042\u308B\u5FC5\u8981\u304C\u3042\u308B\"\"\"\n        ptr,\
    \ access, update = self.ptr, self.__access, self.__update\n        # self.evert(v)\n\
    \        access(v)\n        access(p)\n        ptr[v << 2 | 2] = p\n        ptr[p\
    \ << 2 | 1] = v\n        update(p)\n\n    def cut(self, v: int) -> None:\n   \
    \     \"\"\"\u9802\u70B9v\u3068\u305D\u306E\u89AA\u30CE\u30FC\u30C9\u3068\u306E\
    \u8FBA\u3092\u53D6\u308A\u9664\u304F. v\u304C\u305D\u306E\u90E8\u5206\u6728\u306E\
    \u6839\u3068\u306A\u308B.\"\"\"\n        ptr, access, update = self.ptr, self.__access,\
    \ self.__update\n        access(v)\n        ptr[ptr[v << 2 | 0] << 2 | 2] = -1\n\
    \        ptr[v << 2 | 0] = -1\n        update(v)\n\n    def root(self, v: int)\
    \ -> int:\n        \"\"\"\u9802\u70B9v\u3092\u542B\u3080\u6728\u306E\u6839\u3092\
    \u8FD4\u3059.\"\"\"\n        ptr, access = self.ptr, self.__access\n        access(v)\n\
    \        while ptr[v << 2 | 0] != -1:\n            v = ptr[v << 2 | 0]\n     \
    \   return v\n\n    def parent(self, v: int) -> int:\n        \"\"\"\u9802\u70B9\
    v\u306E\u89AA\u3092\u8FD4\u3059.\"\"\"\n        ptr, access = self.ptr, self.__access\n\
    \        access(v)\n        v = ptr[v << 2 | 0]\n        while ptr[v << 2 | 1]\
    \ != -1:\n            v = ptr[v << 2 | 1]\n        return v\n\n    def evert(self,\
    \ v: int) -> None:\n        \"\"\"\u9802\u70B9v\u3092v\u3092\u542B\u3080\u6728\
    \u306E\u6839\u306B\u3059\u308B.\"\"\"\n        self.__access(v)\n        self.__toggle(v)\n\
    \        self.__push(v)\n\n    def set(self, v: int, x: T) -> None:\n        \"\
    \"\"\u9802\u70B9v\u306E\u5024\u3092x\u306B\u3059\u308B.\"\"\"\n        self.__access(v)\n\
    \        self.val[v] = x\n\n    def add(self, v: int, x: T) -> None:\n       \
    \ \"\"\"\u9802\u70B9v\u306E\u5024\u306Bx\u3092\u52A0\u7B97\u3059\u308B.\"\"\"\n\
    \        self.__access(v)\n        self.val[v] += x\n\n    def path_query(self,\
    \ u: int, v: int) -> T:\n        \"\"\"\u9802\u70B9u,v\u9593\u306E\u30D1\u30B9\
    \u30AF\u30A8\u30EA\u3092\u8FD4\u3059. \u305F\u3060\u3057,u\u3068v\u306F\u9023\u7D50\
    \u3067\u3042\u308B\u5FC5\u8981\u304C\u3042\u308B.\"\"\"\n        self.evert(u)\n\
    \        self.__access(v)\n        return self.sum[v]\n\n    def lca(self, u:\
    \ int, v: int) -> int:\n        \"\"\"\u9802\u70B9u,v\u306ELCA\u3092\u8FD4\u3059\
    . Not verified.\"\"\"\n        assert self.root(u) == self.root(v)\n        self.__access(u)\n\
    \        return self.__access(v)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/link_cut_tree.py
  requiredBy: []
  timestamp: '2024-06-05 17:57:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
  - test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
documentation_of: data_structure/link_cut_tree.py
layout: document
title: Link Cut Tree
---
