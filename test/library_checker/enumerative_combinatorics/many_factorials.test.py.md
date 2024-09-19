---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: enumerative_combinatorics/factorial_iter_mod.py
    title: "\u968E\u4E57\u30AF\u30A8\u30EA mod 998244353"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/many_factorials
    links:
    - https://judge.yosupo.jp/problem/many_factorials
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/many_factorials


    from enumerative_combinatorics.factorial_iter_mod import factorial_iter_mod



    t = int(input())

    qs = [int(input()) for _ in range(t)]

    ans = factorial_iter_mod(qs)

    print(*ans, sep="\n")

    '
  dependsOn:
  - enumerative_combinatorics/factorial_iter_mod.py
  isVerificationFile: true
  path: test/library_checker/enumerative_combinatorics/many_factorials.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/enumerative_combinatorics/many_factorials.test.py
layout: document
title: Many Factorials
---
