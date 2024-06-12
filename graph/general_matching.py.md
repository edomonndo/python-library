---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/matching_on_general_graph.test.py
    title: test/library_checker/graph/matching_on_general_graph.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\nclass GeneralMatching:\n    def __init__(self,\
    \ n: int, edges: list[tuple[int, int]]):\n        self.n = n\n        self.adj\
    \ = adj = [[] for _ in range(n + 1)]\n        self.edges = []\n        cnt = n\
    \ + 1\n        for i, (u, v) in enumerate(edges, n + 1):\n            u += 1\n\
    \            v += 1\n            adj[u].append((v, i))\n            adj[v].append((u,\
    \ i))\n            self.edges.append((u, v))\n        self.mate = [0] * (n + 1)\n\
    \        self.label = [-1] * (n + 1)\n        self.first = [0] * (n + 1)\n\n \
    \   def _eval_first(self, x: int) -> int:\n        label, first, _eval_first =\
    \ self.label, self.first, self._eval_first\n        if label[first[x]] < 0:\n\
    \            return first[x]\n        first[x] = _eval_first(first[x])\n     \
    \   return first[x]\n\n    def _rematch(self, u: int, v: int) -> None:\n     \
    \   mate, label = self.mate, self.label\n        st = [(u, v)]\n        while\
    \ st:\n            u, v = st.pop()\n            t = mate[u]\n            mate[u]\
    \ = v\n            if mate[t] != u:\n                continue\n            if\
    \ label[u] <= self.n:\n                mate[t] = label[u]\n                st.append((label[u],\
    \ t))\n            else:\n                x, y = self.edges[label[u] - self.n\
    \ - 1]\n                st += [(y, x), (x, y)]\n\n    def _assign(self, x: int,\
    \ y: int, num: int) -> None:\n        mate, label, first = self.mate, self.label,\
    \ self.first\n        dq, _eval_first = self.dq, self._eval_first\n        r =\
    \ _eval_first(x)\n        s = _eval_first(y)\n        join = 0\n        if r ==\
    \ s:\n            return\n        label[r] = -num\n        label[s] = -num\n \
    \       while True:\n            if s != 0:\n                r, s = s, r\n   \
    \         r = _eval_first(label[mate[r]])\n            if label[r] == -num:\n\
    \                join = r\n                break\n            label[r] = -num\n\
    \        v = first[x]\n        while v != join:\n            dq.append(v)\n  \
    \          label[v] = num\n            first[v] = join\n            v = first[label[mate[v]]]\n\
    \        v = first[y]\n        while v != join:\n            dq.append(v)\n  \
    \          label[v] = num\n            first[v] = join\n            v = first[label[mate[v]]]\n\
    \        return\n\n    def _check(self, v: int) -> bool:\n        dq, first, label,\
    \ mate = self.dq, self.first, self.label, self.mate\n        adj, _rematch, _assign\
    \ = self.adj, self._rematch, self._assign\n        first[v] = 0\n        label[v]\
    \ = 0\n        dq.append(v)\n        while dq:\n            x = dq.popleft()\n\
    \            for y, lb in adj[x]:\n                if mate[y] == 0 and y != v:\n\
    \                    mate[y] = x\n                    _rematch(x, y)\n       \
    \             return True\n                elif label[y] >= 0:\n             \
    \       _assign(x, y, lb)\n                elif label[mate[y]] < 0:\n        \
    \            label[mate[y]] = x\n                    first[mate[y]] = y\n    \
    \                dq.append(mate[y])\n        return False\n\n    def solve(self)\
    \ -> list[tuple[int, int]]:\n        mate, _check = self.mate, self._check\n \
    \       for i in range(1, self.n + 1):\n            self.dq = deque()\n      \
    \      if mate[i] != 0:\n                continue\n            if _check(i):\n\
    \                self.label = [-1] * (self.n + 1)\n        res = []\n        for\
    \ i in range(1, self.n + 1):\n            if i < mate[i]:\n                res.append((i\
    \ - 1, mate[i] - 1))\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/general_matching.py
  requiredBy: []
  timestamp: '2024-06-12 17:23:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/matching_on_general_graph.test.py
documentation_of: graph/general_matching.py
layout: document
title: "\u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0"
---
