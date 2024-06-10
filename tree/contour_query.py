from tree.centroid_decomposition import CentroidDecomposition

from collections import deque
from typing import Callable, TypeVar

T = TypeVar("T")


class ContourQuery:
    def __init__(self, adj: list[list[int]], f: Callable[[list[T]], None]):
        self.n = n = len(adj)
        self.adj = adj
        cd = CentroidDecomposition(adj, 0)
        self.root = root = cd.get_root()
        self.H = H = cd.get_graph()

        self.par = par = [-1] * n
        self.dep = dep = [-1] * n
        st = [(root, -1, 0)]
        while st:
            v, p, d = st.pop()
            par[v] = p
            dep[v] = d
            for u in H[v]:
                st.append((u, v, d + 1))

        h = max(dep) + 1
        self.vt = vt = [[] for _ in range(n)]
        self.ct = ct = [[] for _ in range(n)]
        self.cpar = cpar = [[-1] * h for _ in range(n)]
        self.dist = dist = [[-1] * h for _ in range(n)]
        self._build()

        self.rdx1 = rdx1 = [[-1] * h for _ in range(n)]
        self.rdx2 = rdx2 = [[-1] * h for _ in range(n)]
        dat = [[] for _ in range(n << 1)]
        for i in range(n):
            dat[i] = [0] * len(vt[i])
            for j, (_, a) in enumerate(vt[i]):
                dat[i][j] = a
                rdx1[a][dep[i]] = j

        self.idx = idx = [[] for _ in range(n)]
        cnt = n
        for i in range(n):
            idx[i] = [0] * len(ct[i])
            for j in range(len(ct[i])):
                if len(ct[i][j]) == 0:
                    continue
                dat[cnt] = [0] * len(ct[i][j])
                for k, (_, a) in enumerate(ct[i][j]):
                    dat[cnt][k] = a
                    rdx2[a][dep[i]] = k
                idx[i][j] = cnt
                cnt += 1

        self.ddx1 = ddx1 = [[] for _ in range(n)]
        for i in range(n):
            m = vt[i][-1][0]
            ddx1[i] = [-1] * (m + 1)
            for j, (a, _) in enumerate(vt[i]):
                if ddx1[i][a] == -1:
                    ddx1[i][a] = j

        self.ddx2 = ddx2 = [[] for _ in range(n)]
        self.ddx3 = ddx3 = [[] for _ in range(n)]
        self.ddx4 = ddx4 = [[] for _ in range(n)]
        for i in range(n):
            sz = len(ct[i])
            ddx2[i] = [0] * sz
            ddx3[i] = [0] * sz
            ddx4[i] = [0] * sz
            for j in range(sz):
                if len(ct[i][j]) == 0:
                    continue
                m = ct[i][j][-1][0]
                ddx2[i][j] = [-1] * (m + 1)
                ddx3[i][j] = [-1] * (m + 1)
                ddx4[i][j] = [-1] * (m + 1)
                for k, (a, _) in enumerate(ct[i][j]):
                    if ddx4[i][j][a] == -1:
                        ddx4[i][j][a] = k
            for j in range(1, len(vt[i])):
                a, b = vt[i][j]
                if ddx2[i][cpar[b][dep[i]]][a] == -1:
                    ddx2[i][cpar[b][dep[i]]][a] = j
                ddx3[i][cpar[b][dep[i]]][a] = j

        f(dat)
        return

    def _build(self):
        adj, dep, H = self.adj, self.dep, self.H
        vt, ct, cpar, dist = self.vt, self.ct, self.cpar, self.dist
        st = [self.root]
        dq = deque()
        while st:
            v = st.pop()
            d = dep[v]
            vt[v].append((0, v))
            ct[v] = [[] for _ in range(len(adj[v]))]
            cpar[v][d] = v
            dist[v][d] = 0
            for i in range(len(adj[v])):
                u = adj[v][i]
                if dep[u] < d:
                    continue
                cpar[u][d] = i
                dist[u][d] = 1  # edge weight
                dq.append((u, 1))
            while dq:
                u, d2 = dq.popleft()
                c = cpar[u][d]
                vt[v].append((d2, u))
                ct[v][c].append((d2, u))
                for i in range(len(adj[u])):
                    u2 = adj[u][i]
                    if dep[u2] < d:
                        continue
                    if cpar[u2][d] != -1:
                        continue
                    cpar[u2][d] = c
                    dist[u2][d] = d2 + 1  # edge weight
                    dq.append((u2, d2 + 1))
            for u in H[v]:
                st.append(u)

    def vertex(self, v: int, f: Callable[[T, T], None]) -> None:
        par, cpar, rdx1, rdx2, idx = self.par, self.cpar, self.rdx1, self.rdx2, self.idx
        f(v, 0)
        u = v
        for d in range(self.dep[v] - 1, -1, -1):
            p = par[u]
            cp = cpar[u][d]
            f(p, rdx1[v][d])
            f(idx[p][cp], rdx2[v][d])
            u = p
        return

    def contour(self, v: int, k: int, f: Callable[[T, T], None]) -> None:
        ddx1, ddx2, ddx3 = self.ddx1, self.ddx2, self.ddx3
        vt, dist, par, cpar = self.vt, self.dist, self.par, self.cpar
        if k < len(ddx1[v]):
            l = ddx1[v][k]
            r = ddx1[v][k + 1] if k + 1 < len(ddx1[v]) else len(vt[v])
            f(v, l, r)
        u = v
        for d in range(self.dep[v] - 1, -1, -1):
            k -= dist[v][d]
            p = par[u]
            cp = cpar[u][d]
            if 0 <= k < len(ddx1[p]):
                l = ddx1[p][k]
                r = ddx1[p][k + 1] if k + 1 < len(ddx1[p]) else len(vt[p])
                if k < len(ddx2[p][cp]):
                    l2 = ddx2[p][cp][k]
                    r2 = ddx3[p][cp][k] + 1
                    f(p, l, l2)
                    f(p, r2, r)
                else:
                    f(p, l, r)
            k += dist[v][d]
            u = p
        return

    def _inner_range_contour(
        self, v: int, k: int, f: Callable[[T, T], None], g: Callable[[T, T], None]
    ):
        ddx1, ddx4 = self.ddx1, self.ddx4
        vt, ct, par, cpar = self.vt, self.ct, self.par, self.cpar
        idx, dist = self.idx, self.dist
        r = ddx1[v][k] if k < len(ddx1[v]) else len(vt[v])
        f(v, r)
        u = v
        for d in range(self.dep[v] - 1, -1, -1):
            k -= dist[v][d]
            p = par[u]
            cp = cpar[u][d]
            if k > 0:
                r = ddx1[p][k] if k < len(ddx1[p]) else len(vt[p])
                f(p, r)
                r2 = ddx4[p][cp][k] if k < len(ddx4[p][cp]) else len(ct[p][cp])
                g(idx[p][cp], r2)
            k += dist[v][d]
            u = p
        return

    def range_contour(
        self,
        v: int,
        l: int,
        r: int,
        f: Callable[[T, T], None],
        g: Callable[[T, T], None],
    ):
        self._inner_range_contour(v, l, g, f)
        self._inner_range_contour(v, r, f, g)
