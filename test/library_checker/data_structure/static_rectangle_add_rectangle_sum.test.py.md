---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: geometory/offline_rectangle_add_rectangle_sum.py
    title: "\u77E9\u5F62\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97(\u30AA\u30D5\
      \u30E9\u30A4\u30F3)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
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
  timestamp: '2024-06-04 17:44:40+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
- /verify/test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py.html
title: test/library_checker/data_structure/static_rectangle_add_rectangle_sum.test.py
---
