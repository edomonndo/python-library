---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: matrix/matrix.py
    title: "\u884C\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_det
    links:
    - https://judge.yosupo.jp/problem/matrix_det
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det


    from matrix.matrix import Matrix


    N = int(input())

    A = [list(map(int, input().split())) for _ in range(N)]


    A = Matrix(N, N, A)

    print(A.determinant())

    '
  dependsOn:
  - matrix/matrix.py
  isVerificationFile: true
  path: library_checker/matrix/matrix_det.test.py
  requiredBy: []
  timestamp: '2023-07-05 16:20:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/matrix/matrix_det.test.py
layout: document
redirect_from:
- /verify/library_checker/matrix/matrix_det.test.py
- /verify/library_checker/matrix/matrix_det.test.py.html
title: library_checker/matrix/matrix_det.test.py
---
