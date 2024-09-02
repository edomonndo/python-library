from typing import Union


class HeavyLightDecomposition:
    def __init__(
        self,
        n: int,
        adj: list[list[Union[int, tuple[int, int]]]],
        root: int = 0,
        has_weight: bool = False,
        is_undirect: bool = True,
    ):
        # assert len(edges) == n-1
        self.n = n
        self.root = root
        self.adj = adj
        self.has_weight = has_weight
        self.is_undirect = is_undirect
        self.par = [-1] * n
        self.depth = [0] * n
        order = self._root_tree()

        self.sz = [1] * self.n
        self._dfs_sz(order)

        self.into = [-1] * n
        self.head = [root] * n
        self.hld = []
        self._dfs_hld()
        # assert len(self.hld) == n

    def _root_tree(self) -> None:
        adj, par, depth = self.adj, self.par, self.depth
        res = []
        st = [self.root]
        while st:
            v = st.pop()
            res.append(v)
            if self.is_undirect and par[v] != -1:
                adj[v].remove(par[v])
            if self.has_weight:
                for e in adj[v]:
                    # assert len(e) == 2
                    u, w = e[0], e[1]
                    par[u] = (v, w)
                    depth[u] = depth[v] + 1
                    st.append(u)
            else:
                for u in adj[v]:
                    par[u] = v
                    depth[u] = depth[v] + 1
                    st.append(u)
        if self.has_weight:
            par[self.root] = (-1, 0)
            self.par = [p for p, _ in par]
        return res

    def _dfs_sz(self, order: list[int]) -> None:
        # calc subtree size
        adj, sz = self.adj, self.sz
        for p in order[::-1]:
            vs = adj[p]
            for i in range(len(vs)):
                x = sz[vs[i]]
                if x > sz[vs[0]]:
                    vs[0], vs[i] = vs[i], vs[0]
                sz[p] += x

    def _dfs_hld(self) -> None:
        # calc hld
        adj, into, head, hld = self.adj, self.into, self.head, self.hld

        st = [self.root]
        while st:
            v = st.pop()
            into[v] = len(hld)
            hld.append(v)
            if self.has_weight:
                for e in adj[v][1:]:
                    u = e[0]
                    head[u] = u
                    st.append(u)
                if adj[v]:
                    u = adj[v][0]
                    head[u] = head[v]
                    st.append(u)
            else:
                for u in adj[v][1:]:
                    head[u] = u
                    st.append(u)
                if adj[v]:
                    u = adj[v][0]
                    head[u] = head[v]
                    st.append(u)

    def build_list(self, a: list[int]) -> list[int]:
        return [a[x] for x in self.hld]

    def lca(self, u: int, v: int) -> int:
        into, par, head, depth = self.into, self.par, self.head, self.depth
        while head[u] != head[v]:
            if into[u] < into[v]:
                u, v = v, u
            u = par[head[u]]
        return u if depth[u] < depth[v] else v

    def dist(self, u: int, v: int) -> int:
        depth = self.depth
        return depth[u] + depth[v] - 2 * depth[self.lca(u, v)]

    def jump(self, u: int, v: int, k: int) -> int:
        head, depth, par = self.head, self.depth, self.par

        d = self.dist(u, v)
        if d < k:
            return -1
        lca = self.lca(u, v)
        if depth[u] - depth[lca] < k:
            u = v
            k = d - k
        h = head[u]
        while depth[u] - depth[h] < k:
            k -= depth[u] - depth[h] + 1
            u = par[h]
            h = head[u]
        return self.hld[self.into[u] - k]

    def is_on_path(self, u: int, v: int, x: int) -> bool:
        return self.dist(u, x) + self.dist(x, v) == self.dist(u, v)

    def index(self, idx: int, edge: bool = False) -> int:
        return self.into[idx] + edge

    def _ascend(self, u: int, v: int) -> list[tuple[int, int]]:
        into, head, par, depth = self.into, self.head, self.par, self.depth
        res = []
        while head[u] != head[v]:
            res.append((into[u], into[head[u]]))
            u = par[head[u]]
        if u != v:
            res.append((into[u], into[v] + 1))
        return res

    def _descend(self, u: int, v: int) -> list[tuple[int, int]]:
        return [(r, l) for l, r in self._ascend(v, u)[::-1]]

    def path_query(self, u: int, v: int, edge: bool = False) -> list[tuple[int, int]]:
        l = self.lca(u, v)
        tmp = self._ascend(u, l)
        if not edge:
            tmp.append((self.into[l], self.into[l]))
        tmp += self._descend(l, v)
        res = []
        for l, r in tmp:
            if l > r:
                l, r = r, l
            res.append((l, r + 1))
        return res

    def path_query_noncommutative(
        self, u: int, v: int, edge: bool = False
    ) -> list[tuple[int, int, bool]]:
        l = self.lca(u, v)
        tmp = self._ascend(u, l)
        if not edge:
            tmp.append((self.into[l], self.into[l]))
        tmp += self._descend(l, v)
        res = []
        for l, r in tmp:
            if l > r:
                res.append((r, l + 1, True))
            else:
                res.append((l, r + 1, False))
        return res

    def subtree_query(self, u: int, edge: bool = False) -> tuple[int, int]:
        return self.into[u] + edge, self.into[u] + self.sz[u]
