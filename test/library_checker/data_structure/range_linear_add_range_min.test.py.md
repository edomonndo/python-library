---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: data_structure/segtree/linear_add_rmq.py
    title: data_structure/segtree/linear_add_rmq.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from data_structure.segtree.linear_add_rmq import LinearAddRmQ\n\n\nn, q\
    \ = map(int, input().split())\nA = [int(x) for x in input().split()]\ninf = float(\"\
    inf\")\nseg = LinearAddRmQ(A)\nfor i in range(q):\n    t, *qu = map(int, input().split())\n\
    \    if t == 0:\n        l, r, b, c = qu\n        seg.apply(l, r, b, c)\n    else:\n\
    \        l, r = qu\n        print(seg.prod(l, r))\n"
  dependsOn:
  - data_structure/segtree/linear_add_rmq.py
  isVerificationFile: true
  path: test/library_checker/data_structure/range_linear_add_range_min.test.py
  requiredBy: []
  timestamp: '2024-09-18 10:00:08+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library_checker/data_structure/range_linear_add_range_min.test.py
layout: document
title: Range Linear Add Range Min
---
