---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/sample_point_shift.py
    title: convolution/sample_point_shift.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shift_of_sampling_points_of_polynomial
    links:
    - https://judge.yosupo.jp/problem/shift_of_sampling_points_of_polynomial
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shift_of_sampling_points_of_polynomial


    from convolution.sample_point_shift import *



    n, m, c = map(int, input().split())

    f = [int(x) for x in input().split()]

    print(*sample_point_shift(f, c, m))

    '
  dependsOn:
  - convolution/sample_point_shift.py
  isVerificationFile: true
  path: test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py
  requiredBy: []
  timestamp: '2024-06-24 10:43:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py
layout: document
redirect_from:
- /verify/test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py
- /verify/test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py.html
title: test/library_checker/polynomial/shift_of_sampling_points_of_polynomial.test.py
---
