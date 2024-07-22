---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/three_edge_connected_components.test.py
    title: Three-Edge-Connected Components
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\n\nsys.setrecursionlimit(2_000_000)\n\n\ndef three_edge_connected_components(adj:\
    \ list[list[int]]) -> list[list[int]]:\n\n    def _enumerate(v: int) -> list[int]:\n\
    \        res = []\n        u = v\n        while True:\n            res.append(u)\n\
    \            seen[u] = 1\n            u = nxt[u]\n            if u == v:\n   \
    \             break\n        return res\n\n    def _absorb(u: int, v: int) ->\
    \ None:\n        deg[u] += deg[v]\n        nxt[u], nxt[v] = nxt[v], nxt[u]\n\n\
    \    def _dfs(v: int, p: int) -> None:\n        nonlocal id_\n        seen[v]\
    \ = 1\n        pre[v] = id_\n        id_ += 1\n        for u in adj[v]:\n    \
    \        if u == v:\n                continue\n            if u == p:\n      \
    \          p = n\n                continue\n            if seen[u]:\n        \
    \        if pre[u] < pre[v]:\n                    deg[v] += 1\n              \
    \      low[v] = min(low[v], pre[u])\n                else:\n                 \
    \   deg[v] -= 1\n                    w = path[v]\n                    while w\
    \ != n and pre[w] <= pre[u] < post[w]:\n                        _absorb(v, w)\n\
    \                        w = path[w]\n                    path[v] = w\n      \
    \          continue\n            _dfs(u, v)\n            if path[u] == n and deg[u]\
    \ <= 1:\n                deg[v] += deg[u]\n                low[v] = min(low[v],\
    \ low[u])\n                continue\n            if deg[u] == 0:\n           \
    \     u = path[u]\n            if low[v] > low[u]:\n                low[v] = low[u]\n\
    \                u, path[v] = path[v], u\n            while u != n:\n        \
    \        _absorb(v, u)\n                u = path[u]\n        post[v] = id_\n\n\
    \    n = len(adj)\n    seen = [0] * n\n    pre = [-1] * n\n    post = [0] * n\n\
    \    path = [n] * n\n    low = [n] * n\n    deg = [0] * n\n    nxt = list(range(n))\n\
    \n    id_ = 0\n    for i in range(n):\n        if not seen[i]:\n            _dfs(i,\
    \ n)\n\n    res = []\n    seen = [0] * n\n    for i in range(n):\n        if not\
    \ seen[i]:\n            res.append(_enumerate(i))\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/three_edge_connected_components.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/three_edge_connected_components.test.py
documentation_of: graph/three_edge_connected_components.py
layout: document
title: "\u4E09\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
