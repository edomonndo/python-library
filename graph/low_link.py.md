---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_a_articulation_points.test.py
    title: "GRL3A \u95A2\u7BC0\u70B9"
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_b_bridges.test.py
    title: "GRL3B \u6A4B"
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/two_edge_connected_components.test.py
    title: Two-Edge-Connected Components
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LowLink:\n    def __init__(self, adj: list[list[int]]):\n        self.n\
    \ = n = len(adj)\n        self.order = order = [-1] * n\n        self.low = low\
    \ = [n] * n\n        self.child = child = [[] for _ in range(n)]\n        self.is_root\
    \ = is_root = [0] * n\n        self.roots = roots = []\n\n        par = [-1] *\
    \ n\n        idx = 0\n        for u in range(n):\n            if order[u] != -1:\n\
    \                continue\n            is_root[u] = 1\n            roots.append(u)\n\
    \            st = [u]\n            par[u] = -2\n            while st:\n      \
    \          v = st.pop()\n                if v >= 0:\n                    if order[v]\
    \ != -1:\n                        continue\n                    order[v] = idx\n\
    \                    low[v] = idx\n                    idx += 1\n            \
    \        if v != u:\n                        child[par[v]].append(v)\n       \
    \                 st.append(~v)\n                    check_p = 0\n           \
    \         for nv in adj[v]:\n                        if nv == par[v] and check_p\
    \ == 0:\n                            check_p += 1\n                          \
    \  continue\n                        elif order[nv] != -1:\n                 \
    \           low[v] = min(low[v], order[nv])\n                        else:\n \
    \                           par[nv] = v\n                            st.append(nv)\n\
    \                    continue\n                v = ~v\n                p = par[v]\n\
    \                low[p] = min(low[p], low[v])\n\n    def get_articulation(self)\
    \ -> list[int]:\n        order, low, is_root, child = self.order, self.low, self.is_root,\
    \ self.child\n        res = []\n        for v in range(self.n):\n            if\
    \ is_root[v]:\n                if len(child[v]) >= 2:\n                    res.append(v)\n\
    \                continue\n            for u in child[v]:\n                if\
    \ order[v] <= low[u]:\n                    res.append(v)\n                   \
    \ break\n        return res\n\n    def get_bridge(self) -> list[tuple[int, int]]:\n\
    \        order, low, roots, child = self.order, self.low, self.roots, self.child\n\
    \        res = []\n        for v in roots:\n            st = [v]\n           \
    \ while st:\n                v = st.pop()\n                for u in child[v]:\n\
    \                    if order[v] < low[u]:\n                        if u < v:\n\
    \                            res.append((u, v))\n                        else:\n\
    \                            res.append((v, u))\n                    st.append(u)\n\
    \        return res\n\n    def two_edge_connected_components(self) -> tuple[list[int],\
    \ list[tuple[int, int]]]:\n        order, low, roots, child = self.order, self.low,\
    \ self.roots, self.child\n\n        components = [-1] * self.n\n        new_edges\
    \ = []\n        idx = 0\n        for v in roots:\n            components[v] =\
    \ idx\n            st = [v]\n            while st:\n                v = st.pop()\n\
    \                for u in child[v]:\n                    if order[v] < low[u]:\n\
    \                        idx += 1\n                        components[u] = idx\n\
    \                        if components[v] < idx:\n                           \
    \ new_edges.append((components[v], idx))\n                        else:\n    \
    \                        new_edges.append((idx, components[v]))\n            \
    \        else:\n                        components[u] = components[v]\n      \
    \              st.append(u)\n            idx += 1\n        return components,\
    \ new_edges\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/low_link.py
  requiredBy: []
  timestamp: '2024-07-22 09:16:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/two_edge_connected_components.test.py
  - test/aoj/grl/grl_3_b_bridges.test.py
  - test/aoj/grl/grl_3_a_articulation_points.test.py
documentation_of: graph/low_link.py
layout: document
redirect_from:
- /library/graph/low_link.py
- /library/graph/low_link.py.html
title: graph/low_link.py
---
