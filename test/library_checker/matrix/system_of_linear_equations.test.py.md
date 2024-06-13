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
    PROBLEM: https://judge.yosupo.jp/problem/system_of_linear_equations
    links:
    - https://judge.yosupo.jp/problem/system_of_linear_equations
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations\n\
    \nfrom matrix.matrix import Matrix\n\nn, m = map(int, input().split())\nA = [[int(x)\
    \ for x in input().split()] for _ in range(n)]\nB = [int(x) for x in input().split()]\n\
    M = Matrix(n, m, A)\ndim, sol, vecs = M.linear_equations(B)\nprint(dim)\nprint(*sol)\n\
    for vec in vecs:\n    print(*vec)\n"
  dependsOn:
  - matrix/matrix.py
  isVerificationFile: true
  path: test/library_checker/matrix/system_of_linear_equations.test.py
  requiredBy: []
  timestamp: '2024-06-13 11:50:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/matrix/system_of_linear_equations.test.py
layout: document
redirect_from:
- /verify/test/library_checker/matrix/system_of_linear_equations.test.py
- /verify/test/library_checker/matrix/system_of_linear_equations.test.py.html
title: test/library_checker/matrix/system_of_linear_equations.test.py
---
