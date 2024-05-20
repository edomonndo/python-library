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
  code: "def fast_power(base, power, mod=10**9 + 7):\n    result = 1\n    while power\
    \ > 0:\n        # If power is odd\n        if power % 2 == 1:\n            result\
    \ = (result * base) % mod\n\n        # Divide the power by 2\n        power =\
    \ power // 2\n        # Multiply base to itself\n        base = (base * base)\
    \ % mod\n\n    return result\n"
  dependsOn: []
  isVerificationFile: false
  path: utility/fast_power.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: utility/fast_power.py
layout: document
title: "\u51AA\u4E57"
---

$a^{b}$を高速に計算する．ただし，$a>=1, b>=0$