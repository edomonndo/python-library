---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: tree/centroid_decomposition.py
    title: "\u91CD\u5FC3\u5206\u89E3"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/vertex_add_range_contour_sum_on_tree.test.py
    title: Vertex Add Range Contour Sum on Tree
  - icon: ':heavy_check_mark:'
    path: test/library_checker/data_structure/vertex_get_range_contour_add_on_tree.test.py
    title: Vertex Get Range Contour Add on Tree
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from tree.centroid_decomposition import CentroidDecomposition\n\nfrom collections\
    \ import deque\nfrom typing import Callable, TypeVar\n\nT = TypeVar(\"T\")\n\n\
    \nclass ContourQuery:\n    def __init__(self, adj: list[list[int]], f: Callable[[list[T]],\
    \ None]):\n        self.n = n = len(adj)\n        self.adj = adj\n        cd =\
    \ CentroidDecomposition(adj, 0)\n        self.root = root = cd.get_root()\n  \
    \      self.H = H = cd.get_graph()\n\n        self.par = par = [-1] * n\n    \
    \    self.dep = dep = [-1] * n\n        st = [(root, -1, 0)]\n        while st:\n\
    \            v, p, d = st.pop()\n            par[v] = p\n            dep[v] =\
    \ d\n            for u in H[v]:\n                st.append((u, v, d + 1))\n\n\
    \        h = max(dep) + 1\n        self.vt = vt = [[] for _ in range(n)]\n   \
    \     self.ct = ct = [[] for _ in range(n)]\n        self.cpar = cpar = [[-1]\
    \ * h for _ in range(n)]\n        self.dist = dist = [[-1] * h for _ in range(n)]\n\
    \        self._build()\n\n        self.rdx1 = rdx1 = [[-1] * h for _ in range(n)]\n\
    \        self.rdx2 = rdx2 = [[-1] * h for _ in range(n)]\n        dat = [[] for\
    \ _ in range(n << 1)]\n        for i in range(n):\n            dat[i] = [0] *\
    \ len(vt[i])\n            for j, (_, a) in enumerate(vt[i]):\n               \
    \ dat[i][j] = a\n                rdx1[a][dep[i]] = j\n\n        self.idx = idx\
    \ = [[] for _ in range(n)]\n        cnt = n\n        for i in range(n):\n    \
    \        idx[i] = [0] * len(ct[i])\n            for j in range(len(ct[i])):\n\
    \                if len(ct[i][j]) == 0:\n                    continue\n      \
    \          dat[cnt] = [0] * len(ct[i][j])\n                for k, (_, a) in enumerate(ct[i][j]):\n\
    \                    dat[cnt][k] = a\n                    rdx2[a][dep[i]] = k\n\
    \                idx[i][j] = cnt\n                cnt += 1\n\n        self.ddx1\
    \ = ddx1 = [[] for _ in range(n)]\n        for i in range(n):\n            m =\
    \ vt[i][-1][0]\n            ddx1[i] = [-1] * (m + 1)\n            for j, (a, _)\
    \ in enumerate(vt[i]):\n                if ddx1[i][a] == -1:\n               \
    \     ddx1[i][a] = j\n\n        self.ddx2 = ddx2 = [[] for _ in range(n)]\n  \
    \      self.ddx3 = ddx3 = [[] for _ in range(n)]\n        self.ddx4 = ddx4 = [[]\
    \ for _ in range(n)]\n        for i in range(n):\n            sz = len(ct[i])\n\
    \            ddx2[i] = [0] * sz\n            ddx3[i] = [0] * sz\n            ddx4[i]\
    \ = [0] * sz\n            for j in range(sz):\n                if len(ct[i][j])\
    \ == 0:\n                    continue\n                m = ct[i][j][-1][0]\n \
    \               ddx2[i][j] = [-1] * (m + 1)\n                ddx3[i][j] = [-1]\
    \ * (m + 1)\n                ddx4[i][j] = [-1] * (m + 1)\n                for\
    \ k, (a, _) in enumerate(ct[i][j]):\n                    if ddx4[i][j][a] == -1:\n\
    \                        ddx4[i][j][a] = k\n            for j in range(1, len(vt[i])):\n\
    \                a, b = vt[i][j]\n                if ddx2[i][cpar[b][dep[i]]][a]\
    \ == -1:\n                    ddx2[i][cpar[b][dep[i]]][a] = j\n              \
    \  ddx3[i][cpar[b][dep[i]]][a] = j\n\n        f(dat)\n        return\n\n    def\
    \ _build(self):\n        adj, dep, H = self.adj, self.dep, self.H\n        vt,\
    \ ct, cpar, dist = self.vt, self.ct, self.cpar, self.dist\n        st = [self.root]\n\
    \        dq = deque()\n        while st:\n            v = st.pop()\n         \
    \   d = dep[v]\n            vt[v].append((0, v))\n            ct[v] = [[] for\
    \ _ in range(len(adj[v]))]\n            cpar[v][d] = v\n            dist[v][d]\
    \ = 0\n            for i in range(len(adj[v])):\n                u = adj[v][i]\n\
    \                if dep[u] < d:\n                    continue\n              \
    \  cpar[u][d] = i\n                dist[u][d] = 1  # edge weight\n           \
    \     dq.append((u, 1))\n            while dq:\n                u, d2 = dq.popleft()\n\
    \                c = cpar[u][d]\n                vt[v].append((d2, u))\n     \
    \           ct[v][c].append((d2, u))\n                for i in range(len(adj[u])):\n\
    \                    u2 = adj[u][i]\n                    if dep[u2] < d:\n   \
    \                     continue\n                    if cpar[u2][d] != -1:\n  \
    \                      continue\n                    cpar[u2][d] = c\n       \
    \             dist[u2][d] = d2 + 1  # edge weight\n                    dq.append((u2,\
    \ d2 + 1))\n            for u in H[v]:\n                st.append(u)\n\n    def\
    \ vertex(self, v: int, f: Callable[[T, T], None]) -> None:\n        par, cpar,\
    \ rdx1, rdx2, idx = self.par, self.cpar, self.rdx1, self.rdx2, self.idx\n    \
    \    f(v, 0)\n        u = v\n        for d in range(self.dep[v] - 1, -1, -1):\n\
    \            p = par[u]\n            cp = cpar[u][d]\n            f(p, rdx1[v][d])\n\
    \            f(idx[p][cp], rdx2[v][d])\n            u = p\n        return\n\n\
    \    def contour(self, v: int, k: int, f: Callable[[T, T], None]) -> None:\n \
    \       ddx1, ddx2, ddx3 = self.ddx1, self.ddx2, self.ddx3\n        vt, dist,\
    \ par, cpar = self.vt, self.dist, self.par, self.cpar\n        if k < len(ddx1[v]):\n\
    \            l = ddx1[v][k]\n            r = ddx1[v][k + 1] if k + 1 < len(ddx1[v])\
    \ else len(vt[v])\n            f(v, l, r)\n        u = v\n        for d in range(self.dep[v]\
    \ - 1, -1, -1):\n            k -= dist[v][d]\n            p = par[u]\n       \
    \     cp = cpar[u][d]\n            if 0 <= k < len(ddx1[p]):\n               \
    \ l = ddx1[p][k]\n                r = ddx1[p][k + 1] if k + 1 < len(ddx1[p]) else\
    \ len(vt[p])\n                if k < len(ddx2[p][cp]):\n                    l2\
    \ = ddx2[p][cp][k]\n                    r2 = ddx3[p][cp][k] + 1\n            \
    \        f(p, l, l2)\n                    f(p, r2, r)\n                else:\n\
    \                    f(p, l, r)\n            k += dist[v][d]\n            u =\
    \ p\n        return\n\n    def _inner_range_contour(\n        self, v: int, k:\
    \ int, f: Callable[[T, T], None], g: Callable[[T, T], None]\n    ):\n        ddx1,\
    \ ddx4 = self.ddx1, self.ddx4\n        vt, ct, par, cpar = self.vt, self.ct, self.par,\
    \ self.cpar\n        idx, dist = self.idx, self.dist\n        r = ddx1[v][k] if\
    \ k < len(ddx1[v]) else len(vt[v])\n        f(v, r)\n        u = v\n        for\
    \ d in range(self.dep[v] - 1, -1, -1):\n            k -= dist[v][d]\n        \
    \    p = par[u]\n            cp = cpar[u][d]\n            if k > 0:\n        \
    \        r = ddx1[p][k] if k < len(ddx1[p]) else len(vt[p])\n                f(p,\
    \ r)\n                r2 = ddx4[p][cp][k] if k < len(ddx4[p][cp]) else len(ct[p][cp])\n\
    \                g(idx[p][cp], r2)\n            k += dist[v][d]\n            u\
    \ = p\n        return\n\n    def range_contour(\n        self,\n        v: int,\n\
    \        l: int,\n        r: int,\n        f: Callable[[T, T], None],\n      \
    \  g: Callable[[T, T], None],\n    ):\n        self._inner_range_contour(v, l,\
    \ g, f)\n        self._inner_range_contour(v, r, f, g)\n"
  dependsOn:
  - tree/centroid_decomposition.py
  isVerificationFile: false
  path: tree/contour_query.py
  requiredBy: []
  timestamp: '2024-06-10 12:42:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/data_structure/vertex_add_range_contour_sum_on_tree.test.py
  - test/library_checker/data_structure/vertex_get_range_contour_add_on_tree.test.py
documentation_of: tree/contour_query.py
layout: document
redirect_from:
- /library/tree/contour_query.py
- /library/tree/contour_query.py.html
title: tree/contour_query.py
---
