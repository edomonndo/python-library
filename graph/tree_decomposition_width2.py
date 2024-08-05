from typing import Optional
from collections import deque
from graph.connectivity.unionfind import UnionFind
import sys

sys.setrecursionlimit(2_000_000)


class TreeDecompositionWidth2:
    def __init__(self, n: int, edges: list[tuple[int, int]]):
        self.n = n
        self.adj = adj = [[] for _ in range(n)]
        for u, v in edges:
            if u == v:
                continue
            if u > v:
                u, v = v, u
            du, dv = len(adj[u]), len(adj[v])
            adj[u].append((v, dv))
            adj[v].append((u, du))

    def _remove_edge(self, u: int, idx_uv: int) -> int:
        adj = self.adj
        v, idx_vu = adj[u][idx_uv]
        if idx_vu != len(adj[v]) - 1:
            w, idx_wv = adj[v][-1]
            adj[v][idx_vu], adj[v][-1] = adj[v][-1], adj[v][idx_vu]
            c, _ = adj[w][idx_wv]
            adj[w][idx_wv] = (c, idx_vu)
        adj[v].pop()
        if idx_uv != len(adj[u]) - 1:
            z, idx_zu = adj[u][-1]
            adj[u][idx_uv], adj[u][-1] = adj[u][-1], adj[u][idx_uv]
            c, _ = adj[z][idx_zu]
            adj[z][idx_zu] = (c, idx_uv)
        adj[u].pop()
        self._remove_multiedges(v, idx_vu)
        self._remove_multiedges(u, idx_uv)
        return v

    def _remove_multiedges(self, u: int, idx_uv: int) -> None:
        def is_unnecessary(idx_uv: int) -> bool:
            us = self.adj[u]
            du = len(us)
            if idx_uv >= du:
                return False
            c = us[idx_uv][0]
            for di in [-2, -1, 1, 2]:
                nidx = idx_uv + di
                if 0 <= nidx < du and c == us[nidx][0]:
                    return True
            return False

        while is_unnecessary(idx_uv):
            self._remove_edge(u, idx_uv)

    def build(self) -> Optional[tuple[list[list[int]], list[tuple[int, int]]]]:
        n, adj = self.n, self.adj
        seen = [0] * n
        dq = deque()
        for i in range(n):
            if len(adj[i]) <= 2:
                dq.append(i)
                seen[i] = 1

        roots = []
        edges = []
        bag = [[] for _ in range(n)]
        link = [[] for _ in range(n)]
        uf = UnionFind(n)
        for i in range(n):
            if not dq:
                return None
            u = dq.popleft()
            if len(adj[u]) == 0:
                bag[i] = [u]
                roots.append(i)
            elif len(adj[u]) == 1:
                v = self._remove_edge(u, 0)
                if len(adj[v]) <= 2:
                    if not seen[v]:
                        seen[v] = 1
                        dq.append(v)
                bag[i] = [u, v]
                link[v].append(i)
            else:
                v = self._remove_edge(u, 0)
                w = self._remove_edge(u, 0)
                if v > w:
                    v, w = w, v
                bag[i] = [u, v, w]
                dv, dw = len(adj[v]), len(adj[w])
                adj[v].append((w, dw))
                adj[w].append((v, dv))
                self._remove_multiedges(v, dv)
                self._remove_multiedges(w, dw)
                if len(adj[v]) <= 2:
                    if not seen[v]:
                        seen[v] = 1
                        dq.append(v)
                if len(adj[w]) <= 2:
                    if not seen[w]:
                        seen[w] = 1
                        dq.append(w)
                link[v].append(i)
                link[w].append(i)

            link[u].reverse()
            for j in link[u]:
                if not uf.same(i, j):
                    edges.append((i, j))
                    uf.merge(i, j)
            adj[u].clear()
            link[u].clear()

        for i in range(len(roots) - 1):
            edges.append((roots[i], roots[i + 1]))
        return bag, edges
