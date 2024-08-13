---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/general_weighted_matching.py
    title: "\u91CD\u307F\u4ED8\u304D\u6700\u5927\u30DE\u30C3\u30C1\u30F3\u30B0"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/general_weighted_matching
    links:
    - https://judge.yosupo.jp/problem/general_weighted_matching
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/general_weighted_matching\n\
    \nfrom graph.general_weighted_matching import GeneralWeightedMatching\n\n\nn,\
    \ m = map(int, input().split())\nedges = [tuple(map(int, input().split())) for\
    \ _ in range(m)]\n\nsolver = GeneralWeightedMatching(n, edges)\nans, cnt = solver.solve()\n\
    print(cnt, ans)\nfor v in range(n):\n    u = solver.match[v]\n    if u > v:\n\
    \        print(v, u)\n"
  dependsOn:
  - graph/general_weighted_matching.py
  isVerificationFile: true
  path: test/library_checker/graph/general_weighted_matching.test.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/general_weighted_matching.test.py
layout: document
title: General Weighted Matching
---

