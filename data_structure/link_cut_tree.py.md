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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LinkCutTree:\n    def __init__(self, op, e, arr: list[int]):\n    \
    \    self.op = op\n        self.e = e\n        self.n = n = len(arr)\n       \
    \ self.ptr = [-1] * (n << 2)  # l, r, p, rev\n        for i in range(n):\n   \
    \         self.ptr[i << 2 | 3] = 0\n        self.val = arr[:]\n        self.sum\
    \ = [e] * (n + 1)\n        self.rev = [e] * (n + 1)\n\n    def _toggle(self, v:\
    \ int):\n        if v == -1:\n            return\n        self.sum[v], self.rev[v]\
    \ = self.rev[v], self.sum[v]\n        self.ptr[v << 2 | 0], self.ptr[v << 2 |\
    \ 1] = (\n            self.ptr[v << 2 | 1],\n            self.ptr[v << 2 | 0],\n\
    \        )\n        self.ptr[v << 2 | 3] ^= 1\n\n    def _push(self, v: int):\n\
    \        if v == -1 or not self.ptr[v << 2 | 3]:\n            return\n       \
    \ self._toggle(self.ptr[v << 2 | 0])\n        self._toggle(self.ptr[v << 2 | 1])\n\
    \        self.ptr[v << 2 | 3] = 0\n\n    def _update(self, v: int):\n        self.sum[v]\
    \ = self.op(\n            self.op(self.sum[self.ptr[v << 2 | 0]], self.val[v]),\n\
    \            self.sum[self.ptr[v << 2 | 1]],\n        )\n        self.rev[v] =\
    \ self.op(\n            self.op(self.rev[self.ptr[v << 2 | 1]], self.val[v]),\n\
    \            self.rev[self.ptr[v << 2 | 0]],\n        )\n\n    def _state(self,\
    \ v: int):\n        p = self.ptr[v << 2 | 2]\n        if self.ptr[p << 2 | 0]\
    \ == v:\n            return 1\n        elif self.ptr[p << 2 | 1] == v:\n     \
    \       return -1\n        else:\n            return 0\n\n    def _rotate(self,\
    \ v: int):\n        s = self._state(v)\n        if s == 0:\n            return\n\
    \        ptr = self.ptr\n        p = ptr[v << 2 | 2]\n        pp = ptr[p << 2\
    \ | 2]\n        t = self._state(p)\n        if s == 1:\n            r = ptr[v\
    \ << 2 | 1]\n            ptr[v << 2 | 1] = p\n            ptr[p << 2 | 0] = r\n\
    \            if r != -1:\n                ptr[r << 2 | 2] = p\n        else:\n\
    \            l = ptr[v << 2 | 0]\n            ptr[v << 2 | 0] = p\n          \
    \  ptr[p << 2 | 1] = l\n            if l != -1:\n                ptr[l << 2 |\
    \ 2] = p\n        ptr[p << 2 | 2] = v\n        ptr[v << 2 | 2] = pp\n        self._update(p)\n\
    \        self._update(v)\n        if t == 0:\n            return\n        elif\
    \ t == 1:\n            ptr[pp << 2 | 0] = v\n        else:\n            ptr[pp\
    \ << 2 | 1] = v\n\n    def _splay(self, v: int):\n        self._push(v)\n    \
    \    while True:\n            s = self._state(v)\n            if not s:\n    \
    \            break\n            p = self.ptr[v << 2 | 2]\n            t = self._state(p)\n\
    \            if t == 0:\n                self._push(p)\n                self._push(v)\n\
    \                self._rotate(v)\n            elif s == t:\n                self._push(self.ptr[p\
    \ << 2 | 2])\n                self._push(p)\n                self._push(v)\n \
    \               self._rotate(p)\n                self._rotate(v)\n           \
    \ else:\n                self._push(self.ptr[p << 2 | 2])\n                self._push(p)\n\
    \                self._push(v)\n                self._rotate(v)\n            \
    \    self._rotate(v)\n\n    def _access(self, v: int) -> int:\n        c = v\n\
    \        r = -1\n        while v != -1:\n            self._splay(v)\n        \
    \    self.ptr[v << 2 | 1] = r\n            self._update(v)\n            r = v\n\
    \            v = self.ptr[v << 2 | 2]\n        self._splay(c)\n        return\
    \ r\n\n    def link(self, v: int, p: int) -> None:\n        \"\"\"\u9802\u70B9\
    v,p\u3092,p\u3092v\u306E\u89AA\u306B\u3057\u3066\u9023\u7D50\u3059\u308B. \u3053\
    \u306E\u3068\u304Dv\u304C\u6839\u3067\u3042\u308B\u5FC5\u8981\u304C\u3042\u308B\
    \"\"\"\n        # self.evert(v)\n        self._access(v)\n        self._access(p)\n\
    \        self.ptr[v << 2 | 2] = p\n        self.ptr[p << 2 | 1] = v\n        self._update(p)\n\
    \n    def cut(self, v: int) -> None:\n        \"\"\"\u9802\u70B9v\u3068\u305D\u306E\
    \u89AA\u30CE\u30FC\u30C9\u3068\u306E\u8FBA\u3092\u53D6\u308A\u9664\u304F. v\u304C\
    \u305D\u306E\u90E8\u5206\u6728\u306E\u6839\u3068\u306A\u308B.\"\"\"\n        self._access(v)\n\
    \        self.ptr[self.ptr[v << 2 | 0] << 2 | 2] = -1\n        self.ptr[v << 2\
    \ | 0] = -1\n        self._update(v)\n\n    def root(self, v: int) -> int:\n \
    \       \"\"\"\u9802\u70B9v\u3092\u542B\u3080\u6728\u306E\u6839\u3092\u8FD4\u3059\
    .\"\"\"\n        self._access(v)\n        while self.ptr[v << 2 | 0] != -1:\n\
    \            v = self.ptr[v << 2 | 0]\n        return v\n\n    def parent(self,\
    \ v: int) -> int:\n        \"\"\"\u9802\u70B9v\u306E\u89AA\u3092\u8FD4\u3059.\"\
    \"\"\n        self._access(v)\n        v = self.ptr[v << 2 | 0]\n        while\
    \ self.ptr[v << 2 | 1] != -1:\n            v = self.ptr[v << 2 | 1]\n        return\
    \ v\n\n    def evert(self, v: int) -> None:\n        \"\"\"\u9802\u70B9v\u3092\
    v\u3092\u542B\u3080\u6728\u306E\u6839\u306B\u3059\u308B.\"\"\"\n        self._access(v)\n\
    \        self._toggle(v)\n        self._push(v)\n\n    def set(self, v: int, x:\
    \ int) -> None:\n        \"\"\"\u9802\u70B9v\u306E\u5024\u3092x\u306B\u3059\u308B\
    .\"\"\"\n        self._access(v)\n        self.val[v] = x\n\n    def add(self,\
    \ v: int, x: int) -> None:\n        \"\"\"\u9802\u70B9v\u306E\u5024\u306Bx\u3092\
    \u52A0\u7B97\u3059\u308B.\"\"\"\n        self._access(v)\n        self.val[v]\
    \ += x\n\n    def path_query(self, u: int, v: int) -> int:\n        \"\"\"\u9802\
    \u70B9u,v\u9593\u306E\u30D1\u30B9\u30AF\u30A8\u30EA\u3092\u8FD4\u3059. \u305F\u3060\
    \u3057,u\u3068v\u306F\u9023\u7D50\u3067\u3042\u308B\u5FC5\u8981\u304C\u3042\u308B\
    .\"\"\"\n        self.evert(u)\n        self._access(v)\n        return self.sum[v]\n\
    \n    def lca(self, u: int, v: int) -> int:\n        \"\"\"\u9802\u70B9u,v\u306E\
    LCA\u3092\u8FD4\u3059. Not verified.\"\"\"\n        assert self.root(u) == self.root(v)\n\
    \        self._access(u)\n        return self._access(v)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/link_cut_tree.py
  requiredBy: []
  timestamp: '2024-04-24 11:17:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/dynamic_tree_vertex_set_path_composite.test.py
  - test/library_checker/data_structure/dynamic_tree_vertex_add_path_sum.test.py
documentation_of: data_structure/link_cut_tree.py
layout: document
title: Link Cut Tree
---
