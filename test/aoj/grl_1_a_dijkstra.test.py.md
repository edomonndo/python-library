---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_A\n\
    \nfrom graph.dijkstra import dijkstra\n\nINF = float(\"inf\")\nN, M, r = map(int,\
    \ input().split())\nG = [[] for _ in range(N)]\nfor _ in range(M):\n    u, v,\
    \ w = map(int, input().split())\n    G[u].append((w, v))\n\ndist, _ = dijkstra(G,\
    \ r)\nfor i in range(N):\n    print(dist[i] if dist[i] != INF else \"INF\")\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_1_a_dijkstra.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_1_a_dijkstra.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_1_a_dijkstra.test.py
- /verify/test/aoj/grl_1_a_dijkstra.test.py.html
title: test/aoj/grl_1_a_dijkstra.test.py
---
