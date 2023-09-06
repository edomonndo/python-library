import heapq


class MinCostArborescence:
    # Edmonds' algorithm
    def __init__(self, N, edges, root):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.r = root
        for u, v, w in edges:
            if v != root:
                heapq.heappush(self.G[v], [w, u, v])

    def calc_min_cost(self, weight=0):
        min_incoming_edges = [None] * self.N
        for edges in self.G:
            if edges:
                min_edge = edges[0]
                min_incoming_edges[min_edge[2]] = min_edge
                weight += min_edge[0]
        vs_in_cycle = self._find_cycle(min_incoming_edges)
        if not vs_in_cycle:
            return weight
        else:
            self._contract_cycle(vs_in_cycle)
            return self.calc_min_cost(weight)

    def _find_cycle(self, incoming_edges):
        in_tree = [0] * self.N
        in_tree[self.r] = 1
        for edge in incoming_edges:
            if edge:
                S = [edge[2]]
                while True:
                    par = incoming_edges[S[-1]][1]
                    if in_tree[par]:
                        while S:
                            in_tree[S.pop()] = 1
                        break
                    elif par in S:
                        return S[S.index(par) :]
                    else:
                        S.append(par)
        return None

    def _contract_cycle(self, vs_in_cycle):
        v_super = vs_in_cycle[0]
        for edges in self.G:
            if edges:
                min_weight = edges[0][0]
                for edge in edges:
                    edge[0] -= min_weight
                    if edge[1] in vs_in_cycle:
                        edge[1] = v_super
                    if edge[2] in vs_in_cycle:
                        edge[2] = v_super
        contracted_edges = []
        for v in vs_in_cycle:
            for edge in self.G[v]:
                if edge[1] != v_super:
                    contracted_edges.append(edge)
            self.G[v] = []
        self.G[v_super] = contracted_edges
        heapq.heapify(self.G[v_super])
