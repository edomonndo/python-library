---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl_1_b_bellman_ford.test.py
    title: test/aoj/grl_1_b_bellman_ford.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def bellmanFord(G: list[list[int]], start: int = 0):\n    INF = float(\"\
    inf\")\n    n = len(G)\n    dist = [INF] * n\n    pre = [-1] * n\n    dist[start]\
    \ = 0\n    loop = 0\n    for i in range(n):\n        loop += 1\n        updated\
    \ = False\n        for u in range(n):\n            if dist[u] == INF:\n      \
    \          continue\n            for w, v in G[u]:\n                nd = dist[u]\
    \ + w\n                if nd < dist[v]:\n                    updated = True\n\
    \                    pre[v] = u\n                    dist[v] = nd\n        if\
    \ not updated:\n            break\n        if i == n - 1:\n            return\
    \ -1, -1\n    return dist, pre\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/bellman_ford.py
  requiredBy: []
  timestamp: '2023-12-04 22:53:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl_1_b_bellman_ford.test.py
documentation_of: graph/bellman_ford.py
layout: document
title: "\u30D9\u30EB\u30DE\u30F3\u30D5\u30A9\u30FC\u30C9"
---

負の辺があるときに最短経路を求められる．
有向閉路があるときは，$(-1,-1)$を返す．
