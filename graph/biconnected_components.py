class BiconnectedComponents:
    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.edges = edges
        self.adj = adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.num_bcc, self.bc_vtx_pair = self._biconnected_components()

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

    def _biconnected_components(self) -> tuple[int, list[tuple[int, int]]]:
        order, par = self._build_dfs_tree(self.adj)

        vtx_to_dfs = [0] * self.n
        for i in range(self.n):
            vtx_to_dfs[order[i]] = i
        low = vtx_to_dfs[:]
        for u in range(self.n):
            for v in self.adj[u]:
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
        for v in range(self.n):
            if len(self.adj[v]) == 0:
                bc_vtx_pair.append((num_bcc, v))
                num_bcc += 1
        return num_bcc, bc_vtx_pair

    def block_cut_tree(self) -> list[list[int]]:
        edges = []
        for u, v in self.bc_vtx_pair:
            edges.append((u + self.n, v))
        bc_tree = [[] for _ in range(self.n + self.num_bcc)]
        for u, v in edges:
            bc_tree[u].append(v)
            bc_tree[v].append(u)
        return bc_tree

    def biconnected_components_verticle(self) -> list[list[int]]:
        res = [[] for _ in range(self.num_bcc)]
        for u, v in self.bc_vtx_pair:
            res[u].append(v)
        return res

    def biconnected_components_edge(self) -> list[tuple[int, int]]:
        bc_tree = self.block_cut_tree()
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

        res = [[] for _ in range(n - self.n)]
        for eid, (u, v) in enumerate(self.edges):
            s = par[v if dep[u] <= dep[v] else u] - self.n
            res[s].append(eid)
        return res
