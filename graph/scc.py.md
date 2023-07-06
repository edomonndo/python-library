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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/PyPy/3.7.13/x64/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import List, Tuple\n\n\ndef scc(N: int, M: int, edges: List[Tuple[int,\
    \ int]]) -> List[int]:\n    start = [0] * (N + 1)\n    elist = [0] * M\n    for\
    \ e in edges:\n        start[e[0] + 1] += 1\n    for i in range(1, N + 1):\n \
    \       start[i] += start[i - 1]\n    counter = start[:]\n    for e in edges:\n\
    \        elist[counter[e[0]]] = e[1]\n        counter[e[0]] += 1\n    visited\
    \ = []\n    low = [0] * N\n    Ord = [-1] * N\n    ids = [0] * N\n    NG = [0,\
    \ 0]\n\n    def dfs(v: int):\n        stack = [(v, -1, 0), (v, -1, 1)]\n     \
    \   while stack:\n            v, bef, t = stack.pop()\n            if t:\n   \
    \             if bef != -1 and Ord[v] != -1:\n                    low[bef] = min(low[bef],\
    \ Ord[v])\n                    stack.pop()\n                    continue\n   \
    \             low[v] = NG[0]\n                Ord[v] = NG[0]\n               \
    \ NG[0] += 1\n                visited.append(v)\n                for i in range(start[v],\
    \ start[v + 1]):\n                    to = elist[i]\n                    if Ord[to]\
    \ == -1:\n                        stack.append((to, v, 0))\n                 \
    \       stack.append((to, v, 1))\n                    else:\n                \
    \        low[v] = min(low[v], Ord[to])\n            else:\n                if\
    \ low[v] == Ord[v]:\n                    while True:\n                       \
    \ u = visited.pop()\n                        Ord[u] = N\n                    \
    \    ids[u] = NG[1]\n                        if u == v:\n                    \
    \        break\n                    NG[1] += 1\n                low[bef] = min(low[bef],\
    \ low[v])\n\n    for i in range(N):\n        if Ord[i] == -1:\n            dfs(i)\n\
    \    for i in range(N):\n        ids[i] = NG[1] - 1 - ids[i]\n    group_num =\
    \ NG[1]\n    counts = [0] * group_num\n    for x in ids:\n        counts[x] +=\
    \ 1\n    groups = [[] for i in range(group_num)]\n    for i in range(N):\n   \
    \     groups[ids[i]].append(i)\n    return groups\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/scc.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/scc.py
layout: document
title: Strongly Connected Components
---

強連結成分に分解する。

### `scc(N: int, M: int, edges: List[Tuple[int, int]]) `

- Args
    - $N$: グラフの頂点の数
    - $M$: 辺の数
    - $edges$: 辺のリスト。各要素は`(u,v)`のタプルで、頂点$u$から頂点$v$への有向辺を指す。
- Return  
sccの返り値は2次元のリスト。 全体のリストの要素数は強連結成分の数だけあって、各リストの要素は強連結成分に含まれる頂点すべてが入る。