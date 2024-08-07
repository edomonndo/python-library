from data_structure.segtree.segment_tree import Segtree


class EulerTour:
    def __init__(self, G, root, vcost):
        N = len(G)
        self.N = N
        self.ET = []
        self.into = [0] * N
        self.out = [0] * N
        self.parent = [-1] * N
        self.depth = [N] * (N + 1)
        # For Path Query
        self.vcost = []
        self.ecost = []
        # For Subtree Query
        self.vcost_st = []
        self.ecost_st = []

        # 非再帰DFS
        stack = [(root, -1, 0)]
        while stack:
            v, p, weight = stack.pop()
            if v >= 0:
                self.into[v] = len(self.ET)
                self.ET.append(v)
                self.depth[v] = 0 if p == -1 else self.depth[p] + 1
                self.vcost.append(vcost[v])
                self.ecost.append(weight)
                self.vcost_st.append(vcost[v])
                self.ecost_st.append(weight)
                self.out[v] = len(self.ET)
                for u, w in G[v]:
                    if u == p:
                        continue
                    self.parent[u] = v
                    stack.append((~v, u, -w))
                    stack.append((u, v, w))
            else:
                v = ~v
                self.ET.append(v)
                self.vcost.append(-vcost[p])
                self.ecost.append(weight)
                self.vcost_st.append(0)
                self.ecost_st.append(0)
                self.out[v] = len(self.ET)

        self.depth_min = Segtree(
            self.ET, lambda u, v: u if self.depth[u] <= self.depth[v] else v, self.N
        )
        self.vcost_subtree_sum = Segtree(self.vcost_st, lambda u, v: u + v, 0)
        self.ecost_subtree_sum = Segtree(self.ecost_st, lambda u, v: u + v, 0)
        self.vcost_path_sum = Segtree(self.vcost, lambda u, v: u + v, 0)
        self.ecost_path_sum = Segtree(self.ecost, lambda u, v: u + v, 0)

    def lca(self, u, v):
        """uとvの最近共通祖先"""
        if self.into[u] > self.into[v]:
            u, v = v, u
        return self.depth_min.prod(self.into[u], self.out[v])

    def dist(self, u, v):
        """uとvの距離"""
        a = self.lca(u, v)
        return (
            self.ecost_path_sum.prod(0, self.out[u])
            + self.ecost_path_sum.prod(0, self.out[v])
            - 2 * self.ecost_path_sum.prod(0, self.out[a])
        )

    def update_parent_edge(self, v, w):
        """vとその親を繋ぐ辺の重みをwに更新"""
        l, r = self.into[v], self.out[v]
        self.ecost_path_sum.set(l, w)
        if r < self.ecost_path_sum.n:
            self.ecost_path_sum.set(r, -w)
        self.ecost_subtree_sum.set(l, w)

    def add_parent_edge(self, v, w):
        """vとその親を繋ぐ辺の重みにwを加算"""
        l, r = self.into[v], self.out[v]
        cur = self.ecost_path_sum.get(l)
        self.ecost_path_sum.set(l, w + cur)
        if r < self.ecost_path_sum.n:
            self.ecost_path_sum.set(r, -(w + cur))
        self.ecost_subtree_sum.set(l, w + self.ecost_subtree_sum.get(l))

    def update_verticle(self, v, w):
        """vの重みをwに更新"""
        l, r = self.into[v], self.out[v]
        self.vcost_path_sum.set(l, w)
        if r < self.vcost_path_sum.n:
            self.vcost_path_sum.set(r, -w)
        self.vcost_subtree_sum.set(l, w)

    def add_verticle(self, v, w):
        """vの重みにwを加算"""
        l, r = self.into[v], self.out[v]
        cur = self.vcost_path_sum.get(l)
        self.vcost_path_sum.set(l, w + cur)
        if r < self.vcost_path_sum.n:
            self.vcost_path_sum.set(r, -(w + cur))
        self.vcost_subtree_sum.set(l, w + self.vcost_subtree_sum.get(l))

    def is_ancestor(self, u, v):
        """True if u is ancestor of v."""
        return self.into[u] <= self.into[v] < self.out[u]

    def subtree_verticle_sum(self, v):
        """Range Sum Query1 頂点vを根とする部分木の頂点の値の和"""
        l, r = self.into[v], self.out[v]
        return self.vcost_subtree_sum.prod(l, r)

    def subtree_edge_sum(self, v):
        """Range Sum Query2 頂点vを根とする部分木の辺の値の和"""
        l, r = self.into[v], self.out[v]
        # 頂点vから親への辺を除去するためにlを１つずらす
        return self.ecost_subtree_sum.prod(l + 1, r)

    def path_verticle_sum(self, u, v=None):
        """Path Query1 根から頂点uまでの頂点の値の和"""
        if v == None:
            return self.vcost_path_sum.prod(0, self.into[u] + 1)

        """Path Query2 頂点uから頂点vまでの頂点の値の和"""
        a = self.lca(u, v)
        return (
            self.vcost_path_sum.prod(0, self.into[u] + 1)
            + self.vcost_path_sum.prod(0, self.into[v] + 1)
            - self.vcost_path_sum.prod(0, self.into[a])
            - self.vcost_path_sum.prod(0, self.into[a] + 1)
        )

    def path_edge_sum(self, v):
        """Path Query3 根から頂点vまでの辺の値の和"""
        return self.ecost_path_sum.prod(0, self.into[v] + 1)
