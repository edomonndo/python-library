---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/fenwick_tree/point_set_range_frequency.py
    title: "1\u70B9\u66F4\u65B0\u30FB\u533A\u9593\u983B\u5EA6\uFF08\u30AA\u30D5\u30E9\
      \u30A4\u30F3\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_frequency
    links:
    - https://judge.yosupo.jp/problem/point_set_range_frequency
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_frequency\n\
    \nfrom data_structure.fenwick_tree.point_set_range_frequency import PointSetRangeFrequency\n\
    \nn, q = map(int, input().split())\nA = [int(x) for x in input().split()]\n\n\
    solver = PointSetRangeFrequency(A)\n\nfor _ in range(q):\n    t, *qu = map(int,\
    \ input().split())\n    if t == 0:\n        p, x = qu\n        solver.add_set_query(p,\
    \ x)\n    else:\n        l, r, x = qu\n        solver.add_freq_query(l, r, x)\n\
    print(*solver.solve(), sep=\"\\n\")\n"
  dependsOn:
  - data_structure/fenwick_tree/point_set_range_frequency.py
  isVerificationFile: true
  path: test/library_checker/data_structure/point_set_range_frequency.test.py
  requiredBy: []
  timestamp: '2024-06-11 11:00:20+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/point_set_range_frequency.test.py
layout: document
title: Point Set Range Frequency
---
