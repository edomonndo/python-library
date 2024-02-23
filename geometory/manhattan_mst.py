from data_structure.SortedSet import SortedSet


class ManhattanMST:
    def __init__(self) -> None:
        self.n = 0
        self.points = []
        self.edges = []

    def add_point(self, i, j):
        self.n += 1
        self.points.append(i)
        self.points.append(j)

    def _sweep(self):
        m = SortedSet()
        d = {}
        for i in self.idx:
            x, y = self.points[i << 1], self.points[(i << 1) + 1]
            while m:
                z = m.le(y)
                if z is None:
                    break
                j = d[z]
                dx = x - self.points[j << 1]
                dy = y - self.points[(j << 1) + 1]
                if dy > dx:
                    break
                self.edges.append((dx + dy, i, j))
                m.discard(z)
                del d[z]
            m.add(y)
            d[y] = i

    def solve(self):
        """
        2次元の点集合[(xi,yi)]から、マンハッタン最小全域木の辺集合を構築する.
        [(distance, i, j)]
        """
        for i in range(2):
            p_sum = [
                self.points[x << 1] + self.points[(x << 1) + 1] for x in range(self.n)
            ]
            self.idx = sorted(range(self.n), key=lambda x: p_sum[x])
            for _ in range(2):
                self._sweep()
                for j in range(self.n):
                    self.points[j << 1], self.points[(j << 1) + 1] = (
                        self.points[(j << 1) + 1],
                        self.points[j << 1],
                    )
            if not i:
                for j in range(self.n):
                    self.points[j << 1] *= -1
        self.edges.sort(key=lambda x: x[0])
