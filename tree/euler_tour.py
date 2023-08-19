class EulerTour:
    def __init__(self, N, G, root, vcost):
        self.N = N
        self.ET = []
        self.into = [0] * N
        self.out = [0] * N
        # For LCA
        self.parent = [-1] * N
        self.depth = []
        # For Path Query
        self.vcost = []
        self.ecost = []
        # For Range Sum Query
        self.vcost_st = []
        self.ecost_st = []

        # 非再帰DFS
        seen = [0] * N
        idx = -1
        depth = 0
        stack = [(~root, -depth, 0), (root, depth, 0)]
        while stack:
            v, depth, weight = stack.pop()
            idx += 1
            if v >= 0:
                self.ET.append(v)
                self.depth.append((depth, v))
                self.vcost.append(vcost[v])
                self.ecost.append(weight)
                self.vcost_st.append(vcost[v])
                self.ecost_st.append(weight)
                seen[v] = 1
                if self.into[v] == 0:
                    self.into[v] = idx
                for w, u in G[v][::-1]:
                    if not seen[u]:
                        self.parent[u] = v
                        stack.append((~u, depth, w))
                        stack.append((u, depth + 1, w))
            else:
                self.ET.append(v + 1)
                self.depth.append((depth, self.parent[~v]))
                self.vcost.append(-vcost[~v])
                self.ecost.append(-weight)
                self.vcost_st.append(0)
                self.ecost_st.append(0)
                self.out[~v] = idx
