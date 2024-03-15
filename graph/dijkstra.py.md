---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_1_a_dijkstra.test.py
    title: test/aoj/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/shortest_path.test.py
    title: test/library_checker/graph/shortest_path.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\n\n\ndef dijkstra(graph: list[list[int]], start: int) -> tuple[list[int],\
    \ list[int]]:\n    INF = float(\"inf\")\n    n = len(graph)\n    dist = [INF]\
    \ * n\n    dist[start] = 0\n    prev = [-1] * n\n\n    que = [(0, start)]  # \u8DDD\
    \u96E2,\u9802\u70B9\n    while que:\n        c, u = heapq.heappop(que)\n     \
    \   if c > dist[u]:\n            continue\n        for nc, v in graph[u]:\n  \
    \          cost = dist[u] + nc\n            if cost < dist[v]:\n             \
    \   dist[v] = cost\n                prev[v] = u\n                heapq.heappush(que,\
    \ (cost, v))\n\n    return dist, prev\n\n\ndef get_path(prev: list[int], start:\
    \ int, goal: int) -> list[int]:\n    path = [goal]\n    while path[-1] != start:\n\
    \        path.append(prev[path[-1]])\n    return path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/dijkstra.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl_1_a_dijkstra.test.py
  - test/library_checker/graph/shortest_path.test.py
documentation_of: graph/dijkstra.py
layout: document
title: "Dijkstra\uFF08\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\uFF09"
---

$N$頂点,$M$辺の有向グラフで,頂点$u$から頂点$v$に距離$c$の辺を`graph[u] = [(c,v)]`で持つ.

### `dijkstra(N, graph, start)`

頂点$start$から各頂点への最短距離を計算する.

注意：距離が負の辺には適用不可

- Args
    - $N$: グラフの頂点数
    - $G$: 隣接リスト.頂点$u$から頂点$v$への距離$c$を`G[u] = [(c, v)]`で表す.
    - $start$: 開始する頂点番号
- Return
    - $dist$: 各頂点への距離を持つリスト
    - $prev$: 各頂点の親頂点を持つリスト  


### `get_path(prev, start, goal)`

頂点$start$から頂点$goal$までのパスを返す

- Args
    - $prev$: 各頂点の親頂点を持つリスト  
    - $start$, $goal$: 頂点番号
- Return
    - $path$: 頂点番号のリスト.(`path[0]=start`, `path[-1]=goal`)


