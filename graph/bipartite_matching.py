class BipartiteMatching:
    def __init__(self, n1: int, n2: int):
        self.n = n1
        self.m = n2
        self.adj = [[] for _ in range(n1)]

    def add_edge(self, a: int, b: int):
        self.adj[a].append(b)

    def solve(self):
        n, m, adj = self.n, self.m, self.adj
        prev = [-1] * n
        root = [-1] * n
        p = [-1] * n
        q = [-1] * m
        updated = True
        while updated:
            updated = False
            s = []
            for v in range(n):
                if p[v] == -1:
                    root[v] = v
                    s.append(v)
            i = 0
            while i < len(s):
                v = s[i]
                i += 1
                if p[root[v]] != -1:
                    continue
                for u in adj[v]:
                    if q[u] == -1:
                        while u != -1:
                            q[u] = v
                            p[v], u = u, p[v]
                            v = prev[v]
                        updated = True
                        break
                    u = q[u]
                    if prev[u] != -1:
                        continue
                    prev[u] = v
                    root[u] = root[v]
                    s.append(u)
            if updated:
                for v in range(n):
                    prev[v] = -1
                    root[v] = -1
        return [(v, p[v]) for v in range(n) if p[v] != -1]
