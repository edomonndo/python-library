---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/sort_points_by_argument.py
    title: "\u504F\u89D2\u30BD\u30FC\u30C8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sort_points_by_argument
    links:
    - https://judge.yosupo.jp/problem/sort_points_by_argument
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sort_points_by_argument\n\
    \nfrom geometory.sort_points_by_argument import sortPointsByArgument\n\nN = int(input())\n\
    A = [tuple(map(int, input().split())) for _ in range(N)]\n\nans = sortPointsByArgument(A)\n\
    for x, y in ans:\n    print(x, y)\n"
  dependsOn:
  - geometory/sort_points_by_argument.py
  isVerificationFile: true
  path: test/library_checker/geometory/sort_points_by_argument.test.py
  requiredBy: []
  timestamp: '2024-06-13 11:50:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/geometory/sort_points_by_argument.test.py
layout: document
title: Sort Points by Argument
---
