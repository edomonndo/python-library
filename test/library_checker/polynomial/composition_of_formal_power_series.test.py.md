---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: polynomial/composition.py
    title: polynomial/composition.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/composition_of_formal_power_series
    links:
    - https://judge.yosupo.jp/problem/composition_of_formal_power_series
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/composition_of_formal_power_series

    from polynomial.composition import *


    n = int(input())

    A = [int(x) for x in input().split()]

    B = [int(x) for x in input().split()]

    print(*composition(A, B))

    '
  dependsOn:
  - polynomial/composition.py
  isVerificationFile: true
  path: test/library_checker/polynomial/composition_of_formal_power_series.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:37:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/composition_of_formal_power_series.test.py
layout: document
redirect_from:
- /verify/test/library_checker/polynomial/composition_of_formal_power_series.test.py
- /verify/test/library_checker/polynomial/composition_of_formal_power_series.test.py.html
title: test/library_checker/polynomial/composition_of_formal_power_series.test.py
---
