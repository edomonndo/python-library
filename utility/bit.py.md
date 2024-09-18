---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/linear_add_rmq.py
    title: "\u7B49\u5DEE\u6570\u5217\u52A0\u7B97\u30FB\u6700\u5C0F\u5024\u53D6\u5F97"
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
  code: "class Bit64:\n    @staticmethod\n    def popcount(x: int) -> int:\n     \
    \   \"\"\"Count number of 1 bit\"\"\"\n        x = ((x >> 1) & 0x5555555555555555)\
    \ + (x & 0x5555555555555555)\n        x = ((x >> 2) & 0x3333333333333333) + (x\
    \ & 0x3333333333333333)\n        x = ((x >> 4) & 0x0F0F0F0F0F0F0F0F) + (x & 0x0F0F0F0F0F0F0F0F)\n\
    \        x = ((x >> 8) & 0x00FF00FF00FF00FF) + (x & 0x00FF00FF00FF00FF)\n    \
    \    x = ((x >> 16) & 0x0000FFFF0000FFFF) + (x & 0x0000FFFF0000FFFF)\n       \
    \ x = ((x >> 32) & 0x00000000FFFFFFFF) + (x & 0x00000000FFFFFFFF)\n        return\
    \ x\n\n    @staticmethod\n    def bit_reverse(x: int) -> int:\n        \"\"\"\
    Flip 1 and 0 bit\"\"\"\n        x = (x >> 32) | (x << 32)\n        x = ((x >>\
    \ 16) & 0x0000FFFF0000FFFF) | ((x << 16) & 0xFFFF0000FFFF0000)\n        x = ((x\
    \ >> 8) & 0x00FF00FF0FF00FF) | ((x << 8) & 0xFF00FF00FF00FF00)\n        x = ((x\
    \ >> 4) & 0x0F0F0F0F0F0F0F0F) | ((x << 4) & 0xF0F0F0F0F0F0F0F0)\n        x = ((x\
    \ >> 2) & 0x3333333333333333) | ((x << 2) & 0xCCCCCCCCCCCCCCCC)\n        x = ((x\
    \ >> 1) & 0x5555555555555555) | ((x << 1) & 0xAAAAAAAAAAAAAAAA)\n        return\
    \ x\n\n    @classmethod\n    def ctz(cls, x: int) -> int:\n        \"\"\"Count\
    \ trailing zeros\"\"\"\n        if x == 0:\n            return -1\n        return\
    \ cls.popcount(~x & (x - 1))\n\n    @classmethod\n    def clz(cls, x: int) ->\
    \ int:\n        \"\"\"Count leading zeros\"\"\"\n        return cls.ctz(cls.bit_reverse(x))\n\
    \n\nclass Bit32:\n    @staticmethod\n    def popcount(x: int) -> int:\n      \
    \  \"\"\"Count number of 1 bit\"\"\"\n        x = ((x >> 1) & 0x55555555) + (x\
    \ & 0x55555555)\n        x = ((x >> 2) & 0x33333333) + (x & 0x33333333)\n    \
    \    x = ((x >> 4) & 0x0F0F0F0F) + (x & 0x0F0F0F0F)\n        x = ((x >> 8) & 0x00FF00FF)\
    \ + (x & 0x00FF00FF)\n        x = ((x >> 16) & 0x0000FFFF) + (x & 0x0000FFFF)\n\
    \        return x\n\n    @staticmethod\n    def bit_reverse(x: int) -> int:\n\
    \        \"\"\"Flip 1 and 0 bit\"\"\"\n        x = (x >> 16) | (x << 16)\n   \
    \     x = ((x >> 8) & 0x00FF00FF) | ((x << 8) & 0xFF00FF00)\n        x = ((x >>\
    \ 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)\n        x = ((x >> 2) & 0x33333333)\
    \ | ((x << 2) & 0xCCCCCCCC)\n        x = ((x >> 1) & 0x55555555) | ((x << 1) &\
    \ 0xAAAAAAAA)\n        return x\n\n    @classmethod\n    def ctz(cls, x: int)\
    \ -> int:\n        \"\"\"Count trailing zeros\"\"\"\n        if x == 0:\n    \
    \        return -1\n        return cls.popcount(~x & (x - 1))\n\n    @classmethod\n\
    \    def clz(cls, x: int) -> int:\n        \"\"\"Count leading zeros\"\"\"\n \
    \       return cls.ctz(cls.bit_reverse(x))\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bit.py
  requiredBy:
  - data_structure/segtree/linear_add_rmq.py
  timestamp: '2024-09-01 02:12:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bit.py
layout: document
redirect_from:
- /library/utility/bit.py
- /library/utility/bit.py.html
title: utility/bit.py
---
