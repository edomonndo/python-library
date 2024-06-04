---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: geometory/offline_static_rectangle_sum.py
    title: "\u77E9\u5F62\u548C(\u30AA\u30D5\u30E9\u30A4\u30F3\u30FB\u9759\u7684)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum\n\
    \nfrom geometory.offline_static_rectangle_sum import solve\n\nn, q = map(int,\
    \ input().split())\nps = [None] * n\nfor i in range(n):\n    ps[i] = tuple(map(int,\
    \ input().split()))\nqs = [None] * q\nfor i in range(q):\n    x1, y1, x2, y2 =\
    \ map(int, input().split())\n    qs[i] = (x1, y1, x2, y2)\n\nans = solve(ps, qs)\n\
    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - geometory/offline_static_rectangle_sum.py
  isVerificationFile: true
  path: test/library_checker/data_structure/rectangle_sum.test.py
  requiredBy: []
  timestamp: '2024-05-27 17:45:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/rectangle_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/rectangle_sum.test.py
- /verify/test/library_checker/data_structure/rectangle_sum.test.py.html
title: test/library_checker/data_structure/rectangle_sum.test.py
---
