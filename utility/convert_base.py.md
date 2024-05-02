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
  code: "def base_10(num_n, n):\n    \"\"\"10\u9032\u6570 \u2192 n\u9032\u6570\"\"\
    \"\n    num_10 = 0\n    for s in str(num_n):\n        num_10 *= n\n        num_10\
    \ += int(s)\n    return num_10\n\n\ndef base_n(num_10, n):\n    \"\"\"n\u9032\u6570\
    \ \u2192 10\u9032\u6570\"\"\"\n    str_n = \"\"\n    while num_10:\n        if\
    \ num_10 % n >= 10:\n            return -1\n        str_n += str(num_10 % n)\n\
    \        num_10 //= n\n    return int(str_n[::-1])\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/convert_base.py
  requiredBy: []
  timestamp: '2024-05-02 15:05:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/convert_base.py
layout: document
title: "\u9032\u6570\u5909\u63DB"
---

10進数 ⇆ n進数