---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: enumerative_combinatorics/factorial_mod.py
    title: enumerative_combinatorics/factorial_mod.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/factorial
    links:
    - https://judge.yosupo.jp/problem/factorial
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorial\n\
    \nfrom enumerative_combinatorics.factorial_mod import factorial_mod\n\n\nt = int(input())\n\
    \nfor _ in range(t):\n    n = int(input())\n    print(factorial_mod(n))\n"
  dependsOn:
  - enumerative_combinatorics/factorial_mod.py
  isVerificationFile: true
  path: test/library_checker/enumerative_combinatorics/factorial.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/enumerative_combinatorics/factorial.test.py
layout: document
title: Factorial
---
