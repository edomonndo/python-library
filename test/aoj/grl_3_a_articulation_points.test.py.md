---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/low_link.py
    title: "\u9593\u63A5\u70B9\uFF0C\u6A4B"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_A\n\
    \nfrom graph.low_link import low_link\n\nN, M = map(int, input().split())\nG =\
    \ [[] for _ in range(N)]\nfor _ in range(M):\n    u, v = map(int, input().split())\n\
    \    G[u].append(v)\n    G[v].append(u)\n\nans, _ = low_link(N, G)\nans.sort()\n\
    if ans:\n    print(*ans, sep=\"\\n\")\n"
  dependsOn:
  - graph/low_link.py
  isVerificationFile: true
  path: test/aoj/grl_3_a_articulation_points.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_3_a_articulation_points.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_3_a_articulation_points.test.py
- /verify/test/aoj/grl_3_a_articulation_points.test.py.html
title: test/aoj/grl_3_a_articulation_points.test.py
---
