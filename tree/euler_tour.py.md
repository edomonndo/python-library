---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
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
    \                self.out[v] = len(self.ET)\n\n        self.depth_min = None\n\
    \        self.vcost_subtree_sum = None\n        self.ecost_subtree_sum = None\n\
    \        self.vcost_path_sum = None\n        self.ecost_path_sum = None\n\n  \
    \  def lca(self, u, v):\n        \"\"\"u\u3068v\u306E\u6700\u8FD1\u5171\u901A\u7956\
    \u5148\"\"\"\n        if self.depth_min is None:\n\n            def op(u, v):\n\
    \                return u if self.depth[u] <= self.depth[v] else v\n\n       \
    \     self.depth_min = SegTree(op, self.N, self.ET)\n\n        if self.into[u]\
    \ > self.into[v]:\n            u, v = v, u\n        return self.depth_min.prod(self.into[u],\
    \ self.out[v])\n\n    def dist(self, u, v):\n        \"\"\"u\u3068v\u306E\u8DDD\
    \u96E2\"\"\"\n        if self.ecost_path_sum is None:\n            self.ecost_path_sum\
    \ = SegTree(lambda u, v: u + v, 0, self.ecost)\n\n        a = self.lca(u, v)\n\
    \        return (\n            self.ecost_path_sum.prod(0, self.out[u])\n    \
    \        + self.ecost_path_sum.prod(0, self.out[v])\n            - 2 * self.ecost_path_sum.prod(0,\
    \ self.out[a])\n        )\n\n    def update_parent_edge(self, v, w):\n       \
    \ \"\"\"v\u3068\u305D\u306E\u89AA\u3092\u7E4B\u3050\u8FBA\u306E\u91CD\u307F\u3092\
    w\u306B\u66F4\u65B0\"\"\"\n        if self.ecost_path_sum is None:\n         \
    \   self.ecost_path_sum = SegTree(lambda u, v: u + v, 0, self.ecost)\n       \
    \ if self.ecost_subtree_sum is None:\n            self.ecost_subtree_sum = SegTree(lambda\
    \ u, v: u + v, 0, self.ecost_st)\n\n        self.ecost_path_sum.set(self.into[v],\
    \ w)\n        if self.out[v] < self.ecost_path_sum._n:\n            self.ecost_path_sum.set(self.out[v],\
    \ -w)\n        self.ecost_subtree_sum.set(self.into[v], w)\n\n    def update_verticle(self,\
    \ v, w):\n        \"\"\"v\u306E\u91CD\u307F\u3092w\u306B\u66F4\u65B0\"\"\"\n \
    \       if self.vcost_path_sum is None:\n            self.vcost_path_sum = SegTree(lambda\
    \ u, v: u + v, 0, self.vcost)\n        if self.vcost_subtree_sum is None:\n  \
    \          self.vcost_subtree_sum = SegTree(lambda u, v: u + v, 0, self.vcost_st)\n\
    \n        self.vcost_path_sum.set(self.into[v], w)\n        if self.out[v] < self.vcost_path_sum._n:\n\
    \            self.vcost_path_sum.set(self.out[v], -w)\n        self.vcost_subtree_sum.set(self.into[v],\
    \ w)\n\n    def is_ancestor(self, u, v):\n        \"\"\"True if u is ancestor\
    \ of v.\"\"\"\n        return self.into[u] <= self.into[v] < self.out[u]\n\n \
    \   def subtree_verticle_sum(self, v):\n        \"\"\"Range Sum Query1 \u9802\u70B9\
    v\u3092\u6839\u3068\u3059\u308B\u90E8\u5206\u6728\u306E\u9802\u70B9\u306E\u5024\
    \u306E\u548C\"\"\"\n        if self.vcost_subtree_sum is None:\n            self.vcost_subtree_sum\
    \ = SegTree(lambda u, v: u + v, 0, self.vcost_st)\n\n        l, r = self.into[v],\
    \ self.out[v]\n        return self.vcost_subtree_sum.prod(l, r)\n\n    def subtree_edge_sum(self,\
    \ v):\n        \"\"\"Range Sum Query2 \u9802\u70B9v\u3092\u6839\u3068\u3059\u308B\
    \u90E8\u5206\u6728\u306E\u8FBA\u306E\u5024\u306E\u548C\"\"\"\n        if self.ecost_subtree_sum\
    \ is None:\n            self.ecost_subtree_sum = SegTree(lambda u, v: u + v, 0,\
    \ self.ecost_st)\n\n        l, r = self.into[v], self.out[v]\n        # \u9802\
    \u70B9v\u304B\u3089\u89AA\u3078\u306E\u8FBA\u3092\u9664\u53BB\u3059\u308B\u305F\
    \u3081\u306Bl\u3092\uFF11\u3064\u305A\u3089\u3059\n        return self.ecost_subtree_sum.prod(l\
    \ + 1, r)\n\n    def path_verticle_sum(self, u, v=None):\n        \"\"\"Path Query1\
    \ \u6839\u304B\u3089\u9802\u70B9u\u307E\u3067\u306E\u9802\u70B9\u306E\u5024\u306E\
    \u548C\"\"\"\n        if self.vcost_path_sum is None:\n            self.vcost_path_sum\
    \ = SegTree(lambda u, v: u + v, 0, self.vcost)\n        if v == None:\n      \
    \      return self.vcost_path_sum.prod(0, self.into[u] + 1)\n\n        \"\"\"\
    Path Query2 \u9802\u70B9u\u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u9802\u70B9\
    \u306E\u5024\u306E\u548C\"\"\"\n        if self.depth_min is None:\n\n       \
    \     def op(u, v):\n                return u if self.depth[u] <= self.depth[v]\
    \ else v\n\n            self.depth_min = SegTree(op, self.N, self.ET)\n      \
    \  a = self.lca(u, v)\n        return (\n            self.vcost_path_sum.prod(0,\
    \ self.into[u] + 1)\n            + self.vcost_path_sum.prod(0, self.into[v] +\
    \ 1)\n            - self.vcost_path_sum.prod(0, self.into[a])\n            - self.vcost_path_sum.prod(0,\
    \ self.into[a] + 1)\n        )\n\n    def path_edge_sum(self, v):\n        \"\"\
    \"Path Query3 \u6839\u304B\u3089\u9802\u70B9v\u307E\u3067\u306E\u8FBA\u306E\u5024\
    \u306E\u548C\"\"\"\n        if self.ecost_path_sum is None:\n            self.ecost_path_sum\
    \ = SegTree(lambda u, v: u + v, 0, self.ecost)\n\n        return self.ecost_path_sum.prod(0,\
    \ self.into[v] + 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/euler_tour.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/euler_tour.py
layout: document
title: Euler tour
---

木をDFS順に訪問し，その結果をさまざまな形式で格納していく.
木の情報を列に変換し，区間計算できるようにする．

参考 https://maspypy.com/euler-tour-のお勉強

- [ABC294G](https://atcoder.jp/contests/abc294/tasks/abc294_g)