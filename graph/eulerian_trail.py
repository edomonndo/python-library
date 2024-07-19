class EulerianTrail:
    def __init__(
        self, n: int, edges: list[tuple[int, int]], is_undirected: bool = True
    ):
        self.n = n
        self.m = len(edges)
        self.edges = edges
        self.is_undirected = is_undirected
        self.adj = [[] for _ in range(n)]
        for eid, (u, v) in enumerate(edges):
            self.adj[u].append((v, eid))
            if is_undirected:
                self.adj[v].append((u, eid))

    def get_edge_order(self) -> tuple[int, list[int]]:
        if self.m == 0:
            return 0, []

        n, m, adj, edges = self.n, self.m, self.adj, self.edges

        s = -1
        if self.is_undirected:
            codd = sum(len(adj[v]) & 1 for v in range(n))
            if codd > 2:
                return -1, []
            if codd == 2:
                for v in range(n):
                    if len(adj[v]) & 1 == 1:
                        s = v
                        break
        else:
            di = [0] * n
            for _, v in edges:
                di[v] += 1
            codd = sum(abs(len(adj[v]) - di[v]) for v in range(n))
            if codd > 2:
                return -1, []
            if codd == 2:
                for v in range(n):
                    if len(adj[v]) > di[v]:
                        s = v
                        break
        if s < 0:
            for v in range(n):
                if len(adj[v]) > 0:
                    s = v
                    break

        ep = [0] * n
        eids = [0] * m
        used = [0] * m
        pp, pq = 0, m
        v = s
        while pp < pq:
            if ep[v] >= len(adj[v]):
                if pp == 0:
                    return -1, []
                pq -= 1
                pp -= 1
                eids[pq] = eids[pp]
                a, b = edges[eids[pq]]
                v ^= a ^ b
            else:
                e = adj[v][ep[v]][1]
                ep[v] += 1
                if used[e]:
                    continue
                used[e] = 1
                eids[pp] = e
                pp += 1
                a, b = edges[e]
                v ^= a ^ b
        return s, eids

    def get_verticle_order(self, start: int, eids: list[int]) -> list[int]:
        path = [start]
        cur = start
        for i in eids:
            u, v = self.edges[i]
            cur ^= u ^ v
            path.append(cur)
        return path
