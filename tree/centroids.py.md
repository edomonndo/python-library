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
  code: "def centroids(adj: list[list[int]], root: int = 0) -> list[int]:\n    n =\
    \ len(adj)\n    res = []\n    size = [0] * n\n    stack = [(~root, -1), (root,\
    \ -1)]\n    while stack:\n        v, p = stack.pop()\n        if v >= 0:\n   \
    \         size[v] = 1\n            is_centroid = True\n            for u in adj[v]:\n\
    \                if u == p:\n                    continue\n                stack.append((~u,\
    \ v))\n                stack.append((u, v))\n        else:\n            v = ~v\n\
    \            for u in adj[v]:\n                if u == p:\n                  \
    \  continue\n                size[v] += size[u]\n                if size[v] >\
    \ n // 2:\n                    is_centroid = False\n            if n - size[v]\
    \ > n // 2:\n                is_centroid = False\n            if is_centroid:\n\
    \                res.append(v)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/centroids.py
  requiredBy: []
  timestamp: '2024-03-15 13:13:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/centroids.py
layout: document
title: "\u91CD\u5FC3\u5224\u5B9A"
---

木の重心を求める.
重心は１つか２つの頂点で返る.

Not verify