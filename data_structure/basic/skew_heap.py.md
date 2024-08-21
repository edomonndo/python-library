---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/directed_mst.py
    title: "\u6700\u5C0F\u5168\u57DF\u6709\u5411\u6728"
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
  code: "from typing import Optional\n\n\nclass SHNode:\n    def __init__(self, val:\
    \ int):\n        self.l = None\n        self.r = None\n        self.val = val\n\
    \        self.lazy = 0\n\n    def lazy_propagate(self):\n        if self.l is\
    \ not None:\n            self.l.lazy += self.lazy\n        if self.r is not None:\n\
    \            self.r.lazy += self.lazy\n        self.val += self.lazy\n       \
    \ self.lazy = 0\n\n\nclass SkewHeap:\n    def __init__(self):\n        self.root\
    \ = None\n\n    def _meld(self, a: Optional[SHNode], b: Optional[SHNode]) -> SHNode:\n\
    \        if a is None:\n            return b\n        if b is None:\n        \
    \    return a\n        if b.val + b.lazy < a.val + a.lazy:\n            a, b =\
    \ b, a\n        a.lazy_propagate()\n        a.r = self._meld(a.r, b)\n       \
    \ a.l, a.r = a.r, a.l\n        return a\n\n    @property\n    def min(self) ->\
    \ int:\n        self.root.lazy_propagate()\n        return self.root.val\n\n \
    \   def push(self, val: int) -> None:\n        node = SHNode(val)\n        self.root\
    \ = self._meld(self.root, node)\n\n    def pop(self) -> int:\n        root = self.root\n\
    \        root.lazy_propagate()\n        self.root = self._meld(root.l, root.r)\n\
    \        return root.val\n\n    def meld(self, other: \"SkewHeap\") -> None:\n\
    \        self.root = self._meld(self.root, other.root)\n\n    def add(self, val:\
    \ int) -> None:\n        self.root.lazy += val\n\n    def empty(self) -> bool:\n\
    \        return self.root is None\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/skew_heap.py
  requiredBy:
  - graph/directed_mst.py
  timestamp: '2024-08-20 10:54:57+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/skew_heap.py
layout: document
redirect_from:
- /library/data_structure/basic/skew_heap.py
- /library/data_structure/basic/skew_heap.py.html
title: data_structure/basic/skew_heap.py
---
