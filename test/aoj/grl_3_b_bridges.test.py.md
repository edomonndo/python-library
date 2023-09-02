---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_3_B\n\
    \nfrom graph.low_link import low_link\n\nN, M = map(int, input().split())\nG =\
    \ [[] for _ in range(N)]\nfor _ in range(M):\n    u, v = map(int, input().split())\n\
    \    G[u].append(v)\n    G[v].append(u)\n\n_, ans = low_link(N, G)\nans.sort()\n\
    for u, v in ans:\n    print(u, v)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_3_b_bridges.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl_3_b_bridges.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_3_b_bridges.test.py
- /verify/test/aoj/grl_3_b_bridges.test.py.html
title: test/aoj/grl_3_b_bridges.test.py
---
