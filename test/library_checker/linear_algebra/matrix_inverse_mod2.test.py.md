---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: linear_algebra/bit_matrix.py
    title: linear_algebra/bit_matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/inverse_matrix_mod_2
    links:
    - https://judge.yosupo.jp/problem/inverse_matrix_mod_2
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/inverse_matrix_mod_2\n\
    \n# import sys\n# sys.set_int_max_str_digits(0)\n\nfrom linear_algebra.bit_matrix\
    \ import BitMatrix\n\n\nn = int(input())\nA = BitMatrix.from_input(n, n)\nA_inv\
    \ = A.inv()\nif A_inv:\n    print(A_inv.tostr())\nelse:\n    print(-1)\n"
  dependsOn:
  - linear_algebra/bit_matrix.py
  isVerificationFile: true
  path: test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
  requiredBy: []
  timestamp: '2024-08-29 23:59:34+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
layout: document
redirect_from:
- /verify/test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
- /verify/test/library_checker/linear_algebra/matrix_inverse_mod2.test.py.html
title: test/library_checker/linear_algebra/matrix_inverse_mod2.test.py
---
