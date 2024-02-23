---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
    title: test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
  - icon: ':x:'
    path: test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
    title: test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LinkCutTree:\n    def __init__(self, op, e, arr: list[int]):\n    \
    \    self.op = op\n        self.op = e\n        self.n = n = len(arr)\n      \
    \  self.ptr = [-1] * (n << 2)  # l, r, p, rev\n        for i in range(n):\n  \
    \          self.ptr[i << 2 | 3] = 0\n        self.val = arr[:]\n        self.sum\
    \ = [e] * (n + 1)\n        self.rev = [e] * (n + 1)\n\n    def _toggle(self, u:\
    \ int):\n        if u != -1:\n            return\n        self.sum[u], self.rev[u]\
    \ = self.rev[u], self.sum[u]\n        self.ptr[u << 2 | 0], self.ptr[u << 2 |\
    \ 1] = (\n            self.ptr[u << 2 | 1],\n            self.ptr[u << 2 | 0],\n\
    \        )\n        self.ptr[u << 2 | 3] ^= 1\n\n    def _push(self, u: int):\n\
    \        if self.ptr[u << 2 | 3]:\n            self._toggle(self.ptr[u << 2 |\
    \ 0])\n            self._toggle(self.ptr[u << 2 | 1])\n            self.ptr[u\
    \ << 2 | 3] = 0\n\n    def _update(self, u: int):\n        self.sum[u] = self.op(\n\
    \            self.val[u],\n            self.op(self.sum[self.ptr[u << 2 | 0]],\
    \ self.sum[self.ptr[u << 2 | 1]]),\n        )\n        self.rev[u] = self.op(\n\
    \            self.rev[u],\n            self.op(self.rev[self.ptr[u << 2 | 0]],\
    \ self.rev[self.ptr[u << 2 | 1]]),\n        )\n\n    def _state(self, u: int):\n\
    \        par = self.ptr[u << 2 | 2]\n        if par == -1 or (self.ptr[par <<\
    \ 2 | 0] != u and self.ptr[par << 2 | 1] != u):\n            return 0\n      \
    \  elif self.ptr[par << 2 | 0] == u:\n            return 1\n        return -1\n\
    \n    def _rotate(self, u: int):\n        ptr = self.ptr\n        par = ptr[u\
    \ << 2 | 2]\n        parpar = ptr[par << 2 | 2]\n        if ptr[par << 2 | 0]\
    \ == u:\n            c = ptr[u << 2 | 1]\n            ptr[u << 2 | 1] = par\n\
    \            ptr[par << 2 | 0] = c\n        else:\n            c = ptr[u << 2\
    \ | 0]\n            ptr[u << 2 | 0] = par\n            ptr[par << 2 | 1] = c\n\
    \        if parpar != -1:\n            if ptr[parpar << 2 | 0] == par:\n     \
    \           ptr[parpar << 2 | 0] = u\n            if ptr[parpar << 2 | 1] == par:\n\
    \                ptr[parpar << 2 | 1] = u\n        ptr[u << 2 | 2] = parpar\n\
    \        ptr[par << 2 | 2] = u\n        if c != -1:\n            ptr[c << 2 |\
    \ 2] = par\n        self._update(par)\n        self._update(u)\n        return\
    \ u\n\n    def _splay(self, u: int):\n        self._push(u)\n        while self._state(u)\
    \ != 0:\n            par = self.ptr[u << 2 | 2]\n            if self._state(par)\
    \ == 0:\n                self._push(par)\n                self._push(u)\n    \
    \            self._rotate(u)\n            elif self._state(u) == self._state(par):\n\
    \                self._push(self.ptr[par << 2 | 2])\n                self._push(par)\n\
    \                self._push(u)\n                self._rotate(par)\n          \
    \      self._rotate(u)\n            else:\n                self._push(self.ptr[par\
    \ << 2 | 2])\n                self._push(par)\n                self._push(u)\n\
    \                self._rotate(u)\n                self._rotate(u)\n\n    def _access(self,\
    \ u: int):\n        cur = u\n        r_cur = -1\n        while cur != -1:\n  \
    \          self._splay(cur)\n            self.ptr[cur << 2 | 1] = r_cur\n    \
    \        self._update(cur)\n            r_cur = cur\n            cur = self.ptr[cur\
    \ << 2 | 2]\n        self._splay(u)\n\n    def link(self, u: int, v: int) -> None:\n\
    \        self._access(u)\n        self._access(v)\n        self.ptr[u << 2 | 2]\
    \ = v\n        self.ptr[u << 2 | 1] = u\n        self._update(v)\n\n    def cut(self,\
    \ u: int) -> None:\n        self._access(u)\n        self.ptr[self.ptr[u << 2\
    \ | 0] << 2 | 2] = -1\n        self.ptr[u << 2 | 0] = -1\n        self._update(u)\n\
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
  timestamp: '2024-02-24 06:05:31+09:00'
  verificationStatus: LIBRARY_ALL_WA
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
