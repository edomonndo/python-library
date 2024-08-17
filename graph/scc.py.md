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
  - icon: ':x:'
    path: test/library_checker/graph/scc.test.py
    title: Strongly Connected Components
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def scc(n: int, edges: list[tuple[int, int]]) -> tuple[list[list[int]], list[int]]:\n\
    \    adj = [[] for _ in range(n)]\n    for u, v in edges:\n        adj[u].append(v)\n\
    \    low = [0] * n\n    comp_num = [0] * n\n    par = [-1] * n\n    ord = [-1]\
    \ * n\n    st1, st2 = [], []\n    groups = []\n    idx = 0\n    for i in range(n):\n\
    \        if ord[i] != -1:\n            continue\n        st1 += [i, i]\n     \
    \   while st1:\n            v = st1.pop()\n            if ord[v] == -1:\n    \
    \            low[v] = ord[v] = idx\n                idx += 1\n               \
    \ st2.append(v)\n                for u in adj[v]:\n                    if ord[u]\
    \ == -1:\n                        st1 += [u, u]\n                        par[u]\
    \ = v\n                        continue\n                    low[v] = min(low[v],\
    \ ord[u])\n            else:\n                if low[v] == ord[v]:\n         \
    \           group = []\n                    u = None\n                    while\
    \ u != v:\n                        u = st2.pop()\n                        ord[u]\
    \ = n\n                        comp_num[u] = len(groups)\n                   \
    \     group.append(u)\n                    groups.append(group)\n            \
    \    p = par[v]\n                if p != -1:\n                    low[p] = min(low[p],\
    \ low[v])\n    return groups, comp_num\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/scc.py
  requiredBy:
  - graph/scc_incremental.py
  timestamp: '2024-08-18 08:15:35+09:00'
  verificationStatus: LIBRARY_SOME_WA
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