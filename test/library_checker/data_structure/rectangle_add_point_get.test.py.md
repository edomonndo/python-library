---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/offline_rectangle_add_point_get.py
    title: "\u77E9\u5F62\u52A0\u7B97\u30FB\uFF11\u70B9\u53D6\u5F97(\u30AA\u30D5\u30E9\
      \u30A4\u30F3)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/rectangle_add_point_get
    links:
    - https://judge.yosupo.jp/problem/rectangle_add_point_get
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_add_point_get\n\
    \nfrom geometory.offline_rectangle_add_point_get import OfflineRectangleAddPointGet\n\
    \n\nn, q = map(int, input().split())\nsolver = OfflineRectangleAddPointGet()\n\
    for _ in range(n):\n    l, d, r, u, w = map(int, input().split())\n    solver.add_rect(l,\
    \ d, r, u, w)\nfor _ in range(q):\n    t, *qu = map(int, input().split())\n  \
    \  if t == 0:\n        l, d, r, u, w = qu\n        solver.add_rect(l, d, r, u,\
    \ w)\n    else:\n        x, y = qu\n        solver.add_query(x, y)\nprint(*solver.solve(),\
    \ sep=\"\\n\")\n"
  dependsOn:
  - geometory/offline_rectangle_add_point_get.py
  isVerificationFile: true
  path: test/library_checker/data_structure/rectangle_add_point_get.test.py
  requiredBy: []
  timestamp: '2024-06-04 17:56:08+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/rectangle_add_point_get.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/rectangle_add_point_get.test.py
- /verify/test/library_checker/data_structure/rectangle_add_point_get.test.py.html
title: test/library_checker/data_structure/rectangle_add_point_get.test.py
---
