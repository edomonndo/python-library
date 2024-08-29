---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: linear_algebra/bit_matrix.py
    title: linear_algebra/bit_matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_det_mod_2
    links:
    - https://judge.yosupo.jp/problem/matrix_det_mod_2
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_det_mod_2


    import sys


    input = sys.stdin.readline().rstrip

    # sys.set_int_max_str_digits(0)


    from linear_algebra.bit_matrix import BitMatrix



    n = int(input())

    A = BitMatrix.from_input(n, n)

    print(A.det())

    '
  dependsOn:
  - linear_algebra/bit_matrix.py
  isVerificationFile: true
  path: test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
  requiredBy: []
  timestamp: '2024-08-30 00:39:24+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
layout: document
redirect_from:
- /verify/test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
- /verify/test/library_checker/linear_algebra/matrix_determinant_mod2.test.py.html
title: test/library_checker/linear_algebra/matrix_determinant_mod2.test.py
---
