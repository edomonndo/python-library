---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/min_of_linear.py
    title: Min of linear
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/min_of_mod_of_linear
    links:
    - https://judge.yosupo.jp/problem/min_of_mod_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/min_of_mod_of_linear\n\
    \nfrom math_.min_of_linear import min_of_linear\n\nT = int(input())\nans = [None]\
    \ * T\nfor i in range(T):\n    N, M, A, B = map(int, input().split())\n    _,\
    \ ans[i] = min_of_linear(0, N, A, B, M)\n\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - math_/min_of_linear.py
  isVerificationFile: true
  path: test/library_checker/math/min_of_linear.test.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/math/min_of_linear.test.py
layout: document
redirect_from:
- /verify/test/library_checker/math/min_of_linear.test.py
- /verify/test/library_checker/math/min_of_linear.test.py.html
title: test/library_checker/math/min_of_linear.test.py
---
