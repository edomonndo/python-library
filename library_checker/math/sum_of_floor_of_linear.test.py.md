---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: math/floor_sum.py
    title: math/floor_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    links:
    - https://judge.yosupo.jp/problem/sum_of_floor_of_linear
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.4/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear\n\
    \nfrom math.floor_sum import floor_sum\n\nT = int(input())\nans = [None] * T\n\
    for i in range(T):\n    N, M, A, B = map(int, input().split())\n    ans[i] = floor_sum(N,\
    \ M, A, B)\n\nprint(*ans, sep=\"\\n\")\n"
  dependsOn:
  - math/floor_sum.py
  isVerificationFile: true
  path: library_checker/math/sum_of_floor_of_linear.test.py
  requiredBy: []
  timestamp: '2023-06-21 08:58:45+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: library_checker/math/sum_of_floor_of_linear.test.py
layout: document
redirect_from:
- /verify/library_checker/math/sum_of_floor_of_linear.test.py
- /verify/library_checker/math/sum_of_floor_of_linear.test.py.html
title: library_checker/math/sum_of_floor_of_linear.test.py
---
