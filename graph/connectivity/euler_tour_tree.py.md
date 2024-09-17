---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/dynamic_connectivity.py
    title: graph/connectivity/dynamic_connectivity.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from functools import reduce\nfrom typing import Callable, TypeVar\n\nT =\
    \ TypeVar(\"T\")\n\n\nclass EulerTourTree:\n\n    class Node:\n        def __init__(self,\
    \ l: int, r: int, e: T):\n            self.par = self.left = self.right = None\n\
    \            self.l, self.r, self.sz = l, r, l == r\n            self.val = self.sum\
    \ = e\n            self.exact = self.child_exact = l < r\n            self.edge_connected\
    \ = self.child_edge_connected = False\n\n        def is_root(self) -> bool:\n\
    \            return self.par is None\n\n    def __init__(self, n: int, op: Callable[[T,\
    \ T], T], e: T):\n        self.n = n\n        self.op = op\n        self.e = e\n\
    \        self.ptr = [{i: self.Node(i, i, self.e)} for i in range(n)]\n\n    def\
    \ _split(self, t: Node) -> tuple[Node, Node]:\n        self._splay(t)\n      \
    \  l = t.left\n        if l:\n            l.par = None\n        t.left = None\n\
    \        return l, self._update(t)\n\n    def _split2(self, t: Node) -> tuple[Node,\
    \ Node]:\n        self._splay(t)\n        l, r = t.left, t.right\n        if l:\n\
    \            l.par = None\n        t.left = None\n        if r:\n            r.par\
    \ = None\n        t.right = None\n        return l, r\n\n    def _split3(self,\
    \ s: Node, t: Node) -> tuple[Node, Node, Node]:\n        a, b = self._split2(s)\n\
    \        if self._same(a, t):\n            c, d = self._split2(t)\n          \
    \  return c, d, b\n        else:\n            c, d = self._split2(t)\n       \
    \     return a, c, d\n\n    def _merge(self, s: Node, t: Node) -> Node:\n    \
    \    if not s:\n            return t\n        if not t:\n            return s\n\
    \        while s.right:\n            s = s.right\n        self._splay(s)\n   \
    \     s.right = t\n        if t:\n            t.par = s\n        return self._update(s)\n\
    \n    def _size(self, t: Node) -> int:\n        return t.sz if t else 0\n\n  \
    \  def _update(self, t: Node) -> Node:\n        t.sum = self.e\n        if t.left:\n\
    \            t.sum = self.op(t.left.sum, t.sum)\n        if t.l == t.r:\n    \
    \        t.sum = self.op(t.sum, t.val)\n        if t.right:\n            t.sum\
    \ = self.op(t.sum, t.right.sum)\n        t.sz = self._size(t.left) + (t.l == t.r)\
    \ + self._size(t.right)\n        t.child_edge_connected = (\n            (t.left.child_edge_connected\
    \ if t.left else False)\n            | t.edge_connected\n            | (t.right.child_edge_connected\
    \ if t.right else False)\n        )\n        t.child_exact = (\n            (t.left.child_exact\
    \ if t.left else False)\n            | t.exact\n            | (t.right.child_exact\
    \ if t.right else False)\n        )\n        return t\n\n    def _push(self, t:\
    \ Node) -> None:\n        # TODO\n        pass\n\n    def _rot(self, t: Node,\
    \ b: bool) -> None:\n        p = t.par\n        pp = p.par\n        if b:\n  \
    \          p.left = t.right\n            if p.left:\n                t.right.par\
    \ = p\n            t.right = p\n        else:\n            p.right = t.left\n\
    \            if p.right:\n                t.left.par = p\n            t.left =\
    \ p\n        p.par = t\n        self._update(p)\n        self._update(t)\n   \
    \     t.par = pp\n        if t.par:\n            if pp.left == p:\n          \
    \      pp.left = t\n            if pp.right == p:\n                pp.right =\
    \ t\n            self._update(pp)\n\n    def _splay(self, t: Node) -> None:\n\
    \        self._push(t)\n        while not t.is_root():\n            p = t.par\n\
    \            if p.is_root():\n                self._push(p)\n                self._push(t)\n\
    \                self._rot(t, p.left == t)\n            else:\n              \
    \  pp = p.par\n                self._push(pp)\n                self._push(p)\n\
    \                self._push(t)\n                b1 = pp.left == p\n          \
    \      b2 = (p.left == t) if b1 else (p.right == t)\n                if b2:\n\
    \                    self._rot(p, b1)\n                    self._rot(t, b1)\n\
    \                else:\n                    self._rot(t, not b1)\n           \
    \         self._rot(t, b1)\n\n    def _get_node(self, l: int, r: int) -> Node:\n\
    \        if r not in self.ptr[l]:\n            self.ptr[l][r] = self.Node(l, r,\
    \ self.e)\n        return self.ptr[l][r]\n\n    @staticmethod\n    def _root(t:\
    \ Node) -> Node:\n        if not t:\n            return t\n        while t.par:\n\
    \            t = t.par\n        return t\n\n    def _same(self, s: Node, t: Node)\
    \ -> bool:\n        if s:\n            self._splay(s)\n        if t:\n       \
    \     self._splay(t)\n        return self._root(s) == self._root(t)\n\n    def\
    \ _reroot(self, t: Node) -> Node:\n        l, r = self._split(t)\n        return\
    \ self._merge(r, l)\n\n    def size(self, v: int) -> int:\n        t = self._get_node(v,\
    \ v)\n        self._splay(t)\n        return t.sz\n\n    def same(self, u: int,\
    \ v: int) -> bool:\n        return self._same(self._get_node(u, u), self._get_node(v,\
    \ v))\n\n    def update(self, v: int, x: T) -> Node:\n        t = self._get_node(v,\
    \ v)\n        self._splay(t)\n        t.val = self.op(t.val, x)\n        self._update(t)\n\
    \n    def edge_update(self, v: int, op: Callable[[int, int], None]) -> None:\n\
    \        t = self._get_node(v, v)\n        self._splay(t)\n        while t and\
    \ t.child_exact:\n            c = t\n            st = [c]\n            while st:\n\
    \                c = st.pop()\n                if c.l < c.r and c.exact:\n   \
    \                 self._splay(c)\n                    c.exact = False\n      \
    \              self._update(c)\n                    op(c.l, c.r)\n           \
    \         continue\n                if c.left and c.left.child_exact:\n      \
    \              st.append(c.left)\n                else:\n                    st.append(c.right)\n\
    \            self._splay(t)\n\n    def try_reconnect(self, v: int, op: Callable[[int],\
    \ bool]) -> bool:\n        t = self._get_node(v, v)\n        self._splay(t)\n\
    \        while t.child_edge_connected:\n            flag = False\n           \
    \ c = t\n            st = [c]\n            while st:\n                c = st.pop()\n\
    \                if c.edge_connected:\n                    self._splay(c)\n  \
    \                  flag = op(c.l)\n                    continue\n            \
    \    if c.left and c.left.child_edge_connected:\n                    st.append(c.left)\n\
    \                else:\n                    st.append(c.right)\n            if\
    \ flag:\n                return True\n            self._splay(t)\n        return\
    \ False\n\n    def edge_connected_update(self, v: int, b: bool) -> None:\n   \
    \     t = self._get_node(v, v)\n        self._splay(t)\n        t.edge_connected\
    \ = b\n        self._update(t)\n\n    def link(self, l: int, r: int) -> bool:\n\
    \        if self.same(l, r):\n            return False\n        ll, lr = self._get_node(l,\
    \ l), self._get_node(l, r)\n        rr, rl = self._get_node(r, r), self._get_node(r,\
    \ l)\n        reduce(self._merge, [self._reroot(ll), lr, self._reroot(rr), rl])\n\
    \        return True\n\n    def cut(self, l: int, r: int) -> bool:\n        ptr\
    \ = self.ptr\n        if r not in ptr[l]:\n            return False\n        s,\
    \ _, u = self._split3(self._get_node(l, r), self._get_node(r, l))\n        self._merge(s,\
    \ u)\n        ptr[l].pop(r)\n        ptr[r].pop(l)\n        return True\n\n  \
    \  def get_sum_edge(self, p: int, v: int) -> T:\n        self.cut(p, v)\n    \
    \    t = self._get_node(v, v)\n        self._splay(t)\n        res = t.sum\n \
    \       self.link(p, v)\n        return res\n\n    def get_sum(self, v: int) ->\
    \ T:\n        t = self._get_node(v, v)\n        self._splay(t)\n        return\
    \ t.sum\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/connectivity/euler_tour_tree.py
  requiredBy:
  - graph/connectivity/dynamic_connectivity.py
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/connectivity/euler_tour_tree.py
layout: document
redirect_from:
- /library/graph/connectivity/euler_tour_tree.py
- /library/graph/connectivity/euler_tour_tree.py.html
title: graph/connectivity/euler_tour_tree.py
---
