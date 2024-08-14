---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: graph/scc_incremental.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3(Incremental)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_c_strongly_connected_components.test.py
    title: "GRL3C \u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/scc.test.py
    title: Strongly Connected Components
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def scc(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:\n    start\
    \ = [0] * (n + 1)\n    m = len(edges)\n    elist = [0] * m\n    for e in edges:\n\
    \        start[e[0] + 1] += 1\n    for i in range(1, n + 1):\n        start[i]\
    \ += start[i - 1]\n    counter = start[:]\n    for e in edges:\n        elist[counter[e[0]]]\
    \ = e[1]\n        counter[e[0]] += 1\n    visited = []\n    low = [0] * n\n  \
    \  ord = [-1] * n\n    ids = [0] * n\n    NG = [0, 0]\n\n    def dfs(v: int):\n\
    \        stack = [(v, -1, 0), (v, -1, 1)]\n        while stack:\n            v,\
    \ bef, t = stack.pop()\n            if t:\n                if bef != -1 and ord[v]\
    \ != -1:\n                    low[bef] = min(low[bef], ord[v])\n             \
    \       stack.pop()\n                    continue\n                low[v] = NG[0]\n\
    \                ord[v] = NG[0]\n                NG[0] += 1\n                visited.append(v)\n\
    \                for i in range(start[v], start[v + 1]):\n                   \
    \ to = elist[i]\n                    if ord[to] == -1:\n                     \
    \   stack.append((to, v, 0))\n                        stack.append((to, v, 1))\n\
    \                    else:\n                        low[v] = min(low[v], ord[to])\n\
    \            else:\n                if low[v] == ord[v]:\n                   \
    \ while True:\n                        u = visited.pop()\n                   \
    \     ord[u] = n\n                        ids[u] = NG[1]\n                   \
    \     if u == v:\n                            break\n                    NG[1]\
    \ += 1\n                low[bef] = min(low[bef], low[v])\n\n    for i in range(n):\n\
    \        if ord[i] == -1:\n            dfs(i)\n    for i in range(n):\n      \
    \  ids[i] = NG[1] - 1 - ids[i]\n    group_num = NG[1]\n    counts = [0] * group_num\n\
    \    for x in ids:\n        counts[x] += 1\n    groups = [[] for i in range(group_num)]\n\
    \    for i in range(n):\n        groups[ids[i]].append(i)\n    return groups\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/scc.py
  requiredBy:
  - graph/scc_incremental.py
  timestamp: '2024-07-23 17:42:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_3_c_strongly_connected_components.test.py
  - test/library_checker/graph/scc.test.py
documentation_of: graph/scc.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
---

強連結成分に分解する.

### `scc(N: int, M: int, edges: List[Tuple[int, int]]) `

- Args
    - $N$: グラフの頂点の数
    - $M$: 辺の数
    - $edges$: 辺のリスト.各要素は`(u,v)`のタプルで,頂点$u$から頂点$v$への有向辺を指す.
- Return  
sccの返り値は2次元のリスト. 全体のリストの要素数は強連結成分の数だけあって,各リストの要素は強連結成分に含まれる頂点すべてが入る.