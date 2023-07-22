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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class WeightedUnionFind:\n    def __init__(self, n, W=[]):\n        self.n\
    \ = n\n        self.parents = [-1] * n\n        self.ng = [False] * n\n      \
    \  self.weight = [0] * n  # W_i - W_{P_i}\n        self.group = n\n        if\
    \ W:\n            self.W = W[:]\n        else:\n            self.W = [0] * n\n\
    \n    def find(self, x):\n        if self.parents[x] < 0:\n            return\
    \ x\n        else:\n            p = self.find(self.parents[x])\n            self.weight[x]\
    \ += self.weight[self.parents[x]]\n            self.parents[x] = p\n         \
    \   return self.parents[x]\n\n    # x = y + w\n    def union(self, x, y, w):\n\
    \        xp = self.find(x)\n        yp = self.find(y)\n        w -= self.weight[x]\n\
    \        x = xp\n        w += self.weight[y]\n        y = yp\n\n        if x ==\
    \ y:\n            if w != 0:\n                self.ng[x] = True\n            return\
    \ False\n        self.group -= 1\n\n        if self.parents[x] > self.parents[y]:\n\
    \            w *= -1\n            x, y = y, x\n\n        self.parents[x] += self.parents[y]\n\
    \        self.weight[y] = -w\n        self.parents[y] = x\n        self.ng[x]\
    \ |= self.ng[y]\n        return True\n\n    def size(self, x):\n        return\
    \ -self.parents[self.find(x)]\n\n    def same(self, x, y):\n        return self.find(x)\
    \ == self.find(y)\n\n    def diff(self, x, y):\n        if not self.same(x, y):\n\
    \            return None\n        else:\n            return self.weight[x] - self.weight[y]\n\
    \n    def members(self, x):\n        root = self.find(x)\n        return [i for\
    \ i in range(self.n) if self.find(i) == root]\n\n    def roots(self):\n      \
    \  return [i for i, x in enumerate(self.parents) if x < 0]\n\n    def group_count(self):\n\
    \        return self.group\n\n    def all_group_members(self):\n        dic =\
    \ {r: [] for r in self.roots()}\n        for i in range(self.n):\n           \
    \ dic[self.find(i)].append(i)\n        return dic\n\n    def __str__(self):\n\
    \        return \"\\n\".join(\"{}: {}\".format(r, self.members(r)) for r in self.roots())\n\
    \n    def add(self, a, b):\n        a = self.find(a)\n        self.W[a] += b\n\
    \n    def get(self, a):\n        p = self.find(a)\n        return self.W[p] +\
    \ self.diff(a, p)\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/weighted_union_find.py
  requiredBy: []
  timestamp: '2023-07-23 00:15:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/weighted_union_find.py
layout: document
redirect_from:
- /library/data_structure/weighted_union_find.py
- /library/data_structure/weighted_union_find.py.html
title: data_structure/weighted_union_find.py
---
