from typing import List
from collections import deque


class LcaDoubling:
    def __init__(self, N: int, G: List[List[int]], root: int = 0):
        self.parent = [-1] * N
        self.depth = [0] * N
        que = deque([root])
        while que:
            v = que.popleft()
            for u in G[v]:
                if self.parent[v] != u:
                    self.parent[u] = v
                    que.append(u)
                    self.depth[u] = self.depth[v] + 1

        self.ancestor = [self.parent]  # self.ancestor[k][u]はuの2**k先の祖先.

        # ダブリング
        k = 1
        while (1 << k) < N:
            anc_k = [0] * N
            for u in range(N):
                if self.ancestor[-1][u] == -1:
                    anc_k[u] = -1
                else:
                    anc_k[u] = self.ancestor[-1][self.ancestor[-1][u]]
            self.ancestor.append(anc_k)
            k += 1

    def lca(self, u: int, v: int) -> int:
        # uよりvの方が深い頂点とする
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        for k, bit in enumerate(reversed(format(self.depth[u] - self.depth[v], "b"))):
            if bit == "1":
                u = self.ancestor[k][u]
        if u == v:
            return u
        for anc in reversed(self.ancestor):
            if anc[u] != anc[v]:
                u = anc[u]
                v = anc[v]
        return self.ancestor[0][u]

    def dist(self, u: int, v: int) -> int:
        c = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[c]

    def up(self, v: int, k: int) -> int:
        i = 0
        while k:
            if k & 1:
                v = self.ancestor[i][v]
            k >>= 1
            i += 1
        return v

    def jump(self, u: int, v: int, i: int) -> int:
        c = self.lca(u, v)
        dist = self.depth[u] + self.depth[v] - 2 * self.depth[c]
        if i > dist:
            return -1

        if i <= self.depth[u] - self.depth[c]:
            return self.up(u, i)

        return self.up(v, dist - i)
