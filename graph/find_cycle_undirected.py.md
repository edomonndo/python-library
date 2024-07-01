---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/cycle_detection_undirected.test.py
    title: test/library_checker/graph/cycle_detection_undirected.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def find_cycle(\n    N: int, M: int, G: list[list[int]]\n) -> tuple[int,\
    \ int, int, list[int], list[int]]:\n    visited = [0] * N\n    finished = [0]\
    \ * M\n    par_v = [None] * N\n    par_e = [None] * N\n\n    for i in range(N):\n\
    \        if visited[i]:\n            continue\n        stack = [(i, -1, -1)]\n\
    \        while stack:\n            v, p, e = stack.pop()  # v: \u9802\u70B9\u756A\
    \u53F7\uFF64p: v\u306E\u89AA\u9802\u70B9,e: v\u3068\u63A5\u7D9A\u3059\u308B\u8FBA\
    \n            if e != -1 and finished[e]:\n                continue\n        \
    \    if visited[v]:\n                par_v[v] = p\n                if e != -1:\n\
    \                    par_e[v] = e\n                return v, p, e, par_v, par_e\n\
    \            visited[v] = 1\n            if e != -1:\n                par_e[v]\
    \ = e\n                finished[e] = 1\n            par_v[v] = p\n           \
    \ for u, e in G[v]:\n                if finished[e]:\n                    continue\n\
    \                stack.append((u, v, e))\n\n    return -1, -1, -1, par_v, par_e\n\
    \n\ndef cycle_detection(N: int, M: int, G: list[int]):\n\n    v, p, e, par_v,\
    \ par_e = find_cycle(N, M, G)\n    if p == -1:\n        return [], []\n    else:\n\
    \        cycle_v = [p]\n        cycle_e = [e]\n        while v != p:\n       \
    \     e = par_e[p]\n            p = par_v[p]\n            cycle_v.append(p)\n\
    \            cycle_e.append(e)\n        return cycle_v[::-1], cycle_e[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/find_cycle_undirected.py
  requiredBy: []
  timestamp: '2024-07-02 07:09:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/cycle_detection_undirected.test.py
documentation_of: graph/find_cycle_undirected.py
layout: document
redirect_from:
- /library/graph/find_cycle_undirected.py
- /library/graph/find_cycle_undirected.py.html
title: graph/find_cycle_undirected.py
---
