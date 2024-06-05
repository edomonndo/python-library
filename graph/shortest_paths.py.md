---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/leftist_heap.py
    title: Leftist Heap
  - icon: ':heavy_check_mark:'
    path: graph/dijkstra.py
    title: "Dijkstra\uFF08\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\uFF09"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/k_shortest_walk.test.py
    title: test/library_checker/graph/k_shortest_walk.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from heapq import *\nfrom data_structure.basic.leftist_heap import LefitistHeap\n\
    from graph.dijkstra import dijkstra\n\n\ndef shortest_paths(n: int, edges: list[tuple[int,\
    \ int, int]], s: int, t: int, k: int):\n    adj = [[] for _ in range(n)]\n   \
    \ adj_rev = [[] for _ in range(n)]\n    for u, v, w in edges:\n        adj[u].append((w,\
    \ v))\n        adj_rev[v].append((w, u))\n    inf = float(\"inf\")\n    dist,\
    \ prev = dijkstra(adj_rev, t)\n    if dist[s] == inf:\n        return []\n\n \
    \   g = [[] for _ in range(n)]\n    for u in range(n):\n        if prev[u] !=\
    \ -1:\n            g[prev[u]].append(u)\n\n    h = [None] * n\n    q = [t]\n \
    \   for u in q:\n        seen = False\n        for w, v in adj[u]:\n         \
    \   if dist[v] == inf:\n                continue\n            c = w + dist[v]\
    \ - dist[u]\n            if not seen and v == prev[u] and c == 0:\n          \
    \      seen = True\n                continue\n            h[u] = LefitistHeap.insert(h[u],\
    \ c, v)\n        for v in g[u]:\n            h[v] = h[u]\n            q.append(v)\n\
    \n    ans = [dist[s]]\n    if not h[s]:\n        return ans\n\n    q = [(dist[s]\
    \ + h[s].key, h[s])]\n    while q and len(ans) < k:\n        cd, ch = heappop(q)\n\
    \        ans.append(cd)\n        if h[ch.value]:\n            heappush(q, (cd\
    \ + h[ch.value].key, h[ch.value]))\n        if ch.left:\n            heappush(q,\
    \ (cd + ch.left.key - ch.key, ch.left))\n        if ch.right:\n            heappush(q,\
    \ (cd + ch.right.key - ch.key, ch.right))\n    return ans\n"
  dependsOn:
  - data_structure/basic/leftist_heap.py
  - graph/dijkstra.py
  isVerificationFile: false
  path: graph/shortest_paths.py
  requiredBy: []
  timestamp: '2024-06-04 09:09:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/k_shortest_walk.test.py
documentation_of: graph/shortest_paths.py
layout: document
title: Shortest paths
---
