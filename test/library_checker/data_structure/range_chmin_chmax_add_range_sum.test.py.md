---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segment_tree_beats.py
    title: Segment Tree Beats
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum\n\
    \nfrom data_structure.segment_tree_beats import SegtreeBeats\n\nN, Q = map(int,\
    \ input().split())\nA = [int(x) for x in input().split()]\ng = SegtreeBeats(A)\n\
    for _ in range(Q):\n    t, *q = map(int, input().split())\n    if t == 0:\n  \
    \      l, r, b = q\n        g.range_chmin(l, r, b)\n    elif t == 1:\n       \
    \ l, r, b = q\n        g.range_chmax(l, r, b)\n    elif t == 2:\n        l, r,\
    \ b = q\n        g.range_add(l, r, b)\n    else:\n        l, r = q\n        print(g.get_sum(l,\
    \ r))\n"
  dependsOn:
  - data_structure/segment_tree_beats.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
  requiredBy: []
  timestamp: '2024-02-09 17:45:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
layout: document
redirect_from:
- /verify/test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
- /verify/test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py.html
title: test/library_checker/data_structure/range_chmin_chmax_add_range_sum.test.py
---
