---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/persistent_queue.test.py
    title: Persistent Queue
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentQueue:\n    def __init__(self, number_of_query: int):\n \
    \       self.q = number_of_query\n        self.h = self.q.bit_length()\n     \
    \   self.idx = -1\n        self.val = [0] * (self.q + 1)\n        self.cnt = [0]\
    \ * (self.q + 1)\n        self.par = [[None] * (self.q + 1) for _ in range(self.h)]\n\
    \n    def append(self, t: int, x):\n        \"\"\"Add x to version t.\"\"\"\n\
    \        assert -1 <= t <= self.idx\n        self.idx += 1\n        assert self.idx\
    \ < self.q\n        self.val[self.idx] = x\n        self.cnt[self.idx] = self.cnt[t]\
    \ + 1\n        self.par[0][self.idx] = t\n        h, p = 1, t\n        while p:\n\
    \            p = self.par[h][self.idx] = self.par[h - 1][p]\n            h +=\
    \ 1\n\n    def popleft(self, t: int):\n        \"\"\"Pop element from version\
    \ t.\"\"\"\n        assert -1 <= t <= self.idx\n        self.idx += 1\n      \
    \  assert self.idx < self.q\n        self.val[self.idx] = self.val[t]\n      \
    \  self.cnt[self.idx] = self.cnt[t] - 1\n        p = self.par[0][self.idx] = self.par[0][t]\n\
    \        h = 1\n        while p:\n            p = self.par[h][self.idx] = self.par[h\
    \ - 1][p]\n            h += 1\n        p = self.idx\n        c = self.cnt[p]\n\
    \        for i in range(self.h):\n            if (c >> i) & 1:\n             \
    \   p = self.par[i][p]\n        return self.val[p]\n"
  dependsOn: []
  isVerificationFile: false
  path: persistent_data_structure/persistent_queue.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/persistent_queue.test.py
documentation_of: persistent_data_structure/persistent_queue.py
layout: document
title: "\u6C38\u7D9A\u30AD\u30E5\u30FC"
---
