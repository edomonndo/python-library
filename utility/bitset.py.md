---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':x:'
    path: linear_algebra/bit_matrix.py
    title: linear_algebra/bit_matrix.py
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
  code: "class BitSet:\n    \"\"\"Bit size: 63\"\"\"\n\n    def __init__(self, n:\
    \ int):\n        self.n = n\n        self.buf = [0] * ((n + 62) // 63)\n\n   \
    \ @staticmethod\n    def _bit_count(n: int) -> int:\n        c = (n & 0x5555555555555555)\
    \ + ((n >> 1) & 0x5555555555555555)\n        c = (c & 0x3333333333333333) + ((c\
    \ >> 2) & 0x3333333333333333)\n        c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4)\
    \ & 0x0F0F0F0F0F0F0F0F)\n        c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)\n\
    \        c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)\n   \
    \     c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)\n      \
    \  return c\n\n    def __repr__(self) -> str:\n        return f\"<BitSet[{self.tostr()}]>\"\
    \n\n    def __getitem__(self, idx: int) -> int:\n        return self.buf[idx >>\
    \ 6] >> (idx & 63) & 1\n\n    def __setitem__(self, idx: int, b: int) -> None:\n\
    \        # assert b == 0 or b == 1\n        if b:\n            self.buf[idx >>\
    \ 6] |= 1 << (idx & 63)\n        else:\n            self.buf[idx >> 6] &= ~(1\
    \ << (idx & 63))\n\n    def __and__(self, other: \"BitSet\") -> \"BitSet\":\n\
    \        return self.__xor__(other)\n\n    def __or__(self, other: \"BitSet\"\
    ) -> \"BitSet\":\n        for i in range(min(len(self.buf), len(other.buf))):\n\
    \            self.buf[i] |= other.buf[i]\n        return self\n\n    def __xor__(self,\
    \ other: \"BitSet\") -> \"BitSet\":\n        for i in range(min(len(self.buf),\
    \ len(other.buf))):\n            self.buf[i] ^= other.buf[i]\n        return self\n\
    \n    def bit_count(self):\n        res = 0\n        for i in range(len(self.buf)):\n\
    \            res += self._bit_count(self.buf[i])\n        return res\n\n    def\
    \ ctz(self):\n        res = 0\n        i = 0\n        while i < len(self.buf)\
    \ and self.buf[i] == 0:\n            res += 63\n            i += 1\n        if\
    \ i < len(self.buf):\n            for sub_czt in range(63):\n                if\
    \ self.buf[i] >> sub_czt & 1:\n                    break\n            res += sub_czt\n\
    \        return min(res, self.n)\n\n    def xor_hint(self, other: \"BitSet\",\
    \ hint: int) -> \"BitSet\":\n        for i in range(hint >> 6, min(len(self.buf),\
    \ len(other.buf))):\n            self.buf[i] ^= other.buf[i]\n        return self\n\
    \n    def tostr(self) -> str:\n        res = [\"1\" if self[i] else \"0\" for\
    \ i in range(self.n)]\n        return \"\".join(res)\n\n    def copy(self) ->\
    \ \"BitSet\":\n        res = BitSet(self.n)\n        res.buf = self.buf[:]\n \
    \       return res\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bitset.py
  requiredBy:
  - linear_algebra/bit_matrix.py
  timestamp: '2024-08-30 00:39:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bitset.py
layout: document
title: Bitset
---
