---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
    title: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegtreeBeats:\n    pINF = 1 << 60\n    nINF = -1 << 60\n\n    def __init__(self,\
    \ arr: list = []) -> None:\n        n = len(arr)\n        size = 1 << (n - 1).bit_length()\n\
    \        self.size = size\n        size2 = size << 1\n        self.fmax = [self.nINF]\
    \ * (size2)\n        self.fmin = [self.pINF] * (size2)\n        self.smax = [self.nINF]\
    \ * (size2)\n        self.smin = [self.pINF] * (size2)\n        self.maxc = [0]\
    \ * (size2)\n        self.minc = [0] * (size2)\n        self.sum = [0] * (size2)\n\
    \        self.add = [0] * (size2)\n        self.upd = [self.pINF] * (size2)\n\
    \        self.up = []\n        self.down = []\n        self.lt = [0] * (size2)\n\
    \        self.rt = [0] * (size2)\n        for i in range(size):\n            self.lt[size\
    \ + i] = i\n            self.rt[size + i] = i + 1\n        for i in range(size)[::-1]:\n\
    \            self.lt[i] = self.lt[i << 1]\n            self.rt[i] = self.rt[i\
    \ << 1 | 1]\n        if arr:\n            for i, a in enumerate(arr):\n      \
    \          self.fmax[size + i] = a\n                self.fmin[size + i] = a\n\
    \                self.maxc[size + i] = 1\n                self.minc[size + i]\
    \ = 1\n                self.sum[size + i] = a\n            for i in range(1, size)[::-1]:\
    \  # self.merge(i)\n                i2, i2p1 = i << 1, i << 1 | 1\n          \
    \      self.sum[i] = self.sum[i2] + self.sum[i2p1]\n                a, b = self.fmax[i2],\
    \ self.fmax[i2p1]\n                if a < b:\n                    self.fmax[i]\
    \ = b\n                    self.maxc[i] = self.maxc[i2p1]\n                  \
    \  self.smax[i] = max(a, self.smax[i2p1])\n                elif a > b:\n     \
    \               self.fmax[i] = a\n                    self.maxc[i] = self.maxc[i2]\n\
    \                    self.smax[i] = max(self.smax[i2], b)\n                else:\n\
    \                    self.fmax[i] = a\n                    self.maxc[i] = self.maxc[i2]\
    \ + self.maxc[i2p1]\n                    self.smax[i] = max(self.smax[i2], self.smax[i2p1])\n\
    \n                a, b = self.fmin[i2], self.fmin[i2p1]\n                if a\
    \ > b:\n                    self.fmin[i] = b\n                    self.minc[i]\
    \ = self.minc[i2p1]\n                    self.smin[i] = min(a, self.smin[i2p1])\n\
    \                elif a < b:\n                    self.fmin[i] = a\n         \
    \           self.minc[i] = self.minc[i2]\n                    self.smin[i] = min(self.smin[i2],\
    \ b)\n                else:\n                    self.fmin[i] = a\n          \
    \          self.minc[i] = self.minc[i2] + self.minc[i2p1]\n                  \
    \  self.smin[i] = min(self.smin[i2], self.smin[i2p1])\n\n    def _up_merge(self):\n\
    \        while self.up:  # self.merge(self.up.pop())\n            k = self.up.pop()\n\
    \            k2, k2p1 = k << 1, k << 1 | 1\n            self.sum[k] = self.sum[k2]\
    \ + self.sum[k2p1]\n            a, b = self.fmax[k2], self.fmax[k2p1]\n      \
    \      if a < b:\n                self.fmax[k] = b\n                self.maxc[k]\
    \ = self.maxc[k2p1]\n                self.smax[k] = max(a, self.smax[k2p1])\n\
    \            elif a > b:\n                self.fmax[k] = a\n                self.maxc[k]\
    \ = self.maxc[k2]\n                self.smax[k] = max(self.smax[k2], b)\n    \
    \        else:\n                self.fmax[k] = a\n                self.maxc[k]\
    \ = self.maxc[k2] + self.maxc[k2p1]\n                self.smax[k] = max(self.smax[k2],\
    \ self.smax[k2p1])\n\n            a, b = self.fmin[k2], self.fmin[k2p1]\n    \
    \        if a > b:\n                self.fmin[k] = b\n                self.minc[k]\
    \ = self.minc[k2p1]\n                self.smin[k] = min(a, self.smin[k2p1])\n\
    \            elif a < b:\n                self.fmin[k] = a\n                self.minc[k]\
    \ = self.minc[k2]\n                self.smin[k] = min(self.smin[k2], b)\n    \
    \        else:\n                self.fmin[k] = a\n                self.minc[k]\
    \ = self.minc[k2] + self.minc[k2p1]\n                self.smin[k] = min(self.smin[k2],\
    \ self.smin[k2p1])\n\n    def _down_propagate(self, k):\n        if self.size\
    \ <= k:\n            pass  # ?\n        else:\n            a = self.upd[k]\n \
    \           if a != self.pINF:\n                self._update(k << 1, a)\n    \
    \            self._update(k << 1 | 1, a)\n                self.upd[k] = self.pINF\n\
    \            else:\n                a = self.add[k]\n                if a:\n \
    \                   self._add(k << 1, a)\n                    self._add(k << 1\
    \ | 1, a)\n                    self.add[k] = 0\n                a, b = self.fmax[k],\
    \ self.fmin[k]\n                if a < self.fmax[k << 1]:\n                  \
    \  self._chmax(k << 1, a)\n                if self.fmin[k << 1] < b:\n       \
    \             self._chmin(k << 1, b)\n                if a < self.fmax[k << 1\
    \ | 1]:\n                    self._chmax(k << 1 | 1, a)\n                if self.fmin[k\
    \ << 1 | 1] < b:\n                    self._chmin(k << 1 | 1, b)\n        self.down.append(k\
    \ << 1)\n        self.down.append(k << 1 | 1)\n\n    def _update(self, k, x):\n\
    \        a, b = self.lt[k], self.rt[k]\n        self.fmax[k] = x\n        self.smax[k]\
    \ = self.nINF\n        self.fmin[k] = x\n        self.smin[k] = self.pINF\n  \
    \      self.maxc[k] = b - a\n        self.minc[k] = b - a\n        self.sum[k]\
    \ = x * (b - a)\n        self.add[k] = 0\n        self.upd[k] = x\n\n    def _add(self,\
    \ k, x):\n        self.fmax[k] += x\n        if self.smax[k] != self.nINF:\n \
    \           self.smax[k] += x\n        self.fmin[k] += x\n        if self.smin[k]\
    \ != self.pINF:\n            self.smin[k] += x\n        self.sum[k] += x * (self.rt[k]\
    \ - self.lt[k])\n        if self.upd[k] != self.pINF:\n            self.upd[k]\
    \ += x\n        else:\n            self.add[k] += x\n\n    def _chmax(self, k,\
    \ x):\n        a = self.fmax[k]\n        self.sum[k] += (x - a) * self.maxc[k]\n\
    \        if a == self.fmin[k]:\n            self.fmax[k] = x\n            self.fmin[k]\
    \ = x\n        elif a == self.smin[k]:\n            self.fmax[k] = x\n       \
    \     self.smin[k] = x\n        else:\n            self.fmax[k] = x\n        a\
    \ = self.upd[k]\n        if a != self.pINF and x < a:\n            self.upd[k]\
    \ = x\n\n    def _chmin(self, k, x):\n        a = self.fmin[k]\n        self.sum[k]\
    \ += (x - a) * self.minc[k]\n        if a == self.fmax[k]:\n            self.fmin[k]\
    \ = x\n            self.fmax[k] = x\n        elif a == self.smax[k]:\n       \
    \     self.fmin[k] = x\n            self.smax[k] = x\n        else:\n        \
    \    self.fmin[k] = x\n        a = self.upd[k]\n        if a != self.pINF and\
    \ a < x:\n            self.upd[k] = x\n\n    def range_chmax(self, l, r, x):\n\
    \        self.down.append(1)\n        while self.down:\n            k = self.down.pop()\n\
    \            if r <= self.lt[k] or self.rt[k] <= l or x <= self.fmin[k]:\n   \
    \             continue\n            if l <= self.lt[k] and self.rt[k] <= r and\
    \ x < self.smin[k]:\n                self._chmin(k, x)\n                continue\n\
    \            self._down_propagate(k)\n            self.up.append(k)\n        self._up_merge()\n\
    \n    def range_chmin(self, l, r, x):\n        self.down.append(1)\n        while\
    \ self.down:\n            k = self.down.pop()\n            if r <= self.lt[k]\
    \ or self.rt[k] <= l or self.fmax[k] <= x:\n                continue\n       \
    \     if l <= self.lt[k] and self.rt[k] <= r and self.smax[k] < x:\n         \
    \       self._chmax(k, x)\n                continue\n            self._down_propagate(k)\n\
    \            self.up.append(k)\n        self._up_merge()\n\n    def range_add(self,\
    \ l, r, x):\n        self.down.append(1)\n        while self.down:\n         \
    \   k = self.down.pop()\n            if r <= self.lt[k] or self.rt[k] <= l:\n\
    \                continue\n            if l <= self.lt[k] and self.rt[k] <= r:\n\
    \                self._add(k, x)\n                continue\n            self._down_propagate(k)\n\
    \            self.up.append(k)\n        self._up_merge()\n\n    def range_update(self,\
    \ l, r, x):\n        self.down.append(1)\n        while self.down:\n         \
    \   k = self.down.pop()\n            if r <= self.lt[k] or self.rt[k] <= l:\n\
    \                continue\n            if l <= self.lt[k] and self.rt[k] <= r:\n\
    \                self._update(k, x)\n                continue\n            self._down_propagate(k)\n\
    \            self.up.append(k)\n        self._up_merge()\n\n    def get_max(self,\
    \ l, r):\n        self.down.append(1)\n        v = self.nINF\n        while self.down:\n\
    \            k = self.down.pop()\n            if r <= self.lt[k] or self.rt[k]\
    \ <= l:\n                continue\n            if l <= self.lt[k] and self.rt[k]\
    \ <= r:\n                v = max(v, self.fmax[k])\n                continue\n\
    \            self._down_propagate(k)\n        return v\n\n    def get_min(self,\
    \ l, r):\n        self.down.append(1)\n        v = self.pINF\n        while self.down:\n\
    \            k = self.down.pop()\n            if r <= self.lt[k] or self.rt[k]\
    \ <= l:\n                continue\n            if l <= self.lt[k] and self.rt[k]\
    \ <= r:\n                v = min(v, self.fmin[k])\n                continue\n\
    \            self._down_propagate(k)\n        return v\n\n    def get_sum(self,\
    \ l, r):\n        self.down.append(1)\n        v = 0\n        while self.down:\n\
    \            k = self.down.pop()\n            if r <= self.lt[k] or self.rt[k]\
    \ <= l:\n                continue\n            if l <= self.lt[k] and self.rt[k]\
    \ <= r:\n                v += self.sum[k]\n                continue\n        \
    \    self._down_propagate(k)\n        return v\n\n    def get(self, k):\n    \
    \    return self.get_sum(k, k + 1)\n\n    def add(self, k, x):\n        self.range_add(k,\
    \ k + 1, x)\n\n    def update(self, k, x):\n        self.range_update(k, k + 1,\
    \ x)\n\n    def chmin(self, k, x):\n        self.range_chmin(k, k + 1, x)\n\n\
    \    def chmax(self, k, x):\n        self.range_chmax(k, k + 1, x)\n\n    def\
    \ __str__(self):\n        return str([self.get(i) for i in range(self.n)])\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/segment_tree_beats.py
  requiredBy: []
  timestamp: '2024-02-09 17:45:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
documentation_of: data_structure/segment_tree_beats.py
layout: document
redirect_from:
- /library/data_structure/segment_tree_beats.py
- /library/data_structure/segment_tree_beats.py.html
title: data_structure/segment_tree_beats.py
---
