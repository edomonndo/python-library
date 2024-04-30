class RollbackUnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent_or_size = [-1] * n
        self.history = []
        self.sum = [0] * n
        self.snap = 0

    def merge(self, a: int, b: int) -> bool:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            self.history.append((-1, -1))
            self.history.append((-1, -1))
            return False
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.history.append((x, self.parent_or_size[x]))
        self.history.append((y, self.parent_or_size[y]))
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        self.sum[x] += self.sum[y]
        return True

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        if self.parent_or_size[a] < 0:
            return a
        # 経路圧縮しない
        # self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.leader(self.parent_or_size[a])

    def size(self, a: int) -> int:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [0 for i in range(self.n)]
        group_size = [0 for i in range(self.n)]
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

    def undo(self) -> None:
        y, py = self.history.pop()
        x, px = self.history.pop()
        if y == -1:
            return
        if self.parent_or_size[x] != px:
            self.sum[x] -= self.sum[y]
        self.parent_or_size[y] = py
        self.parent_or_size[x] = px
        return

    def snapshot(self):
        self.snap = len(self.history) >> 1

    def get_state(self):
        return len(self.history) >> 1

    def rollback(self, state=-1):
        if state == -1:
            state = self.snap
        state <<= 1
        assert state <= len(self.history)
        while state < len(self.history):
            self.undo()
        return

    def add(self, a: int, x: int) -> None:
        while a >= 0:
            self.sum[a] += x
            a = self.parent_or_size[a]

    def group_sum(self, a: int) -> int:
        return self.sum[self.leader(a)]
