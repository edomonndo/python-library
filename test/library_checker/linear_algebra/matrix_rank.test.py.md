---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: linear_algebra/matrix.py
    title: linear_algebra/matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_rank
    links:
    - https://judge.yosupo.jp/problem/matrix_rank
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank


    from linear_algebra.matrix import Matrix


    n, m = map(int, input().split())

    A = [[int(x) for x in input().split()] for _ in range(n)]

    M = Matrix(n, m, A)

    print(M.rank())

    '
  dependsOn:
  - linear_algebra/matrix.py
  isVerificationFile: true
  path: test/library_checker/linear_algebra/matrix_rank.test.py
  requiredBy: []
  timestamp: '2024-07-23 17:42:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/linear_algebra/matrix_rank.test.py
layout: document
title: Rank of Matrix
---
