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
  code: "from atcoder.segtree import SegTree\nclass EulerTour:\n    def __init__(self,\
    \ G, root, vcost):\n        N = len(G)\n        self.N = N\n        self.ET =\
    \ []\n        self.into = [0] * N\n        self.out = [0] * N\n        # For LCA\n\
    \        self.parent = [-1] * N\n        self.depth = [N] * (N+1)\n        # For\
    \ Path Query\n        self.vcost = []\n        self.ecost = []\n        # For\
    \ Range Sum Query\n        self.vcost_st = []\n        self.ecost_st = []\n\n\
    \        # \u975E\u518D\u5E30DFS\n        stack = [(root, -1, 0)]\n        while\
    \ stack:\n            v, p, weight = stack.pop()\n            if v >= 0:\n   \
    \             self.into[v] = len(self.ET)\n                self.ET.append(v)\n\
    \                self.depth[v]=0 if p==-1 else self.depth[p]+1\n             \
    \   self.vcost.append(vcost[v])\n                self.ecost.append(weight)\n \
    \               self.vcost_st.append(vcost[v])\n                self.ecost_st.append(weight)\n\
    \                self.out[v] = len(self.ET)\n                for u,w in G[v]:\n\
    \                    if u==p:continue\n                    self.parent[u] = v\n\
    \                    stack.append((~v, u, -w))\n                    stack.append((u,\
    \ v, w))\n            else:\n                v = ~v\n                self.ET.append(v)\n\
    \                self.vcost.append(-vcost[v])\n                self.ecost.append(weight)\n\
    \                self.vcost_st.append(0)\n                self.ecost_st.append(0)\n\
    \                self.out[v] = len(self.ET)\n        \n        def op(u, v):\n\
    \            return u if self.depth[u] <= self.depth[v] else v\n        self.depth_min\
    \ = SegTree(op, N, self.ET)\n        self.rv_path = SegTree(lambda u, v: u+v,\
    \ 0, self.ecost)\n    \n    def lca(self, u, v):\n        \"\"\"u\u3068v\u306E\
    \u6700\u8FD1\u5171\u901A\u7956\u5148\"\"\"\n        if self.into[u] > self.into[v]:\
    \ u, v = v, u\n        return self.depth_min.prod(self.into[u], self.out[v])\n\
    \n    def dist(self, u, v):\n        \"\"\"u\u3068v\u306E\u8DDD\u96E2\"\"\"\n\
    \        a = self.lca(u, v)\n        return self.rv_path.prod(0, self.out[u])+self.rv_path.prod(0,\
    \ self.out[v])-2*self.rv_path.prod(0, self.out[a])\n    \n    def update_parent_edge(self,\
    \ v, w):\n        \"\"\"v\u3068\u305D\u306E\u89AA\u3092\u7E4B\u3050\u8FBA\u306E\
    \u91CD\u307F\u3092w\u306B\u66F4\u65B0\"\"\"\n        self.rv_path.set(self.into[v],\
    \ w)\n        self.rv_path.set(self.out[v], -w)\n    \n    def is_ancestor(self,\
    \ u, v): \n        \"\"\"u\u306Fv\u306E\u7956\u5148\u304B\uFF1F\"\"\"\n      \
    \  return self.into[u] <= self.into[v] < self.out[u]"
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