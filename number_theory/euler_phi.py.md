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
  code: "def euler_phi(N: int) -> int:\n    res = N\n    upper = int(N**0.5)\n   \
    \ for i in range(2, upper + 1):\n        if N % i == 0:\n            res -= res\
    \ // i\n            while N % i == 0:\n                N //= i\n    if N > 1:\n\
    \        res -= res // N\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: number_theory/euler_phi.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: number_theory/euler_phi.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u306E\u03C6\u95A2\u6570(\u30C8\u30FC\u30B7\u30A7\u30F3\
  \u30C8\u95A2\u6570)"
---

正の整数$n$に対して，$n$と互いに素である$1$以上$n$以下の自然数の個数を返す．