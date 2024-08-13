---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: polynomial/multipoint_evaluation.py
    title: Multipoint Evaluation
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/multipoint_evaluation
    links:
    - https://judge.yosupo.jp/problem/multipoint_evaluation
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation

    from polynomial.multipoint_evaluation import *


    n, m = map(int, input().split())

    C = [int(x) for x in input().split()]

    P = [int(x) for x in input().split()]

    print(*multipoint_evaluation(C, P))

    '
  dependsOn:
  - polynomial/multipoint_evaluation.py
  isVerificationFile: true
  path: test/library_checker/polynomial/multipoint_evaluation.test.py
  requiredBy: []
  timestamp: '2024-07-02 08:45:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/multipoint_evaluation.test.py
layout: document
title: Multipoint Evaluation
---
