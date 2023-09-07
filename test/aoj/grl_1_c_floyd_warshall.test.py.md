---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/GRL_1_C\n\
    \nfrom graph.floyd_warshall import floyd_warshall\n\nINF = float(\"inf\")\nN,\
    \ M = map(int, input().split())\nedges = [tuple(map(int, input().split())) for\
    \ _ in range(M)]\n\ndist = floyd_warshall(N, edges, True)\n\nfor i in range(N):\n\
    \    if dist[i][i] < 0:\n        print(\"NEGATIVE CYCLE\")\n        exit()\n\n\
    for u in range(N):\n    ans = []\n    for v in range(N):\n        ans.append(dist[u][v]\
    \ if dist[u][v] != INF else \"INF\")\n    print(*ans)\n"
  dependsOn: []
  isVerificationFile: true
  path: test/aoj/grl_1_c_floyd_warshall.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl_1_c_floyd_warshall.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl_1_c_floyd_warshall.test.py
- /verify/test/aoj/grl_1_c_floyd_warshall.test.py.html
title: test/aoj/grl_1_c_floyd_warshall.test.py
---
