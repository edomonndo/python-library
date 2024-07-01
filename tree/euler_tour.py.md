---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: atcoder/segtree.py
    title: atcoder/segtree.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lowest_common_ancestor.test.py
    title: GRL5C LCA (Lowest Common Ancestor)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_path_sum_et.test.py
    title: Vertex Add Path Sum (Euler Tour)
  - icon: ':heavy_check_mark:'
    path: test/library_checker/tree/vertex_add_subtree_sum_et.test.py
    title: Vertex Add Subtree Sum (Euler Tour)
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from atcoder.segtree import SegTree\n\n\nclass EulerTour:\n    def __init__(self,\
    \ G, root, vcost):\n        N = len(G)\n        self.N = N\n        self.ET =\
    \ []\n        self.into = [0] * N\n        self.out = [0] * N\n        self.parent\
    \ = [-1] * N\n        self.depth = [N] * (N + 1)\n        # For Path Query\n \
    \       self.vcost = []\n        self.ecost = []\n        # For Subtree Query\n\
    \        self.vcost_st = []\n        self.ecost_st = []\n\n        # \u975E\u518D\
    \u5E30DFS\n        stack = [(root, -1, 0)]\n        while stack:\n           \
    \ v, p, weight = stack.pop()\n            if v >= 0:\n                self.into[v]\
    \ = len(self.ET)\n                self.ET.append(v)\n                self.depth[v]\
    \ = 0 if p == -1 else self.depth[p] + 1\n                self.vcost.append(vcost[v])\n\
    \                self.ecost.append(weight)\n                self.vcost_st.append(vcost[v])\n\
    \                self.ecost_st.append(weight)\n                self.out[v] = len(self.ET)\n\
    \                for u, w in G[v]:\n                    if u == p:\n         \
    \               continue\n                    self.parent[u] = v\n           \
    \         stack.append((~v, u, -w))\n                    stack.append((u, v, w))\n\
    \            else:\n                v = ~v\n                self.ET.append(v)\n\
    \                self.vcost.append(-vcost[p])\n                self.ecost.append(weight)\n\
    \                self.vcost_st.append(0)\n                self.ecost_st.append(0)\n\
    \                self.out[v] = len(self.ET)\n\n        self.depth_min = SegTree(\n\
    \            lambda u, v: u if self.depth[u] <= self.depth[v] else v, self.N,\
    \ self.ET\n        )\n        self.vcost_subtree_sum = SegTree(lambda u, v: u\
    \ + v, 0, self.vcost_st)\n        self.ecost_subtree_sum = SegTree(lambda u, v:\
    \ u + v, 0, self.ecost_st)\n        self.vcost_path_sum = SegTree(lambda u, v:\
    \ u + v, 0, self.vcost)\n        self.ecost_path_sum = SegTree(lambda u, v: u\
    \ + v, 0, self.ecost)\n\n    def lca(self, u, v):\n        \"\"\"u\u3068v\u306E\
    \u6700\u8FD1\u5171\u901A\u7956\u5148\"\"\"\n        if self.into[u] > self.into[v]:\n\
    \            u, v = v, u\n        return self.depth_min.prod(self.into[u], self.out[v])\n\
    \n    def dist(self, u, v):\n        \"\"\"u\u3068v\u306E\u8DDD\u96E2\"\"\"\n\
    \        a = self.lca(u, v)\n        return (\n            self.ecost_path_sum.prod(0,\
    \ self.out[u])\n            + self.ecost_path_sum.prod(0, self.out[v])\n     \
    \       - 2 * self.ecost_path_sum.prod(0, self.out[a])\n        )\n\n    def update_parent_edge(self,\
    \ v, w):\n        \"\"\"v\u3068\u305D\u306E\u89AA\u3092\u7E4B\u3050\u8FBA\u306E\
    \u91CD\u307F\u3092w\u306B\u66F4\u65B0\"\"\"\n        l, r = self.into[v], self.out[v]\n\
    \        self.ecost_path_sum.set(l, w)\n        if r < self.ecost_path_sum._n:\n\
    \            self.ecost_path_sum.set(r, -w)\n        self.ecost_subtree_sum.set(l,\
    \ w)\n\n    def add_parent_edge(self, v, w):\n        \"\"\"v\u3068\u305D\u306E\
    \u89AA\u3092\u7E4B\u3050\u8FBA\u306E\u91CD\u307F\u306Bw\u3092\u52A0\u7B97\"\"\"\
    \n        l, r = self.into[v], self.out[v]\n        cur = self.ecost_path_sum.get(l)\n\
    \        self.ecost_path_sum.set(l, w + cur)\n        if r < self.ecost_path_sum._n:\n\
    \            self.ecost_path_sum.set(r, -(w + cur))\n        self.ecost_subtree_sum.set(l,\
    \ w + self.ecost_subtree_sum.get(l))\n\n    def update_verticle(self, v, w):\n\
    \        \"\"\"v\u306E\u91CD\u307F\u3092w\u306B\u66F4\u65B0\"\"\"\n        l,\
    \ r = self.into[v], self.out[v]\n        self.vcost_path_sum.set(l, w)\n     \
    \   if r < self.vcost_path_sum._n:\n            self.vcost_path_sum.set(r, -w)\n\
    \        self.vcost_subtree_sum.set(l, w)\n\n    def add_verticle(self, v, w):\n\
    \        \"\"\"v\u306E\u91CD\u307F\u306Bw\u3092\u52A0\u7B97\"\"\"\n        l,\
    \ r = self.into[v], self.out[v]\n        cur = self.vcost_path_sum.get(l)\n  \
    \      self.vcost_path_sum.set(l, w + cur)\n        if r < self.vcost_path_sum._n:\n\
    \            self.vcost_path_sum.set(r, -(w + cur))\n        self.vcost_subtree_sum.set(l,\
    \ w + self.vcost_subtree_sum.get(l))\n\n    def is_ancestor(self, u, v):\n   \
    \     \"\"\"True if u is ancestor of v.\"\"\"\n        return self.into[u] <=\
    \ self.into[v] < self.out[u]\n\n    def subtree_verticle_sum(self, v):\n     \
    \   \"\"\"Range Sum Query1 \u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\
    \u6728\u306E\u9802\u70B9\u306E\u5024\u306E\u548C\"\"\"\n        l, r = self.into[v],\
    \ self.out[v]\n        return self.vcost_subtree_sum.prod(l, r)\n\n    def subtree_edge_sum(self,\
    \ v):\n        \"\"\"Range Sum Query2 \u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\
    \u90E8\u5206\u6728\u306E\u8FBA\u306E\u5024\u306E\u548C\"\"\"\n        l, r = self.into[v],\
    \ self.out[v]\n        # \u9802\u70B9v\u304B\u3089\u89AA\u3078\u306E\u8FBA\u3092\
    \u9664\u53BB\u3059\u308B\u305F\u3081\u306Bl\u3092\uFF11\u3064\u305A\u3089\u3059\
    \n        return self.ecost_subtree_sum.prod(l + 1, r)\n\n    def path_verticle_sum(self,\
    \ u, v=None):\n        \"\"\"Path Query1 \u6839\u304B\u3089\u9802\u70B9u\u307E\
    \u3067\u306E\u9802\u70B9\u306E\u5024\u306E\u548C\"\"\"\n        if v == None:\n\
    \            return self.vcost_path_sum.prod(0, self.into[u] + 1)\n\n        \"\
    \"\"Path Query2 \u9802\u70B9u\u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u9802\
    \u70B9\u306E\u5024\u306E\u548C\"\"\"\n        a = self.lca(u, v)\n        return\
    \ (\n            self.vcost_path_sum.prod(0, self.into[u] + 1)\n            +\
    \ self.vcost_path_sum.prod(0, self.into[v] + 1)\n            - self.vcost_path_sum.prod(0,\
    \ self.into[a])\n            - self.vcost_path_sum.prod(0, self.into[a] + 1)\n\
    \        )\n\n    def path_edge_sum(self, v):\n        \"\"\"Path Query3 \u6839\
    \u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u8FBA\u306E\u5024\u306E\u548C\"\"\"\
    \n        return self.ecost_path_sum.prod(0, self.into[v] + 1)\n"
  dependsOn:
  - atcoder/segtree.py
  isVerificationFile: false
  path: tree/euler_tour.py
  requiredBy: []
  timestamp: '2024-06-04 17:27:40+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_c_lowest_common_ancestor.test.py
  - test/library_checker/tree/vertex_add_path_sum_et.test.py
  - test/library_checker/tree/vertex_add_subtree_sum_et.test.py
documentation_of: tree/euler_tour.py
layout: document
title: Euler tour
---

木をDFS順に訪問し，その結果をさまざまな形式で格納していく.
木の情報を列に変換し，区間計算できるようにする．

参考 https://maspypy.com/euler-tour-のお勉強

- [ABC294G](https://atcoder.jp/contests/abc294/tasks/abc294_g)