---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: data_structure/segtree/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  _extendedRequiredBy: []
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
  code: "from data_structure.segtree.lazy_segment_tree import LazySegtree\n\ninf =\
    \ 1 << 30\n\n\nclass PermutationTree:\n\n    class Node:\n        def __init__(\n\
    \            self,\n            l: int = inf,\n            r: int = -1,\n    \
    \        mn: int = inf,\n            mx: int = -1,\n            t: int = 0,\n\
    \            par: int = -1,\n        ):\n            self.l = l\n            self.r\
    \ = r\n            self.mn = mn\n            self.mx = mx\n            self.type\
    \ = t  # 0: prime, 1: asc, -1: desc\n            self.par = par\n\n        def\
    \ __str__(self):\n            return f\"Node<l={self.l}, r={self.r}>, p={self.par}>\"\
    \n\n        __repr__ = __str__\n\n    def __init__(self, P: list[int]):\n    \
    \    self.n = n = len(P)\n        self.nodes = [self.Node(i, i + 1, P[i], P[i]\
    \ + 1, 0, -1) for i in range(n)]\n        # \u533A\u9593\u52A0\u7B97\u30FB\u533A\
    \u9593\u6700\u5C0F\u5024\n        self.seg = LazySegtree(\n            [0] * n,\
    \ min, inf, lambda f, x: f + x, lambda f, g: f + g, 0\n        )\n        self._build(P)\n\
    \n    def _add_child(self, v: int, p: int) -> None:\n        cur, par = self.nodes[v],\
    \ self.nodes[p]\n        cur.par = p\n        if par.l > cur.l:\n            par.l\
    \ = cur.l\n        if par.r < cur.r:\n            par.r = cur.r\n        if par.mn\
    \ > cur.mn:\n            par.mn = cur.mn\n        if par.mx < cur.mx:\n      \
    \      par.mx = cur.mx\n        return\n\n    def _build(self, P: list[int]) ->\
    \ None:\n        seg, nodes, add_child = self.seg, self.nodes, self._add_child\n\
    \        mxs = [-1]\n        mns = [-1]\n        st = []\n        for i in range(self.n):\n\
    \            while mxs[-1] != -1 and P[mxs[-1]] < P[i]:\n                mx =\
    \ mxs.pop()\n                seg.apply(mxs[len(mxs) - 1] + 1, mx + 1, P[i] - P[mx])\n\
    \            while mns[-1] != -1 and P[mns[-1]] > P[i]:\n                mn =\
    \ mns.pop()\n                seg.apply(mns[len(mns) - 1] + 1, mn + 1, P[mn] -\
    \ P[i])\n            mxs.append(i)\n            mns.append(i)\n            seg.apply(0,\
    \ i, -1)\n            cur = i\n            while st:\n                t = st[-1]\n\
    \                nt, nc = nodes[t], nodes[cur]\n                if (nt.type ==\
    \ 1 and nt.mx == nc.mn) or (\n                    nt.type == -1 and nt.mn == nc.mx\n\
    \                ):\n                    add_child(cur, t)\n                 \
    \   st.pop()\n                    cur = t\n                elif nt.mx == nc.mn\
    \ or nt.mn == nc.mx:\n                    p = len(nodes)\n                   \
    \ nodes.append(self.Node())\n                    nodes[p].type = 1 if nt.mx ==\
    \ nc.mn else -1\n                    add_child(cur, p)\n                    add_child(t,\
    \ p)\n                    st.pop()\n                    cur = p\n            \
    \    elif seg.prod(0, nc.l) == 0:\n                    p = len(nodes)\n      \
    \              nodes.append(self.Node())\n                    np = nodes[p]\n\
    \                    np.type = 0\n                    add_child(cur, p)\n    \
    \                while True:\n                        add_child(st.pop(), p)\n\
    \                        if np.r - np.l == np.mx - np.mn:\n                  \
    \          break\n                    cur = p\n                else:\n       \
    \             break\n            st.append(cur)\n\n        for i in range(self.n):\n\
    \            nodes[i].type = 1\n        return\n\n    def par(self, v: int) ->\
    \ int:\n        return self.nodes[v].par\n\n    def left(self, v: int) -> int:\n\
    \        return self.nodes[v].l\n\n    def right(self, v: int) -> int:\n     \
    \   return self.nodes[v].r\n\n    def max(self, v: int) -> int:\n        return\
    \ self.nodes[v].mx\n\n    def min(self, v: int) -> int:\n        return self.nodes[v].mn\n\
    \n    def type(self, v: int) -> int:\n        return self.nodes[v].type\n\n  \
    \  def size(self) -> int:\n        return len(self.nodes)\n\n    def is_lineaer(self,\
    \ v: int) -> bool:\n        return self.nodes[v].type != 0\n\n    def is_prime(self,\
    \ v: int) -> bool:\n        return self.nodes[v].type == 0\n\n    def gen_graph(self)\
    \ -> tuple[int, list[list[int]]]:\n        n = len(self.nodes)\n        adj =\
    \ [[] for _ in range(n)]\n        for i in range(n):\n            if self.nodes[i].par\
    \ != -1:\n                adj[self.nodes.par].append(i)\n            else:\n \
    \               root = i\n        return root, adj\n\n\nn = int(input())\nP =\
    \ [int(x) for x in input().split()]\npt = PermutationTree(P)\nprint(pt.size())\n\
    for i in range(pt.size()):\n    print(\n        pt.par(i),\n        pt.left(i),\n\
    \        pt.right(i) - 1,\n        \"linear\" if pt.is_lineaer(i) else \"prime\"\
    ,\n    )\n"
  dependsOn:
  - data_structure/segtree/lazy_segment_tree.py
  isVerificationFile: false
  path: graph/tree/permutation_tree.py
  requiredBy: []
  timestamp: '2024-08-05 20:55:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/tree/permutation_tree.py
layout: document
title: "\u9806\u5217\u6728"
---
