---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/static_range_lis_query.py
    title: "\u9759\u7684\u533A\u9593\u6700\u9577\u5897\u52A0\u6587\u5B57\u5217\u30AF\
      \u30A8\u30EA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_lis_query
    links:
    - https://judge.yosupo.jp/problem/static_range_lis_query
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_lis_query


    from data_structure.static_range_lis_query import StaticRangeLISQuery


    n, q = map(int, input().split())

    P = [int(x) + 1 for x in input().split()]

    Q = [tuple(map(int, input().split())) for _ in range(q)]

    ans = StaticRangeLISQuery(P, Q)

    print(*ans, sep="\n")

    '
  dependsOn:
  - data_structure/static_range_lis_query.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_range_lis_query.test.py
  requiredBy: []
  timestamp: '2024-05-28 15:29:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_range_lis_query.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/static_range_lis_query.test.py
- /verify/test/library_checker/data_structure/static_range_lis_query.test.py.html
title: test/library_checker/data_structure/static_range_lis_query.test.py
---
