---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/chromatic_number.py
    title: "\u5F69\u8272\u6570"
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
    \ x = ((x >> 1) & 0x55555555) + (x & 0x55555555)\n    x = ((x >> 2) & 0x33333333)\
    \ + (x & 0x33333333)\n    x = ((x >> 4) & 0x0F0F0F0F) + (x & 0x0F0F0F0F)\n   \
    \ x = ((x >> 8) & 0x00FF00FF) + (x & 0x00FF00FF)\n    x = ((x >> 16) & 0x0000FFFF)\
    \ + (x & 0x0000FFFF)\n    return x\n\n\ndef bit_reverse(x: int) -> int:\n    \"\
    \"\"Flip 1 and 0 bit\"\"\"\n    x = (x >> 16) | (x << 16)\n    x = ((x >> 8) &\
    \ 0x00FF00FF) | ((x << 8) & 0xFF00FF00)\n    x = ((x >> 4) & 0x0F0F0F0F) | ((x\
    \ << 4) & 0xF0F0F0F0)\n    x = ((x >> 2) & 0x33333333) | ((x << 2) & 0xCCCCCCCC)\n\
    \    x = ((x >> 1) & 0x55555555) | ((x << 1) & 0xAAAAAAAA)\n    return x\n\n\n\
    def ctz(x: int) -> int:\n    \"\"\"Count trailing zeros\"\"\"\n    if x == 0:\n\
    \        return -1\n    return popcount(~x & (x - 1))\n\n\ndef clz(x: int) ->\
    \ int:\n    \"\"\"Count leading zeros\"\"\"\n    return ctz(bit_reverse(x))\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/bit32_operation.py
  requiredBy:
  - graph/chromatic_number.py
  timestamp: '2024-06-05 17:57:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/bit32_operation.py
layout: document
title: "\u30D3\u30C3\u30C8\u6F14\u7B97(32bit)"
---


