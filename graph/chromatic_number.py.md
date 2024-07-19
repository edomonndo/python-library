---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: utility/bit32_operation.py
    title: "\u30D3\u30C3\u30C8\u6F14\u7B97(32bit)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/chromatic_number.test.py
    title: Chromatic Number
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from utility.bit32_operation import *\n\n\ndef chromatic_number(n: int, edges:\
    \ list[tuple[int, int]]) -> int:\n    adj = [0] * n\n    for u, v in edges:\n\
    \        adj[u] |= 1 << v\n        adj[v] |= 1 << u\n\n    dp = [0] * (1 << n)\n\
    \    cur = [0] * (1 << n)\n\n    dp[0] = 1\n    for bit in range(1, 1 << n):\n\
    \        v = ctz(bit)\n        dp[bit] = dp[bit ^ (1 << v)] + dp[(bit ^ (1 <<\
    \ v)) & (~adj[v])]\n\n    for bit in range(1 << n):\n        if (n - popcount(bit))\
    \ & 1:\n            cur[bit] = -1\n        else:\n            cur[bit] = 1\n\n\
    \    for k in range(1, n):\n        tmp = 0\n        for bit in range(1 << n):\n\
    \            cur[bit] *= dp[bit]\n            tmp += cur[bit]\n        if tmp\
    \ != 0:\n            res = k\n            break\n    else:\n        res = n\n\
    \    return res\n"
  dependsOn:
  - utility/bit32_operation.py
  isVerificationFile: false
  path: graph/chromatic_number.py
  requiredBy: []
  timestamp: '2024-06-05 17:57:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/chromatic_number.test.py
documentation_of: graph/chromatic_number.py
layout: document
title: "\u5F69\u8272\u6570"
---
