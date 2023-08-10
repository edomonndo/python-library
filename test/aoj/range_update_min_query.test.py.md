---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/lazy_segment_tree.py
    title: "\u9045\u5EF6\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Lazy Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_F
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_F
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_F\n\
    \nfrom data_structure.lazy_segment_tree import LazySegtree\n\nN, Q = map(int,\
    \ input().split())\nINF = (1 << 31) - 1\nA = [INF] * N\nID = float(\"inf\")\n\
    G = LazySegtree(\n    A, min, ID, lambda f, x: x if f == ID else f, lambda f,\
    \ g: g if f == ID else f, ID\n)\n\nfor _ in range(Q):\n    t, *q = map(int, input().split())\n\
    \    if t == 0:\n        s, t, x = q\n        G.apply(s, t + 1, x)\n    else:\n\
    \        s, t = q\n        print(G.prod(s, t + 1))\n"
  dependsOn:
  - data_structure/lazy_segment_tree.py
  isVerificationFile: true
  path: test/aoj/range_update_min_query.test.py
  requiredBy: []
  timestamp: '2023-08-10 08:46:39+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/range_update_min_query.test.py
layout: document
redirect_from:
- /verify/test/aoj/range_update_min_query.test.py
- /verify/test/aoj/range_update_min_query.test.py.html
title: test/aoj/range_update_min_query.test.py
---
