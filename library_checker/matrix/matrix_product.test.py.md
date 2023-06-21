---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: matrix/matrix.py
    title: matrix/matrix.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/matrix_product
    links:
    - https://judge.yosupo.jp/problem/matrix_product
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_product\n\
    \nfrom matrix.matrix import Matrix\n\nN, M, K = map(int, input().split())\nA =\
    \ list(map(int, input().split()))\nB = list(map(int, input().split()))\n\nA =\
    \ Matrix(N, M, A)\nB = Matrix(M, K, B)\n\nC = A * B\nfor row in C:\n    print(*row)\n"
  dependsOn:
  - matrix/matrix.py
  isVerificationFile: true
  path: library_checker/matrix/matrix_product.test.py
  requiredBy: []
  timestamp: '2023-06-21 08:58:45+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/matrix/matrix_product.test.py
layout: document
redirect_from:
- /verify/library_checker/matrix/matrix_product.test.py
- /verify/library_checker/matrix/matrix_product.test.py.html
title: library_checker/matrix/matrix_product.test.py
---
