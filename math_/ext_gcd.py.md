---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/ntl/ntl_1_e_extended_euclidean.test.py
    title: "NTL1E \u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\
      \u6CD5"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def ext_gcd(a: int, b: int) -> int:\n    x = v = 1\n    y = w = 0\n    while\
    \ b:\n        q = a // b\n        a, b, x, w, y, v = b, a % b, w, x - q * w, v,\
    \ y - q * v\n    return x, y\n"
  dependsOn: []
  isVerificationFile: false
  path: math_/ext_gcd.py
  requiredBy: []
  timestamp: '2023-08-26 01:45:36+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/ntl/ntl_1_e_extended_euclidean.test.py
documentation_of: math_/ext_gcd.py
layout: document
title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u52A9\u6CD5"
---

2つの整数$a,b$について，  
$$ax+by=gcd(a,b)$$  
の整数解$(x,y)$を返す．