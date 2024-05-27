---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: geometory/offline_point_add_rectangle_sum.py
    title: geometory/offline_point_add_rectangle_sum.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum\n\
    from geometory.offline_point_add_rectangle_sum import OfflinePointAddRectangleSum\n\
    \n\nn, q = map(int, input().split())\nG = OfflinePointAddRectangleSum()\nfor _\
    \ in range(n):\n    x, y, w = map(int, input().split())\n    G.add_point(x, y,\
    \ w)\nfor i in range(q):\n    t, *qu = map(int, input().split())\n    if t ==\
    \ 0:\n        x, y, w = qu\n        G.add_point(x, y, w)\n    else:\n        x1,\
    \ y1, x2, y2 = qu\n        G.add_query(x1, y1, x2, y2)\n\nans = G.solve()\nprint(*ans,\
    \ sep=\"\\n\")\n"
  dependsOn:
  - geometory/offline_point_add_rectangle_sum.py
  isVerificationFile: true
  path: test/library_checker/data_structure/point_add_rectangle_sum.test.py
  requiredBy: []
  timestamp: '2024-05-27 17:45:23+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/point_add_rectangle_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/point_add_rectangle_sum.test.py
- /verify/test/library_checker/data_structure/point_add_rectangle_sum.test.py.html
title: test/library_checker/data_structure/point_add_rectangle_sum.test.py
---
