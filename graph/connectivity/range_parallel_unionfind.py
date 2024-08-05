from graph.connectivity.unionfind import UnionFind


class RangeParallelUnionFind:
    def __init__(self, n):
        self.n = n
        self.ufs = []
        num = 1
        while (1 << (num * 2)) < n:
            num += 1
        for i in range(num):
            self.ufs.append(UnionFind(max(1, n - (1 << (i * 2)) + 1)))

    def enumerate(self, u: int, v: int, d: int) -> list[tuple[int, int]]:
        "enumerate pair of (u, v) corresponds to merge(u + i, v + i) for i in range(d)"
        if u == v or d <= 0:
            return
        assert 0 <= u < self.n and 0 <= v < self.n
        assert u + d <= self.n and v + d <= self.n
        if u > v:
            u, v = v, u
        res = []
        width = v - u

        def dfs(p: int, num: int):
            st = [(p, num)]
            while st:
                p, num = st.pop()
                if self.ufs[num].same(p, p + width):
                    continue
                self.ufs[num].merge(p, p + width)
                if num == 0:
                    res.append((p, p + width))
                    continue
                for t in range(4):
                    st.append((p + (t << (2 * num - 2)), num - 1))
            return

        b = 0
        w = 1
        while w * 4 < d:
            b += 1
            w *= 4
        while d > 0:
            d = max(0, d - w)
            dfs(u + d, b)
        return res
