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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.12/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import defaultdict\nimport bisect\n\n\nclass KDTree:\n \
    \   def __init__(self, N, XY):\n        self.N = N\n        self.id = {v: i for\
    \ i, v in enumerate(XY)}\n        data = defaultdict(list)\n        for i, (x,\
    \ y) in enumerate(XY):\n            data[x].append(y)\n        for ys in data.values():\n\
    \            ys.sort()\n        self.X = sorted(data.keys())\n        self.data\
    \ = data\n\n    def query(self, sx, sy, tx, ty):\n        res = []\n        l\
    \ = bisect.bisect_left(self.X, sx)\n        r = bisect.bisect_right(self.X, tx)\n\
    \        for x in self.X[l:r]:\n            yl = bisect.bisect_left(self.data[x],\
    \ sy)\n            yr = bisect.bisect_right(self.data[x], ty)\n            for\
    \ y in self.data[x][yl:yr]:\n                res.append(self.id[(x, y)])\n   \
    \     return res\n"
  dependsOn: []
  isVerificationFile: false
  path: geometory/kd_tree.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: geometory/kd_tree.py
layout: document
title: KD tree
---
