from data_structure.segtree.segment_tree import Segtree


class AuxiliaryTree:
    def __init__(self, adj: list[list[int]], root=0):
        self.n = len(adj)
        self.ET, self.into, self.out, self.depth = self._euler_tour(adj, root)

        def op(u, v):
            return u if self.depth[u] <= self.depth[v] else v

        self.depth_min = Segtree(self.ET, op, self.n)

    @staticmethod
    def _euler_tour(adj: list[list[int]], root: int = 0):
        n = len(adj)
        ET = []
        into = [0] * n
        out = [0] * n
        depth = [n] * (n + 1)

        # Euler Tour
        stack = [(root, -1)]
        while stack:
            v, p = stack.pop()
            if v >= 0:
                into[v] = len(ET)
                ET.append(v)
                depth[v] = 0 if p == -1 else depth[p] + 1
                out[v] = len(ET)
                for u in adj[v]:
                    if u == p:
                        continue
                    stack.append((~v, u))
                    stack.append((u, v))
            else:
                v = ~v
                ET.append(v)
                out[v] = len(ET)
        return ET, into, out, depth

    def _lca(self, u, v):
        """uとvの最近共通祖先"""
        if self.into[u] > self.into[v]:
            u, v = v, u
        return self.depth_min.prod(self.into[u], self.out[v])

    def build(self, vs: list[int]) -> dict[list[int]]:
        """頂点集合vsとそれらのLCAを含む木を構築する."""
        vs.sort(key=self.into.__getitem__)
        k = len(vs)
        for i in range(k - 1):
            x = self._lca(vs[i], vs[i + 1])
            vs.append(x)
        vs.sort(key=self.into.__getitem__)
        root = vs[0]
        stack = []
        p = -1
        res = dict()
        for v in vs:
            if v == p:
                continue
            while stack and self.out[stack[-1]] < self.into[v]:
                stack.pop()
            if stack:
                res[stack[-1]].append(v)
            res[v] = []
            stack.append(v)
            p = v
        return root, res
