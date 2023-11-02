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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\ndef bfs(N, G, s):\n    dist = [-1] * N\n\
    \    dist[s] = 0\n\n    que = deque([s])\n    while que:\n        v = que.popleft()\n\
    \        for u in G[v]:\n            if dist[u] == -1:\n                dist[u]\
    \ = dist[v] + 1\n                que.append(u)\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/bfs.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/bfs.py
layout: document
title: "\u5E45\u512A\u5148\u63A2\u7D22"
---
