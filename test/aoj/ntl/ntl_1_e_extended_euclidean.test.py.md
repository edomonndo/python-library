---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/ext_gcd.py
    title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u52A9\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/NTL_1_E


    from math_.ext_gcd import ext_gcd


    a, b = map(int, input().split())

    x, y = ext_gcd(a, b)

    print(x, y)

    '
  dependsOn:
  - math_/ext_gcd.py
  isVerificationFile: true
  path: test/aoj/ntl/ntl_1_e_extended_euclidean.test.py
  requiredBy: []
  timestamp: '2024-06-19 11:57:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/ntl/ntl_1_e_extended_euclidean.test.py
layout: document
redirect_from:
- /verify/test/aoj/ntl/ntl_1_e_extended_euclidean.test.py
- /verify/test/aoj/ntl/ntl_1_e_extended_euclidean.test.py.html
title: test/aoj/ntl/ntl_1_e_extended_euclidean.test.py
---
