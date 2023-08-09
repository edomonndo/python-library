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
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E\n\
    \nfrom data_structure.dual_segment_tree import DualSegtree\n\nN, Q = map(int,\
    \ input().split())\nA = [0] * N\nINF = float(\"inf\")\nG = DualSegtree(A, min,\
    \ INF, lambda f, x: f + x, lambda f, g: f + g, 0)\n\nfor _ in range(Q):\n    t,\
    \ *q = map(int, input().split())\n    if t == 0:\n        s, t, x = q\n      \
    \  G.apply(s - 1, t, x)\n    else:\n        x = q[0]\n        print(G.get(x -\
    \ 1))\n"
  dependsOn:
  - data_structure/dual_segment_tree.py
  isVerificationFile: true
  path: test/aoj/range_add_query.test.py
  requiredBy: []
  timestamp: '2023-08-10 00:04:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/range_add_query.test.py
layout: document
redirect_from:
- /verify/test/aoj/range_add_query.test.py
- /verify/test/aoj/range_add_query.test.py.html
title: test/aoj/range_add_query.test.py
---
