---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/shortest_paths.py
    title: Shortest paths
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
  code: "class LefitistHeap:\n    def __init__(self, rank: int, key: int, value: int,\
    \ left: int, right: int):\n        self.rank = rank\n        self.key = key\n\
    \        self.value = value\n        self.left = left\n        self.right = right\n\
    \n    @staticmethod\n    def insert(a: \"LefitistHeap\", key: int, value: int):\n\
    \        if not a or key < a.key:\n            return LefitistHeap(1, key, value,\
    \ a, None)\n        l, r = a.left, LefitistHeap.insert(a.right, key, value)\n\
    \        if not l or r.rank > l.rank:\n            l, r = r, l\n        return\
    \ LefitistHeap((r.rank if r else 0) + 1, a.key, a.value, l, r)\n\n    def __lt__(self,\
    \ _):\n        return False\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/leftist_heap.py
  requiredBy:
  - graph/shortest_paths.py
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/leftist_heap.py
layout: document
redirect_from:
- /library/data_structure/basic/leftist_heap.py
- /library/data_structure/basic/leftist_heap.py.html
title: data_structure/basic/leftist_heap.py
---
