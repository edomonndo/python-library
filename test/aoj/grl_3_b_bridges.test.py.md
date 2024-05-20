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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B\n\
    \nfrom graph.low_link import low_link\n\nN, M = map(int, input().split())\nG =\
    \ [[] for _ in range(N)]\nfor _ in range(M):\n    u, v = map(int, input().split())\n\
    \    G[u].append(v)\n    G[v].append(u)\n\n_, ans = low_link(G)\nans.sort()\n\
    for u, v in ans:\n    print(u, v)\n"
  dependsOn:
  - graph/low_link.py
  isVerificationFile: true
  path: test/aoj/grl_3_b_bridges.test.py
  requiredBy: []
  timestamp: '2024-02-09 17:45:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_3_b_bridges.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_3_b_bridges.test.py
- /verify/test/aoj/grl_3_b_bridges.test.py.html
title: test/aoj/grl_3_b_bridges.test.py
---