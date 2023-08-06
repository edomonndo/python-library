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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def make_divisors(n: int):\n    lower_divisors, upper_divisors = [], []\n\
    \    i = 1\n    while i * i <= n:\n        if n % i == 0:\n            lower_divisors.append(i)\n\
    \            if i != n // i:\n                upper_divisors.append(n // i)\n\
    \        i += 1\n    return lower_divisors + upper_divisors[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/divisors.py
  requiredBy: []
  timestamp: '2023-07-06 11:56:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math_/divisors.py
layout: document
title: "\u7D04\u6570\u5217\u6319"
---

### `make_divisors(n: int)`

$n$の約数を列挙する.