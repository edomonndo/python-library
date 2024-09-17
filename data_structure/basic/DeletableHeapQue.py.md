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
  code: "from collections import defaultdict\nfrom heapq import *\n\n\nclass DeletableMaxHeapQ:\n\
    \    def __init__(self, X):\n        self.H = []\n        self.HC = defaultdict(int)\n\
    \        if X:\n            self.H = X\n            heapify(self.H)\n        \
    \    for x in X:\n                self.HC[x] += 1\n\n    def hpush(self, x):\n\
    \        heappush(self.H, -x)\n        self.HC[x] += 1\n\n    def hpop(self):\n\
    \        t = -heappop(self.H)\n        while not self.HC[t]:\n            t =\
    \ -heappop(self.H)\n        self.HC[t] -= 1\n        return t\n\n    def hmax(self):\n\
    \        t = -self.H[0]\n        while not self.HC[t]:\n            heappop(self.H)\n\
    \            t = -self.H[0]\n        return t\n\n    def hdel(self, x):\n    \
    \    assert self.HC[x] > 0\n        self.HC[x] -= 1\n\n    def __contains__(self,\
    \ x):\n        return 1 if x in self.HC and self.HC[x] else 0\n\n\nclass DeletableMinHeapQ:\n\
    \    def __init__(self, X):\n        self.H = []\n        self.HC = defaultdict(int)\n\
    \        if X:\n            self.H = X\n            heapify(self.H)\n        \
    \    for x in X:\n                self.HC[x] += 1\n\n    def hpush(self, x):\n\
    \        heappush(self.H, x)\n        self.HC[x] += 1\n\n    def hpop(self):\n\
    \        t = heappop(self.H)\n        while not self.HC[t]:\n            t = heappop(self.H)\n\
    \        self.HC[t] -= 1\n        return t\n\n    def hmin(self):\n        t =\
    \ self.H[0]\n        while not self.HC[t]:\n            heappop(self.H)\n    \
    \        t = self.H[0]\n        return t\n\n    def hdel(self, x):\n        assert\
    \ self.HC[x] > 0\n        self.HC[x] -= 1\n\n    def __contains__(self, x):\n\
    \        return 1 if x in self.HC and self.HC[x] else 0\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/DeletableHeapQue.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/DeletableHeapQue.py
layout: document
redirect_from:
- /library/data_structure/basic/DeletableHeapQue.py
- /library/data_structure/basic/DeletableHeapQue.py.html
title: data_structure/basic/DeletableHeapQue.py
---
