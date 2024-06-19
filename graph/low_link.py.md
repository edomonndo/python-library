---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_a_articulation_points.test.py
    title: test/aoj/grl/grl_3_a_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_3_b_bridges.test.py
    title: test/aoj/grl/grl_3_b_bridges.test.py
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/two_edge_connected_components.test.py
    title: test/library_checker/graph/two_edge_connected_components.test.py
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
    \ = n = len(adj)\n        order = [-1] * n\n        low = [n] * n\n        par\
    \ = [-1] * n\n        children = [[] for _ in range(n)]\n\n        seen = [0]\
    \ * n\n        idx = 0\n        for u in range(n):\n            if order[u] !=\
    \ -1:\n                continue\n            seen[u] = 1\n            st = [u]\n\
    \            par[u] = -2\n            while st:\n                v = st.pop()\n\
    \                if v >= 0:\n                    if order[v] != -1:\n        \
    \                continue\n                    order[v] = idx\n              \
    \      low[v] = idx\n                    idx += 1\n                    if v !=\
    \ u:\n                        children[par[v]].append(v)\n                   \
    \     st.append(~v)\n                    check_p = 0\n                    for\
    \ nv in adj[v]:\n                        if nv == par[v] and check_p == 0:\n \
    \                           check_p += 1\n                            continue\n\
    \                        elif order[nv] != -1:\n                            low[v]\
    \ = min(low[v], order[nv])\n                        else:\n                  \
    \          par[nv] = v\n                            st.append(nv)\n          \
    \          continue\n                v = ~v\n                p = par[v]\n    \
    \            low[p] = min(low[p], low[v])\n        self.order = order\n      \
    \  self.low = low\n        self.roots = [i for i, v in enumerate(seen) if v]\n\
    \        self.children = children\n\n    def get_articulation(self) -> list[int]:\n\
    \        order, low, roots, children = self.order, self.low, self.roots, self.children\n\
    \        res = [0] * self.n\n        for v in range(self.n):\n            if v\
    \ in roots:\n                if len(children[v]) >= 2:\n                    res[v]\
    \ = 1\n                continue\n            for u in children[v]:\n         \
    \       if order[v] <= low[u]:\n                    res[v] = 1\n             \
    \       break\n        return res\n\n    def get_bridge(self) -> list[tuple[int,\
    \ int]]:\n        order, low, roots, children = self.order, self.low, self.roots,\
    \ self.children\n        res = []\n        for v in roots:\n            st = [v]\n\
    \            while st:\n                v = st.pop()\n                for u in\
    \ children[v]:\n                    if order[v] < low[u]:\n                  \
    \      if u < v:\n                            res.append((u, v))\n           \
    \             else:\n                            res.append((v, u))\n        \
    \            st.append(u)\n        return res\n\n    def two_edge_connected_components(self)\
    \ -> tuple[list[int], list[tuple[int, int]]]:\n        order, low, roots, children\
    \ = self.order, self.low, self.roots, self.children\n\n        components = [-1]\
    \ * self.n\n        new_edges = []\n        idx = 0\n        for v in roots:\n\
    \            components[v] = idx\n            st = [v]\n            while st:\n\
    \                v = st.pop()\n                for u in children[v]:\n       \
    \             if order[v] < low[u]:\n                        idx += 1\n      \
    \                  components[u] = idx\n                        if components[v]\
    \ < idx:\n                            new_edges.append((components[v], idx))\n\
    \                        else:\n                            new_edges.append((idx,\
    \ components[v]))\n                    else:\n                        components[u]\
    \ = components[v]\n                    st.append(u)\n            idx += 1\n  \
    \      return components, new_edges\n\n    def three_edge_connected_components(self)\
    \ -> list[int]:\n        order, low, roots, children = self.order, self.low, self.roots,\
    \ self.children\n        raise NotImplementedError\n\n    def biconnected_components(self)\
    \ -> list[int]:\n        order, low, roots, children = self.order, self.low, self.roots,\
    \ self.children\n        raise NotImplementedError\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/low_link.py
  requiredBy: []
  timestamp: '2024-06-12 10:06:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/two_edge_connected_components.test.py
  - test/aoj/grl/grl_3_a_articulation_points.test.py
  - test/aoj/grl/grl_3_b_bridges.test.py
documentation_of: graph/low_link.py
layout: document
title: "\u9593\u63A5\u70B9\uFF0C\u6A4B"
---

グラフから取り除くと連結でなくなる頂点(間接点)と辺(橋)を求める．