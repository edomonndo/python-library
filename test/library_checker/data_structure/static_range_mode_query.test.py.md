---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/static_range_mode_query.py
    title: "\u533A\u9593\u6700\u983B\u5024\u30AF\u30A8\u30EA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_mode_query
    links:
    - https://judge.yosupo.jp/problem/static_range_mode_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_mode_query\n\
    from data_structure.static_range_mode_query import StaticRangeModeQuery\n\nn,\
    \ q = map(int, input().split())\nA = [int(x) for x in input().split()]\nRMQ =\
    \ StaticRangeModeQuery(A)\nfor _ in range(q):\n    l, r = map(int, input().split())\n\
    \    print(*RMQ.query(l, r))\n"
  dependsOn:
  - data_structure/static_range_mode_query.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_range_mode_query.test.py
  requiredBy: []
  timestamp: '2024-05-21 17:51:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_range_mode_query.test.py
layout: document
title: Static Range Mode Query
---
