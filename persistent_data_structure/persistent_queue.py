class PersistentQueue:
    def __init__(self, number_of_query: int):
        self.q = number_of_query
        self.h = self.q.bit_length()
        self.idx = -1
        self.val = [0] * (self.q + 1)
        self.cnt = [0] * (self.q + 1)
        self.par = [[None] * (self.q + 1) for _ in range(self.h)]

    def append(self, t: int, x):
        """Add x to version t."""
        assert -1 <= t <= self.idx
        self.idx += 1
        assert self.idx < self.q
        self.val[self.idx] = x
        self.cnt[self.idx] = self.cnt[t] + 1
        self.par[0][self.idx] = t
        h, p = 1, t
        while p:
            p = self.par[h][self.idx] = self.par[h - 1][p]
            h += 1

    def popleft(self, t: int):
        """Pop element from version t."""
        assert -1 <= t <= self.idx
        self.idx += 1
        assert self.idx < self.q
        self.val[self.idx] = self.val[t]
        self.cnt[self.idx] = self.cnt[t] - 1
        p = self.par[0][self.idx] = self.par[0][t]
        h = 1
        while p:
            p = self.par[h][self.idx] = self.par[h - 1][p]
            h += 1
        p = self.idx
        c = self.cnt[p]
        for i in range(self.h):
            if (c >> i) & 1:
                p = self.par[i][p]
        return self.val[p]
