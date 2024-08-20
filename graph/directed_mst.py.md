---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: data_structure/basic/skew_heap.py
    title: data_structure/basic/skew_heap.py
  - icon: ':heavy_check_mark:'
    path: graph/connectivity/unionfind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/library_checker/graph/directed_mst.test.py
    title: Directed MST
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from typing import Optional\n\nfrom graph.connectivity.unionfind import UnionFind\n\
    from data_structure.basic.skew_heap import SkewHeap\n\n\ndef directed_mst(\n \
    \   n: int, edges: list[tuple[int, int, int]], root: int = 0\n) -> Optional[list[int]]:\n\
    \n    m = len(edges)\n    heaps = [SkewHeap() for _ in range(n)]\n    for ei,\
    \ (_, v, w) in enumerate(edges):\n        heaps[v].push(w * m + ei)\n\n    uf\
    \ = UnionFind(n)\n    from_ = [0] * n\n    cost = [0] * n\n    used = [0] * n\n\
    \    used[root] = 2\n    stem = [-1] * n\n    eis = []\n    par_e = [-1] * m\n\
    \n    for v in range(n):\n        if used[v] != 0:\n            continue\n   \
    \     selected, st, cnt = [], [], 0\n        while used[v] != 2:\n           \
    \ used[v] = 1\n            selected.append(v)\n            if heaps[v].empty():\n\
    \                return None\n            cost[v], ei = divmod(heaps[v].pop(),\
    \ m)\n            from_[v] = uf.leader(edges[ei][0])\n            if stem[v] ==\
    \ -1:\n                stem[v] = ei\n            if from_[v] == v:\n         \
    \       continue\n            eis.append(ei)\n            while cnt:\n       \
    \         par_e[st.pop()] = ei\n                cnt -= 1\n            st.append(ei)\n\
    \            if used[from_[v]] == 1:\n                p = v\n                while\
    \ True:\n                    if not heaps[p].empty():\n                      \
    \  heaps[p].add(-cost[p] * m)\n                    if p != v:\n              \
    \          uf.merge(v, p)\n                        heaps[v].meld(heaps[p])\n \
    \                   p = uf.leader(from_[p])\n                    cnt += 1\n  \
    \                  if p == v:\n                        break\n            else:\n\
    \                v = from_[v]\n        for v in selected:\n            used[v]\
    \ = 2\n\n    used = [0] * m\n    res = []\n    for ei in eis[::-1]:\n        if\
    \ used[ei]:\n            continue\n        res.append(ei)\n        x = stem[edges[ei][1]]\n\
    \        while x != ei:\n            used[x] = 1\n            x = par_e[x]\n \
    \   return res\n"
  dependsOn:
  - graph/connectivity/unionfind.py
  - data_structure/basic/skew_heap.py
  isVerificationFile: false
  path: graph/directed_mst.py
  requiredBy: []
  timestamp: '2024-08-20 10:54:57+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/library_checker/graph/directed_mst.test.py
documentation_of: graph/directed_mst.py
layout: document
redirect_from:
- /library/graph/directed_mst.py
- /library/graph/directed_mst.py.html
title: graph/directed_mst.py
---
