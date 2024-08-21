from heapq import *

from graph.connectivity.unionfind import UnionFind
from graph.bipartite_matching import bipartite_matching


class RegularBipartiteGlaph:
    def __init__(self, l: int, r: int, edges: list[tuple[int, int]]):
        self.l = l
        self.r = r
        self.el = []
        self.er = []
        for u, v in edges:
            self.el.append(u)
            self.er.append(v)
        self._regularize()

    def _contract(self, deg: list[int], k: int) -> UnionFind:
        pq = []
        for i in range(len(deg)):
            heappush(pq, (deg[i], i))
        uf = UnionFind(len(deg))
        while len(pq) > 1:
            di, i = heappop(pq)
            dj, j = heappop(pq)
            if di + dj > k:
                continue
            uf.merge(i, j)
            heappush(pq, (di + dj, i))
        return uf

    def _regularize(self):
        dl = [0] * self.l
        dr = [0] * self.r
        for i in self.el:
            dl[i] += 1
        for i in self.er:
            dr[i] += 1
        self.k = k = max(max(dl), max(dr))
        ufl = self._contract(dl, k)
        ufr = self._contract(dr, k)
        cl = cr = 0
        idl = [0] * self.l
        idr = [0] * self.r
        for i in range(self.l):
            if ufl.leader(i) == i:
                idl[i] = cl
                cl += 1
        for i in range(self.r):
            if ufr.leader(i) == i:
                idr[i] = cr
                cr += 1
        self.n = n = max(cl, cr)
        self.lt = []
        self.rt = []
        dl = [0] * n
        dr = [0] * n
        for i in range(len(self.el)):
            l = idl[ufl.leader(self.el[i])]
            r = idr[ufr.leader(self.er[i])]
            self.lt.append(l)
            self.rt.append(r)
            dl[l] += 1
            dr[r] += 1
        j = 0
        for i in range(n):
            while dl[i] < k:
                while dr[j] == k:
                    j += 1
                self.lt.append(i)
                self.rt.append(j)
                dl[i] += 1
                dr[j] += 1


class BipartiteEdgeColoring:
    def __init__(self, rg: RegularBipartiteGlaph):
        self.n = rg.n
        self.k = rg.k
        self.lt = rg.lt
        self.rt = rg.rt
        self.group = []
        self.color = [-1] * self.n * self.k

    def euler_trail(self, edge: list[tuple[int, int]]) -> list[tuple[int, int]]:
        g = [[] for _ in range(self.n * 2)]
        m = len(edge)
        for i, e in enumerate(edge):
            g[self.lt[e]].append((self.rt[e] + self.n, i))
            g[self.rt[e] + self.n].append((self.lt[e], i))
        used_vtx = [False] * self.n * 2
        used_edge = [False] * m
        res = []
        for i in range(2 * self.n):
            if used_vtx[i]:
                continue
            st = [(i, -1)]
            ord = []
            while st:
                j = st[-1][0]
                used_vtx[j] = True
                if g[j]:
                    v, e = g[j].pop()
                    if used_edge[e]:
                        continue
                    used_edge[e] = True
                    st.append((v, e))
                else:
                    v, e = st.pop()
                    ord.append(e)
            res.extend(ord[:-1][::-1])
        for i, p in enumerate(res):
            res[i] = edge[p]
        return res

    def solve(self):
        ord = [i for i in range(len(self.lt))]
        st = [(self.k, ord)]
        while st:
            k, edge = st.pop()
            if k == 0:
                continue
            if k == 1:
                self.group.append(edge)
            elif k % 2 == 0:
                path = self.euler_trail(edge)
                ord1 = []
                ord2 = []
                for i, p in enumerate(path):
                    if i % 2 == 0:
                        ord1.append(p)
                    else:
                        ord2.append(p)
                st += [(k // 2, ord1), (k // 2, ord2)]
            else:
                match_l, _ = bipartite_matching(
                    self.n, self.n, [(self.lt[i], self.rt[i]) for i in range(len(edge))]
                )
                ord = []
                matched = []
                for i in edge:
                    if match_l[self.lt[i]] == self.rt[i]:
                        match_l[self.lt[i]] = -1
                        matched.append(i)
                    else:
                        ord.append(i)
                self.group.append(matched)
                st.append((k - 1, ord))
        for i in range(self.k):
            for j in self.group[i]:
                self.color[j] = i
