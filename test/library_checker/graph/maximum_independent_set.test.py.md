---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/maximum_independent_set.py
    title: "\u6700\u5927\u72EC\u7ACB\u70B9\u96C6\u5408"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/maximum_independent_set
    links:
    - https://judge.yosupo.jp/problem/maximum_independent_set
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: '# verification-helper: PROBLEM https://judge.yosupo.jp/problem/maximum_independent_set


    from graph.maximum_independent_set import maximum_independnet_set


    n, m = map(int, input().split())

    es = [tuple(map(int, input().split())) for _ in range(m)]

    size, res = maximum_independnet_set(n, es)

    print(size)

    print(*res)

    '
  dependsOn:
  - graph/maximum_independent_set.py
  isVerificationFile: true
  path: test/library_checker/graph/maximum_independent_set.test.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/maximum_independent_set.test.py
layout: document
title: Maximum Independent Set
---

