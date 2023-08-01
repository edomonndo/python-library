---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: math_/floor_sum.py
    title: Floor sum
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    links:
    - https://judge.yosupo.jp/problem/sum_of_floor_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
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
  timestamp: '2023-08-01 14:51:05+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/math/sum_of_floor_of_linear.test.py
layout: document
redirect_from:
- /verify/test/library_checker/math/sum_of_floor_of_linear.test.py
- /verify/test/library_checker/math/sum_of_floor_of_linear.test.py.html
title: test/library_checker/math/sum_of_floor_of_linear.test.py
---
