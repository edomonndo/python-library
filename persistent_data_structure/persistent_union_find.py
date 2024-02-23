from persistent_data_structure.persistent_array import PersistentArray


class PersistentUnionFind:
    def __init__(self, n: int, auto_update: bool = True):
        self.n = n
        self.parent_or_size = PersistentArray(n, -1, False)
        self.auto_update = auto_update
        self.last = 0

    def leader(self, t: int, a) -> int:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        cur = a
        while True:
            nxt = self.parent_or_size.get(t, cur)
            if nxt < 0:
                return cur
            cur = nxt

    def same(self, t: int, a: int, b: int) -> bool:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        return self.leader(t, a) == self.leader(t, b)

    def merge(self, t: int, a: int, b: int) -> int:
        assert 0 <= a < self.n, "0<=a<n,a={0},n={1}".format(a, self.n)
        assert 0 <= b < self.n, "0<=b<n,b={0},n={1}".format(b, self.n)
        x = self.leader(t, a)
        y = self.leader(t, b)
        if x == y:
            if self.auto_update:
                self.last = self.update()
            return x
        px = self.parent_or_size.get(t, x)
        py = self.parent_or_size.get(t, y)
        if -px < -py:
            x, y = y, x
            px, py = py, px
        self.parent_or_size.set(t, x, px + py)
        self.parent_or_size.set(t, y, x)
        if self.auto_update:
            self.last = self.update()
        return x

    def update(self):
        self.last = self.parent_or_size.update()
        return self.last
