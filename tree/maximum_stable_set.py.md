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
  code: "def max_stable_set(adj: list[list[int]], r: int = 0) -> list[int]:\n    n\
    \ = len(adj)\n\n    selected = [0] * n\n    stack = [(~r, -1), (r, -1)]\n    while\
    \ stack:\n        v, p = stack.pop()\n        if v >= 0:\n            for u in\
    \ adj[v]:\n                if u != p:\n                    stack += [(~u, v),\
    \ (u, v)]\n            continue\n        v = ~v\n        all_children_not_selected\
    \ = all(selected[u] == 0 for u in adj[v] if u != p)\n        if all_children_not_selected:\n\
    \            selected[v] = 1\n\n    return selected\n"
  dependsOn: []
  isVerificationFile: false
  path: tree/maximum_stable_set.py
  requiredBy: []
  timestamp: '2024-05-09 09:04:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tree/maximum_stable_set.py
layout: document
title: "\u6728\u306E\u6700\u5927\u5B89\u5B9A\u96C6\u5408"
---

[参考](https://algo-method.com/tasks/978)