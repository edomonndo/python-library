---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: linear_algebra/matrix.py
    title: "\u884C\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_matrix
    links:
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \nfrom linear_algebra.matrix import Matrix\n\nn, k = map(int, input().split())\n\
    A = [[int(x) for x in input().split()] for _ in range(n)]\nM = Matrix(n, n, A)\n\
    M = M**k\nfor i in range(n):\n    tmp = [M[i][j] for j in range(n)]\n    print(\"\
    \ \".join(map(str, tmp)))\n"
  dependsOn:
  - linear_algebra/matrix.py
  isVerificationFile: true
  path: test/library_checker/linear_algebra/pow_of_matrix.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/linear_algebra/pow_of_matrix.test.py
layout: document
redirect_from:
- /verify/test/library_checker/linear_algebra/pow_of_matrix.test.py
- /verify/test/library_checker/linear_algebra/pow_of_matrix.test.py.html
title: test/library_checker/linear_algebra/pow_of_matrix.test.py
---
