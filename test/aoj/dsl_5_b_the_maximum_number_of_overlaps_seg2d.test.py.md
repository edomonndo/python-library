---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: data_structure/segtree/segtree_2d.py
    title: "\u4E8C\u6B21\u5143\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B\n\
    \nfrom data_structure.segtree.segtree_2d import Segtree2d\n\nn = int(input())\n\
    seg = Segtree2d(1000, 1000, max, 0, [])\nfor _ in range(n):\n    x1, y1, x2, y2\
    \ = map(int, input().split())\n    seg.set(x1, y1, seg.get(x1, y1) + 1)\n    seg.set(x1,\
    \ y2, seg.get(x1, y2) - 1)\n    seg.set(x2, y1, seg.get(x2, y1) - 1)\n    seg.set(x2,\
    \ y2, seg.get(x2, y2) + 1)\n\nans = 0\nfor x in range(1000):\n    for y in range(1000):\n\
    \        ans = max(ans, seg.prod(0, 0, x + 1, y + 1))\nprint(ans)\n"
  dependsOn:
  - data_structure/segtree/segtree_2d.py
  isVerificationFile: true
  path: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py
  requiredBy: []
  timestamp: '2024-06-09 10:02:15+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py
- /verify/test/aoj/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py.html
title: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_seg2d.test.py
---
