class CentroidDecomposition:
    """
    order[v]: 重心分解後の部分木における重心vのdfs順.重心vの部分木はorderが重心vより大きいbfsで到達可能な頂点
    depth[v]: 重心分解後の部分木における重心vの深さ.
    belong[v]: 重心分解後の部分木における重心vの親の重心(根は-1).
    """

    def __init__(self, adj: list[list[int]], root: int = 0) -> None:
        n = len(adj)
        # 部分木のサイズ
        size = [1] * n
        stack = [(~root, -1), (root, -1)]
        while stack:
            v, p = stack.pop()
            if v >= 0:
                for u in adj[v]:
                    if u != p:
                        stack.append((~u, v))
                        stack.append((u, v))
            else:
                v = ~v
                for u in adj[v]:
                    if u != p:
                        size[v] += size[u]
        # 重心分解
        self.order = order = [-1] * n
        self.depth = depth = [-1] * n
        self.belong = belong = [-1] * n
        stack = [(root, -1, 0)]  # 　current, previous, depth
        for i in range(n):
            v, p, d = stack.pop()
            while True:
                for u in adj[v]:
                    if order[u] == -1 and size[u] * 2 > size[v]:
                        size[v], size[u], v = size[v] - size[u], size[v], u
                        break
                else:
                    # 頂点vが重心のとき
                    break
            order[v], depth[v], belong[v] = i, d, p
            if size[v] > 1:
                for u in adj[v]:
                    if order[u] == -1:
                        stack.append((u, v, d + 1))

    def find(self, u: int, v: int) -> int:
        """
        頂点u,vの両方を含む最も小さい部分木の重心を返す
        """
        du, dv = self.depth[u], self.depth[v]
        for _ in range(du - 1, dv - 1, -1):
            u = self.belong[u]
        for _ in range(dv - 1, du - 1, -1):
            v = self.belong[v]
        while u != v:
            u, v = self.belong[u], self.belong[v]
        return u

    def get(self, v: int) -> list[int]:
        """
        重心分解後の部分木で,頂点vが属する部分木をサイズの昇順に列挙する
        """
        res = []
        for _ in range(self.depth[v], -1, -1):
            res.append(v)
            v = self.belong[v]
        return res
