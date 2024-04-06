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
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.13/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def centroids(\n    adj: list[list[int]], vcost: list[int] = None, root:\
    \ int = 0\n) -> list[int]:\n    n = len(adj)\n    if vcost is None:\n        vcost\
    \ = [1] * n\n\n    size = vcost[:]\n    stack = [(root, -1)]\n    while stack:\n\
    \        v, p = stack.pop()\n        if v >= 0:\n            for u in adj[v]:\n\
    \                if u != p:\n                    stack += [(~u, v), (u, v)]\n\
    \        elif p != -1:\n            size[p] += size[~v]\n\n    half = size[root]\
    \ // 2\n    stack = [(root, -1)]\n    res = []\n    while stack:\n        v, p\
    \ = stack.pop()\n        if v >= 0:\n            for u in adj[v]:\n          \
    \      if u != p:\n                    stack += [(~u, v), (u, v)]\n        else:\n\
    \            v = ~v\n            if any(u != p and size[u] > half for u in adj[v]):\n\
    \                continue\n            if size[root] - size[v] > half:\n     \
    \           continue\n            res.append(v)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/centroids.py
  requiredBy: []
  timestamp: '2024-04-07 01:04:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/centroids.py
layout: document
title: "\u91CD\u5FC3\u5224\u5B9A"
---

木の重心を求める.
重心は１つか２つの頂点で返る.

Verify:
- https://atcoder.jp/contests/abc348/tasks/abc348_e