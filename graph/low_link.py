class LowLink:
    def __init__(self, adj: list[list[int]]):
        self.n = n = len(adj)
        order = [-1] * n
        low = [n] * n
        par = [-1] * n
        children = [[] for _ in range(n)]

        seen = [0] * n
        idx = 0
        for u in range(n):
            if order[u] != -1:
                continue
            seen[u] = 1
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
                        children[par[v]].append(v)
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
        self.order = order
        self.low = low
        self.roots = [i for i, v in enumerate(seen) if v]
        self.children = children

    def get_articulation(self) -> list[int]:
        order, low, roots, children = self.order, self.low, self.roots, self.children
        res = [0] * self.n
        for v in range(self.n):
            if v in roots:
                if len(children[v]) >= 2:
                    res[v] = 1
                continue
            for u in children[v]:
                if order[v] <= low[u]:
                    res[v] = 1
                    break
        return res

    def get_bridge(self) -> list[tuple[int, int]]:
        order, low, roots, children = self.order, self.low, self.roots, self.children
        res = []
        for v in roots:
            st = [v]
            while st:
                v = st.pop()
                for u in children[v]:
                    if order[v] < low[u]:
                        res.append((v, u))
                    st.append(u)
        return res

    def two_edge_connected_components(self) -> tuple[list[int], list[tuple[int, int]]]:
        order, low, roots, children = self.order, self.low, self.roots, self.children

        components = [-1] * self.n
        new_edges = []
        idx = 0
        for v in roots:
            components[v] = idx
            st = [v]
            while st:
                v = st.pop()
                for u in children[v]:
                    if order[v] < low[u]:
                        idx += 1
                        components[u] = idx
                        new_edges.append((components[v], idx))
                    else:
                        components[u] = components[v]
                    st.append(u)
            idx += 1
        return components, new_edges

    def three_edge_connected_components(self) -> list[int]:
        order, low, roots, children = self.order, self.low, self.roots, self.children
        raise NotImplementedError

    def biconnected_components(self) -> list[int]:
        order, low, roots, children = self.order, self.low, self.roots, self.children
        raise NotImplementedError
