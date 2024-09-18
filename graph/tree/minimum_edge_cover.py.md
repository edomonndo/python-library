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
  code: "def min_edge_cover(adj: list[list[int]], r: int = 0) -> tuple[int, list[int]]:\n\
    \    n = len(adj)\n\n    selected = [0] * n\n    cnt_selected_edge = 0\n    stack\
    \ = [(~r, -1), (r, -1)]\n    while stack:\n        v, p = stack.pop()\n      \
    \  if v >= 0 and selected[v] == 0:\n            for u in adj[v]:\n           \
    \     if u != p:\n                    stack += [(~u, v), (u, v)]\n           \
    \ continue\n        v = ~v\n        if selected[v] == 0:\n            selected[v]\
    \ = selected[p] = 1\n            cnt_selected_edge += 1\n\n    return cnt_selected_edge,\
    \ selected\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/minimum_edge_cover.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/tree/minimum_edge_cover.py
layout: document
title: "\u6728\u306E\u6700\u5C0F\u8FBA\u88AB\u8986"
---

[参考](https://algo-method.com/tasks/981)