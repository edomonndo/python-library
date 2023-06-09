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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.3/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple, Optional\n\n\ndef two_sat(n: int, clause:\
    \ List[Tuple[int, bool, int, bool]]) -> Optional[List[bool]]:\n    answer = [0]\
    \ * n\n    edges = []\n    N = 2 * n\n    for s in clause:\n        i, f, j, g\
    \ = s\n        edges.append((2 * i + (0 if f else 1), 2 * j + (1 if g else 0)))\n\
    \        edges.append((2 * j + (0 if g else 1), 2 * i + (1 if f else 0)))\n  \
    \  M = len(edges)\n    start = [0] * (N + 1)\n    elist = [0] * M\n    for e in\
    \ edges:\n        start[e[0] + 1] += 1\n    for i in range(1, N + 1):\n      \
    \  start[i] += start[i - 1]\n    counter = start[:]\n    for e in edges:\n   \
    \     elist[counter[e[0]]] = e[1]\n        counter[e[0]] += 1\n    visited = []\n\
    \    low = [0] * N\n    Ord = [-1] * N\n    ids = [0] * N\n    NG = [0, 0]\n\n\
    \    def dfs(v):\n        stack = [(v, -1, 0), (v, -1, 1)]\n        while stack:\n\
    \            v, bef, t = stack.pop()\n            if t:\n                if bef\
    \ != -1 and Ord[v] != -1:\n                    low[bef] = min(low[bef], Ord[v])\n\
    \                    stack.pop()\n                    continue\n             \
    \   low[v] = NG[0]\n                Ord[v] = NG[0]\n                NG[0] += 1\n\
    \                visited.append(v)\n                for i in range(start[v], start[v\
    \ + 1]):\n                    to = elist[i]\n                    if Ord[to] ==\
    \ -1:\n                        stack.append((to, v, 0))\n                    \
    \    stack.append((to, v, 1))\n                    else:\n                   \
    \     low[v] = min(low[v], Ord[to])\n            else:\n                if low[v]\
    \ == Ord[v]:\n                    while True:\n                        u = visited.pop()\n\
    \                        Ord[u] = N\n                        ids[u] = NG[1]\n\
    \                        if u == v:\n                            break\n     \
    \               NG[1] += 1\n                low[bef] = min(low[bef], low[v])\n\
    \n    for i in range(N):\n        if Ord[i] == -1:\n            dfs(i)\n    for\
    \ i in range(N):\n        ids[i] = NG[1] - 1 - ids[i]\n    for i in range(n):\n\
    \        if ids[2 * i] == ids[2 * i + 1]:\n            return None\n        answer[i]\
    \ = ids[2 * i] < ids[2 * i + 1]\n    return answer\n"
  dependsOn: []
  isVerificationFile: false
  path: math/two_sat.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: math/two_sat.py
layout: document
redirect_from:
- /library/math/two_sat.py
- /library/math/two_sat.py.html
title: math/two_sat.py
---
