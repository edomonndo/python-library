---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: tree/rooted_tree.py
    title: "\u6839\u4ED8\u304D\u6728"
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
  code: "from tree.rooted_tree import rooted_tree\n\n\ndef min_vertex_cover(adj: list[list[int]])\
    \ -> list[int]:\n    n = len(adj)\n    children, par = rooted_tree(adj, 0)\n\n\
    \    deg = [0] * n\n    stack = []\n    for v in range(n):\n        deg[v] = len(children[v])\n\
    \        if deg[v] == 0:\n            stack.append(v)\n\n    selected = [0] *\
    \ n\n    while stack:\n        v = stack.pop()\n\n        has_not_selected_v =\
    \ any(selected[u] == 0 for u in children[v])\n        if has_not_selected_v:\n\
    \            selected[v] = 1\n\n        p = par[v]\n        deg[p] -= 1\n    \
    \    if deg[p] == 0:\n            stack.append(p)\n\n    return selected\n"
  dependsOn:
  - tree/rooted_tree.py
  isVerificationFile: false
  path: tree/minimum_vertex_cover.py
  requiredBy: []
  timestamp: '2024-05-04 16:25:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/minimum_vertex_cover.py
layout: document
title: "\u6728\u306E\u6700\u5C0F\u9802\u70B9\u88AB\u8986"
---

[参考](https://algo-method.com/tasks/980)