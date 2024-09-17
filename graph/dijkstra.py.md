---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/shortest_paths.py
    title: Shortest paths
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_1_a_dijkstra.test.py
    title: "GRL1A \u5358\u4E00\u59CB\u70B9\u6700\u77ED\u7D4C\u8DEF"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/shortest_path.test.py
    title: Shortest Path
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import *\n\n\ndef dijkstra(graph: list[list[int]], start: int)\
    \ -> tuple[list[int], list[int]]:\n    INF = float(\"inf\")\n    n = len(graph)\n\
    \    dist = [INF] * n\n    dist[start] = 0\n    prev = [-1] * n\n\n    que = [(0,\
    \ start)]  # \u8DDD\u96E2,\u9802\u70B9\n    while que:\n        c, u = heappop(que)\n\
    \        if c > dist[u]:\n            continue\n        for nc, v in graph[u]:\n\
    \            cost = dist[u] + nc\n            if cost < dist[v]:\n           \
    \     dist[v] = cost\n                prev[v] = u\n                heappush(que,\
    \ (cost, v))\n\n    return dist, prev\n\n\ndef get_path(prev: list[int], start:\
    \ int, goal: int) -> list[int]:\n    path = [goal]\n    while path[-1] != start:\n\
    \        path.append(prev[path[-1]])\n    return path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/dijkstra.py
  requiredBy:
  - graph/shortest_paths.py
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/shortest_path.test.py
  - test/aoj/grl/grl_1_a_dijkstra.test.py
documentation_of: graph/dijkstra.py
layout: document
redirect_from:
- /library/graph/dijkstra.py
- /library/graph/dijkstra.py.html
title: graph/dijkstra.py
---
