class RangeUnionFind:
    def __init__(self, n):
        self.data = [-1] * n
        self.left = [0] * n
        self.right = [1] * n

    def leader(self, k) -> int:
        if self.data[k] < 0:
            return k
        self.data[k] = self.leader(self.data[k])

    def merge(self, x, y) -> bool:
        x = self.leader(x)
        y = self.leader(y)
        if x == y:
            return False
        if self.data[x] > self.data[y]:
            x, y = y, x
        self.data[x] += self.data[y]
        self.data[y] = x
        self.left[x] = min(self.left[x], self.left[y])
        self.right[x] = max(self.right[x], self.right[y])
        return True

    def range_merge(self, l, r) -> None:
        l = max(l, 0)
        r = min(r, len(self.data))
        if l < r:
            m = self.right[self.leader(l)]
            while m < r:
                assert self.left[self.leader(m)] == m
                self.merge(l, m)
                m = self.right[self.leader(l)]

    def size(self, k) -> int:
        return -self.data[self.leader(k)]

    def same(self, x, y) -> bool:
        return self.leader(x) == self.leader(y)
