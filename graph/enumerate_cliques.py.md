---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/enumerate_cliques.test.py
    title: Enumerate Cliques
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\n\ndef enumerate_cliques(\n\
    \    n: int,\n    edges: tuple[int, int],\n    calc: Callable[[T, T], T],\n  \
    \  merge: Callable[[T, T], T],\n    e: T = 0,\n    include_empty: bool = False,\n\
    ) -> T:\n    g = [[0] * n for _ in range(n)]\n    deg = [0] * n\n    for u, v\
    \ in edges:\n        g[u][v] = g[v][u] = 1\n        deg[u] += 1\n        deg[v]\
    \ += 1\n\n    m = len(edges)\n    sm = 0\n    while (sm + 1) ** 2 <= 2 * m:\n\
    \        sm += 1\n\n    def compress(g: list[list[int]], sz: int, tmp: list[int])\
    \ -> list[int]:\n        bit = [0] * sz\n        for i in range(sz):\n       \
    \     for j in range(i):\n                if not g[tmp[i]][tmp[j]]:\n        \
    \            bit[i] |= 1 << j\n                    bit[j] |= 1 << i\n        return\
    \ bit\n\n    def f(g: list[list[int]], tmp: list[int], include_empty: bool, inner:\
    \ bool) -> None:\n        nonlocal res\n\n        sz = len(tmp) - inner\n    \
    \    bit = compress(g, sz, tmp)\n\n        for S in range(1 << sz):\n        \
    \    ok = 1\n            for i in range(sz):\n                if (S >> i) & 1\
    \ and S & bit[i]:\n                    ok = 0\n                    break\n   \
    \         if ok and (S or include_empty):\n                vs = [tmp[-1]] if inner\
    \ else []\n                for i in range(sz):\n                    if (S >> i)\
    \ & 1:\n                        vs.append(tmp[i])\n                res = merge(res,\
    \ calc(vs))\n        return\n\n    V = [1] * n\n    res = e\n    while True:\n\
    \        tmp = []\n        for u in range(n):\n            if V[u] and deg[u]\
    \ < sm:\n                for v in range(n):\n                    if u != v and\
    \ V[v] and g[u][v]:\n                        tmp.append(v)\n                tmp.append(u)\n\
    \                break\n        if not tmp:\n            break\n        f(g, tmp,\
    \ True, True)\n\n        u = tmp[-1]\n        V[u] = deg[u] = 0\n        for v\
    \ in range(n):\n            if u != v and V[v] and g[u][v]:\n                deg[v]\
    \ -= 1\n\n    tmp = [u for u in range(n) if V[u]]\n    f(g, tmp, include_empty,\
    \ False)\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/enumerate_cliques.py
  requiredBy: []
  timestamp: '2024-07-19 16:23:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/enumerate_cliques.test.py
documentation_of: graph/enumerate_cliques.py
layout: document
title: Enumerate Cliques
---
