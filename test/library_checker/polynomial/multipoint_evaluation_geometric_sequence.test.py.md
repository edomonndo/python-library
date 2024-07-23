---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: polynomial/chirp_z.py
    title: polynomial/chirp_z.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/multipoint_evaluation_on_geometric_sequence
    links:
    - https://judge.yosupo.jp/problem/multipoint_evaluation_on_geometric_sequence
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/multipoint_evaluation_on_geometric_sequence

    from polynomial.chirp_z import *


    n, m, a, r = map(int, input().split())

    C = [int(x) for x in input().split()]

    print(*chirp_z(C, r, m, a))

    '
  dependsOn:
  - polynomial/chirp_z.py
  isVerificationFile: true
  path: test/library_checker/polynomial/multipoint_evaluation_geometric_sequence.test.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/polynomial/multipoint_evaluation_geometric_sequence.test.py
layout: document
title: Multipoint Evaluation (Geometric Sequence)
---
