---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/static_range_inversion_query.py
    title: "\u9759\u7684\u533A\u9593\u53CD\u8EE2\u30AF\u30A8\u30EA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_inversions_query
    links:
    - https://judge.yosupo.jp/problem/static_range_inversions_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_inversions_query


    from data_structure.static_range_inversion_query import StaticRangeInversionQuery


    n, q = map(int, input().split())

    A = [int(x) for x in input().split()]

    Q = [tuple(map(int, input().split())) for _ in range(q)]

    ans = StaticRangeInversionQuery(A, Q)

    print(*ans, sep="\n")

    '
  dependsOn:
  - data_structure/static_range_inversion_query.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_range_inversion_query.test.py
  requiredBy: []
  timestamp: '2024-05-28 15:29:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_range_inversion_query.test.py
layout: document
title: Static Range Inversion Query
---