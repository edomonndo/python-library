---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: data_structure/segment_tree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
    links:
    - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A\n\
    \nfrom data_structure.segment_tree import RangeMinQuery\n\nN, Q = map(int, input().split())\n\
    INF = (1 << 31) - 1\nG = RangeMinQuery([INF] * N)\n\nans = []\nfor _ in range(Q):\n\
    \    t, x, y = map(int, input().split())\n    if t == 0:\n        G.update(x,\
    \ y)\n    else:\n        ans.append(G.query(x, y + 1))\nprint(*ans, sep=\"\\n\"\
    )\n"
  dependsOn:
  - data_structure/segment_tree.py
  isVerificationFile: true
  path: test/aoj/dsl_2_a_range_min_query.test.py
  requiredBy: []
  timestamp: '2023-08-19 03:09:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl_2_a_range_min_query.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl_2_a_range_min_query.test.py
- /verify/test/aoj/dsl_2_a_range_min_query.test.py.html
title: test/aoj/dsl_2_a_range_min_query.test.py
---
