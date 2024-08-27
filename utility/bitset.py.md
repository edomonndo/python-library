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
  code: "from itertools import zip_longest\nfrom typing import Union\n\n\nclass BitSet:\n\
    \n    def __init__(self, str_or_int: Union[str, int] = \"\") -> None:\n      \
    \  self._bin = str_or_int if isinstance(str_or_int, str) else bin(str_or_int)[2:]\n\
    \        self._buckets = []  # little endian\n        self._len = 0\n        for\
    \ i in range(0, len(self._bin), 63):\n            group = int(self._bin[i : i\
    \ + 63], 2)\n            self._buckets.append(group)\n            self._len +=\
    \ self._bit_count_ll(group)\n\n    @staticmethod\n    def _bit_count_ll(n: int)\
    \ -> int:\n        \"\"\"`O(1)` counts bit of int smaller than\"\"\"\n       \
    \ c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)\n        c =\
    \ (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)\n        c = (c &\
    \ 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)\n        c = (c & 0x00FF00FF00FF00FF)\
    \ + ((c >> 8) & 0x00FF00FF00FF00FF)\n        c = (c & 0x0000FFFF0000FFFF) + ((c\
    \ >> 16) & 0x0000FFFF0000FFFF)\n        c = (c & 0x00000000FFFFFFFF) + ((c >>\
    \ 32) & 0x00000000FFFFFFFF)\n        return c\n\n    def add(self, n: int) ->\
    \ bool:\n        row, col = n // 63, n % 63\n        if n in self:\n         \
    \   return False\n        self._ensure_capacity(row + 1)\n        self._buckets[row]\
    \ |= 1 << col\n        self._len += 1\n        return True\n\n    def discard(self,\
    \ n: int) -> bool:\n        row, col = n // 63, n % 63\n        if len(self._buckets)\
    \ <= row or n not in self:\n            return False\n        self._buckets[row]\
    \ &= ~(1 << col)\n        self._len += 1\n        return True\n\n    def _bit_count(self)\
    \ -> int:\n        res = 0\n        for bucket in self._buckets:\n           \
    \ res += self._bit_count_ll(bucket)\n        return res\n\n    def _ensure_capacity(self,\
    \ n: int) -> None:\n        if len(self._buckets) < n:\n            self._buckets.extend([0]\
    \ * (n - len(self._buckets)))\n\n    def __and__(self, other: \"BitSet\") -> int:\n\
    \        res = 0\n        for b1, b2 in zip(self._buckets, other._buckets):\n\
    \            res += self._bit_count_ll(b1 & b2)\n        return res\n\n    def\
    \ __or__(self, other: \"BitSet\") -> int:\n        res = 0\n        for b1, b2\
    \ in zip_longest(self._buckets, other._buckets, fillvalue=0):\n            res\
    \ += self._bit_count_ll(b1 | b2)\n        return res\n\n    def __xor__(self,\
    \ other: \"BitSet\") -> int:\n        res = 0\n        for b1, b2 in zip_longest(self._buckets,\
    \ other._buckets, fillvalue=0):\n            res += self._bit_count_ll(b1 ^ b2)\n\
    \        return res\n\n    def __contains__(self, n: int) -> bool:\n        row,\
    \ col = n // 63, n % 63\n        return len(self._buckets) > row and not not (self._buckets[row]\
    \ & (1 << col))\n\n    def __repr__(self) -> str:\n        return f\"BitSet({self._bin})\"\
    \n\n    def __len__(self) -> int:\n        return self._len\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bitset.py
  requiredBy: []
  timestamp: '2024-08-27 13:47:08+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bitset.py
layout: document
title: Bitset
---
