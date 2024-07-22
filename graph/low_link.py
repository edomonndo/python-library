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
