---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/dual_segment_tree.py
    title: "\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dual Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D\n\
    \nfrom data_structure.dual_segment_tree import DualSegtree\n\nN, Q = map(int,\
    \ input().split())\nINF = (1 << 31) - 1\nA = [INF] * N\nID = float(\"inf\")\n\
    G = DualSegtree(\n    A, lambda f, x: x if f == ID else f, lambda f, g: g if f\
    \ == ID else f, ID\n)\n\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        s, t, x = q\n        G.apply(s, t + 1, x)\n    else:\n\
    \        x = q[0]\n        print(G.get(x))\n"
  dependsOn:
  - data_structure/dual_segment_tree.py
  isVerificationFile: true
  path: test/aoj/dsl_2_d_range_update_query.test.py
  requiredBy: []
  timestamp: '2024-02-26 12:20:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_2_d_range_update_query.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_2_d_range_update_query.test.py
- /verify/test/aoj/dsl_2_d_range_update_query.test.py.html
title: test/aoj/dsl_2_d_range_update_query.test.py
---
