---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/convolution/bitwise_xor_convolution.test.py
    title: Bitwise Xor Convolution
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "MOD = 998244353\n\n\ndef walsh_hadamard_tranform(buf: list[int], inv: bool\
    \ = False):\n    i, n = 1, len(buf)\n    while i < n:\n        for j in range(0,\
    \ n, i << 1):\n            for k in range(i):\n                s, t = buf[j +\
    \ k], buf[j + k + i]\n                buf[j + k], buf[j + k + i] = (s + t) % MOD,\
    \ (s - t) % MOD\n        i <<= 1\n    if inv:\n        inv_n = pow(n, -1, MOD)\n\
    \        for i in range(n):\n            buf[i] = (buf[i] * inv_n) % MOD\n\n\n\
    def bitwise_xor_conv(f: list[int], g: list[int]):\n    n = len(f)\n    assert\
    \ n == len(g)\n    walsh_hadamard_tranform(f, False)\n    walsh_hadamard_tranform(g,\
    \ False)\n    for i in range(n):\n        f[i] = (f[i] * g[i]) % MOD\n    walsh_hadamard_tranform(f,\
    \ True)\n"
  dependsOn: []
  isVerificationFile: false
  path: convolution/walsh_hadamard_tranform.py
  requiredBy: []
  timestamp: '2024-09-03 09:26:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/convolution/bitwise_xor_convolution.test.py
documentation_of: convolution/walsh_hadamard_tranform.py
layout: document
title: "\u30A6\u30A9\u30EB\u30B7\u30E5\u30A2\u30C0\u30DE\u30FC\u30EB\u5909\u63DB"
---
