class BellmanFord:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.adj_rev = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, u: int, v: int, w: int):
        self.adj[u].append(v)
        self.adj_rev[v].append(u)
        self.edges.append((u, v, w))

    @staticmethod
    def _can_reach(adj: list[list[int]], v: int) -> list[bool]:
        res = [False] * len(adj)
        res[v] = True
        stack = [v]
        while stack:
            v = stack.pop()
            for u in adj[v]:
                if not res[u]:
                    res[u] = True
                    stack.append(u)
        return res

    def solve(self, s: int) -> tuple[bool, list[int]]:
        n = self.n
        assert 0 <= s < n
        rs = self._can_reach(self.adj, s)
        rt = self._can_reach(self.adj_rev, t)
        edges = [
            (u, v, w) for u, v, w in self.edges if rs[u] and rt[u] and rs[v] and rt[v]
        ]

        inf = float("inf")
        dist = [inf] * n
        dist[s] = 0
        for i in range(n):
            for u, v, w in edges:
                if i == n - 1 and dist[v] > dist[u] + w:
                    return False, -1
                dist[v] = min(dist[v], dist[u] + w)
        return True, dist
