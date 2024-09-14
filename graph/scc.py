from graph.csr import CSR


class SCC:
    def __init__(self, n: int):
        self.n = n
        self.edges = []

    def from_edge(self, edges: list[tuple[int, int]]):
        self.edges = edges

    def add_edge(self, src: int, dst: int) -> None:
        # assert 0 <= src < self.n
        # assert 0 <= dst < self.n
        self.edges.append((src, dst))

    def scc_ids(self) -> tuple[int, list[list[int]]]:
        n, edges = self.n, self.edges
        adj = CSR.build(n, edges, True)
        visited = []
        low = [0] * n
        ord = [-1] * n
        ids = [0] * n
        idx = group_num = 0
        for i in range(n):
            if ord[i] != -1:
                continue
            st = [(~i, -1), (i, -1)]
            while st:
                v, p = st.pop()
                if v >= 0:
                    if p != -1 and ord[v] != -1:
                        low[p] = min(low[p], ord[v])
                        st.pop()
                        continue
                    low[v] = ord[v] = idx
                    idx += 1
                    visited.append(v)
                    for u in adj[v]:
                        if ord[u] == -1:
                            st += [(~u, v), (u, v)]
                        else:
                            low[v] = min(low[v], ord[u])
                    continue
                v = ~v
                if low[v] == ord[v]:
                    while True:
                        u = visited.pop()
                        ord[u] = n
                        ids[u] = group_num
                        if u == v:
                            break
                    group_num += 1
                low[p] = min(low[p], low[v])
        for i in range(n):
            ids[i] = group_num - 1 - ids[i]
        self.group_num = group_num
        self.ids = ids
        return group_num, ids

    def get_mapping(self) -> list[list[int]]:
        if self.ids is not None:
            self.scc_ids()
        group_num, ids = self.group_num, self.ids
        counts = [0] * group_num
        for x in ids:
            counts[x] += 1
        groups = [[] for _ in range(group_num)]
        for i in range(n):
            groups[ids[i]].append(i)
        return groups
