---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segtree/linear_add_rmq.py
    title: "\u7B49\u5DEE\u6570\u5217\u52A0\u7B97\u30FB\u6700\u5C0F\u5024\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_linear_add_range_min
    links:
    - https://judge.yosupo.jp/problem/range_linear_add_range_min
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_linear_add_range_min\n\
    \nfrom data_structure.segtree.linear_add_rmq import LinearAddRmQ\n\nn, q = map(int,\
    \ input().split())\nA = [int(x) for x in input().split()]\ninf = float(\"inf\"\
    )\nseg = LinearAddRmQ(A)\nfor i in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        l, r, b, c = qu\n        seg.apply(l, r, b, c)\n    else:\n\
    \        l, r = qu\n        print(seg.prod(l, r))\n"
  dependsOn:
  - data_structure/segtree/linear_add_rmq.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_linear_add_range_min.test.py
  requiredBy: []
  timestamp: '2024-09-18 10:52:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_linear_add_range_min.test.py
layout: document
title: Range Linear Add Range Min
---
