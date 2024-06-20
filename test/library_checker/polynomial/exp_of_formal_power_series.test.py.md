---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: convolution/formal_power_series.py
    title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/exp_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/exp_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/exp_of_formal_power_series

    from convolution.formal_power_series import FPS


    n = int(input())

    A = [int(x) for x in input().split()]

    print(*FPS.exp(A))

    '
  dependsOn:
  - convolution/formal_power_series.py
  isVerificationFile: true
  path: test/library_checker/polynomial/exp_of_formal_power_series.test.py
  requiredBy: []
  timestamp: '2024-06-20 09:29:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/exp_of_formal_power_series.test.py
layout: document
redirect_from:
- /verify/test/library_checker/polynomial/exp_of_formal_power_series.test.py
- /verify/test/library_checker/polynomial/exp_of_formal_power_series.test.py.html
title: test/library_checker/polynomial/exp_of_formal_power_series.test.py
---
