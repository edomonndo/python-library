---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: tree/contour_query.py
    title: "\u7B49\u9AD8\u7DDA\u30AF\u30A8\u30EA"
  _extendedVerifiedWith:
  - icon: ':grey_question:'
    path: test/atcoder/abc291h.test.py
    title: test/atcoder/abc291h.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class CentroidDecomposition:\n    \"\"\"\n    order[v]: \u91CD\u5FC3\u5206\
    \u89E3\u5F8C\u306E\u90E8\u5206\u6728\u306B\u304A\u3051\u308B\u91CD\u5FC3v\u306E\
    dfs\u9806.\u91CD\u5FC3v\u306E\u90E8\u5206\u6728\u306Forder\u304C\u91CD\u5FC3v\u3088\
    \u308A\u5927\u304D\u3044bfs\u3067\u5230\u9054\u53EF\u80FD\u306A\u9802\u70B9\n\
    \    depth[v]: \u91CD\u5FC3\u5206\u89E3\u5F8C\u306E\u90E8\u5206\u6728\u306B\u304A\
    \u3051\u308B\u91CD\u5FC3v\u306E\u6DF1\u3055.\n    belong[v]: \u91CD\u5FC3\u5206\
    \u89E3\u5F8C\u306E\u90E8\u5206\u6728\u306B\u304A\u3051\u308B\u91CD\u5FC3v\u306E\
    \u89AA\u306E\u91CD\u5FC3(\u6839\u306F-1).\n    g[v]: \u91CD\u5FC3\u5206\u89E3\u5F8C\
    \u306E\u91CD\u5FC3\u9593\u306E\u6709\u5411\u30B0\u30E9\u30D5\n    root: \u91CD\
    \u5FC3\u5206\u89E3\u5F8C\u306E\u6700\u521D\u306E\u91CD\u5FC3\n    \"\"\"\n\n \
    \   def __init__(self, adj: list[list[int]], root: int = 0) -> None:\n       \
    \ self.n = n = len(adj)\n        # \u90E8\u5206\u6728\u306E\u30B5\u30A4\u30BA\n\
    \        size = [1] * n\n        stack = [(~root, -1), (root, -1)]\n        while\
    \ stack:\n            v, p = stack.pop()\n            if v >= 0:\n           \
    \     for u in adj[v]:\n                    if u != p:\n                     \
    \   stack.append((~u, v))\n                        stack.append((u, v))\n    \
    \        else:\n                v = ~v\n                for u in adj[v]:\n   \
    \                 if u != p:\n                        size[v] += size[u]\n   \
    \     # \u91CD\u5FC3\u5206\u89E3\n        self.order = order = [-1] * n\n    \
    \    self.depth = depth = [-1] * n\n        self.belong = belong = [-1] * n\n\
    \        self.g = [[] for _ in range(n)]\n        self.root = -1\n        stack\
    \ = [(root, -1, 0)]  # \u3000current, previous, depth\n        for i in range(n):\n\
    \            v, p, d = stack.pop()\n            while True:\n                for\
    \ u in adj[v]:\n                    if order[u] == -1 and size[u] * 2 > size[v]:\n\
    \                        size[v], size[u], v = size[v] - size[u], size[v], u\n\
    \                        break\n                else:\n                    # \u9802\
    \u70B9v\u304C\u91CD\u5FC3\u306E\u3068\u304D\n                    break\n     \
    \       if p != -1:\n                self.g[p].append(v)\n            else:\n\
    \                self.root = v\n            order[v], depth[v], belong[v] = i,\
    \ d, p\n            if size[v] > 1:\n                for u in adj[v]:\n      \
    \              if order[u] == -1:\n                        stack.append((u, v,\
    \ d + 1))\n\n    def find(self, u: int, v: int) -> int:\n        \"\"\"\n    \
    \    \u9802\u70B9u,v\u306E\u4E21\u65B9\u3092\u542B\u3080\u6700\u3082\u5C0F\u3055\
    \u3044\u90E8\u5206\u6728\u306E\u91CD\u5FC3\u3092\u8FD4\u3059\n        \"\"\"\n\
    \        du, dv = self.depth[u], self.depth[v]\n        for _ in range(du - 1,\
    \ dv - 1, -1):\n            u = self.belong[u]\n        for _ in range(dv - 1,\
    \ du - 1, -1):\n            v = self.belong[v]\n        while u != v:\n      \
    \      u, v = self.belong[u], self.belong[v]\n        return u\n\n    def get(self,\
    \ v: int) -> list[int]:\n        \"\"\"\n        \u91CD\u5FC3\u5206\u89E3\u5F8C\
    \u306E\u90E8\u5206\u6728\u3067,\u9802\u70B9v\u304C\u5C5E\u3059\u308B\u90E8\u5206\
    \u6728\u3092\u30B5\u30A4\u30BA\u306E\u6607\u9806\u306B\u5217\u6319\u3059\u308B\
    \n        \"\"\"\n        res = []\n        for _ in range(self.depth[v], -1,\
    \ -1):\n            res.append(v)\n            v = self.belong[v]\n        return\
    \ res\n\n    def get_root(self) -> int:\n        assert 0 <= self.root < self.n\n\
    \        return self.root\n\n    def get_graph(self) -> list[list[int]]:\n   \
    \     return self.g\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/centroid_decomposition.py
  requiredBy:
  - tree/contour_query.py
  timestamp: '2024-06-10 12:42:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith:
  - test/atcoder/abc291h.test.py
documentation_of: tree/centroid_decomposition.py
layout: document
title: "\u91CD\u5FC3\u5206\u89E3"
---

References:
- https://qiita.com/navel_tos/items/d1a2fd2b63e73380eadb