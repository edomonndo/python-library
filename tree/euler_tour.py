from atcoder.segtree import SegTree
class EulerTour:
    def __init__(self, G, root, vcost):
        N = len(G)
        self.N = N
        self.ET = []
        self.into = [0] * N
        self.out = [0] * N
        self.depth = [N] * (N+1)
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
                self.depth[v]=0 if p==-1 else self.depth[p]+1
                self.vcost.append(vcost[v])
                self.ecost.append(weight)
                self.vcost_st.append(vcost[v])
                self.ecost_st.append(weight)
                self.out[v] = len(self.ET)
                for u,w in G[v]:
                    if u==p:continue
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
        
        self.depth_min = None
        self.vcost_subtree_sum = None
        self.ecost_subtree_sum = None
        self.vcost_path_sum = None
        self.ecost_path_sum = None

    def lca(self, u, v):
        """uとvの最近共通祖先"""
        if self.depth_min is None:
            def op(u, v):
                return u if self.depth[u] <= self.depth[v] else v
            self.depth_min = SegTree(op, self.N, self.ET)

        if self.into[u] > self.into[v]: u, v = v, u
        return self.depth_min.prod(self.into[u], self.out[v])

    def dist(self, u, v):
        """uとvの距離"""
        if self.ecost_path_sum is None:
            self.ecost_path_sum = SegTree(lambda u, v: u+v, 0, self.ecost)
        
        a = self.lca(u, v)
        return self.ecost_path_sum.prod(0, self.out[u])+self.ecost_path_sum.prod(0, self.out[v])-2*self.ecost_path_sum.prod(0, self.out[a])
    
    def update_parent_edge(self, v, w):
        """vとその親を繋ぐ辺の重みをwに更新"""
        if self.ecost_path_sum is None:
            self.ecost_path_sum = SegTree(lambda u, v: u+v, 0, self.ecost)
        if self.ecost_subtree_sum is None:
            self.ecost_subtree_sum = SegTree(lambda u,v: u+v, 0, self.ecost_st)

        self.ecost_path_sum.set(self.into[v], w)
        self.ecost_path_sum.set(self.out[v], -w)
        self.ecost_subtree_sum.set(self.into[v], w)

    def update_verticle(self, v, w):
        """vの重みをwに更新"""
        if self.vcost_path_sum is None:
            self.vcost_path_sum = SegTree(lambda u,v: u+v, 0, self.vcost)
        if self.vcost_subtree_sum is None:
            self.vcost_subtree_sum = SegTree(lambda u,v: u+v, 0, self.vcost_st)

        self.vcost_path_sum.set(self.into[v], w)
        self.vcost_path_sum.set(self.out[v], -w)
        self.vcost_subtree_sum.set(self.into[v], w)
    
    def is_ancestor(self, u, v): 
        """True if u is ancestor of v."""
        return self.into[u] <= self.into[v] < self.out[u]
    
    def subtree_verticle_sum(self, v):
        """Range Sum Query1 頂点vを根とする部分木の頂点の値の和"""
        if self.vcost_subtree_sum is None:
            self.vcost_subtree_sum = SegTree(lambda u,v: u+v, 0, self.vcost_st)

        l, r = self.into[v], self.out[v]
        return self.vcost_subtree_sum.prod(l, r)
    
    def subtree_edge_sum(self, v):
        """Range Sum Query2 頂点vを根とする部分木の辺の値の和"""
        if self.ecost_subtree_sum is None:
            self.ecost_subtree_sum = SegTree(lambda u,v: u+v, 0, self.ecost_st)

        l, r = self.into[v], self.out[v]
        # 頂点vから親への辺を除去するためにlを１つずらす
        return self.ecost_subtree_sum.prod(l + 1, r)
        
    def path_verticle_sum(self, v):
        """Path Query1 根から頂点vまでの頂点の値の和"""
        if self.vcost_path_sum is None:
            self.vcost_path_sum = SegTree(lambda u,v: u+v, 0, self.vcost)
        
        return self.vcost_path_sum.prod(0, self.into[v] + 1)
    
    def path_edge_sum(self, v):
        """Path Query2 根から頂点vまでの辺の値の和"""
        if self.ecost_path_sum is None:
            self.ecost_path_sum = SegTree(lambda u,v: u+v, 0, self.ecost)
        
        return self.ecost_path_sum.prod(0, self.into[v] + 1)