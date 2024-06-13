---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 76, in _render_source_code_stat\n    bundled_code = language.bundle(\n\
    \  File \"/opt/hostedtoolcache/PyPy/3.10.14/x64/lib/pypy3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "inf = 1 << 60\n\nfrom collections import deque\n\n\nclass GeneralWeightedMatching:\n\
    \    def __init__(self, n, edges: list[tuple[int, int, int]]):\n        self.n\
    \ = n\n        self.nx = n\n        self.m = m = (n << 1) + 1\n        m2 = m\
    \ * m\n        self.U = [0] * m2\n        self.V = [0] * m2\n        self.W =\
    \ [0] * m2\n        for u, v, w in edges:\n            u += 1\n            v +=\
    \ 1\n            self.W[u * m + v] = max(self.W[u * m + v], w)\n            self.W[v\
    \ * m + u] = max(self.W[v * m + u], w)\n        self.match = [0] * m\n       \
    \ self.slack = [0] * m\n        self.flower = [[] for _ in range(m)]\n       \
    \ self.flower_from = [0] * m2\n        self.label = [0] * m\n        self.root\
    \ = [0] * m\n        self.par = [0] * m\n        self.col = [0] * m\n        self.vis\
    \ = [0] * m\n        self.dq = deque()\n        self.t = 0\n        for u in range(1,\
    \ m):\n            for v in range(1, m):\n                self.U[u * m + v] =\
    \ u\n                self.V[u * m + v] = v\n\n    def _dist(self, u: int, v: int)\
    \ -> int:\n        U, V, W = self.U, self.V, self.W\n        label, m = self.label,\
    \ self.m\n\n        u, v = U[u * m + v], V[u * m + v]\n        return label[u]\
    \ + label[v] - (W[u * m + v] << 1)\n\n    def _update_slack(self, u: int, x: int)\
    \ -> None:\n        slack, _dist = self.slack, self._dist\n\n        if not slack[x]\
    \ or _dist(u, x) < _dist(slack[x], x):\n            slack[x] = u\n\n    def _set_slack(self,\
    \ x: int) -> None:\n        slack, root, col = self.slack, self.root, self.col\n\
    \        W, _update_slack = self.W, self._update_slack\n\n        slack[x] = 0\n\
    \        for u in range(1, self.n + 1):\n            if W[u * self.m + x] > 0\
    \ and root[u] != x and col[root[u]] == 0:\n                _update_slack(u, x)\n\
    \n    def _dq_push(self, x: int) -> None:\n        dq, flower = self.dq, self.flower\n\
    \n        st = [x]\n        while st:\n            x = st.pop()\n            if\
    \ x <= self.n:\n                dq.append(x)\n                continue\n     \
    \       for fi in flower[x]:\n                st.append(fi)\n\n    def _set_root(self,\
    \ x: int, b: int) -> None:\n        root, flower = self.root, self.flower\n\n\
    \        st = [x]\n        while st:\n            x = st.pop()\n            root[x]\
    \ = b\n            if x <= self.n:\n                continue\n            for\
    \ fi in flower[x]:\n                st.append(fi)\n\n    def _get_pr(self, b:\
    \ int, xr: int) -> int:\n        flower = self.flower\n\n        f = flower[b]\n\
    \        pr = f.index(xr)\n        if pr & 1:\n            f = flower[b] = f[0:1]\
    \ + f[1:][::-1]\n            return len(f) - pr\n        else:\n            return\
    \ pr\n\n    def _set_match(self, u: int, v: int) -> None:\n        match, flower,\
    \ flower_from = self.match, self.flower, self.flower_from\n        _get_pr, _set_match\
    \ = self._get_pr, self._set_match\n        U, V, m = self.U, self.V, self.m\n\n\
    \        match[u] = V[u * m + v]\n        if u <= self.n:\n            return\n\
    \        xr = flower_from[u * m + U[u * m + v]]\n        pr = _get_pr(u, xr)\n\
    \        f = flower[u]\n        for i in range(pr):\n            _set_match(f[i],\
    \ f[i ^ 1])\n        _set_match(xr, v)\n        flower[u] = f[pr:] + f[:pr]\n\n\
    \    def _augment(self, u: int, v: int) -> None:\n        root, par, match, _set_match\
    \ = self.root, self.par, self.match, self._set_match\n\n        xnv = root[match[u]]\n\
    \        _set_match(u, v)\n        while xnv:\n            _set_match(xnv, root[par[xnv]])\n\
    \            u, v = root[par[xnv]], xnv\n            xnv = root[match[u]]\n  \
    \          _set_match(u, v)\n\n    def _get_lca(self, u: int, v: int) -> int:\n\
    \        vis, root, match, par = self.vis, self.root, self.match, self.par\n\n\
    \        self.t += 1\n        while u or v:\n            if not u:\n         \
    \       u, v = v, u\n                continue\n            if vis[u] == self.t:\n\
    \                return u\n            vis[u] = self.t\n            u = root[match[u]]\n\
    \            if u:\n                u = root[par[u]]\n            u, v = v, u\n\
    \        return 0\n\n    def _add_blossom(self, u: int, lca: int, v: int) -> None:\n\
    \        root, label, col, match = self.root, self.label, self.col, self.match\n\
    \        flower, par, flower_from = self.flower, self.par, self.flower_from\n\
    \        U, V, W, m = self.U, self.V, self.W, self.m\n        _dist, _set_slack\
    \ = self._dist, self._set_slack\n        _dq_push, _set_root = self._dq_push,\
    \ self._set_root\n\n        b = self.n + 1\n        while b <= self.nx and root[b]:\n\
    \            b += 1\n        if b > self.nx:\n            self.nx += 1\n     \
    \   label[b] = 0\n        col[b] = 0\n        match[b] = match[lca]\n        f\
    \ = flower[b] = [lca]\n        x = u\n        while x != lca:\n            f.append(x)\n\
    \            y = root[match[x]]\n            f.append(y)\n            _dq_push(y)\n\
    \            x = root[par[y]]\n        f = flower[b] = f[0:1] + f[1:][::-1]\n\
    \        x = v\n        while x != lca:\n            f.append(x)\n           \
    \ y = root[match[x]]\n            f.append(y)\n            _dq_push(y)\n     \
    \       x = root[par[y]]\n        _set_root(b, b)\n        for x in range(1, self.nx\
    \ + 1):\n            W[b * m + x] = W[x * m + b] = 0\n        for x in range(1,\
    \ self.n + 1):\n            flower_from[b * m + x] = 0\n        for xs in f:\n\
    \            for x in range(1, self.nx + 1):\n                if W[b * m + x]\
    \ == 0 or _dist(xs, x) < _dist(b, x):\n                    U[b * m + x] = U[xs\
    \ * m + x]\n                    U[x * m + b] = U[x * m + xs]\n               \
    \     V[b * m + x] = V[xs * m + x]\n                    V[x * m + b] = V[x * m\
    \ + xs]\n                    W[b * m + x] = W[xs * m + x]\n                  \
    \  W[x * m + b] = W[x * m + xs]\n            for x in range(1, self.n + 1):\n\
    \                if flower_from[xs * m + x]:\n                    flower_from[b\
    \ * m + x] = xs\n        _set_slack(b)\n\n    def _expand_blossom(self, b: int)\
    \ -> None:\n        flower, flower_from, par = self.flower, self.flower_from,\
    \ self.par\n        root, col, slack = self.root, self.col, self.slack\n     \
    \   _set_root, _set_slack = self._set_root, self._set_slack\n        _dq_push,\
    \ _get_pr = self._dq_push, self._get_pr\n        U, m = self.U, self.m\n\n   \
    \     f = flower[b]\n        for fi in f:\n            _set_root(fi, fi)\n   \
    \     xr = flower_from[b * m + U[b * m + par[b]]]\n        pr = _get_pr(b, xr)\n\
    \        for i in range(0, pr, 2):\n            xs = f[i]\n            xns = f[i\
    \ + 1]\n            par[xs] = U[xns * m + xs]\n            col[xs] = 1\n     \
    \       col[xns] = 0\n            slack[xs] = 0\n            _set_slack(xns)\n\
    \            _dq_push(xns)\n        col[xr] = 1\n        par[xr] = par[b]\n  \
    \      for xs in f[pr + 1 :]:\n            col[xs] = -1\n            _set_slack(xs)\n\
    \        root[b] = 0\n\n    def _on_found_edge(self, u: int, v: int) -> int:\n\
    \        root, par, col = self.root, self.par, self.col\n        slack, match\
    \ = self.slack, self.match\n        _dq_push, _get_lca = self._dq_push, self._get_lca\n\
    \        _augment, _add_blossom = self._augment, self._add_blossom\n        U,\
    \ V, m = self.U, self.V, self.m\n\n        eu = U[u * m + v]\n        ev = V[u\
    \ * m + v]\n        u = root[eu]\n        v = root[ev]\n        if col[v] == -1:\n\
    \            par[v] = eu\n            col[v] = 1\n            nu = root[match[v]]\n\
    \            slack[v] = slack[nu] = 0\n            col[nu] = 0\n            _dq_push(nu)\n\
    \        elif col[v] == 0:\n            lca = _get_lca(u, v)\n            if not\
    \ lca:\n                _augment(u, v)\n                _augment(v, u)\n     \
    \           return 1\n            else:\n                _add_blossom(u, lca,\
    \ v)\n        return 0\n\n    def matching(self) -> int:\n        col, slack,\
    \ root = self.col, self.slack, self.root\n        label, match, par, dq = self.label,\
    \ self.match, self.par, self.dq\n        _dq_push, _on_found_edge, _dist = self._dq_push,\
    \ self._on_found_edge, self._dist\n        _update_slack, _expand_blossom = self._update_slack,\
    \ self._expand_blossom\n        W, m = self.W, self.m\n\n        for i in range(self.nx\
    \ + 1):\n            col[i] = -1\n            slack[i] = 0\n        dq.clear()\n\
    \        for x in range(1, self.nx + 1):\n            if root[x] == x and not\
    \ match[x]:\n                par[x] = 0\n                col[x] = 0\n        \
    \        _dq_push(x)\n        if not dq:\n            return 0\n        while\
    \ True:\n            while dq:\n                u = dq.popleft()\n           \
    \     if col[root[u]] == 1:\n                    continue\n                for\
    \ v in range(1, self.n + 1):\n                    if W[u * m + v] and root[u]\
    \ != root[v]:\n                        if _dist(u, v) == 0:\n                \
    \            if _on_found_edge(u, v):\n                                return\
    \ 1\n                        else:\n                            _update_slack(u,\
    \ root[v])\n            d = inf\n            for b in range(self.n + 1, self.nx\
    \ + 1):\n                if root[b] == b and col[b] == 1:\n                  \
    \  d = min(d, label[b] >> 1)\n            for x in range(1, self.nx + 1):\n  \
    \              if root[x] == x and slack[x]:\n                    if col[x] ==\
    \ -1:\n                        d = min(d, _dist(slack[x], x))\n              \
    \      elif self.col[x] == 0:\n                        d = min(d, _dist(slack[x],\
    \ x) >> 1)\n            for u in range(1, self.n + 1):\n                if col[root[u]]\
    \ == 0:\n                    if label[u] <= d:\n                        return\
    \ 0\n                    label[u] -= d\n                elif col[root[u]] == 1:\n\
    \                    label[u] += d\n            for b in range(self.n + 1, self.nx\
    \ + 1):\n                if root[b] == b:\n                    if col[b] == 0:\n\
    \                        label[b] += d << 1\n                    elif col[b] ==\
    \ 1:\n                        label[b] -= d << 1\n            dq.clear()\n   \
    \         for x in range(1, self.nx + 1):\n                if (\n            \
    \        root[x] == x\n                    and slack[x]\n                    and\
    \ root[slack[x]] != x\n                    and _dist(slack[x], x) == 0\n     \
    \               and _on_found_edge(slack[x], x)\n                ):\n        \
    \            return 1\n            for b in range(self.n + 1, self.nx + 1):\n\
    \                if root[b] == b and col[b] == 1 and label[b] == 0:\n        \
    \            _expand_blossom(b)\n        return 0\n\n    def solve(self) -> tuple[int,\
    \ int]:\n        root, flower, flower_from = self.root, self.flower, self.flower_from\n\
    \        label, match = self.label, self.match\n        W, m = self.W, self.m\n\
    \n        cnt = 0\n        ans = 0\n        for u in range(self.n + 1):\n    \
    \        root[u] = u\n            flower[u].clear()\n        w_max = 0\n     \
    \   for u in range(1, self.n + 1):\n            for v in range(1, self.n + 1):\n\
    \                flower_from[u * m + v] = u if u == v else 0\n               \
    \ w_max = max(w_max, W[u * m + v])\n        for u in range(1, self.n + 1):\n \
    \           label[u] = w_max\n        while self.matching():\n            cnt\
    \ += 1\n        for u in range(1, self.n + 1):\n            if match[u] and match[u]\
    \ < u:\n                ans += W[u * m + match[u]]\n        for i in range(self.n):\n\
    \            match[i] = match[i + 1] - 1\n        return ans, cnt\n\n\nn, m =\
    \ map(int, input().split())\nedges = [tuple(map(int, input().split())) for _ in\
    \ range(m)]\n\nsolver = GeneralWeightedMatching(n, edges)\nans, cnt = solver.solve()\n\
    print(cnt, ans)\nfor v in range(n):\n    u = solver.match[v]\n    if u > v:\n\
    \        print(v, u)\n"
  dependsOn: []
  isVerificationFile: false
  path: graph/general_weighted_matching.py
  requiredBy: []
  timestamp: '2024-06-13 11:50:32+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: graph/general_weighted_matching.py
layout: document
redirect_from:
- /library/graph/general_weighted_matching.py
- /library/graph/general_weighted_matching.py.html
title: graph/general_weighted_matching.py
---
