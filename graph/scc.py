from graph.csr import CSR


class SCC:
    def __init__(self, n: int, edges: list[tuple[int, int]]):
        self.n = n
        ord = [0] * n
        adj = CSR.build(n, edges, True)
        idx = n
        par = [-1] * n
        eis = [0] * n
        for s in range(n):
            if par[s] == -1:
                par[s], p = -2, s
                while p >= 0:
                    arr = adj[p]
                    if eis[p] == len(arr):
                        idx -= 1
                        ord[idx], p = p, par[p]
                        continue
                    q = arr[eis[p]]
                    eis[p] += 1
                    if par[q] == -1:
                        par[q], p = p, q
        for i in range(len(edges)):
            u, v = edges[i]
            edges[i] = (v, u)
        rev = CSR.build(n, edges, True)
        sep = [0]
        csr = [0] * n
        vis = [0] * n
        p1, p2 = 0, 0
        for s in ord:
            if not vis[s]:
                csr[p2], vis[s] = s, 1
                p2 += 1
                while p1 < p2:
                    v = csr[p1]
                    for u in rev[v]:
                        if not vis[u]:
                            vis[u] = 1
                            csr[p2] = u
                            p2 += 1
                    p1 += 1
                sep.append(p2)
        self.induce = CSR.from_raw(sep, csr)
        self._componet_count = len(self.induce)

    def count_components(self):
        return self._componet_count

    def get_mapping(self):
        res = [0] * self.n
        for i in range(self.componet_count):
            for v in self.induce[i]:
                res[v] = i
        return res
