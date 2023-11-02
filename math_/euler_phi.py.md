---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/ntl_1_d_euler_phi.test.py
    title: test/aoj/ntl_1_d_euler_phi.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def euler_phi(N: int) -> int:\n    res = N\n    upper = int(N**0.5)\n   \
    \ for i in range(2, upper + 1):\n        if N % i == 0:\n            res -= res\
    \ // i\n            while N % i == 0:\n                N //= i\n    if N > 1:\n\
    \        res -= res // N\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/euler_phi.py
  requiredBy: []
  timestamp: '2023-08-26 01:45:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/ntl_1_d_euler_phi.test.py
documentation_of: math_/euler_phi.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u306E\u03C6\u95A2\u6570(\u30C8\u30FC\u30B7\u30A7\u30F3\
  \u30C8\u95A2\u6570)"
---

正の整数$n$に対して，$n$と互いに素である$1$以上$n$以下の自然数の個数を返す．