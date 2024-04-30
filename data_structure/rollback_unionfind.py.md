---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: data_structure/offline_dynamic_connectivity.py
    title: data_structure/offline_dynamic_connectivity.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/persistent_unionfind.test.py
    title: test/library_checker/data_structure/persistent_unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class RollbackUnionFind:\n    def __init__(self, n: int):\n        self.n\
    \ = n\n        self.parent_or_size = [-1] * n\n        self.history = []\n   \
    \     self.sum = [0] * n\n        self.snap = 0\n\n    def merge(self, a: int,\
    \ b: int) -> bool:\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a,\
    \ self.n)\n        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n\
    \        x = self.leader(a)\n        y = self.leader(b)\n        if x == y:\n\
    \            self.history.append((-1, -1))\n            self.history.append((-1,\
    \ -1))\n            return False\n        if -self.parent_or_size[x] < -self.parent_or_size[y]:\n\
    \            x, y = y, x\n        self.history.append((x, self.parent_or_size[x]))\n\
    \        self.history.append((y, self.parent_or_size[y]))\n        self.parent_or_size[x]\
    \ += self.parent_or_size[y]\n        self.parent_or_size[y] = x\n        self.sum[x]\
    \ += self.sum[y]\n        return True\n\n    def same(self, a: int, b: int) ->\
    \ bool:\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n\
    \        assert 0 <= b < self.n, \"0<=b<n,b={0},n={1}\".format(b, self.n)\n  \
    \      return self.leader(a) == self.leader(b)\n\n    def leader(self, a):\n \
    \       assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n   \
    \     if self.parent_or_size[a] < 0:\n            return a\n        # \u7D4C\u8DEF\
    \u5727\u7E2E\u3057\u306A\u3044\n        # self.parent_or_size[a] = self.leader(self.parent_or_size[a])\n\
    \        return self.leader(self.parent_or_size[a])\n\n    def size(self, a: int)\
    \ -> int:\n        assert 0 <= a < self.n, \"0<=a<n,a={0},n={1}\".format(a, self.n)\n\
    \        return -self.parent_or_size[self.leader(a)]\n\n    def groups(self):\n\
    \        leader_buf = [0 for i in range(self.n)]\n        group_size = [0 for\
    \ i in range(self.n)]\n        for i in range(self.n):\n            leader_buf[i]\
    \ = self.leader(i)\n            group_size[leader_buf[i]] += 1\n        result\
    \ = [[] for i in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n        result2 = []\n        for i in range(self.n):\n\
    \            if len(result[i]) > 0:\n                result2.append(result[i])\n\
    \        return result2\n\n    def undo(self) -> None:\n        y, py = self.history.pop()\n\
    \        x, px = self.history.pop()\n        if y == -1:\n            return\n\
    \        if self.parent_or_size[x] != px:\n            self.sum[x] -= self.sum[y]\n\
    \        self.parent_or_size[y] = py\n        self.parent_or_size[x] = px\n  \
    \      return\n\n    def snapshot(self):\n        self.snap = len(self.history)\
    \ >> 1\n\n    def get_state(self):\n        return len(self.history) >> 1\n\n\
    \    def rollback(self, state=-1):\n        if state == -1:\n            state\
    \ = self.snap\n        state <<= 1\n        assert state <= len(self.history)\n\
    \        while state < len(self.history):\n            self.undo()\n        return\n\
    \n    def add(self, a: int, x: int) -> None:\n        while a >= 0:\n        \
    \    self.sum[a] += x\n            a = self.parent_or_size[a]\n\n    def group_sum(self,\
    \ a: int) -> int:\n        return self.sum[self.leader(a)]\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/rollback_unionfind.py
  requiredBy:
  - data_structure/offline_dynamic_connectivity.py
  timestamp: '2024-04-30 11:25:39+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/persistent_unionfind.test.py
documentation_of: data_structure/rollback_unionfind.py
layout: document
title: Rollback Union Find
---

UnionFindにundoやrollbackの操作を加えた構造．
代わりに経路圧縮をしていないため，通常のUnionFindの操作は$O(logN)$となる．

通常のUnionFindeに加えて以下の操作が可能である．

### undo()

直前の`merge`操作を取り消す． $O(1)$

### snapshot()

現在の状態を保存する. $O(1)$

### get_state()

現在の`merge`操作が行われた回数を返す. $O(1)$

### rollback(state: int=-1)

`state=-1`のとき，snapshot()で保存した状態に戻す.
`state!=-1`のとき，`merge`が`state`回操作されたときの状態に戻す．

