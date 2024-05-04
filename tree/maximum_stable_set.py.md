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
  code: "from tree.rooted_tree import rooted_tree\n\n\ndef max_stable_set(adj: list[list[int]])\
    \ -> list[int]:\n    n = len(adj)\n    children, par = rooted_tree(adj, 0)\n\n\
    \    deg = [0] * n\n    stack = []\n    for v in range(n):\n        deg[v] = len(children[v])\n\
    \        if deg[v] == 0:\n            stack.append(v)\n\n    selected = [0] *\
    \ n\n    while stack:\n        v = stack.pop()\n        all_children_not_selected\
    \ = all(selected[u] == 0 for u in children[v])\n        if all_children_not_selected:\n\
    \            selected[v] = 1\n\n        nv = par[v]\n        deg[nv] -= 1\n  \
    \      if deg[nv] == 0:\n            stack.append(nv)\n\n    return selected\n"
  dependsOn:
  - tree/rooted_tree.py
  isVerificationFile: false
  path: tree/maximum_stable_set.py
  requiredBy: []
  timestamp: '2024-05-04 16:25:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/maximum_stable_set.py
layout: document
title: "\u6728\u306E\u6700\u5927\u5B89\u5B9A\u96C6\u5408"
---

[参考](https://algo-method.com/tasks/978)