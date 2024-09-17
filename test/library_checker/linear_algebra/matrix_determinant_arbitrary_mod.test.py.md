---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: linear_algebra/determinant_arbitrary.py
    title: linear_algebra/determinant_arbitrary.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod
    links:
    - https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det_arbitrary_mod


    from linear_algebra.determinant_arbitrary import determinant_arbitrary_mod


    N, MOD = map(int, input().split())

    A = [list(map(int, input().split())) for _ in range(N)]


    print(determinant_arbitrary_mod(N, A, MOD))

    '
  dependsOn:
  - linear_algebra/determinant_arbitrary.py
  isVerificationFile: true
  path: test/library_checker/linear_algebra/matrix_determinant_arbitrary_mod.test.py
  requiredBy: []
  timestamp: '2024-07-23 17:42:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/linear_algebra/matrix_determinant_arbitrary_mod.test.py
layout: document
title: Determinant of Matrix (Arbitrary Mod)
---
