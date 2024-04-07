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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Bitset:\n\n    @staticmethod\n    def __popcount(n):\n        n -=\
    \ (n >> 1) & 0x5555555555555555\n        n = (n & 0x3333333333333333) + ((n >>\
    \ 2) & 0x3333333333333333)\n        n = (n + (n >> 4)) & 0x0F0F0F0F0F0F0F0F\n\
    \        n += (n >> 8) & 0x00FF00FF00FF00FF\n        n += (n >> 16) & 0x0000FFFF0000FFFF\n\
    \        n += (n >> 32) & 0x00000000FFFFFFFF\n        return n & 0x7F\n\n    def\
    \ __init__(self, n, bit_size=63):\n        self.N = n\n        self.__bit_size\
    \ = bit_size\n\n        self.__block = (n + bit_size - 1) // bit_size\n      \
    \  self.__msk_b = (1 << bit_size) - 1\n        self.__msk_s = (1 << (n % bit_size))\
    \ - 1\n        self.__on = [1 << i for i in range(bit_size)]\n        self.__off\
    \ = [0] * bit_size\n        for k in range(bit_size):\n            self.__off[k]\
    \ = ((1 << bit_size) - 1) ^ (1 << k)\n        del k\n\n        self.__bit = [0]\
    \ * self.__block\n\n    def __len__(self):\n        assert self.__bit_size <=\
    \ 63\n        x = 0\n        for bit in self.__bit:\n            x += self.__popcount(bit)\n\
    \        return x\n\n    def __bool__(self):\n        return self.any()\n\n  \
    \  def __str__(self):\n        return \" \".join(map(str, [i for i in range(self.N)\
    \ if i in self]))\n\n    def __repr__(self):\n        return \"<Bitset: \" + (str(self)\
    \ if self else \"empty\") + \">\"\n\n    def __contains__(self, index):\n    \
    \    k, i = divmod(index, self.__bit_size)\n        return bool((self.__bit[k]\
    \ >> i) & 1)\n\n    __getitem__ = __contains__\n\n    def __setitem__(self, index,\
    \ value):\n        self.set(index, value)\n\n    def set(self, index=-1, value=1):\n\
    \        if index == -1:\n            if value:\n                self.__bit[-1]\
    \ = self.__msk_s\n                for k in range(self.__block - 1):\n        \
    \            self.__bit[k] = self.__msk_b\n            else:\n               \
    \ for k in range(self.__block):\n                    self.__bit[k] = 0\n     \
    \   else:\n            k, i = divmod(index, self.__bit_size)\n            if value:\n\
    \                self.__bit[k] |= self.__on[i]\n            else:\n          \
    \      self.__bit[k] &= self.__off[i]\n\n    def reset(self, index=-1):\n    \
    \    self.set(index, value=0)\n\n    def flip(self, index=-1):\n        if index\
    \ == -1:\n            for k in range(self.__block - 1):\n                self.__bit[k]\
    \ = self.__bit[k] ^ self.__msk_b\n            if self.N % self.__bit_size:\n \
    \               self.__bit[-1] = self.__bit[-1] ^ self.__msk_s\n            else:\n\
    \                self.__bit[-1] = self.__bit[-1] ^ self.__msk_b\n        else:\n\
    \            k, i = divmod(index, self.__bit_size)\n            self.__bit[k]\
    \ ^= self.__on[i]\n\n    test = __contains__\n\n    def any(self):\n        for\
    \ bit in self.__bit:\n            if bit:\n                return True\n     \
    \   return False\n\n    def all(self):\n        for k in range(self.__block -\
    \ 1):\n            if self.__bit[k] != self.__msk_b:\n                return False\n\
    \        if self.N % self.__bit_size:\n            return self.__bit[-1] == self.__msk_s\n\
    \        else:\n            return self.__bit[-1] == self.__msk_b\n\n    def __iand__(self,\
    \ other):\n        for k in range(self.__block):\n            self.__bit[k] &=\
    \ other.__bit[k]\n        return self\n\n    def __and__(self, other):\n     \
    \   X = self.copy()\n        X &= other\n        return X\n\n    def __ior__(self,\
    \ other):\n        for k in range(self.__block):\n            self.__bit[k] |=\
    \ other.__bit[k]\n        return self\n\n    def __or__(self, other):\n      \
    \  X = self.copy()\n        X |= other\n        return X\n\n    def __ixor__(self,\
    \ other):\n        for k in range(self.__block):\n            self.__bit[k] ^=\
    \ other.__bit[k]\n        return self\n\n    def __xor__(self, other):\n     \
    \   X = self.copy()\n        X ^= other\n        return X\n\n    def __eq__(self,\
    \ other):\n        for k in range(self.__block):\n            if self.__bit[k]\
    \ != other.__bit[k]:\n                return False\n        return True\n\n  \
    \  def __neq__(self, other):\n        return not (self == other)\n\n    def copy(self):\n\
    \        X = Bitset()\n        X.__bit = self.__bit.copy()\n        return X\n\
    \n    count = __len__\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bitset.py
  requiredBy: []
  timestamp: '2024-04-07 15:13:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bitset.py
layout: document
redirect_from:
- /library/utility/bitset.py
- /library/utility/bitset.py.html
title: utility/bitset.py
---
