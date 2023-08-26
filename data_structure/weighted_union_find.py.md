---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/aoj/dsl_1_b_weighted_union_find.test.py
    title: test/aoj/dsl_1_b_weighted_union_find.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class WeightedUnionFind:\n    def __init__(self, n, W=None):\n        self.n\
    \ = n\n        self.parent_or_size = [-1] * n\n        self.ng = [False] * n\n\
    \        self.weight = [0] * n  # W_i - W_{P_i}\n        self.group = n\n    \
    \    if W is None:\n            self.W = [0] * n\n        else:\n            self.W\
    \ = W\n\n    # a = b + w\n    def merge(self, a, b, w):\n        assert 0 <= a\
    \ < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n        assert 0 <= b <\
    \ self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n        x = self.leader(a)\n\
    \        y = self.leader(b)\n        w -= self.weight[a]\n        w += self.weight[b]\n\
    \n        if x == y:\n            if w != 0:\n                self.ng[x] = True\n\
    \            return x\n        self.group -= 1\n        if -self.parent_or_size[x]\
    \ < -self.parent_or_size[y]:\n            w *= -1\n            x, y = y, x\n \
    \       self.parent_or_size[x] += self.parent_or_size[y]\n        self.parent_or_size[y]\
    \ = x\n        self.weight[y] = -w\n        self.ng[x] |= self.ng[y]\n       \
    \ return x\n\n    def same(self, a, b):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\"\
    .format(a, self.n)\n        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b,\
    \ self.n)\n        return self.leader(a) == self.leader(b)\n\n    def leader(self,\
    \ a):\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n\
    \        if self.parent_or_size[a] < 0:\n            return a\n        self.weight[a]\
    \ += self.weight[self.parent_or_size[a]]\n        self.parent_or_size[a] = self.leader(self.parent_or_size[a])\n\
    \        return self.parent_or_size[a]\n\n    def size(self, a):\n        assert\
    \ 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n        return -self.parent_or_size[self.leader(a)]\n\
    \n    def group_count(self):\n        return self.group\n\n    def groups(self):\n\
    \        leader_buf = [0 for i in range(self.n)]\n        group_size = [0 for\
    \ i in range(self.n)]\n        for i in range(self.n):\n            leader_buf[i]\
    \ = self.leader(i)\n            group_size[leader_buf[i]] += 1\n        result\
    \ = [[] for i in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n        result2 = []\n        for i in range(self.n):\n\
    \            if len(result[i]) > 0:\n                result2.append(result[i])\n\
    \        return result2\n\n    def diff(self, a, b):\n        if not self.same(a,\
    \ b):\n            return None\n        else:\n            return self.weight[a]\
    \ - self.weight[b]\n\n    def add(self, a, b):\n        a = self.leader(a)\n \
    \       self.W[a] += b\n\n    def get(self, a):\n        p = self.leader(a)\n\
    \        return self.W[p] + self.diff(a, p)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/weighted_union_find.py
  requiredBy: []
  timestamp: '2023-08-26 10:33:44+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/aoj/dsl_1_b_weighted_union_find.test.py
documentation_of: data_structure/weighted_union_find.py
layout: document
title: "\u91CD\u307F\u4ED8\u304D Union Find"
---

未履修
別名：ポテンシャルUnion Find.