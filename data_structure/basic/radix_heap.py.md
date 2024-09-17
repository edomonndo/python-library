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
  code: "class RadixHeap:\n    def __init__(self, n: int, min_key: int = 0, max_key:\
    \ int = 1 << 32):\n        width = max_key - min_key\n        assert width > 0\n\
    \        self.data = [[] for _ in range(width.bit_length() + 1)]\n        self.last\
    \ = 0\n        self.size = 0\n        self.used = [0] * n\n\n    def push(self,\
    \ x: int, key: int) -> bool:\n        if self.last <= x:\n            self.size\
    \ += 1\n            self.data[(x ^ self.last).bit_length()].append((x, key))\n\
    \            return True\n        return False\n\n    def pop(self) -> tuple[int,\
    \ int]:\n        if self.size <= 0:\n            raise IndexError\n        for\
    \ i, d in enumerate(self.data):\n            if d:\n                break\n  \
    \      if i == 0:\n            new_last, new_key = self.data[i].pop()\n      \
    \      self.used[new_key] = 1\n            self.size -= 1\n        else:\n   \
    \         new_last, new_key = min(d)\n            self.used[new_key] = 1\n   \
    \         for x, key in d:\n                if self.used[key]:\n             \
    \       self.size -= 1\n                    continue\n                self.data[(x\
    \ ^ new_last).bit_length()].append((x, key))\n            self.last = new_last\n\
    \            self.data[i] = []\n        return new_last, new_key\n\n    def __len__(self):\n\
    \        return self.size\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/radix_heap.py
  requiredBy: []
  timestamp: '2024-05-21 07:51:26+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/radix_heap.py
layout: document
redirect_from:
- /library/data_structure/basic/radix_heap.py
- /library/data_structure/basic/radix_heap.py.html
title: data_structure/basic/radix_heap.py
---
