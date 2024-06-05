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
  code: "def popcount(x: int) -> int:\n    \"\"\"Count number of 1 bit\"\"\"\n   \
    \ x = ((x >> 1) & 0x5555555555555555) + (x & 0x5555555555555555)\n    x = ((x\
    \ >> 2) & 0x3333333333333333) + (x & 0x3333333333333333)\n    x = ((x >> 4) &\
    \ 0x0F0F0F0F0F0F0F0F) + (x & 0x0F0F0F0F0F0F0F0F)\n    x = ((x >> 8) & 0x00FF00FF00FF00FF)\
    \ + (x & 0x00FF00FF00FF00FF)\n    x = ((x >> 16) & 0x0000FFFF0000FFFF) + (x &\
    \ 0x0000FFFF0000FFFF)\n    x = ((x >> 32) & 0x00000000FFFFFFFF) + (x & 0x00000000FFFFFFFF)\n\
    \    return x\n\n\ndef bit_reverse(x: int) -> int:\n    \"\"\"Flip 1 and 0 bit\"\
    \"\"\n    x = (x >> 32) | (x << 32)\n    x = ((x >> 16) & 0x0000FFFF0000FFFF)\
    \ | ((x << 16) & 0xFFFF0000FFFF0000)\n    x = ((x >> 8) & 0x00FF00FF0FF00FF) |\
    \ ((x << 8) & 0xFF00FF00FF00FF00)\n    x = ((x >> 4) & 0x0F0F0F0F0F0F0F0F) | ((x\
    \ << 4) & 0xF0F0F0F0F0F0F0F0)\n    x = ((x >> 2) & 0x3333333333333333) | ((x <<\
    \ 2) & 0xCCCCCCCCCCCCCCCC)\n    x = ((x >> 1) & 0x5555555555555555) | ((x << 1)\
    \ & 0xAAAAAAAAAAAAAAAA)\n    return x\n\n\ndef ctz(x: int) -> int:\n    \"\"\"\
    Count trailing zeros\"\"\"\n    if x == 0:\n        return -1\n    return popcount(~x\
    \ & (x - 1))\n\n\ndef clz(x: int) -> int:\n    \"\"\"Count leading zeros\"\"\"\
    \n    return ctz(bit_reverse(x))\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bit64_operation.py
  requiredBy: []
  timestamp: '2024-06-05 17:57:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bit64_operation.py
layout: document
title: "\u30D3\u30C3\u30C8\u6F14\u7B97(64bit)"
---


