---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: enumerative_combinatorics/derangement.py
    title: enumerative_combinatorics/derangement.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/montmort_number_mod
    links:
    - https://judge.yosupo.jp/problem/montmort_number_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod


    from enumerative_combinatorics.derangement import derangement


    n, m = map(int, input().split())

    print(*derangement(n, m)[1:])

    '
  dependsOn:
  - enumerative_combinatorics/derangement.py
  isVerificationFile: true
  path: test/library_checker/enumerative_combinatorics/montmort_number_mod.test.py
  requiredBy: []
  timestamp: '2024-08-26 12:24:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/enumerative_combinatorics/montmort_number_mod.test.py
layout: document
title: Montmort Number
---
