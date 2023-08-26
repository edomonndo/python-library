---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple\nfrom heapq import heappush, heappop\n\n\n\
    def dijkstra(N: int, graph: List[List[int]], start: int) -> Tuple[List[int], List[int]]:\n\
    \    INF = float(\"inf\")\n    dist = [INF] * N\n    dist[start] = 0\n    prev\
    \ = [-1] * N\n\n    que = [(0, start)]  # \u8DDD\u96E2,\u9802\u70B9\n    while\
    \ que:\n        c, u = heappop(que)\n        if c > dist[u]:\n            continue\n\
    \        for nc, v in graph[u]:\n            cost = dist[u] + nc\n           \
    \ if cost < dist[v]:\n                dist[v] = cost\n                prev[v]\
    \ = u\n                heappush(que, (cost, v))\n\n    return dist, prev\n\n\n\
    def get_path(prev: List[int], start: int, goal: int) -> List[int]:\n    path =\
    \ [goal]\n    while path[-1] != start:\n        path.append(prev[path[-1]])\n\
    \    return path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
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


