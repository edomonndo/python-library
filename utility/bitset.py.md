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
  code: "class BitSet:\n    \"\"\"64 Bit\"\"\"\n\n    def __init__(self, n: int):\n\
    \        self.n = n\n        self.buf = [0] * ((n + 63) // 64)\n\n    def __getitem__(self,\
    \ idx: int) -> int:\n        return self.buf[idx >> 6] >> (idx & 0x3F) & 1\n\n\
    \    def __setitem__(self, idx: int, b: int) -> None:\n        # assert b == 0\
    \ or b == 1\n        if b:\n            self.buf[idx >> 6] |= 1 << (idx & 0x3F)\n\
    \        else:\n            self.buf[idx >> 6] &= ~(1 << (idx & 0x3F))\n\n   \
    \ def __and__(self, other: \"BitSet\") -> \"BitSet\":\n        return self.__xor__(other)\n\
    \n    def __or__(self, other: \"BitSet\") -> \"BitSet\":\n        sz = min(len(self.buf),\
    \ len(other.buf))\n        for i in range(sz):\n            self.buf[i] |= other.buf[i]\n\
    \        return self\n\n    def __xor__(self, other: \"BitSet\") -> \"BitSet\"\
    :\n        sz = min(len(self.buf), len(other.buf))\n        for i in range(sz):\n\
    \            self.buf[i] ^= other.buf[i]\n        return self\n\n    def tostr(self)\
    \ -> str:\n        res = [\"1\" if self[i] else \"0\" for i in range(self.n)]\n\
    \        return \"\".join(res)\n\n    def copy(self) -> \"BitSet\":\n        res\
    \ = BitSet(self.n)\n        res.buf = self.buf[:]\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bitset.py
  requiredBy: []
  timestamp: '2024-09-01 02:12:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bitset.py
layout: document
redirect_from:
- /library/utility/bitset.py
- /library/utility/bitset.py.html
title: utility/bitset.py
---
