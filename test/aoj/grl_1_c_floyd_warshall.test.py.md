---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/floyd_warshall.py
    title: "\u30D5\u30ED\u30A4\u30C9\u30FB\u30EF\u30FC\u30B7\u30E3\u30EB(\u5168\u70B9\
      \u5BFE\u6700\u77ED\u8DDD\u96E2)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C\n\
    \nfrom graph.floyd_warshall import floyd_warshall\n\nINF = float(\"inf\")\nN,\
    \ M = map(int, input().split())\nedges = [tuple(map(int, input().split())) for\
    \ _ in range(M)]\n\ndist = floyd_warshall(N, edges, True)\n\nfor i in range(N):\n\
    \    if dist[i][i] < 0:\n        print(\"NEGATIVE CYCLE\")\n        exit()\n\n\
    for u in range(N):\n    ans = []\n    for v in range(N):\n        ans.append(dist[u][v]\
    \ if dist[u][v] != INF else \"INF\")\n    print(*ans)\n"
  dependsOn:
  - graph/floyd_warshall.py
  isVerificationFile: true
  path: test/aoj/grl_1_c_floyd_warshall.test.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_1_c_floyd_warshall.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_1_c_floyd_warshall.test.py
- /verify/test/aoj/grl_1_c_floyd_warshall.test.py.html
title: test/aoj/grl_1_c_floyd_warshall.test.py
---
