from typing import Callable


class HeavyLightDecomposition:
    def __init__(self, n: int, edges: list[tuple[int, int]], root: int = 0):
        self.n = n
        self.root = root
        self.depth = [0] * n
        self.into = [-1] * n
        self.out = [-1] * n
        self.nxt = [root] * n
        self.par = [root] * n
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self._dfs_sz()
        self._dfs_hld()

    def _dfs_sz(self) -> None:
        # calc subtree size
        adj, par, depth = self.adj, self.par, self.depth
        sz = [0] * self.n
        st = [self.root]
        while st:
            v = st.pop()
            if v >= 0:
                sz[v] = 1
                if len(adj[v]) >= 2 and adj[v][-1] == par[v]:
                    adj[v][-1], adj[v][-2] = adj[v][-2], adj[v][-1]
                for i, u in enumerate(adj[v]):
                    if u == par[v]:
                        continue
                    depth[u] = depth[v] + 1
                    par[u] = v
                    st += [i, ~u, u]
                continue
            v = ~v
            p = par[v]
            i = st.pop()
            sz[p] += sz[v]
            if sz[v] > sz[adj[p][-1]]:
                adj[p][-1], adj[p][i] = adj[p][i], adj[p][-1]

    def _dfs_hld(self):
        # calc hld
        adj, into, out, par, nxt = self.adj, self.into, self.out, self.par, self.nxt
        idx = 0
        st = [~self.root, self.root]
        while st:
            v = st.pop()
            if v >= 0:
                into[v] = idx
                idx += 1
                for u in adj[v]:
                    if u == par[v]:
                        continue
                    nxt[u] = nxt[v] if u == adj[v][-1] else u
                    st += [~u, u]
                continue
            out[~v] = idx

    def ascend(self, u: int, v: int) -> list[tuple[int, int]]:
        into, par, nxt = self.into, self.par, self.nxt
        res = []
        while nxt[u] != nxt[v]:
            res.append((into[u], into[nxt[u]]))
            u = par[nxt[u]]
        if u != v:
            res.append((into[u], into[v] + 1))
        return res

    def descend(self, u: int, v: int) -> list[tuple[int, int]]:
        into, par, nxt = self.into, self.par, self.nxt
        res = []
        while u != v:
            if nxt[u] == nxt[v]:
                res.append((into[u] + 1, into[v]))
                break
            res.append((into[nxt[v]], into[v]))
            v = par[nxt[v]]
        return res[::-1]

    def lca(self, u: int, v: int) -> int:
        into, par, nxt, depth = self.into, self.par, self.nxt, self.depth
        while nxt[u] != nxt[v]:
            if into[u] < into[v]:
                u, v = v, u
            u = par[nxt[u]]
        return u if depth[u] < depth[v] else v

    def dist(self, u: int, v: int) -> int:
        depth = self.depth
        return depth[u] + depth[v] - 2 * depth[self.lca(u, v)]

    def path_query(
        self, u: int, v: int, f: Callable[[int, int], None], edge: bool = False
    ) -> None:
        into = self.into
        l = self.lca(u, v)
        for a, b in self.ascend(u, l):
            s, t = a + 1, b
            f(s, t) if s < t else f(t, s)
        if not edge:
            f(into[l], into[l] + 1)
        for a, b in self.descend(l, v):
            s, t = a, b + 1
            f(s, t) if s < t else f(t, s)

    def path_noncommutative_query(
        self, u: int, v: int, f: Callable[[int, int], None], edge: bool = False
    ) -> None:
        into = self.into
        l = self.lca(u, v)
        for a, b in self.ascend(u, l):
            f(a + 1, b)
        if not edge:
            f(into[l], into[l] + 1)
        for a, b in self.descend(l, v):
            f(a, b + 1)

    def subtree_query(
        self, u: int, f: Callable[[int, int], None], edge: bool = False
    ) -> None:
        f(self.into[u] + edge, self.out[u])
