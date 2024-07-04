---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: polynomial/formal_power_series.py
    title: "\u5F62\u5F0F\u7684\u51AA\u7D1A\u6570"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/sqrt_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_of_formal_power_series\n\
    from polynomial.formal_power_series import FPS\n\nn = int(input())\nA = [int(x)\
    \ for x in input().split()]\nans = FPS.sqrt(A)\nif ans:\n    print(*ans)\nelse:\n\
    \    print(-1)\n"
  dependsOn:
  - polynomial/formal_power_series.py
  isVerificationFile: true
  path: test/library_checker/polynomial/sqrt_of_formal_power_series.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/sqrt_of_formal_power_series.test.py
layout: document
redirect_from:
- /verify/test/library_checker/polynomial/sqrt_of_formal_power_series.test.py
- /verify/test/library_checker/polynomial/sqrt_of_formal_power_series.test.py.html
title: test/library_checker/polynomial/sqrt_of_formal_power_series.test.py
---