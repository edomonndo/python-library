---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library_checker/graph/general_weighted_matching.test.py
    title: General Weighted Matching
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\ninf = 1 << 60\n\n\nclass GeneralWeightedMatching:\n\
    \    def __init__(self, n, edges: list[tuple[int, int, int]]):\n        self.n\
    \ = n\n        self.nx = n\n        self.m = m = 2 * n + 1\n        m2 = m * m\n\
    \        self.U = [0] * m2\n        self.V = [0] * m2\n        self.W = [0] *\
    \ m2\n        self.match = [0] * m\n        self.slack = [0] * m\n        self.flower\
    \ = [[] for _ in range(m)]\n        self.flower_from = [0] * m2\n        self.label\
    \ = [0] * m\n        self.root = [0] * m\n        self.par = [0] * m\n       \
    \ self.col = [0] * m\n        self.vis = [0] * m\n        self.que = deque()\n\
    \        self.t = 0\n        for u in range(1, m):\n            for v in range(1,\
    \ m):\n                self.U[u * m + v] = u\n                self.V[u * m + v]\
    \ = v\n        for u, v, w in edges:\n            u += 1\n            v += 1\n\
    \            self.W[u * m + v] = max(self.W[u * m + v], w)\n            self.W[v\
    \ * m + u] = max(self.W[v * m + u], w)\n\n    def dist(self, u: int, v: int) ->\
    \ int:\n        U, V, W, label, m = self.U, self.V, self.W, self.label, self.m\n\
    \n        u, v = U[u * m + v], V[u * m + v]\n        return label[u] + label[v]\
    \ - W[u * m + v] * 2\n\n    def update_slack(self, u: int, x: int) -> None:\n\
    \        slack, dist = self.slack, self.dist\n\n        if not slack[x] or dist(u,\
    \ x) < dist(slack[x], x):\n            slack[x] = u\n\n    def set_slack(self,\
    \ x: int) -> None:\n        slack, root, col, W = self.slack, self.root, self.col,\
    \ self.W\n\n        slack[x] = 0\n        for u in range(1, self.n + 1):\n   \
    \         if W[u * self.m + x] > 0 and root[u] != x and col[root[u]] == 0:\n \
    \               self.update_slack(u, x)\n\n    def que_push(self, x: int) -> None:\n\
    \        que, flower = self.que, self.flower\n\n        st = [x]\n        while\
    \ st:\n            x = st.pop()\n            if x <= self.n:\n               \
    \ que.append(x)\n                continue\n            st += flower[x]\n\n   \
    \ def set_root(self, x: int, b: int) -> None:\n        root, flower = self.root,\
    \ self.flower\n\n        st = [x]\n        while st:\n            x = st.pop()\n\
    \            root[x] = b\n            if x <= self.n:\n                continue\n\
    \            st += flower[x]\n\n    def get_pr(self, b: int, xr: int) -> int:\n\
    \        f = self.flower[b]\n        pr = f.index(xr)\n        if pr & 1:\n  \
    \          f = self.flower[b] = f[0:1] + f[1:][::-1]\n            return len(f)\
    \ - pr\n        else:\n            return pr\n\n    def set_match(self, u: int,\
    \ v: int) -> None:\n        match, flower, U, V = self.match, self.flower, self.U,\
    \ self.V\n\n        match[u] = V[u * self.m + v]\n        if u <= self.n:\n  \
    \          return\n        xr = self.flower_from[u * self.m + U[u * self.m + v]]\n\
    \        pr = self.get_pr(u, xr)\n        f = flower[u]\n        for i in range(pr):\n\
    \            self.set_match(f[i], f[i ^ 1])\n        self.set_match(xr, v)\n \
    \       flower[u] = f[pr:] + f[:pr]\n\n    def augment(self, u: int, v: int) ->\
    \ None:\n        root, match, par = self.root, self.match, self.par\n\n      \
    \  xnv = root[match[u]]\n        self.set_match(u, v)\n        while xnv:\n  \
    \          self.set_match(xnv, root[par[xnv]])\n            u, v = root[par[xnv]],\
    \ xnv\n            xnv = root[match[u]]\n            self.set_match(u, v)\n\n\
    \    def get_lca(self, u: int, v: int) -> int:\n        vis, root, match, par\
    \ = self.vis, self.root, self.match, self.par\n\n        self.t += 1\n       \
    \ while u or v:\n            if not u:\n                u, v = v, u\n        \
    \        continue\n            if vis[u] == self.t:\n                return u\n\
    \            vis[u] = self.t\n            u = root[match[u]]\n            if u:\n\
    \                u = root[par[u]]\n            u, v = v, u\n        return 0\n\
    \n    def add_blossom(self, u: int, lca: int, v: int) -> None:\n        root,\
    \ match, par = self.root, self.match, self.par\n        U, V, W, m, flower_from\
    \ = self.U, self.V, self.W, self.m, self.flower_from\n\n        b = self.n + 1\n\
    \        while b <= self.nx and root[b]:\n            b += 1\n        if b > self.nx:\n\
    \            self.nx += 1\n        self.label[b] = 0\n        self.col[b] = 0\n\
    \        match[b] = match[lca]\n        f = self.flower[b] = []\n        f.append(lca)\n\
    \        x = u\n        while x != lca:\n            f.append(x)\n           \
    \ y = root[match[x]]\n            f.append(y)\n            self.que_push(y)\n\
    \            x = root[par[y]]\n        f = self.flower[b] = f[0:1] + f[1:][::-1]\n\
    \        x = v\n        while x != lca:\n            f.append(x)\n           \
    \ y = root[match[x]]\n            f.append(y)\n            self.que_push(y)\n\
    \            x = root[par[y]]\n        self.set_root(b, b)\n        for x in range(1,\
    \ self.nx + 1):\n            W[b * m + x] = W[x * m + b] = 0\n        for x in\
    \ range(1, self.n + 1):\n            flower_from[b * m + x] = 0\n        for xs\
    \ in f:\n            for x in range(1, self.nx + 1):\n                if W[b *\
    \ m + x] == 0 or self.dist(xs, x) < self.dist(b, x):\n                    U[b\
    \ * m + x] = U[xs * m + x]\n                    U[x * m + b] = U[x * m + xs]\n\
    \                    V[b * m + x] = V[xs * m + x]\n                    V[x * m\
    \ + b] = V[x * m + xs]\n                    W[b * m + x] = W[xs * m + x]\n   \
    \                 W[x * m + b] = W[x * m + xs]\n            for x in range(1,\
    \ self.n + 1):\n                if flower_from[xs * m + x]:\n                \
    \    flower_from[b * m + x] = xs\n        self.set_slack(b)\n\n    def expand_blossom(self,\
    \ b: int) -> None:\n        par, col, slack = self.par, self.col, self.slack\n\
    \        U, m = self.U, self.m\n\n        f = self.flower[b]\n        for fi in\
    \ f:\n            self.set_root(fi, fi)\n        xr = self.flower_from[b * m +\
    \ U[b * m + par[b]]]\n        pr = self.get_pr(b, xr)\n        f = self.flower[b]\n\
    \        for i in range(0, pr, 2):\n            xs = f[i]\n            xns = f[i\
    \ + 1]\n            par[xs] = U[xns * m + xs]\n            col[xs] = 1\n     \
    \       col[xns] = 0\n            slack[xs] = 0\n            self.set_slack(xns)\n\
    \            self.que_push(xns)\n        col[xr] = 1\n        par[xr] = par[b]\n\
    \        for i in range(pr + 1, len(f)):\n            xs = f[i]\n            col[xs]\
    \ = -1\n            self.set_slack(xs)\n        self.root[b] = 0\n\n    def on_found_edge(self,\
    \ u: int, v: int) -> int:\n        root, match, slack = self.root, self.match,\
    \ self.slack\n        col, par = self.col, self.par\n\n        eu = self.U[u *\
    \ self.m + v]\n        ev = self.V[u * self.m + v]\n        u = root[eu]\n   \
    \     v = root[ev]\n        if col[v] == -1:\n            par[v] = eu\n      \
    \      col[v] = 1\n            nu = root[match[v]]\n            slack[v] = slack[nu]\
    \ = 0\n            col[nu] = 0\n            self.que_push(nu)\n        elif col[v]\
    \ == 0:\n            lca = self.get_lca(u, v)\n            if not lca:\n     \
    \           self.augment(u, v)\n                self.augment(v, u)\n         \
    \       return 1\n            else:\n                self.add_blossom(u, lca,\
    \ v)\n        return 0\n\n    def matching(self) -> int:\n        root, match,\
    \ col, par = self.root, self.match, self.col, self.par\n        slack, label,\
    \ W = self.slack, self.label, self.W\n\n        for i in range(self.nx + 1):\n\
    \            col[i] = -1\n            slack[i] = 0\n        self.que.clear()\n\
    \        for x in range(1, self.nx + 1):\n            if root[x] == x and not\
    \ match[x]:\n                par[x] = 0\n                col[x] = 0\n        \
    \        self.que_push(x)\n        if not self.que:\n            return 0\n  \
    \      while True:\n            while self.que:\n                u = self.que.popleft()\n\
    \                if col[root[u]] == 1:\n                    continue\n       \
    \         for v in range(1, self.n + 1):\n                    if W[u * self.m\
    \ + v] and root[u] != root[v]:\n                        if self.dist(u, v) ==\
    \ 0:\n                            if self.on_found_edge(u, v):\n             \
    \                   return 1\n                        else:\n                \
    \            self.update_slack(u, root[v])\n            d = inf\n            for\
    \ b in range(self.n + 1, self.nx + 1):\n                if root[b] == b and col[b]\
    \ == 1:\n                    d = min(d, label[b] // 2)\n            for x in range(1,\
    \ self.nx + 1):\n                if root[x] == x and slack[x]:\n             \
    \       if col[x] == -1:\n                        d = min(d, self.dist(slack[x],\
    \ x))\n                    elif col[x] == 0:\n                        d = min(d,\
    \ self.dist(slack[x], x) // 2)\n            for u in range(1, self.n + 1):\n \
    \               if col[root[u]] == 0:\n                    if label[u] <= d:\n\
    \                        return 0\n                    label[u] -= d\n       \
    \         elif col[root[u]] == 1:\n                    label[u] += d\n       \
    \     for b in range(self.n + 1, self.nx + 1):\n                if root[b] ==\
    \ b:\n                    if col[b] == 0:\n                        label[b] +=\
    \ d * 2\n                    elif col[b] == 1:\n                        label[b]\
    \ -= d * 2\n            self.que.clear()\n            for x in range(1, self.nx\
    \ + 1):\n                sx = slack[x]\n                if root[x] == x and sx\
    \ and root[sx] != x and self.dist(sx, x) == 0:\n                    if self.on_found_edge(sx,\
    \ x):\n                        return 1\n            for b in range(self.n + 1,\
    \ self.nx + 1):\n                if root[b] == b and col[b] == 1 and label[b]\
    \ == 0:\n                    self.expand_blossom(b)\n        return 0\n\n    def\
    \ solve(self) -> tuple[int, int]:\n        root, flower, flower_from = self.root,\
    \ self.flower, self.flower_from\n        match, label, W, m = self.match, self.label,\
    \ self.W, self.m\n\n        cnt = 0\n        ans = 0\n        for u in range(self.n\
    \ + 1):\n            root[u] = u\n            flower[u].clear()\n        w_max\
    \ = 0\n        for u in range(1, self.n + 1):\n            for v in range(1, self.n\
    \ + 1):\n                flower_from[u * m + v] = u if u == v else 0\n       \
    \         w_max = max(w_max, W[u * m + v])\n        for u in range(1, self.n +\
    \ 1):\n            label[u] = w_max\n        while self.matching():\n        \
    \    cnt += 1\n        for u in range(1, self.n + 1):\n            if match[u]\
    \ and match[u] < u:\n                ans += W[u * m + match[u]]\n        for i\
    \ in range(self.n):\n            match[i] = match[i + 1] - 1\n        return ans,\
    \ cnt\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/general_weighted_matching.py
  requiredBy: []
  timestamp: '2024-08-14 05:50:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library_checker/graph/general_weighted_matching.test.py
documentation_of: graph/general_weighted_matching.py
layout: document
redirect_from:
- /library/graph/general_weighted_matching.py
- /library/graph/general_weighted_matching.py.html
title: graph/general_weighted_matching.py
---
