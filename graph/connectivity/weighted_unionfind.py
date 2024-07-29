from typing import Optional, TypeVar

T = TypeVar("T")


class WeightedUnionFind:
    def __init__(self, n, e: T = 0):
        self.n = n
        self.parent_or_size = [-1] * n
        self.ng = [False] * n
        self.group = n
        self.e = e
        self.weight = [e for _ in range(n)]  # W_i - W_{P_i}
        self.base = [e for _ in range(n)]

    # weight[a] - weight[b] = w
    def merge(self, a: int, b: int, w: T) -> int:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            if w != self.e:
                self.ng[x] = True
            return x
        self.group -= 1
        if self.parent_or_size[x] < self.parent_or_size[y]:
            a, b = b, a
            x, y = y, x
            w = self.e - w
        self.parent_or_size[y] += self.parent_or_size[x]
        self.parent_or_size[x] = y
        self.weight[x] = self.e - self.weight[a] + w + self.weight[b]
        self.ng[y] |= self.ng[x]
        return y

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        p = self.parent_or_size[a]
        if p < 0:
            return a
        r = self.leader(p)
        self.parent_or_size[a] = r
        self.weight[a] = self.weight[a] + self.weight[p]
        return r

    def size(self, a: int) -> int:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def group_count(self) -> int:
        return self.group

    def groups(self) -> list[list[int]]:
        leader_buf = [0 for _ in range(self.n)]
        group_size = [0 for _ in range(self.n)]
        for i in range(self.n):
            leader_buf[i] = self.leader(i)
            group_size[leader_buf[i]] += 1
        result = [[] for i in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)
        result2 = []
        for i in range(self.n):
            if len(result[i]) > 0:
                result2.append(result[i])
        return result2

    def diff(self, a: int, b: int) -> Optional[T]:
        if not self.same(a, b):
            return None
        else:
            self.leader(a)
            self.leader(b)
            return self.weight[a] - self.weight[b]

    def add(self, a: int, w: T) -> None:
        a = self.leader(a)
        self.base[a] = self.base[a] + w

    def get(self, a: int) -> T:
        p = self.leader(a)
        return self.base[p] + self.diff(a, p)
