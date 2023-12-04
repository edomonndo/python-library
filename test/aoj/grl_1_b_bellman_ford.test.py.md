---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: graph/bellman_ford.py
    title: "\u30D9\u30EB\u30DE\u30F3\u30D5\u30A9\u30FC\u30C9"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_B\n\
    \nfrom graph.bellman_ford import bellmanFord\n\nINF = float(\"inf\")\nN, M, r\
    \ = map(int, input().split())\nG = [[] for _ in range(N)]\nfor _ in range(M):\n\
    \    u, v, w = map(int, input().split())\n    G[u].append((w, v))\n\ndist, _ =\
    \ bellmanFord(N, G, r)\nif dist == -1:\n    print(\"NEGATIVE CYCLE\")\n    exit()\n\
    \nfor d in dist:\n    if d == INF:\n        print(\"INF\")\n    else:\n      \
    \  print(d)\n"
  dependsOn:
  - graph/bellman_ford.py
  isVerificationFile: true
  path: test/aoj/grl_1_b_bellman_ford.test.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/aoj/grl_1_b_bellman_ford.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_1_b_bellman_ford.test.py
- /verify/test/aoj/grl_1_b_bellman_ford.test.py.html
title: test/aoj/grl_1_b_bellman_ford.test.py
---
