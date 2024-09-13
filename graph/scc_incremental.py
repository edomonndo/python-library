from graph.csr import CSR
from graph.scc import SCC
from graph.connectivity.unionfind import UnionFind


class IncrementalScc:

    def __init__(self, n: int):
        self.n = n
        self.edges = []

    def add_edge(self, src: int, dst: int) -> None:
        # assert 0 <= src < self.n
        # assert 0 <= dst < self.n
        self.edges.append((src, dst))

    def solve(self) -> CSR:
        n = self.n
        edges = self.edges
        scc = SCC(n)
        for u, v in edges:
            scc.add_edge(u, v)
        scc.build()
        cc = scc.get_mapping()
        del scc
        eis = [i for i, (u, v) in enumerate(edges) if cc[u] == cc[v]]
        sep = [0] * (len(edges) + 1)
        nc = []

        def dfs(n: int, x: int, eis: list[int]):
            m = len(eis)
            if x == m:
                return
            if x + 1 == m:
                uf = UnionFind(n)
                for ei in eis:
                    u, v = edges[ei]
                    if uf.same(u, v):
                        continue
                    uf.merge(u, v)
                    sep[eis[x] + 1] += 1
                    nc.append(ei)
                return
            sz = 0
            idx = [-1] * n
            for ei in eis:
                u, v = edges[ei]
                for j in [u, v]:
                    if idx[j] == -1:
                        idx[j] = sz
                        sz += 1
                edges[ei] = (idx[u], idx[v])
            y = (x + m) >> 1
            scc = SCC(sz)
            for ei in eis[:y]:
                u, v = edges[ei]
                scc.add_edge(u, v)
            scc.build()
            cc = scc.get_mapping()
            del scc
            eis_left, eis_right = [], []
            for ei in eis[:x]:
                u, v = edges[ei]
                if cc[u] == cc[v]:
                    eis_left.append(ei)
                else:
                    eis_right.append(ei)
            xl = len(eis_left)
            for ei in eis[x:y]:
                u, v = edges[ei]
                if cc[u] == cc[v]:
                    eis_left.append(ei)
                else:
                    eis_right.append(ei)
            xr = len(eis_right)
            for ei in eis[y:]:
                u, v = edges[ei]
                if cc[u] != cc[v]:
                    eis_right.append(ei)
            dfs(sz, xl, eis_left)
            for ei in eis_right:
                u, v = edges[ei]
                edges[ei] = (cc[u], cc[v])
            dfs(sz, xr, eis_right)

        dfs(n, 0, eis)
        for i in range(len(sep) - 1):
            sep[i + 1] += sep[i]
        return CSR(len(sep) - 1, sep, nc)
