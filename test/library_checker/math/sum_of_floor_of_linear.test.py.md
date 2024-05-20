---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: math_/floor_sum.py
    title: Floor sum
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    links:
    - https://judge.yosupo.jp/problem/sum_of_floor_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear\n\
    \nfrom math_.floor_sum import floor_sum\n\nT = int(input())\nans = [None] * T\n\
    for i in range(T):\n    N, M, A, B = map(int, input().split())\n    ans[i] = floor_sum(N,\
    \ M, A, B)\n\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - math_/floor_sum.py
  isVerificationFile: true
  path: test/library_checker/math/sum_of_floor_of_linear.test.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/math/sum_of_floor_of_linear.test.py
layout: document
redirect_from:
- /verify/test/library_checker/math/sum_of_floor_of_linear.test.py
- /verify/test/library_checker/math/sum_of_floor_of_linear.test.py.html
title: test/library_checker/math/sum_of_floor_of_linear.test.py
---
