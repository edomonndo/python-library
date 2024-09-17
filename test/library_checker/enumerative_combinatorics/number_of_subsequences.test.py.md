---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: enumerative_combinatorics/number_of_subsequences.py
    title: enumerative_combinatorics/number_of_subsequences.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/number_of_subsequences
    links:
    - https://judge.yosupo.jp/problem/number_of_subsequences
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_subsequences


    from enumerative_combinatorics.number_of_subsequences import solve


    n = int(input())

    A = [int(x) for x in input().split()]

    print(solve(A))

    '
  dependsOn:
  - enumerative_combinatorics/number_of_subsequences.py
  isVerificationFile: true
  path: test/library_checker/enumerative_combinatorics/number_of_subsequences.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/enumerative_combinatorics/number_of_subsequences.test.py
layout: document
title: Number of Subsequences
---
