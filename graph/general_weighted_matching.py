inf = 1 << 60

from collections import deque


class GeneralWeightedMatching:
    def __init__(self, n, edges: list[tuple[int, int, int]]):
        self.n = n
        self.nx = n
        self.m = m = (n << 1) + 1
        m2 = m * m
        self.U = [0] * m2
        self.V = [0] * m2
        self.W = [0] * m2
        for u, v, w in edges:
            u += 1
            v += 1
            self.W[u * m + v] = max(self.W[u * m + v], w)
            self.W[v * m + u] = max(self.W[v * m + u], w)
        self.match = [0] * m
        self.slack = [0] * m
        self.flower = [[] for _ in range(m)]
        self.flower_from = [0] * m2
        self.label = [0] * m
        self.root = [0] * m
        self.par = [0] * m
        self.col = [0] * m
        self.vis = [0] * m
        self.dq = deque()
        self.t = 0
        for u in range(1, m):
            for v in range(1, m):
                self.U[u * m + v] = u
                self.V[u * m + v] = v

    def _dist(self, u: int, v: int) -> int:
        U, V, W = self.U, self.V, self.W
        label, m = self.label, self.m

        u, v = U[u * m + v], V[u * m + v]
        return label[u] + label[v] - (W[u * m + v] << 1)

    def _update_slack(self, u: int, x: int) -> None:
        slack, _dist = self.slack, self._dist

        if not slack[x] or _dist(u, x) < _dist(slack[x], x):
            slack[x] = u

    def _set_slack(self, x: int) -> None:
        slack, root, col = self.slack, self.root, self.col
        W, _update_slack = self.W, self._update_slack

        slack[x] = 0
        for u in range(1, self.n + 1):
            if W[u * self.m + x] > 0 and root[u] != x and col[root[u]] == 0:
                _update_slack(u, x)

    def _dq_push(self, x: int) -> None:
        dq, flower = self.dq, self.flower

        st = [x]
        while st:
            x = st.pop()
            if x <= self.n:
                dq.append(x)
                continue
            for fi in flower[x]:
                st.append(fi)

    def _set_root(self, x: int, b: int) -> None:
        root, flower = self.root, self.flower

        st = [x]
        while st:
            x = st.pop()
            root[x] = b
            if x <= self.n:
                continue
            for fi in flower[x]:
                st.append(fi)

    def _get_pr(self, b: int, xr: int) -> int:
        flower = self.flower

        f = flower[b]
        pr = f.index(xr)
        if pr & 1:
            f = flower[b] = f[0:1] + f[1:][::-1]
            return len(f) - pr
        else:
            return pr

    def _set_match(self, u: int, v: int) -> None:
        match, flower, flower_from = self.match, self.flower, self.flower_from
        _get_pr, _set_match = self._get_pr, self._set_match
        U, V, m = self.U, self.V, self.m

        match[u] = V[u * m + v]
        if u <= self.n:
            return
        xr = flower_from[u * m + U[u * m + v]]
        pr = _get_pr(u, xr)
        f = flower[u]
        for i in range(pr):
            _set_match(f[i], f[i ^ 1])
        _set_match(xr, v)
        flower[u] = f[pr:] + f[:pr]

    def _augment(self, u: int, v: int) -> None:
        root, par, match, _set_match = self.root, self.par, self.match, self._set_match

        xnv = root[match[u]]
        _set_match(u, v)
        while xnv:
            _set_match(xnv, root[par[xnv]])
            u, v = root[par[xnv]], xnv
            xnv = root[match[u]]
            _set_match(u, v)

    def _get_lca(self, u: int, v: int) -> int:
        vis, root, match, par = self.vis, self.root, self.match, self.par

        self.t += 1
        while u or v:
            if not u:
                u, v = v, u
                continue
            if vis[u] == self.t:
                return u
            vis[u] = self.t
            u = root[match[u]]
            if u:
                u = root[par[u]]
            u, v = v, u
        return 0

    def _add_blossom(self, u: int, lca: int, v: int) -> None:
        root, label, col, match = self.root, self.label, self.col, self.match
        flower, par, flower_from = self.flower, self.par, self.flower_from
        U, V, W, m = self.U, self.V, self.W, self.m
        _dist, _set_slack = self._dist, self._set_slack
        _dq_push, _set_root = self._dq_push, self._set_root

        b = self.n + 1
        while b <= self.nx and root[b]:
            b += 1
        if b > self.nx:
            self.nx += 1
        label[b] = 0
        col[b] = 0
        match[b] = match[lca]
        f = flower[b] = [lca]
        x = u
        while x != lca:
            f.append(x)
            y = root[match[x]]
            f.append(y)
            _dq_push(y)
            x = root[par[y]]
        f = flower[b] = f[0:1] + f[1:][::-1]
        x = v
        while x != lca:
            f.append(x)
            y = root[match[x]]
            f.append(y)
            _dq_push(y)
            x = root[par[y]]
        _set_root(b, b)
        for x in range(1, self.nx + 1):
            W[b * m + x] = W[x * m + b] = 0
        for x in range(1, self.n + 1):
            flower_from[b * m + x] = 0
        for xs in f:
            for x in range(1, self.nx + 1):
                if W[b * m + x] == 0 or _dist(xs, x) < _dist(b, x):
                    U[b * m + x] = U[xs * m + x]
                    U[x * m + b] = U[x * m + xs]
                    V[b * m + x] = V[xs * m + x]
                    V[x * m + b] = V[x * m + xs]
                    W[b * m + x] = W[xs * m + x]
                    W[x * m + b] = W[x * m + xs]
            for x in range(1, self.n + 1):
                if flower_from[xs * m + x]:
                    flower_from[b * m + x] = xs
        _set_slack(b)

    def _expand_blossom(self, b: int) -> None:
        flower, flower_from, par = self.flower, self.flower_from, self.par
        root, col, slack = self.root, self.col, self.slack
        _set_root, _set_slack = self._set_root, self._set_slack
        _dq_push, _get_pr = self._dq_push, self._get_pr
        U, m = self.U, self.m

        f = flower[b]
        for fi in f:
            _set_root(fi, fi)
        xr = flower_from[b * m + U[b * m + par[b]]]
        pr = _get_pr(b, xr)
        for i in range(0, pr, 2):
            xs = f[i]
            xns = f[i + 1]
            par[xs] = U[xns * m + xs]
            col[xs] = 1
            col[xns] = 0
            slack[xs] = 0
            _set_slack(xns)
            _dq_push(xns)
        col[xr] = 1
        par[xr] = par[b]
        for xs in f[pr + 1 :]:
            col[xs] = -1
            _set_slack(xs)
        root[b] = 0

    def _on_found_edge(self, u: int, v: int) -> int:
        root, par, col = self.root, self.par, self.col
        slack, match = self.slack, self.match
        _dq_push, _get_lca = self._dq_push, self._get_lca
        _augment, _add_blossom = self._augment, self._add_blossom
        U, V, m = self.U, self.V, self.m

        eu = U[u * m + v]
        ev = V[u * m + v]
        u = root[eu]
        v = root[ev]
        if col[v] == -1:
            par[v] = eu
            col[v] = 1
            nu = root[match[v]]
            slack[v] = slack[nu] = 0
            col[nu] = 0
            _dq_push(nu)
        elif col[v] == 0:
            lca = _get_lca(u, v)
            if not lca:
                _augment(u, v)
                _augment(v, u)
                return 1
            else:
                _add_blossom(u, lca, v)
        return 0

    def matching(self) -> int:
        col, slack, root = self.col, self.slack, self.root
        label, match, par, dq = self.label, self.match, self.par, self.dq
        _dq_push, _on_found_edge, _dist = self._dq_push, self._on_found_edge, self._dist
        _update_slack, _expand_blossom = self._update_slack, self._expand_blossom
        W, m = self.W, self.m

        for i in range(self.nx + 1):
            col[i] = -1
            slack[i] = 0
        dq.clear()
        for x in range(1, self.nx + 1):
            if root[x] == x and not match[x]:
                par[x] = 0
                col[x] = 0
                _dq_push(x)
        if not dq:
            return 0
        while True:
            while dq:
                u = dq.popleft()
                if col[root[u]] == 1:
                    continue
                for v in range(1, self.n + 1):
                    if W[u * m + v] and root[u] != root[v]:
                        if _dist(u, v) == 0:
                            if _on_found_edge(u, v):
                                return 1
                        else:
                            _update_slack(u, root[v])
            d = inf
            for b in range(self.n + 1, self.nx + 1):
                if root[b] == b and col[b] == 1:
                    d = min(d, label[b] >> 1)
            for x in range(1, self.nx + 1):
                if root[x] == x and slack[x]:
                    if col[x] == -1:
                        d = min(d, _dist(slack[x], x))
                    elif self.col[x] == 0:
                        d = min(d, _dist(slack[x], x) >> 1)
            for u in range(1, self.n + 1):
                if col[root[u]] == 0:
                    if label[u] <= d:
                        return 0
                    label[u] -= d
                elif col[root[u]] == 1:
                    label[u] += d
            for b in range(self.n + 1, self.nx + 1):
                if root[b] == b:
                    if col[b] == 0:
                        label[b] += d << 1
                    elif col[b] == 1:
                        label[b] -= d << 1
            dq.clear()
            for x in range(1, self.nx + 1):
                if (
                    root[x] == x
                    and slack[x]
                    and root[slack[x]] != x
                    and _dist(slack[x], x) == 0
                    and _on_found_edge(slack[x], x)
                ):
                    return 1
            for b in range(self.n + 1, self.nx + 1):
                if root[b] == b and col[b] == 1 and label[b] == 0:
                    _expand_blossom(b)
        return 0

    def solve(self) -> tuple[int, int]:
        root, flower, flower_from = self.root, self.flower, self.flower_from
        label, match = self.label, self.match
        W, m = self.W, self.m

        cnt = 0
        ans = 0
        for u in range(self.n + 1):
            root[u] = u
            flower[u].clear()
        w_max = 0
        for u in range(1, self.n + 1):
            for v in range(1, self.n + 1):
                flower_from[u * m + v] = u if u == v else 0
                w_max = max(w_max, W[u * m + v])
        for u in range(1, self.n + 1):
            label[u] = w_max
        while self.matching():
            cnt += 1
        for u in range(1, self.n + 1):
            if match[u] and match[u] < u:
                ans += W[u * m + match[u]]
        for i in range(self.n):
            match[i] = match[i + 1] - 1
        return ans, cnt


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

solver = GeneralWeightedMatching(n, edges)
ans, cnt = solver.solve()
print(cnt, ans)
for v in range(n):
    u = solver.match[v]
    if u > v:
        print(v, u)
