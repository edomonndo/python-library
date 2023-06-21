---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: matrix/matrix.py
    title: matrix/matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/inverse_matrix
    links:
    - https://judge.yosupo.jp/problem/inverse_matrix
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix


    from matrix.matrix import Matrix


    N = int(input())

    A = [list(map(int, input().split())) for _ in range(N)]


    A = Matrix(N, N, A)

    print(A.inverse())

    '
  dependsOn:
  - matrix/matrix.py
  isVerificationFile: true
  path: library_checker/matrix/matrix_inverse.test.py
  requiredBy: []
  timestamp: '2023-06-21 21:40:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: library_checker/matrix/matrix_inverse.test.py
layout: document
redirect_from:
- /verify/library_checker/matrix/matrix_inverse.test.py
- /verify/library_checker/matrix/matrix_inverse.test.py.html
title: library_checker/matrix/matrix_inverse.test.py
---
