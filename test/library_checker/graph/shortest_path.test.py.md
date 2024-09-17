---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: graph/dijkstra.py
    title: graph/dijkstra.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/shortest_path
    links:
    - https://judge.yosupo.jp/problem/shortest_path
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path\n\
    \nfrom graph.dijkstra import dijkstra, get_path\n\nINF = float(\"inf\")\nN, M,\
    \ s, t = map(int, input().split())\nG = [[] for _ in range(N)]\nfor _ in range(M):\n\
    \    u, v, c = map(int, input().split())\n    G[u].append((c, v))\n\ndist, prev\
    \ = dijkstra(G, s)\n\nif dist[t] == INF:\n    print(-1)\n    exit()\n\npath =\
    \ get_path(prev, s, t)\nprint(dist[t], len(path) - 1)\nfor i in range(len(path)\
    \ - 1):\n    print(path[i], path[i + 1])\n"
  dependsOn:
  - graph/dijkstra.py
  isVerificationFile: true
  path: test/library_checker/graph/shortest_path.test.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library_checker/graph/shortest_path.test.py
layout: document
title: Shortest Path
---

