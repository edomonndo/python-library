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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def min_vertex_cover(adj: list[list[int]], r: int = 0) -> list[int]:\n  \
    \  n = len(adj)\n\n    selected = [0] * n\n    stack = [(~r, -1), (r, -1)]\n \
    \   while stack:\n        v, p = stack.pop()\n        if v >= 0:\n           \
    \ for u in adj[v]:\n                if u != p:\n                    stack += [(~u,\
    \ v), (u, v)]\n            continue\n        v = ~v\n        has_not_selected_v\
    \ = any(selected[u] == 0 for u in adj[v] if u != p)\n        if has_not_selected_v:\n\
    \            selected[v] = 1\n\n    return selected\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/minimum_vertex_cover.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/tree/minimum_vertex_cover.py
layout: document
redirect_from:
- /library/graph/tree/minimum_vertex_cover.py
- /library/graph/tree/minimum_vertex_cover.py.html
title: graph/tree/minimum_vertex_cover.py
---
