---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/offline_rectangle_add_rectangle_sum.py
    title: geometory/offline_rectangle_add_rectangle_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum\n\
    \nfrom geometory.offline_rectangle_add_rectangle_sum import (\n    OfflineRectangleAddRectangleSum,\n\
    )\n\nn, q = map(int, input().split())\nsolver = OfflineRectangleAddRectangleSum()\n\
    for _ in range(n):\n    l, d, r, u, w = map(int, input().split())\n    solver.add_rect(l,\
    \ d, r, u, w)\nfor _ in range(q):\n    l, d, r, u = map(int, input().split())\n\
    \    solver.add_query(l, d, r, u)\nprint(*solver.solve(), sep=\"\\n\")\n"
  dependsOn:
  - geometory/offline_rectangle_add_rectangle_sum.py
  isVerificationFile: true
  path: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
layout: document
title: Static Rectangle Add Rectangle Sum
---
