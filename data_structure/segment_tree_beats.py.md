---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
    title: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegtreeBeats:\n    inf = float(\"inf\")\n\n    def __init__(self, V):\n\
    \        self.n = len(V)\n        self.log = (self.n - 1).bit_length()\n     \
    \   self.size = size = 1 << self.log\n        size2 = size << 1\n        self.fmax\
    \ = [-self.inf] * size2\n        self.fmin = [self.inf] * size2\n        self.smax\
    \ = [-self.inf] * size2\n        self.smin = [self.inf] * size2\n        self.maxc\
    \ = [0] * size2\n        self.minc = [0] * size2\n        self.sum = [0] * size2\n\
    \        self.add = [0] * size2\n        self.upd = [self.inf] * size2\n     \
    \   self.up = []\n        self.down = []\n        self.lt = [0] * size2\n    \
    \    self.rt = [0] * size2\n        for i in range(self.n):\n            self.lt[size\
    \ + i] = i\n            self.rt[size + i] = i + 1\n        for i in reversed(range(size)):\n\
    \            self.lt[i] = self.lt[i << i]\n            self.rt[i] = self.rt[(i\
    \ << 1) | 1]\n        if V:\n            for i, x in enumerate(V):\n         \
    \       self.fmax[size + i] = x\n                self.fmin[size + i] = x\n   \
    \             self.maxc[size + i] = 1\n                self.minc[size + i] = 1\n\
    \                self.sum[size + i] = x\n            for i in range(1, size):\n\
    \                self._merge(i)\n\n    def _merge(self, i):\n        cl, cr =\
    \ i << 1, (i << 1) | 1\n        a, b = self.fmax[cl], self.fmax[cr]\n        if\
    \ a < b:\n            self.fmax[i] = b\n            self.maxc[i] = self.maxc[cr]\n\
    \            self.smax[i] = max(a, self.smax[cr])\n        elif a > b:\n     \
    \       self.fmax[i] = a\n            self.maxc[i] = self.maxc[cl]\n         \
    \   self.smax[i] = max(b, self.smax[cl])\n        else:\n            self.fmax[i]\
    \ = a\n            self.maxc[i] = self.maxc[cl] + self.maxc[cr]\n            self.smax[i]\
    \ = max(self.smax[cl], self.smax[cr])\n        a, b = self.fmin[cl], self.fmin[cr]\n\
    \        if a > b:\n            self.fmin[i] = b\n            self.minc[i] = self.minc[cr]\n\
    \            self.smin[i] = min(a, self.smin[cr])\n        elif a < b:\n     \
    \       self.fmin[i] = a\n            self.minc[i] = self.minc[cl]\n         \
    \   self.smin[i] = min(b, self.smin[cl])\n        else:\n            self.fmin[i]\
    \ = a\n            self.minc[i] = self.minc[cl] + self.minc[cr]\n            self.smin[i]\
    \ = min(self.smin[cl], self.smin[cr])\n\n    def _up_merge(self):\n        while\
    \ self.up:\n            i = self.up.pop()\n            self._merge(i)\n\n    def\
    \ _update(self, i, x):\n        a, b = self.lt[i], self.rt[i]\n        self.fmax[i]\
    \ = x\n        self.smax[i] = -self.inf\n        self.fmin[i] = x\n        self.smin[i]\
    \ = self.inf\n        self.maxc[i] = b - a\n        self.minc[i] = b - a\n   \
    \     self.sum[i] = x * (b - a)\n        self.add[i] = 0\n        self.upd[i]\
    \ = x\n\n    def _add(self, i, x):\n        self.fmax[i] += x\n        if self.smax[i]\
    \ != -self.inf:\n            self.smax[i] += x\n        self.fmin[i] += x\n  \
    \      if self.smin[i] != self.inf:\n            self.smin[i] += x\n        self.sum[i]\
    \ += x * (self.rt[i] - self.lt[i])\n        if self.upd[i] != self.inf:\n    \
    \        self.upd[i] += x\n        else:\n            self.add[i] += x\n\n   \
    \ def _chmax(self, i, x):\n        a = self.fmax[i]\n        self.sum[i] += self.maxc[i]\
    \ * (x - a)\n        self.fmax[i] = x\n        if a == self.fmin[i]:\n       \
    \     self.fmin[i] = x\n        elif a == self.smin[i]:\n            self.smin[i]\
    \ = x\n        a = self.upd[i]\n        if a != self.inf and x < a:\n        \
    \    self.upd[i] = x\n\n    def _chmin(self, i, x):\n        a = self.fmin[i]\n\
    \        self.sum[i] += self.minc[i] * (x - a)\n        self.fmin[i] = x\n   \
    \     if a == self.fmax[i]:\n            self.fmax[i] = x\n        elif a == self.smax[i]:\n\
    \            self.smax[i] = x\n        a = self.upd[i]\n        if a != self.inf\
    \ and x > a:\n            self.upd[i] = x\n\n    def _down_propagate(self, i):\n\
    \        if i >= self.size:\n            return\n        x = self.upd[i]\n   \
    \     cl, cr = i << 1, (i << 1) | 1\n        if x != self.inf:\n            self._update(cl,\
    \ x)\n            self._update(cr, x)\n            self.add[i] = 0\n        else:\n\
    \            x = self.add[i]\n            if x:\n                self._add(cl,\
    \ x)\n                self._add(cr, x)\n                self.add[i] = 0\n    \
    \        a, b = self.fmax[i], self.fmin[i]\n            if a < self.fmax[cl]:\n\
    \                self._chmax(cl, a)\n            if b > self.fmin[cl]:\n     \
    \           self._chmin(cl, b)\n            if a < self.fmax[cr]:\n          \
    \      self._chmax(cr, a)\n            if b > self.fmin[cr]:\n               \
    \ self._chmin(cr, b)\n\n    def range_ch_max(self, l, r, x):\n        assert 0\
    \ <= l and l < r and r <= self.n\n        self.down.append(1)\n        while self.down:\n\
    \            i = self.down.pop()\n            if r <= self.lt[i] or self.rt[i]\
    \ <= l or x <= self.fmin[i]:\n                continue\n            if l <= self.lt[i]\
    \ and self.rt[i] <= r and x < self.smin[i]:\n                self._chmin(i, x)\n\
    \                continue\n            self._down_propagate(i)\n            self.up.append(i)\n\
    \        self._up_merge()\n\n    def range_ch_min(self, l, r, x):\n        assert\
    \ 0 <= l and l < r and r <= self.n\n        self.down.append(1)\n        while\
    \ self.down:\n            i = self.down.pop()\n            if r <= self.lt[i]\
    \ or self.rt[i] <= l or x >= self.fmax[i]:\n                continue\n       \
    \     if l <= self.lt[i] and self.rt[i] <= r and x > self.smax[i]:\n         \
    \       self._chmax(i, x)\n                continue\n            self._down_propagate(i)\n\
    \            self.up.append(i)\n        self._up_merge()\n\n    def range_add(self,\
    \ l, r, x):\n        assert 0 <= l and l < r and r <= self.n\n        self.down.append(1)\n\
    \        while self.down:\n            i = self.down.pop()\n            if r <=\
    \ self.lt[i] or self.rt[i] <= l:\n                continue\n            if l <=\
    \ self.lt[i] and self.rt[i] <= r:\n                self._add(i, x)\n         \
    \       continue\n            self._down_propagate(i)\n            self.up.append(i)\n\
    \        self._up_merge()\n\n    def range_update(self, l, r, x):\n        assert\
    \ 0 <= l and l < r and r <= self.n\n        self.down.append(1)\n        while\
    \ self.down:\n            i = self.down.pop()\n            if r <= self.lt[i]\
    \ or self.rt[i] <= l:\n                continue\n            if l <= self.lt[i]\
    \ and self.rt[i] <= r:\n                self._update(i, x)\n                continue\n\
    \            self._down_propagate(i)\n            self.up.append(i)\n        self._up_merge()\n\
    \n    def get_max(self, l, r):\n        assert 0 <= l and l < r and r <= self.n\n\
    \        self.down.append(1)\n        res = -self.inf\n        while self.down:\n\
    \            i = self.down.pop()\n            if r <= self.lt[i] or self.rt[i]\
    \ <= l:\n                continue\n            if l <= self.lt[i] and self.rt[i]\
    \ <= r:\n                res = max(res, self.fmax[i])\n                continue\n\
    \            self._down_propagate(i)\n        return res\n\n    def get_min(self,\
    \ l, r):\n        assert 0 <= l and l < r and r <= self.n\n        self.down.append(1)\n\
    \        res = self.inf\n        while self.down:\n            i = self.down.pop()\n\
    \            if r <= self.lt[i] or self.rt[i] <= l:\n                continue\n\
    \            if l <= self.lt[i] and self.rt[i] <= r:\n                res = min(res,\
    \ self.fmin[i])\n                continue\n            self._down_propagate(i)\n\
    \        return res\n\n    def get_sum(self, l, r):\n        assert 0 <= l and\
    \ l < r and r <= self.n\n        self.down.append(1)\n        res = 0\n      \
    \  while self.down:\n            i = self.down.pop()\n            if r <= self.lt[i]\
    \ or self.rt[i] <= l:\n                continue\n            if l <= self.lt[i]\
    \ and self.rt[i] <= r:\n                res += self.sum[i]\n                continue\n\
    \            self._down_propagate(i)\n        return res\n\n    def set(self,\
    \ p, x):\n        assert 0 <= p and p < self.n\n        self.range_update(p, p\
    \ + 1, x)\n\n    def get(self, p):\n        assert 0 <= p and p < self.n\n   \
    \     return self.get_sum(p, p + 1)\n\n    def update(self, p, x):\n        assert\
    \ 0 <= p and p < self.n\n        self.range_update(p, p + 1, x)\n\n    def chmin(self,\
    \ p, x):\n        assert 0 <= p and p < self.n\n        self.range_chmin(p, p\
    \ + 1, x)\n\n    def chmax(self, p, x):\n        assert 0 <= p and p < self.n\n\
    \        self.range_chmax(p, p + 1, x)\n\n    def __str__(self):\n        return\
    \ str([self.get(i) for i in range(self.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segment_tree_beats.py
  requiredBy: []
  timestamp: '2024-02-09 16:12:14+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
documentation_of: data_structure/segment_tree_beats.py
layout: document
redirect_from:
- /library/data_structure/segment_tree_beats.py
- /library/data_structure/segment_tree_beats.py.html
title: data_structure/segment_tree_beats.py
---
