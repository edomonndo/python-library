from collections import deque

inf = 1 << 60


class GeneralWeightedMatching:
    def __init__(self, n, edges: list[tuple[int, int, int]]):
        self.n = n
        self.nx = n
        self.m = m = 2 * n + 1
        m2 = m * m
        self.U = [0] * m2
        self.V = [0] * m2
        self.W = [0] * m2
        self.match = [0] * m
        self.slack = [0] * m
        self.flower = [[] for _ in range(m)]
        self.flower_from = [0] * m2
        self.label = [0] * m
        self.root = [0] * m
        self.par = [0] * m
        self.col = [0] * m
        self.vis = [0] * m
        self.que = deque()
        self.t = 0
        for u in range(1, m):
            for v in range(1, m):
                self.U[u * m + v] = u
                self.V[u * m + v] = v
        for u, v, w in edges:
            u += 1
            v += 1
            self.W[u * m + v] = max(self.W[u * m + v], w)
            self.W[v * m + u] = max(self.W[v * m + u], w)

    def dist(self, u: int, v: int) -> int:
        U, V, W, label, m = self.U, self.V, self.W, self.label, self.m

        u, v = U[u * m + v], V[u * m + v]
        return label[u] + label[v] - W[u * m + v] * 2

    def update_slack(self, u: int, x: int) -> None:
        slack, dist = self.slack, self.dist

        if not slack[x] or dist(u, x) < dist(slack[x], x):
            slack[x] = u

    def set_slack(self, x: int) -> None:
        slack, root, col, W = self.slack, self.root, self.col, self.W

        slack[x] = 0
        for u in range(1, self.n + 1):
            if W[u * self.m + x] > 0 and root[u] != x and col[root[u]] == 0:
                self.update_slack(u, x)

    def que_push(self, x: int) -> None:
        que, flower = self.que, self.flower

        st = [x]
        while st:
            x = st.pop()
            if x <= self.n:
                que.append(x)
                continue
            st += flower[x]

    def set_root(self, x: int, b: int) -> None:
        root, flower = self.root, self.flower

        st = [x]
        while st:
            x = st.pop()
            root[x] = b
            if x <= self.n:
                continue
            st += flower[x]

    def get_pr(self, b: int, xr: int) -> int:
        f = self.flower[b]
        pr = f.index(xr)
        if pr & 1:
            f = self.flower[b] = f[0:1] + f[1:][::-1]
            return len(f) - pr
        else:
            return pr

    def set_match(self, u: int, v: int) -> None:
        match, flower, U, V = self.match, self.flower, self.U, self.V

        match[u] = V[u * self.m + v]
        if u <= self.n:
            return
        xr = self.flower_from[u * self.m + U[u * self.m + v]]
        pr = self.get_pr(u, xr)
        f = flower[u]
        for i in range(pr):
            self.set_match(f[i], f[i ^ 1])
        self.set_match(xr, v)
        flower[u] = f[pr:] + f[:pr]

    def augment(self, u: int, v: int) -> None:
        root, match, par = self.root, self.match, self.par

        xnv = root[match[u]]
        self.set_match(u, v)
        while xnv:
            self.set_match(xnv, root[par[xnv]])
            u, v = root[par[xnv]], xnv
            xnv = root[match[u]]
            self.set_match(u, v)

    def get_lca(self, u: int, v: int) -> int:
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

    def add_blossom(self, u: int, lca: int, v: int) -> None:
        root, match, par = self.root, self.match, self.par
        U, V, W, m, flower_from = self.U, self.V, self.W, self.m, self.flower_from

        b = self.n + 1
        while b <= self.nx and root[b]:
            b += 1
        if b > self.nx:
            self.nx += 1
        self.label[b] = 0
        self.col[b] = 0
        match[b] = match[lca]
        f = self.flower[b] = []
        f.append(lca)
        x = u
        while x != lca:
            f.append(x)
            y = root[match[x]]
            f.append(y)
            self.que_push(y)
            x = root[par[y]]
        f = self.flower[b] = f[0:1] + f[1:][::-1]
        x = v
        while x != lca:
            f.append(x)
            y = root[match[x]]
            f.append(y)
            self.que_push(y)
            x = root[par[y]]
        self.set_root(b, b)
        for x in range(1, self.nx + 1):
            W[b * m + x] = W[x * m + b] = 0
        for x in range(1, self.n + 1):
            flower_from[b * m + x] = 0
        for xs in f:
            for x in range(1, self.nx + 1):
                if W[b * m + x] == 0 or self.dist(xs, x) < self.dist(b, x):
                    U[b * m + x] = U[xs * m + x]
                    U[x * m + b] = U[x * m + xs]
                    V[b * m + x] = V[xs * m + x]
                    V[x * m + b] = V[x * m + xs]
                    W[b * m + x] = W[xs * m + x]
                    W[x * m + b] = W[x * m + xs]
            for x in range(1, self.n + 1):
                if flower_from[xs * m + x]:
                    flower_from[b * m + x] = xs
        self.set_slack(b)

    def expand_blossom(self, b: int) -> None:
        par, col, slack = self.par, self.col, self.slack
        U, m = self.U, self.m

        f = self.flower[b]
        for fi in f:
            self.set_root(fi, fi)
        xr = self.flower_from[b * m + U[b * m + par[b]]]
        pr = self.get_pr(b, xr)
        f = self.flower[b]
        for i in range(0, pr, 2):
            xs = f[i]
            xns = f[i + 1]
            par[xs] = U[xns * m + xs]
            col[xs] = 1
            col[xns] = 0
            slack[xs] = 0
            self.set_slack(xns)
            self.que_push(xns)
        col[xr] = 1
        par[xr] = par[b]
        for i in range(pr + 1, len(f)):
            xs = f[i]
            col[xs] = -1
            self.set_slack(xs)
        self.root[b] = 0

    def on_found_edge(self, u: int, v: int) -> int:
        root, match, slack = self.root, self.match, self.slack
        col, par = self.col, self.par

        eu = self.U[u * self.m + v]
        ev = self.V[u * self.m + v]
        u = root[eu]
        v = root[ev]
        if col[v] == -1:
            par[v] = eu
            col[v] = 1
            nu = root[match[v]]
            slack[v] = slack[nu] = 0
            col[nu] = 0
            self.que_push(nu)
        elif col[v] == 0:
            lca = self.get_lca(u, v)
            if not lca:
                self.augment(u, v)
                self.augment(v, u)
                return 1
            else:
                self.add_blossom(u, lca, v)
        return 0

    def matching(self) -> int:
        root, match, col, par = self.root, self.match, self.col, self.par
        slack, label, W = self.slack, self.label, self.W

        for i in range(self.nx + 1):
            col[i] = -1
            slack[i] = 0
        self.que.clear()
        for x in range(1, self.nx + 1):
            if root[x] == x and not match[x]:
                par[x] = 0
                col[x] = 0
                self.que_push(x)
        if not self.que:
            return 0
        while True:
            while self.que:
                u = self.que.popleft()
                if col[root[u]] == 1:
                    continue
                for v in range(1, self.n + 1):
                    if W[u * self.m + v] and root[u] != root[v]:
                        if self.dist(u, v) == 0:
                            if self.on_found_edge(u, v):
                                return 1
                        else:
                            self.update_slack(u, root[v])
            d = inf
            for b in range(self.n + 1, self.nx + 1):
                if root[b] == b and col[b] == 1:
                    d = min(d, label[b] // 2)
            for x in range(1, self.nx + 1):
                if root[x] == x and slack[x]:
                    if col[x] == -1:
                        d = min(d, self.dist(slack[x], x))
                    elif col[x] == 0:
                        d = min(d, self.dist(slack[x], x) // 2)
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
                        label[b] += d * 2
                    elif col[b] == 1:
                        label[b] -= d * 2
            self.que.clear()
            for x in range(1, self.nx + 1):
                sx = slack[x]
                if root[x] == x and sx and root[sx] != x and self.dist(sx, x) == 0:
                    if self.on_found_edge(sx, x):
                        return 1
            for b in range(self.n + 1, self.nx + 1):
                if root[b] == b and col[b] == 1 and label[b] == 0:
                    self.expand_blossom(b)
        return 0

    def solve(self) -> tuple[int, int]:
        root, flower, flower_from = self.root, self.flower, self.flower_from
        match, label, W, m = self.match, self.label, self.W, self.m

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
