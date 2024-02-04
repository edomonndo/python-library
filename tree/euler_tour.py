from atcoder.segtree import SegTree
class EulerTour:
    def __init__(self, G, root, vcost):
        N = len(G)
        self.N = N
        self.ET = []
        self.into = [0] * N
        self.out = [0] * N
        # For LCA
        self.parent = [-1] * N
        self.depth = [N] * (N+1)
        # For Path Query
        self.vcost = []
        self.ecost = []
        # For Range Sum Query
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
                    self.parent[u] = v
                    stack.append((~v, u, -w))
                    stack.append((u, v, w))
            else:
                v = ~v
                self.ET.append(v)
                self.vcost.append(-vcost[v])
                self.ecost.append(weight)
                self.vcost_st.append(0)
                self.ecost_st.append(0)
                self.out[v] = len(self.ET)
        
        def op(u, v):
            return u if self.depth[u] <= self.depth[v] else v
        self.depth_min = SegTree(op, N, self.ET)
        self.rv_path = SegTree(lambda u, v: u+v, 0, self.ecost)
    
    def lca(self, u, v):
        """uとvの最近共通祖先"""
        if self.into[u] > self.into[v]: u, v = v, u
        return self.depth_min.prod(self.into[u], self.out[v])

    def dist(self, u, v):
        """uとvの距離"""
        a = self.lca(u, v)
        return self.rv_path.prod(0, self.out[u])+self.rv_path.prod(0, self.out[v])-2*self.rv_path.prod(0, self.out[a])
    
    def update_parent_edge(self, v, w):
        """vとその親を繋ぐ辺の重みをwに更新"""
        self.rv_path.set(self.into[v], w)
        self.rv_path.set(self.out[v], -w)
    
    def is_ancestor(self, u, v): 
        """uはvの祖先か？"""
        return self.into[u] <= self.into[v] < self.out[u]