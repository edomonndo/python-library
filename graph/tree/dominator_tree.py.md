---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/dominator_tree.test.py
    title: Dominator Tree
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def dominator_tree(g: list[list[int]], r: int = 0):\n    n = len(g)\n\n \
    \   # label nodes with the arrival times of a dfs\n    sdom = [-1] * n\n    par\
    \ = [-1] * n\n    vs = []\n    k = 0\n\n    stack = [(r, -1)]\n    while stack:\n\
    \        v, p = stack.pop()\n        if sdom[v] != -1:\n            continue\n\
    \        if p != -1:\n            par[v] = p\n        sdom[v] = k\n        k +=\
    \ 1\n        vs.append(v)\n        for c in g[v]:\n            if sdom[c] == -1:\n\
    \                stack.append((c, v))\n\n    grev = [[] for _ in range(n)]\n \
    \   for u in range(n):\n        if sdom[u] == -1:\n            continue\n    \
    \    for v in g[u]:\n            grev[v].append(u)\n\n    # Union find\n    uf_par\
    \ = list(range(n))  # parent\n    val = list(range(n))  # min of sdom's v\n\n\
    \    def compress(v):\n        vs = []\n        while v != uf_par[v]:\n      \
    \      vs.append(v)\n            v = uf_par[v]\n        r = v\n        for v in\
    \ vs[::-1]:\n            if sdom[val[v]] > sdom[val[uf_par[v]]]:\n           \
    \     val[v] = val[uf_par[v]]\n            uf_par[v] = r\n        return val[v]\n\
    \n    # calculate sdom\n    us = [0] * n\n    bucket = [[] for _ in range(n)]\n\
    \    for w in vs[1:][::-1]:\n        for v in grev[w]:\n            sdom[w] =\
    \ min(sdom[w], sdom[compress(v)])\n        bucket[vs[sdom[w]]].append(w)\n   \
    \     p = par[w]\n        for v in bucket[p]:\n            us[v] = compress(v)\n\
    \        bucket[p] = []\n        uf_par[w] = p\n\n    # calculate idom\n    idom\
    \ = [-1] * n\n    idom[r] = sdom[r]\n    for w in vs[1:]:\n        u = us[w]\n\
    \        idom[w] = sdom[w] if sdom[w] == sdom[u] else idom[u]\n    for v in vs:\n\
    \        idom[v] = vs[idom[v]]\n    return idom\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/tree/dominator_tree.py
  requiredBy: []
  timestamp: '2024-07-04 12:06:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/dominator_tree.test.py
documentation_of: graph/tree/dominator_tree.py
layout: document
title: Dominator Tree
---

有向グラフから支配木を作成する．