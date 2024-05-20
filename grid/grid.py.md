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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\nclass Grid:\n    def __init__(self, h,\
    \ w, C, sentinel=\"#\"):\n        self.h = h\n        self.w = w + 1\n       \
    \ self.hw = self.h * self.w\n        self.move = [1, self.w, -1, -self.w]\n  \
    \      self.C = []\n        for row in C:\n            for cell in row:\n    \
    \            self.C.append(cell)\n            self.C.append(sentinel)\n      \
    \  self.sentinel = sentinel\n\n    def __str__(self):\n        res = []\n    \
    \    for i in range(self.h):\n            for j in range(self.w - 1):\n      \
    \          res.append(self.C[i][j])\n            res.append(\"\\n\")\n       \
    \ return \"\".join(res)\n\n    def bfs(self, sx, sy, gx=None, gy=None):\n    \
    \    s = sx * self.w + sy\n        if gx is not None and gy is not None:\n   \
    \         g = gx * self.w + gy\n        else:\n            g = None\n        dist\
    \ = [-1] * self.hw\n        dist[s] = 0\n        q = deque([s])\n        while\
    \ q:\n            v = q.popleft()\n            if g and v == g:\n            \
    \    return dist[v]\n            for dv in self.move:\n                nv = v\
    \ + dv\n                if dist[nv] == -1 and self.C[nv] != self.sentinel:\n \
    \                   dist[nv] = dist[v] + 1\n                    q.append(nv)\n\
    \        return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: grid/grid.py
  requiredBy: []
  timestamp: '2023-11-02 17:09:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: grid/grid.py
layout: document
title: "\u30B0\u30EA\u30C3\u30C9"
---

グリッド上を探索する．
- 近傍は上下4方向
- 番兵をH+1行目，W+1列目に配置し，盤面外参照の判別を簡略化
- 高速化のため配列を１次元化
