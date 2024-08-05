class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent_or_size = [-1 for i in range(n)]

    def merge(self, a: int, b: int) -> int:
        # assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        # assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a: int, b: int) -> bool:
        # assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        # assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        # assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if self.parent_or_size[a] < 0:
            return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a: int) -> int:
        # assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> list[int]:
        leader_buf = [0 for i in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        return [group for group in result if len(group) > 0]
