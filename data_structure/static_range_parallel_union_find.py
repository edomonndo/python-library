from atcoder.dsu import DSU


class StaticRangeParallelUnionFind:
    def __init__(self, n):
        self.n = n
        self.qs = [[] for _ in range(n + 1)]

    def merge(self, x, y, d):
        """merge(x+i, y+i) for i in range(d)"""
        if d == 0:
            return
        self.qs[min(d, self.n)].append((x, y))

    def build(self) -> DSU:
        n = self.n
        uf = DSU(n)
        q = []
        for d in reversed(range(1, n + 1)):
            q += self.qs[d]
            nq = []
            for x, y in q:
                if uf.same(x, y):
                    continue
                uf.merge(x, y)
                nq.append((x + 1, y + 1))
            q = nq
        return uf
