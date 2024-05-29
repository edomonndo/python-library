---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: data_structure/range_set_range_composite.py
    title: data_structure/range_set_range_composite.py
  - icon: ':warning:'
    path: test/library_checker/data_structure/predecessor_problem.py
    title: test/library_checker/data_structure/predecessor_problem.py
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
  code: "from array import array\n\n\nclass WordsizeTreeSet:\n\n    def __init__(self,\
    \ n: int, a: list[int] = None):\n        assert n > 0\n        self.n = n\n  \
    \      data = []\n        size = 0\n        if a:\n            n >>= 5\n     \
    \       A = array(\"I\", bytes(4 * (n + 1)))\n            for a_ in a:\n     \
    \           assert 0 <= a_ < self.n\n                if A[a_ >> 5] >> (a_ & 31)\
    \ & 1 == 0:\n                    size += 1\n                    A[a_ >> 5] |=\
    \ 1 << (a_ & 31)\n            data.append(A)\n            while n:\n         \
    \       a = array(\"I\", bytes(4 * ((n >> 5) + 1)))\n                for i in\
    \ range(n + 1):\n                    if A[i]:\n                        a[i >>\
    \ 5] |= 1 << (i & 31)\n                data.append(a)\n                A = a\n\
    \                n >>= 5\n        else:\n            while n:\n              \
    \  n >>= 5\n                data.append(array(\"I\", bytes(4 * (n + 1))))\n  \
    \      self.data = data\n        self.size = size\n\n    def add(self, x: int)\
    \ -> bool:\n        data = self.data\n        if data[0][x >> 5] >> (x & 31) &\
    \ 1:\n            return False\n        for a in data:\n            a[x >> 5]\
    \ |= 1 << (x & 31)\n            x >>= 5\n        self.size += 1\n        return\
    \ True\n\n    def discard(self, x: int) -> bool:\n        data = self.data\n \
    \       if data[0][x >> 5] >> (x & 31) & 1 == 0:\n            return False\n \
    \       self.size -= 1\n        for a in data:\n            a[x >> 5] &= ~(1 <<\
    \ (x & 31))\n            x >>= 5\n            if a[x]:\n                break\n\
    \        return True\n\n    def ge(self, x: int) -> int:\n        assert 0 <=\
    \ x < self.n\n        d = 0\n        data = self.data\n        while True:\n \
    \           if d >= len(data) or x >> 5 >= len(data[d]):\n                return\
    \ -1\n            m = data[d][x >> 5] & ((~0) << (x & 31))\n            if m ==\
    \ 0:\n                d += 1\n                x = (x >> 5) + 1\n            else:\n\
    \                x = (x >> 5 << 5) + (m & -m).bit_length() - 1\n             \
    \   if d == 0:\n                    break\n                x <<= 5\n         \
    \       d -= 1\n        return x\n\n    def gt(self, x: int) -> int:\n       \
    \ assert 0 <= x < self.n\n        if x + 1 == self.n:\n            return -1\n\
    \        return self.ge(x + 1)\n\n    def le(self, x: int) -> int:\n        assert\
    \ 0 <= x < self.n\n        d = 0\n        data = self.data\n        while True:\n\
    \            if x < 0 or d >= len(data):\n                return -1\n        \
    \    m = data[d][x >> 5] & ~((~1) << (x & 31))\n            if m == 0:\n     \
    \           d += 1\n                x = (x >> 5) - 1\n            else:\n    \
    \            x = (x >> 5 << 5) + m.bit_length() - 1\n                if d == 0:\n\
    \                    break\n                x <<= 5\n                x += 31\n\
    \                d -= 1\n        return x\n\n    def lt(self, x: int) -> int:\n\
    \        assert 0 <= x < self.n\n        if x - 1 == 0:\n            return -1\n\
    \        return self.le(x - 1)\n\n    def member(self, x: int) -> int:\n     \
    \   return self.data[0][x >> 5] >> (x & 31) & 1\n\n    __contains__ = member\n\
    \n    def __len__(self):\n        return self.size\n"
  dependsOn: []
  isVerificationFile: false
  path: data_structure/basic/wordsize_tree_set.py
  requiredBy:
  - test/library_checker/data_structure/predecessor_problem.py
  - data_structure/range_set_range_composite.py
  timestamp: '2024-05-29 13:44:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: data_structure/basic/wordsize_tree_set.py
layout: document
redirect_from:
- /library/data_structure/basic/wordsize_tree_set.py
- /library/data_structure/basic/wordsize_tree_set.py.html
title: data_structure/basic/wordsize_tree_set.py
---
