from typing import Optional


class ChordalGraph:
    def __init__(self, n: int, edges: list[tuple[int, int]]):
        self.n = n
        self.m = len(edges)
        self.edges = edges
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.status = 0
        self.x = self.y = self.z = -1
        self.adj2: Optional[list[list[int]]] = None
        self.mcsordered: Optional[list[int]] = None
        self._is_chordal_graph: Optional[bool] = None
        self.induced_cycle: Optional[list[int]] = None

    def _contract(self, mapping: list[int]) -> list[list[int]]:
        new_adj = [[] for _ in range(self.n)]
        for u, v in self.edges:
            nu, nv = mapping[u], mapping[v]
            new_adj[nu].append(nv)
            new_adj[nv].append(nu)
        return new_adj

    def _adj_query(
        self, adj: list[list[int]], qs: list[tuple[int, int]], qadj: list[list[int]]
    ) -> list[bool]:
        n = len(adj)
        q = len(qs)
        res = [False] * q
        buf = [-1] * n
        for i in range(n):
            for j in adj[i]:
                buf[j] = i
            for qj in qadj[i]:
                if buf[qs[qj][1]] == i:
                    res[qj] = True
        return res

    def get_max_cardinality_search_order(self) -> list[int]:
        if self.status >= 1:
            return self.mcsordered
        res = [0] * self.n
        idx = [0] * self.n
        lp = list(range(self.n * 2 + 1))
        rp = list(range(self.n * 2 + 1))

        def insert(i: int, j: int) -> None:
            rp[lp[j]] = i
            lp[i] = lp[j]
            lp[j], rp[i] = i, j

        def erase(i: int) -> None:
            rp[lp[i]] = rp[i]
            lp[rp[i]] = lp[i]

        for i in range(self.n):
            insert(i, self.n)
        li = self.n
        for i in range(self.n):
            li += 1
            while lp[li] == li:
                li -= 1
            v = lp[li]
            idx[v] = -1
            erase(v)
            for u in self.adj[v]:
                if idx[u] >= 0:
                    erase(u)
                    idx[u] += 1
                    insert(u, self.n + idx[u])
            res[i] = v
        self.status = 1
        self.mcsordered = res
        return res

    def is_chordal_graph(self) -> bool:
        if self.status < 1:
            self.get_max_cardinality_search_order()
        if self.status >= 2:
            return self._is_chordal_graph

        inv_mcs = [0] * self.n
        for i, v in enumerate(self.mcsordered):
            inv_mcs[v] = i
        self.adj2 = adj2 = self._contract(inv_mcs)

        pre = [-1] * self.n
        for i in range(self.n):
            for j in adj2[i]:
                if j < i and pre[i] < j:
                    pre[i] = j

        es = []
        qadj = [[] for _ in range(self.n)]
        Z = []
        for i in range(self.n):
            if pre[i] == -1:
                continue
            for j in adj2[i]:
                if j < pre[i]:
                    qadj[pre[i]].append(len(es))
                    es.append((pre[i], j))
                    Z.append(i)
        qres = self._adj_query(adj2, es, qadj)
        for i, (u, v) in enumerate(es):
            if not qres[i]:
                self.x, self.y, self.z = v, u, Z[i]
                break
        self.status = 2
        self._is_chordal_graph = self.z == -1
        return self._is_chordal_graph

    def find_induced_cycle(self) -> list[int]:
        if self.status >= 3:
            return self.induced_cycle
        if self.is_chordal_graph():
            self.status = 3
            self.induced_cycle = []
            return self.induced_cycle
        dist = [0] * self.n
        par = [-1] * self.n
        bfs = [self.x, self.y]
        for inc in self.adj2[self.z]:
            par[inc] = -2
        dist[self.x] = -1
        dist[self.y] = 1
        par[self.x] = par[self.y] = self.z
        d = self.n + 1
        x = y = -1
        i = 0
        while i < len(bfs):
            p = bfs[i]
            for q in self.adj2[p]:
                if q < p and par[q] != -2:
                    if dist[p] < 0 and dist[q] > 0 and dist[q] - dist[p] < d:
                        d = dist[q] - dist[p]
                        x, y = p, q
                    elif dist[p] > 0 and dist[q] and dist[p] - dist[q] < d:
                        d = dist[p] - dist[q]
                        x, y = q, p
                    elif dist[q] == 0:
                        dist[q] = dist[p] + (-1 if dist[p] < 0 else 1)
                        par[q] = p
                        bfs.append(q)
            i += 1

        res = [0] * (d + 1)
        off = -dist[x]
        try:
            res[off] = self.mcsordered[self.z]
        except IndexError:
            print(f"{off=}")
            print(f"{x=}")
            print(len(res))
            exit()
        for k in [x, y]:
            while True:
                res[dist[k] + off] = self.mcsordered[k]
                k = par[k]
                if k == self.z:
                    break
        self.status = 3
        self.induced_cycle = res
        return self.induced_cycle

    def get_perfect_elimination_order(self) -> list[int]:
        if not self.is_chordal_graph():
            return []
        res = self.get_max_cardinality_search_order()
        return res[::-1]
