---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: number_theory/nimber.py
    title: number_theory/nimber.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/nim_product_64
    links:
    - https://judge.yosupo.jp/problem/nim_product_64
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/nim_product_64\n\
    \nfrom number_theory.nimber import Nimber\n\nt = int(input())\nnim = Nimber()\n\
    for _ in range(t):\n    a, b = map(int, input().split())\n    print(nim.product_64(a,\
    \ b))\n"
  dependsOn:
  - number_theory/nimber.py
  isVerificationFile: true
  path: test/library_checker/number_theory/nim_product_64.test.py
  requiredBy: []
  timestamp: '2024-09-05 15:49:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/number_theory/nim_product_64.test.py
layout: document
title: Nim Product
---
