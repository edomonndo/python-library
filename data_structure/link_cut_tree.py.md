---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
    title: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
  - icon: ':x:'
    path: test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
    title: test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LinkCutTree:\n    def __init__(self, op, e, arr: list[int]):\n    \
    \    self.op = op\n        self.e = e\n        self.n = n = len(arr)\n       \
    \ self.ptr = [-1] * (n << 2)  # l, r, p, rev\n        for i in range(n):\n   \
    \         self.ptr[i << 2 | 3] = 0\n        self.val = arr[:]\n        self.sum\
    \ = [e] * (n + 1)\n        self.rev = [e] * (n + 1)\n\n    def _toggle(self, u:\
    \ int):\n        if u == -1:\n            return\n        self.sum[u], self.rev[u]\
    \ = self.rev[u], self.sum[u]\n        self.ptr[u << 2 | 0], self.ptr[u << 2 |\
    \ 1] = (\n            self.ptr[u << 2 | 1],\n            self.ptr[u << 2 | 0],\n\
    \        )\n        self.ptr[u << 2 | 3] ^= 1\n\n    def _push(self, u: int):\n\
    \        if u == -1 or not self.ptr[u << 2 | 3]:\n            return\n       \
    \ self._toggle(self.ptr[u << 2 | 0])\n        self._toggle(self.ptr[u << 2 | 1])\n\
    \        self.ptr[u << 2 | 3] = 0\n\n    def _update(self, u: int):\n        self.sum[u]\
    \ = self.op(\n            self.op(self.sum[self.ptr[u << 2 | 0]], self.val[u]),\n\
    \            self.sum[self.ptr[u << 2 | 1]],\n        )\n        self.rev[u] =\
    \ self.op(\n            self.op(self.rev[self.ptr[u << 2 | 1]], self.val[u]),\n\
    \            self.rev[self.ptr[u << 2 | 0]],\n        )\n\n    def _state(self,\
    \ u: int):\n        p = self.ptr[u << 2 | 2]\n        if self.ptr[p << 2 | 0]\
    \ == u:\n            return 1\n        elif self.ptr[p << 2 | 1] == u:\n     \
    \       return -1\n        else:\n            return 0\n\n    def _rotate(self,\
    \ u: int):\n        s = self._state(u)\n        if s == 0:\n            return\n\
    \        ptr = self.ptr\n        p = ptr[u << 2 | 2]\n        pp = ptr[p << 2\
    \ | 2]\n        t = self._state(p)\n        if s == 1:\n            r = ptr[u\
    \ << 2 | 1]\n            ptr[u << 2 | 1] = p\n            ptr[p << 2 | 0] = r\n\
    \            if r != -1:\n                ptr[r << 2 | 2] = p\n        else:\n\
    \            l = ptr[u << 2 | 0]\n            ptr[u << 2 | 0] = p\n          \
    \  ptr[p << 2 | 1] = l\n            if l != -1:\n                ptr[l << 2 |\
    \ 2] = p\n        ptr[p << 2 | 2] = u\n        ptr[u << 2 | 2] = pp\n        self._update(p)\n\
    \        self._update(u)\n        if t == 0:\n            return\n        elif\
    \ t == 1:\n            ptr[pp << 2 | 0] = u\n        else:\n            ptr[pp\
    \ << 2 | 1] = u\n\n    def _splay(self, u: int):\n        self._push(u)\n    \
    \    while True:\n            s = self._state(u)\n            if not s:\n    \
    \            break\n            p = self.ptr[u << 2 | 2]\n            t = self._state(p)\n\
    \            if t == 0:\n                self._push(p)\n                self._push(u)\n\
    \                self._rotate(u)\n            elif s == t:\n                self._push(self.ptr[p\
    \ << 2 | 2])\n                self._push(p)\n                self._push(u)\n \
    \               self._rotate(p)\n                self._rotate(u)\n           \
    \ else:\n                self._push(self.ptr[p << 2 | 2])\n                self._push(p)\n\
    \                self._push(u)\n                self._rotate(u)\n            \
    \    self._rotate(u)\n\n    def _access(self, u: int):\n        c = u\n      \
    \  r = -1\n        while u != -1:\n            self._splay(u)\n            self.ptr[u\
    \ << 2 | 1] = r\n            self._update(u)\n            r = u\n            u\
    \ = self.ptr[u << 2 | 2]\n        self._splay(c)\n\n    def link(self, u: int,\
    \ v: int) -> None:\n        self._access(u)\n        self._access(v)\n       \
    \ self.ptr[u << 2 | 2] = v\n        self.ptr[v << 2 | 1] = u\n        self._update(v)\n\
    \n    def cut(self, u: int) -> None:\n        self._access(u)\n        self.ptr[self.ptr[u\
    \ << 2 | 0] << 2 | 2] = -1\n        self.ptr[u << 2 | 0] = -1\n        self._update(u)\n\
    \n    def root(self, u: int) -> int:\n        self._access(u)\n        while self.ptr[u\
    \ << 2 | 0] != -1:\n            u = self.ptr[u << 2 | 0]\n        return u\n\n\
    \    def evert(self, u: int) -> None:\n        self._access(u)\n        self._toggle(u)\n\
    \        self._push(u)\n\n    def set(self, u: int, x: int) -> None:\n       \
    \ self._access(u)\n        self.val[u] = x\n\n    def add(self, u: int, x: int)\
    \ -> None:\n        self._access(u)\n        self.val[u] += x\n\n    def path_query(self,\
    \ u: int, v: int) -> int:\n        self.evert(u)\n        self._access(v)\n  \
    \      return self.sum[v]\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/link_cut_tree.py
  requiredBy: []
  timestamp: '2024-02-26 12:20:09+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
  - test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
documentation_of: data_structure/link_cut_tree.py
layout: document
redirect_from:
- /library/data_structure/link_cut_tree.py
- /library/data_structure/link_cut_tree.py.html
title: data_structure/link_cut_tree.py
---
