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
  code: "def scc(n: int, edges: list[tuple[int, int]]) -> tuple[list[list[int]], list[int]]:\n\
    \    adj = [[] for _ in range(n)]\n    for u, v in edges:\n        adj[u].append(v)\n\
    \    low = [0] * n\n    comp = [0] * n\n    par = [-1] * n\n    ord = [-1] * n\n\
    \    st1, st2 = [], []\n    groups = []\n    idx = 0\n    for i in range(n):\n\
    \        if ord[i] != -1:\n            continue\n        st1 += [i, i]\n     \
    \   while st1:\n            v = st1.pop()\n            if ord[v] == -1:\n    \
    \            low[v] = ord[v] = idx\n                idx += 1\n               \
    \ st2.append(v)\n                for u in adj[v]:\n                    if ord[u]\
    \ == -1:\n                        st1 += [u, u]\n                        par[u]\
    \ = v\n                        continue\n                    low[v] = min(low[v],\
    \ ord[u])\n            else:\n                if low[v] == ord[v]:\n         \
    \           group = []\n                    u = None\n                    while\
    \ u != v:\n                        u = st2.pop()\n                        ord[u]\
    \ = n\n                        comp[u] = len(groups)\n                       \
    \ group.append(u)\n                    groups.append(group)\n                p\
    \ = par[v]\n                if p != -1:\n                    low[p] = min(low[p],\
    \ low[v])\n\n    groups = groups[::-1]  # \u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\
    \u30BD\u30FC\u30C8\u9806\n    for i in range(n):\n        comp[i] = len(groups)\
    \ - 1 - comp[i]\n    return groups, comp\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/scc.py
  requiredBy:
  - graph/scc_incremental.py
  timestamp: '2024-08-18 09:11:40+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/scc.test.py
  - test/aoj/grl/grl_3_c_strongly_connected_components.test.py
documentation_of: graph/scc.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
