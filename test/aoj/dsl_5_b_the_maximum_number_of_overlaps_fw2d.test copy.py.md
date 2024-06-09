---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/fenwick_tree/dynamic_fenwick_tree_2d.py
    title: "\u4E8C\u6B21\u5143\u52D5\u7684Fenwick Tree"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B\n\
    \nfrom data_structure.fenwick_tree.dynamic_fenwick_tree_2d import DynamicFenwickTree2d\n\
    \nn = int(input())\nfw = DynamicFenwickTree2d(1000, 1000, 0)\nfor _ in range(n):\n\
    \    x1, y1, x2, y2 = map(int, input().split())\n    fw.add_rect(x1, y1, x2 -\
    \ 1, y2 - 1, 1)\n\nans = 0\nfor x in range(1000):\n    for y in range(1000):\n\
    \        ans = max(ans, fw.sum0(x, y))\nprint(ans)\n"
  dependsOn:
  - data_structure/fenwick_tree/dynamic_fenwick_tree_2d.py
  isVerificationFile: false
  path: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
  requiredBy: []
  timestamp: '2024-06-09 10:02:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
layout: document
redirect_from:
- /library/test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
- /library/test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py.html
title: test/aoj/dsl_5_b_the_maximum_number_of_overlaps_fw2d.test copy.py
---
