---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_c_floyd_warshall.test.py
    title: "GRL1C \u5168\u70B9\u5BFE\u9593\u6700\u77ED\u7D4C\u8DEF"
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def floyd_warshall(\n    N: int, edges: list[tuple[int, int, int]], directed=False\n\
    ) -> list[list[int]]:\n    INF = float(\"inf\")\n    dist = [[INF] * N for _ in\
    \ range(N)]\n    for i in range(N):\n        dist[i][i] = 0\n\n    for u, v, w\
    \ in edges:\n        dist[u][v] = w\n        if not directed:\n            dist[v][u]\
    \ = w\n\n    for i in range(N):\n        for u in range(N):\n            for v\
    \ in range(N):\n                nd = dist[u][i] + dist[i][v]\n               \
    \ if dist[u][v] > nd:\n                    dist[u][v] = nd\n\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/floyd_warshall.py
  requiredBy: []
  timestamp: '2023-09-15 08:31:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_1_c_floyd_warshall.test.py
documentation_of: graph/floyd_warshall.py
layout: document
redirect_from:
- /library/graph/floyd_warshall.py
- /library/graph/floyd_warshall.py.html
title: graph/floyd_warshall.py
---
