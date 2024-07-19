class LowLink:
    def __init__(self, adj: list[list[int]]):
        self.n = n = len(adj)
        self.order = order = [-1] * n
        self.low = low = [n] * n
        self.child = child = [[] for _ in range(n)]
        self.is_root = is_root = [0] * n
        self.roots = roots = []

        par = [-1] * n
        idx = 0
        for u in range(n):
            if order[u] != -1:
                continue
            is_root[u] = 1
            roots.append(u)
            st = [u]
            par[u] = -2
            while st:
                v = st.pop()
                if v >= 0:
                    if order[v] != -1:
                        continue
                    order[v] = idx
                    low[v] = idx
                    idx += 1
                    if v != u:
                        child[par[v]].append(v)
                        st.append(~v)
                    check_p = 0
                    for nv in adj[v]:
                        if nv == par[v] and check_p == 0:
                            check_p += 1
                            continue
                        elif order[nv] != -1:
                            low[v] = min(low[v], order[nv])
                        else:
                            par[nv] = v
                            st.append(nv)
                    continue
                v = ~v
                p = par[v]
                low[p] = min(low[p], low[v])

    def get_articulation(self) -> list[int]:
        order, low, is_root, child = self.order, self.low, self.is_root, self.child
        res = []
        for v in range(self.n):
            if is_root[v]:
                if len(child[v]) >= 2:
                    res.append(v)
                continue
            for u in child[v]:
                if order[v] <= low[u]:
                    res.append(v)
                    break
        return res

    def get_bridge(self) -> list[tuple[int, int]]:
        order, low, roots, child = self.order, self.low, self.roots, self.child
        res = []
        for v in roots:
            st = [v]
            while st:
                v = st.pop()
                for u in child[v]:
                    if order[v] < low[u]:
                        if u < v:
                            res.append((u, v))
                        else:
                            res.append((v, u))
                    st.append(u)
        return res

    def two_edge_connected_components(self) -> tuple[list[int], list[tuple[int, int]]]:
        order, low, roots, child = self.order, self.low, self.roots, self.child

        components = [-1] * self.n
        new_edges = []
        idx = 0
        for v in roots:
            components[v] = idx
            st = [v]
            while st:
                v = st.pop()
                for u in child[v]:
                    if order[v] < low[u]:
                        idx += 1
                        components[u] = idx
                        if components[v] < idx:
                            new_edges.append((components[v], idx))
                        else:
                            new_edges.append((idx, components[v]))
                    else:
                        components[u] = components[v]
                    st.append(u)
            idx += 1
        return components, new_edges

    @staticmethod
    def _build_dfs_tree(adj: list[list[int]]):
        n = len(adj)
        dfs_order = []
        par = [-2] * n
        eid = [0] * n
        for r in range(n):
            if par[r] != -2:
                continue
            v = r
            par[v] = -1
            while v >= 0:
                if eid[v] == 0:
                    dfs_order.append(v)
                if eid[v] == len(adj[v]):
                    v = par[v]
                    continue
                u = adj[v][eid[v]]
                eid[v] += 1
                if par[u] != -2:
                    continue
                v, par[u] = u, v
        return dfs_order, par

    @classmethod
    def _biconnected_components(
        cls, adj: list[list[int]]
    ) -> tuple[int, list[tuple[int, int]]]:
        n = len(adj)
        order, par = cls._build_dfs_tree(adj)

        vtx_to_dfs = [0] * n
        for i in range(n):
            vtx_to_dfs[order[i]] = i
        low = vtx_to_dfs[:]
        for u in range(n):
            for v in adj[u]:
                low[u] = min(low[u], vtx_to_dfs[v])
        for v in order[::-1]:
            p = par[v]
            if p >= 0:
                low[p] = min(low[p], low[v])
        num_bcc = 0
        bc_vtx_pair = []
        for v in order:
            if par[v] >= 0:
                p = par[v]
                if low[v] < vtx_to_dfs[p]:
                    low[v] = low[p]
                    bc_vtx_pair.append((low[v], v))
                else:
                    low[v] = num_bcc
                    num_bcc += 1
                    bc_vtx_pair += [(low[v], p), (low[v], v)]
        for v in range(n):
            if len(adj[v]) == 0:
                bc_vtx_pair.append((num_bcc, v))
                num_bcc += 1
        return num_bcc, bc_vtx_pair

    @classmethod
    def block_cut_tree(cls, adj: list[list[int]]) -> list[list[int]]:
        num_bcc, bc_vtx_pair = cls._biconnected_components(adj)
        n = len(adj)
        edges = []
        for u, v in bc_vtx_pair:
            edges.append((u + n, v))
        bc_tree = [[] for _ in range(n + num_bcc)]
        for u, v in edges:
            bc_tree[u].append(v)
            bc_tree[v].append(u)
        return bc_tree

    @classmethod
    def biconnected_components_verticle(cls, adj: list[list[int]]) -> list[list[int]]:
        num_bcc, bc_vtx_pair = cls._biconnected_components(adj)
        res = [[] for _ in range(num_bcc)]
        for u, v in bc_vtx_pair:
            res[u].append(v)
        return res

    @classmethod
    def biconnected_components_edge(
        cls, n: int, edges: list[tuple[int, int]]
    ) -> list[tuple[int, int]]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        bc_tree = cls.block_cut_tree(adj)
        n = len(bc_tree)
        par = [-1] * n
        dep = [0] * n
        bfs = [None] * n
        l, r = 0, 0
        for root in range(n):
            if par[root] >= 0:
                continue
            bfs[r] = root
            r += 1
            while l < r and r < n:
                v = bfs[l]
                for u in bc_tree[v]:
                    if par[v] != u:
                        par[u] = v
                        dep[u] = dep[v] + 1
                        bfs[r] = u
                        r += 1
                l += 1

        res = [[] for _ in range(n - len(adj))]
        for eid, (u, v) in enumerate(edges):
            s = par[v if dep[u] <= dep[v] else u] - len(adj)
            res[s].append(eid)
        return res

    @classmethod
    def three_edge_connected_components(cls, adj: list[list[int]]) -> list[int]:
        raise NotImplementedError
